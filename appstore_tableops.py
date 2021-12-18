import boto3
from boto3.dynamodb.conditions import Key
import hashlib
import random
from decimal import Decimal
import json

#The following function creates a user. The input should be made by the user.
#This function is used in populating the table.

def create_user(userdata):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    username = userdata['username']
    email = userdata['email']
    phone = userdata['phone']
    
    user = {
        'PK'      : '{0}'.format(username), 
        'SK'      : 'PROFILE',
        'Email'   : email,
        'Phone'   : phone,
        'Installed_Apps'    : [],
        'Apps_Purchased'    : []
    }
    table.put_item(Item=user)
    print("User {0} created.".format(username))



#The following function adds apps to the table.
#This function is used to populate the table.

def add_apps(appdata):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    app_name = appdata['app_name']
    category = appdata['category']
    size = appdata['size']
    price = appdata['price']
    content_rating = appdata['content_rating']
    developer = appdata['developer']
    os = appdata['os']
    rating = appdata['rating']
    installs = appdata['installs']
    version = appdata['version']
    appdesc = appdata['app_description']
    app_id = hashlib.sha256(app_name.encode()).hexdigest()[:8]
    
    item = {
        'PK'                : '#APP#{0}'.format(app_id), 
        'SK'                : app_name,
        'Category'          : category,
        'Size'              : size,
        'Price'             : price,
        'Content_Rating'    : content_rating,
        'Developer'         : developer,
        'Operating_System'  : os,
        'Rating'            : rating,
        'Installs'          : installs,
        'App_Version'       : version,
        'App_Description'   : appdesc
    }
    
    table.put_item(Item=item)
    print("Added {0} into database. The App's ID is {1}.".format(app_name, app_id))



#The following function adds a device to the table. Its primary key is the name of its OS.
#This function is used to populate the table.

def add_device_os(device_os):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    os_name = device_os['os_name']
    model_id = device_os['model_id']
    model_name = device_os['model_name']
    manufacturer = device_os['manufacturer']
    
    
    item = {
        'PK'                : os_name, 
        'SK'                : '#MODEL#{0}'.format(model_id),
        'Model_Name'        : model_name,
        'Manufacturer'      : manufacturer
    }
    table.put_item(Item=item)
    print("Device {0} added to {1}.".format(model_name, os_name))
    


#The following app adds a review to our table under the app ID.
#This function is used in Access Pattern 4

def add_review(app_id, review):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    username = review['username']
    review_rating = review['review_rating']
    review_content = review['review_content']
    likes = review['likes']
    review_id = hashlib.sha256(str(random.random()).encode()).hexdigest()[:random.randrange(1, 20)]
    
    item = {
        'PK'                : app_id, 
        'SK'                : '#REVIEW#{0}'.format(review_id),
        'Username'          : username,
        'Review_Rating'     : review_rating,
        'Review_Content'    : review_content,
        'Likes'             : likes,
        'Comments'          : []
    }
    table.put_item(Item=item)
    print("Review added. The review ID is {0}. Thank you for your feedback, {1}.".format(review_id, username))



#The following two functions updates the list of installed and purchased apps of the user.
#The user just has to input their username and the name of the app for it to append.
#These functions are used in Access Patterns 5 and 6

def add_installed_apps(username, app_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    try:
        # Update item in table for the given username key.
        retsp = table.update_item(
            Key={'PK' : '{0}'.format(username),
                 'SK' : 'PROFILE'
            },
            UpdateExpression= 'SET Installed_Apps = list_append(Installed_Apps, :apps)',
            ExpressionAttributeValues={':apps': [app_name]}
            )
        print("App {} added to installed apps.".format(app_name))
    except Exception as err:
        print("Error message {0}".format(err))

def add_apps_purchased(username, app_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    try:
        # Update item in table for the given username key.
        retsp = table.update_item(
            Key={'PK' : '{0}'.format(username),
                 'SK' : 'PROFILE'
            },
            UpdateExpression='SET #AP = list_append(#AP, :apps)',
            ExpressionAttributeNames={'#AP' : 'Apps_Purchased'},
            ExpressionAttributeValues={':apps': [app_name]}
            )
        print("App {} added to purchased apps.".format(app_name))
    except Exception as err:
        print("Error message {0}".format(err))
    


#The following function adds a comment to an existing review. The user needs to note the app and the review id.
#This function is used in Access Pattern 6

def add_review_comment(app_id, review_id, comment):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    try:
        retsp = table.update_item(
            Key={'PK' : app_id,
                 'SK' : review_id
            },
            UpdateExpression='SET Comments = list_append(Comments, :content)',
            ExpressionAttributeValues={':content': [comment]}
            )
        print("Comment added.")
    except Exception as err:
        print("Error message {0}".format(err))



#The following function allows the user to add a payment method to their account.
#This function is used for Access Pattern 7

def add_payment_method(paymentdetails):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    username = paymentdetails['username']
    label = paymentdetails['label']
    account_num = paymentdetails['account_num']
    card_type = paymentdetails['card_type']
    expiration_date = paymentdetails['expiration_date']
    security_code = paymentdetails['security_code']
    
    item = {
        'PK'                : '{0}'.format(username), 
        'SK'                : '#PAY#{0}'.format(label),
        'Account_Number'    : account_num,
        'Card_Type'         : card_type,
        'Expiration_Date'   : expiration_date,
        'Security_Code'     : security_code
    }
    table.put_item(Item=item)
    print("Added {0} to account.".format(label))



#The following function updates the app description of an app.
#This function is used in Access Pattern 9

def add_appdesc(app_id, app_name, app_desc):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    try:
        retsp = table.update_item(
            Key={'PK' : app_id,
                'SK' : app_name
            },
            UpdateExpression='set App_Description = :desc',
            ExpressionAttributeValues={':desc': {'S':app_desc}}
            )
        print("App description successfully updated.")
    except Exception as err:
        print("Error message {0}".format(err))
    
