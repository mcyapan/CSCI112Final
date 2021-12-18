import appstore_queryops as query 
import appstore_tableops as table

if __name__ == '__main__' :
    
    #Access Pattern 3
    userresp = input('Would you like to display apps for a certain category less than a specific size? Enter Yes or No: ')
    if userresp == 'Yes':
        cat = input('Please input the category you wish to display: ')
        size = input('Please input the maximum size: ')
        query.query_category_size(cat, size)
    elif userresp == 'No':
        print('Okay.')
    else:
        print('Invalid input.')
    
    user = input('Please input your username: ')
    
    #Access Pattern 4
    revresp = input('Would you like to leave a review for an app? Enter Yes or No: ')
    if revresp == 'Yes':
        name = input('Please input the app name: ')
        appid = query.scan_appname(name)
        review_rating = input('Please input your rating: ')
        review_content = input('Please input your review: ')
        content = {
            'username' : user,
            'review_rating' : review_rating,
            'review_content' : review_content,
            'likes' : 0
        }
        table.add_review(appid, content)
    elif revresp =='No':
        print('Okay.')
    else:
        print('Invalid input.')
    
    #Access Pattern 5
    insresp = input('Would you like to install apps? Enter Yes or No: ')
    if insresp == 'Yes':
        app = input('Input the app name: ')
        table.add_installed_apps(user, app)
    elif insresp == 'No':
        print('Okay.')
    else:
        print('Invalid input.')
        
    purresp = input('Would you like to purchase apps? Enter Yes or No: ')
    if purresp == 'Yes':
        app = input('Input the app name: ')
        table.add_apps_purchased(user, app)
    elif purresp == 'No':
        print('Okay.')
    else:
        print('Invalid input.')
 
    #Access Pattern 6
    comresp = input('Would you like to leave comments on a review? Enter Yes or No: ')
    if comresp == 'Yes':
        app=input('Please enter the app name: ')
        appid = query.scan_appname(app)
        query.query_app_reviews(appid)
        revid = input('Please input the review ID you wish to comment on. Please enter with this format, #REVIEW#xxxxx. ')
        comment = input('Please put your comment: ')
        table.add_review_comment(appid, revid, comment)
    elif comresp == 'No':
        print('Okay.')
    else: 
        print('Invalid input.')
    
    #Access Pattern 7    
    payresp = input('Would you like to add a payment method? Enter Yes or No: ')
    if payresp == 'Yes':
        label = input('Please input the label of this payment method: ')
        account_num = input('Please input your account number: ')
        card_type = input('Please input the card type (e.g., Debit, Credit): ')
        expiration_date = input('Please input the expiration date: ')
        security_code = input('Please input the security code: ')
        payment = {
            'username' : user,
            'label' : label,
            'account_num' : account_num,
            'card_type' : card_type,
            'expiration_date' : expiration_date,
            'security_code' : security_code
        }
        table.add_payment_method(payment)
    elif payresp == 'No':
        print('Okay')
    else: 
        print('Invalid input.')
    