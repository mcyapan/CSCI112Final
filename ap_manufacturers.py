import appstore_queryops as query 

if __name__ == '__main__' :
    #Access Pattern 10
    osresp = input('Would you like to know how many apps use your OS? Enter Yes or No: ')
    if osresp == 'Yes':
        osname = input('Please input your OS: ')
        query.scan_OS_apps(osname)
    elif osresp == 'No':
        print('Okay.')
    else:
        print('Invalid input.')
    
    deviceresp = input('Would you like to see the devices that host your OS from a specific manufacturer? Enter Yes or No: ')
    if deviceresp == 'Yes':
        os = input('Please input the name of your OS: ')
        manu = input('Please input the name of the manufacturer: ')
        query.query_OS_devices(os, manu)
    elif deviceresp =='No':
        print('Okay.')
    else:
        print('Invalid input.')