import appstore_queryops as query 

if __name__ == '__main__' :
    #Access Pattern 1
    catresp = input('Would you like to display the top 10 apps for each category with respect to its rating? Enter Yes or No: ')
    if catresp == 'Yes':
        top10cat = input('Please input the category you wish to display: ')
        query.query_category(top10cat)
    elif catresp == 'No':
        print('Okay.')
    else:
        print('Invalid input.')
    
    #Access Pattern 2
    cardresp = input('Would you like to determine how many users use a certain card type? Enter Yes or No: ')
    if cardresp == 'Yes':
        card = input('Please input the card type you want to count: ')
        query.scan_cardtype(card)
    elif cardresp =='No':
        print('Okay.')
    else:
        print('Invalid input.')