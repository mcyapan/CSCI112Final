import boto3
from boto3.dynamodb.conditions import Key
import hashlib
import random
from decimal import Decimal
from datetime import date 
from pprint import pprint

#Access Pattern 1

def query_category(category):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    response = table.query(
        IndexName='Category_Index',
        KeyConditionExpression= Key('Category').eq(category),
        ScanIndexForward = False,
        Limit = 10
    )
    pprint(response['Items'])



#Access Pattern 2

def scan_cardtype(card_type):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    response = table.scan(
        FilterExpression = '#CT = :card',
        ExpressionAttributeNames = {'#CT' : 'Card_Type'},
        ExpressionAttributeValues = {':card' : card_type}
    )

    pprint('There are {0} users who use {1} as their card type.'.format(response['Count'], card_type))



#Access Pattern 3

def query_category_size(category, size):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    response = table.query(
        IndexName='Category_Index',
        KeyConditionExpression=Key('Category').eq(category),
        FilterExpression = '#S <= :size',
        ExpressionAttributeNames = {'#S' : 'Size'},
        ExpressionAttributeValues = {':size' : size},
        ScanIndexForward = False
    )
    pprint(response['Items'])



#Access Pattern 4

def scan_appname(appname):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    response = table.scan(
        FilterExpression = '#SK = :app',
        ExpressionAttributeNames = {'#SK' : 'SK'},
        ExpressionAttributeValues = {':app' : appname}
    )
    app = response['Items'][0]
    return(app['PK'])

#Access Pattern 6

def query_app_reviews(app_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    response = table.query(
        KeyConditionExpression = Key('PK').eq(app_id) &
        Key('SK').begins_with('#REVIEW#')
    )
    pprint(response['Items'])


#Access Pattern 8

def query_category_installs(category, installs):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    response = table.query(
        IndexName='Category_Index',
        KeyConditionExpression=Key('Category').eq(category),
        FilterExpression = '#I >= :installs',
        ExpressionAttributeNames = {'#I' : 'Installs'},
        ExpressionAttributeValues = {':installs' : installs}
    )
    pprint(response['Items'])
    
def query_developer(developer):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    response = table.query(
        IndexName='Developer_Index',
        KeyConditionExpression=Key('Developer').eq(developer)
    )
    pprint(response['Items'])
    
#Access Pattern 10

def scan_OS_apps(os_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    response = table.scan(
        FilterExpression = '#OS = :OS',
        ExpressionAttributeNames = {'#OS' : 'Operating_System'},
        ExpressionAttributeValues = {':OS' : os_name}
    )

    pprint('Your operating system has {} apps.'.format(response['Count']))

def query_OS_devices(os_name, manufacturer):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('appstore')
    
    response = table.query(
        KeyConditionExpression=Key('PK').eq(os_name),
        FilterExpression = '#Manu = :Manu',
        ExpressionAttributeNames = {'#Manu' : 'Manufacturer'},
        ExpressionAttributeValues = {':Manu' : manufacturer}
    )

    pprint('{0} has {1} devices in your OS.'.format(manufacturer, response['Count']))



