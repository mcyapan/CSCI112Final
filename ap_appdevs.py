import appstore_queryops as query 
import appstore_tableops as table

if __name__ == '__main__' :
    #Access Pattern 8
    catresp = input('Would you like to display apps for a certain category with a greater number of installs than a specific number? Enter Yes or No: ')
    if catresp == 'Yes':
        cat = input('Please input the category you wish to display: ')
        installs = input('Please input the minimum number of installs: ')
        query.query_category_installs(cat, installs)
    elif catresp == 'No':
        print('Okay.')
    else:
        print('Invalid input.')
    
    devresp = input('Would you like to see the apps from a specific developer? Enter Yes or No: ')
    if devresp == 'Yes':
        dev = input('Please input the developer name: ')
        query.query_developer(dev)
    elif devresp =='No':
        print('Okay.')
    else:
        print('Invalid input.')
    
    #Access Pattern 9
    descresp = input('Would you like to update an app descripton? Enter Yes or No: ')
    if descresp == 'Yes':
        appid = input('Please input the app id: ')
        appname = input('Please input the app name: ')
        app_desc = input('Please input the updated app description: ')
        table.add_appdesc(appid, appname, app_desc)
    elif devresp =='No':
        print('Okay.')
    else:
        print('Invalid input.')  