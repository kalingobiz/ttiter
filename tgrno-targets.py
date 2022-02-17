import tweepy
from time import sleep

import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import yaml
##ky=input("Enter Twitter APP No: ")
##twitter_api="twitter_api"+ky
# Open the file function


import csv
import gspread
import pandas as pd
from datetime import datetime
import pytz
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('counter')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(2)
#sheet_instance = sheet.sheet1



def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)


def assign(rt):
    global count,targets
    print(rt)
    if rt not in targets.keys(): 
        targets[rt]=1
    else:
        targets[rt]+=1
        print(targets[rt])
   
    if count%50==0:
        data=[]
        for key,values in targets.items():
            data.append([key,values])
        output_DataFrame = pd.DataFrame(data, columns = ['screen_name',  'tweets'])
        output_DataFrame.to_csv('targets.csv', index=False)
    return	count+1


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):

        cou=assign(status.user.screen_name)
    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        #sys.exit()
        pass

if __name__ == "__main__":
    global count,targets
    file=open('targets.csv')
    targets={}
    for row in file.readlines()[1:]:
        key,value=row.replace('\n','').split(',')
        targets[key]=int(value)
    
    # complete authorization and initialize API endpoint
    count=0
    CONSUMER_KEY = 'om0tOOHNviZlKD09b6GCzqUFR'
    CONSUMER_SECRET = 'jemMbR68ZcGj31LRxY279gU18piPyOVtjdZDHMP1JugMiFNcz3'
    ACCESS_KEY = '1441749230666739713-7BVEEuejo6Yx6d7kvklAPwKtNvj7vv'
    ACCESS_SECRET = 'ThDYnLv65iOX3acsh8Gscua1WW9AXDOlzEhhCS3jIW6kO'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    # initialize stream
    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended_tweet')
    tags = ["#NoMore"]
##    tags = ["#NoMore"]
    tags = ['#TigrayGenocide']
    while True:
##        try:
            stream.filter(track=tags)
##        except:
##            print('pass')
##            pass
