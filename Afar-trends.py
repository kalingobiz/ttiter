import tweepy
from time import sleep

import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import yaml
##ky=input("Enter Twitter APP No: ")
##twitter_api="twitter_api"+ky
# Open the file function



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
    global count
    count+=1
    modul=10
    print(count)
    if count%modul==0:
        last_row = str(int(next_available_row(sheet_instance)))
        next_row = next_available_row(sheet_instance)
        last_a=sheet_instance.acell('A'+last_row).value
        last_date=sheet_instance.acell('C'+last_row).value
        last_time=sheet_instance.acell('D'+last_row).value
        last_count=sheet_instance.acell('F'+last_row).value
        today=datetime.now(pytz.timezone('Africa/Addis_Ababa')).strftime('%Y-%m-%d')
        
        time = datetime.now(pytz.timezone('Africa/Addis_Ababa')).strftime("%H:%M:%S")
        cuhr,cumint,cusec=time.split(':')
        shhr,shmint,shsec=str(last_time).split(':')


        if datetime.fromisoformat(datetime.now(pytz.timezone('Africa/Addis_Ababa')).strftime('%Y-%m-%d'))>datetime.fromisoformat(last_date) :
            dtime = datetime.now(pytz.timezone('Africa/Addis_Ababa')).strftime("%Y-%m-%d %H:%M:%S")

            sheet_instance.append_row([last_a,rt,today,time,dtime,rt])
    #        sheet_instance.update_acell("A{}".format(next_row), today)
    ##        sheet_instance.update_acell("B{}".format(next_row), rt)
    ##        sheet_instance.update_acell("C{}".format(next_row), time)
            count=1
        elif int(cuhr) > int(shhr):

            gscount=int(last_count)+rt
            dtime = datetime.now(pytz.timezone('Africa/Addis_Ababa')).strftime("%Y-%m-%d %H:%M:%S")
            sheet_instance.update_acell("F{}".format(next_row), gscount)
##            sheet_instance.append_row([last_a,gscount,today,time,dtime])
        else:
            gscount=int(last_count)+modul
            sheet_instance.update_acell("F{}".format(last_row), gscount)

    return	count


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):

        cou=assign(1)
    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        #sys.exit()
        pass

if __name__ == "__main__":
    # complete authorization and initialize API endpoint
    count=0
    CONSUMER_KEY = 'xgF9uHYUyxdYx7vfnBJcd38b6'
    CONSUMER_SECRET = 'Ci5iphY4mgllSjeZmNQ2leyzflZwNvZ8BopeTJlhnPMSjM6Im6'
    ACCESS_KEY = '1446545295681130502-M0nJP1Z1LpRzmjyRumyFmmfHKGbXh7'
    ACCESS_SECRET = '0e1tZ8jwLezIO7WWaNJ2DpblQ7DG6PwlvydNzZ5JQCft8'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    # initialize stream
    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended_tweet')
    tags = ["#NoMore"]
##    tags = ["#NoMore"]
    tags = ['#Afarunderattack','#AfarGenocide','#AfarMassacre','#AfarCantWait','#AfarIsBleeding','#afar ']
    while True:
        try:
            stream.filter(track=tags)
        except:
            print('pass')
            pass
