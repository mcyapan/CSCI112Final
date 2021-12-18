import appstore_tableops as tableops
import pandas as pd
import csv
from decimal import Decimal
import json
from pprint import pprint

if __name__ == '__main__' :
    appresp = input('Would you like to add apps in your table? Enter Yes or No: ')
    if appresp == 'Yes':
        appfile = input('Please enter the appdata CSV file name: ')
        applist = []
        with open(appfile, 'r') as app:
            for line in csv.DictReader(app):
                line['installs'] = int(line['installs'])
                line['rating'] = Decimal(str(line['rating']))
                applist.append(line)
        for app in applist:
            tableops.add_apps(app)
    elif appresp == 'No':
        print('Okay.')
    else:
        print('Invalid input.')
    
    userresp = input('Would you like to add users in your table? Enter Yes or No: ')
    if userresp == 'Yes':
        userdata = input('Please enter the userdata CSV file name: ')
        user_df = pd.read_csv(userdata)
        userlist = []
        for index, row in user_df.iterrows():
            userdict = row.to_dict()
            userlist.append(userdict)
        for user in userlist:
            tableops.create_user(user)
    elif userresp == 'No':
        print('Okay.')
    else: 
        print('Invalid input.')
    
    osresp = input('Would you like to add operating system and devices in your table? Enter Yes or No: ')
    if osresp == 'Yes':
        osdata = input('Please enter the OSdata CSV file name: ')
        os_df = pd.read_csv(osdata)
        oslist = []
        for index, row in os_df.iterrows():
            osdict = row.to_dict()
            oslist.append(osdict)
        for os in oslist:
            tableops.add_device_os(os)
    elif osresp == 'No':
        print('Okay.')
    else:
        print('Invalid input.')