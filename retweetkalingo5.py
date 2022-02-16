import tweepy
from time import sleep
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME
import yaml
import sys
import random
import gspread
import pandas as pd
from datetime import datetime
import pytz
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)
creds2 = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
# authorize the clientsheet
client = gspread.authorize(creds2)
client2 = gspread.authorize(creds2)
# get the instance of the Spreadsheet
sheet = client.open('counter')
#sheet2 = client.open('Auth')
sheet2 = client2.open('Auth')
# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)
#sheet_instance = sheet.sheet1
sheet_instanceA = sheet2.get_worksheet(0)




##ky=input("Enter Twitter APP No: ")
##twitter_api="twitter_api"+ky
# Open the file function
def process_yaml(yamlfile):
    with open(yamlfile) as file:
        return yaml.safe_load(file)

# Access API/app/consumer key function
def app_key(data,i):
    twitter_api="twitter_api"+str(i)
    return data[twitter_api]["app_key"]

# Access API/app/consumer secret function
def app_secret(data,i):
    twitter_api="twitter_api"+str(i)
    return data[twitter_api]["app_secret"]

# Access oauth_token function
def oauth_token(data,i):
    twitter_api="twitter_api"+str(i)
    return data[twitter_api]["oauth_token"]

# Access oauth_token_secret function
def oauth_token_secret(data,i):
    twitter_api="twitter_api"+str(i)
    return data[twitter_api]["oauth_token_secret"]

##data =  process_yaml()
##CONSUMER_KEY = app_key(data)
##CONSUMER_SECRET = app_secret(data)
##ACCESS_KEY = oauth_token(data)
##ACCESS_SECRET = oauth_token_secret(data)
##auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
##auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
##auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
##auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#ua = UserAgent()
#proxies = get_proxies(ua)

##port=input('insert the proxy port: ')
global apis,apis_filtered,errors,usersr
errors={}
apis=[]
apis_filtered=[]
def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

def assign(rt):
    global count
    global apis,apis_filtered,errors
    rests=(300*len(apis_filtered))+1
    count+=1
    modul=20
    last_row = str(int(next_available_row(sheet_instance))-1)
    last_count=sheet_instance.acell('B'+last_row).value
    next_row = next_available_row(sheet_instance)
    last_date=sheet_instance.acell('A'+last_row).value

    today=datetime.now(pytz.timezone('Africa/Addis_Ababa')).strftime('%Y-%m-%d')
    time = datetime.now(pytz.timezone('Africa/Addis_Ababa')).strftime("%H:%M:%S")
    #print(count)
    if count % modul==0:
##        st.text(count)
        if datetime.fromisoformat(datetime.now(pytz.timezone('Africa/Addis_Ababa')).strftime('%Y-%m-%d'))>datetime.fromisoformat(last_date):
            sheet_instance.update_acell("A{}".format(next_row), today)
            sheet_instance.update_acell("B{}".format(next_row), modul)
            #sheet_instance.update_acell("C{}".format(next_row), modul)
            count=modul
        else:
            gscount=int(last_count)+modul
            sheet_instance.update_acell("B{}".format(last_row), gscount)
    if count>rests:
        count=1
    return	count
# StreamListener class inherits from tweepy.StreamListener and overrides on_status/on_error methods.
class StreamListener(tweepy.StreamListener):

    def on_status(self, status):


##        print(status.id_str)
        global apis,apis_filtered,errors,usersr

        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        global accs,configacc,configacc2
        global count
        try:
          #self.retweet(staus.id)
##          api.retweet(status.id)
##          api.create_favorite(status.id)
          #print('Retweeting users: @'+status.user.screen_name)

          #sleep(SLEEP_TIME)
          i=1
          modul=20
          apii=''
          rt=0
          selected=0
          if accs>1:
              selected=random.randint(0, accs-1)
          elif accs==0:
              configacc=configacc2.copy()
              for ap in apis_filtered:
                  apis.append(ap)
##                  apis=apis_filtered
              accs=len(apis_filtered)

##              selected=random.randint(0, len(apis))
         # print("========================================================================")
          #print("------------------------------------------------------------------------")
##          print(configacc[selected])
          if count % modul==0:
            print(configacc[selected])
          #print("--------------------------")
          lists = ['EthiopiaResili1','OI1LnOY3iWbQlWT','SecondLine18','kaleabhaile8','5iiOZuZTr4kWBVY','mare69509315','HahuL07']
          if status.user.screen_name not in lists:
         # if (status.user.screen_name not in configacc2) :



              counter2=count
              try:
                apis[selected].retweet(status.id_str)
                try:
                    apis[selected].create_favorite(status.id_str)
                except:
                    pass
                rt+=1
                counter2=assign(rt)
                if count % modul==0:
                 print("========================================================================")
                apis.pop(selected)
                configacc.pop(selected)
                accs-=1
                if count % modul==0:
                     print(str(counter2)+'. '+ 'Retweeting users: @'+status.user.screen_name)
                     #get_apis()
                counter2+=1
                minsleep=int(36/len(apis_filtered)-1)+1
                sleep(random.randrange(minsleep,18-len(apis_filtered)))

              except tweepy.TweepError as e:
                print(e.reason)
                if errors[configacc[selected]]>=11:
                    configacc.pop(selected)
                    accs-=1
                else:
                    errors[configacc[selected]]+=1
                #print("-----------------------------------------++++ERROR++++-------------------------------------- @"+str(count))
##                print("Errored Id: "+str(status.id))
                pass


##              for apii in apis:
####                    if  i!=1:
##                    print("Account "+str(i)+" retweeting...")
##                    print("____________________________________________")
##                    try:
##
####                            apii.retweet(status.id_str)
####                            apii.create_favorite(status.id_str)
##
##
##                        rt+=1
##                    except tweepy.TweepError as e:
##                        print(e.reason)
##                        print("Errored Id: "+str(status.id))
##                        pass
##                    i+=1

##              if rt>0:

              rests=(300*len(apis_filtered))
              if counter2>=rests+1:
              	print('limit reached')
              	#get_apis()
              	sleep(15*60)
              	counter2=0
              	count=1
          	#sys.exit()



        except tweepy.TweepError as e:
        	print(e.reason)
        	pass

    	#status.retweet()
    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        pass

def get_apis():
    global apis,apis_filtered,errors,configacc2,configacc,usersr
    apis=[]
    apis_filtered=[]
    errors={}
    configacc=[]
    configacc2=[]
    usersr=[]
    k=1
    for item in sheet_instanceA.col_values(1)[1:]:
        usersr.append(sheet_instanceA.col_values(2)[k])
        k+=1
    j=1
    end=int(len(sheet_instanceA.col_values(1)[1:])/2)+1
##    j=end
    for item in sheet_instanceA.col_values(1)[1:end]:
    ##    print(item,sheet_instanceA.col_values(2)[i],sheet_instanceA.col_values(3)[i],sheet_instanceA.col_values(4)[i],sheet_instanceA.col_values(5)[i],sheet_instanceA.col_values(6)[i])
        CONSUMER_KEY = sheet_instanceA.col_values(3)[j]
        CONSUMER_SECRET = sheet_instanceA.col_values(4)[j]
        ACCESS_KEY = sheet_instanceA.col_values(5)[j]
        ACCESS_SECRET = sheet_instanceA.col_values(6)[j]
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
    ##    print(api.retweets_of_me())
        apis.append(api)
        apis_filtered.append(api)
        configacc.append(sheet_instanceA.col_values(2)[j])
        configacc2.append(sheet_instanceA.col_values(2)[j])
        errors[sheet_instanceA.col_values(2)[j]]=0
        j+=1

    print(len(apis))

if __name__ == "__main__":
    #global counter
    global accs,configacc,configacc2,usersr
    #global apis,apis_filtered,errors

##    configacc=['EthiopiaResili1','OI1LnOY3iWbQlWT','SecondLine18','kaleabhaile8','5iiOZuZTr4kWBVY','mare69509315']
##    configacc=['EthiopiaResili1','SecondLine18','kaleabhaile8']
##   #configacc.pop(1)
####    configacc2= ['EthiopiaResili1','OI1LnOY3iWbQlWT','SecondLine18','kaleabhaile8','5iiOZuZTr4kWBVY','mare69509315']
##    configacc2=['EthiopiaResili1','SecondLine18','kaleabhaile8']
    #configacc2.pop(1)
    get_apis()
    '''
    RETWEET APP

    '''

#########################THIS TWO LINES REMOVE RESILIANCE ACCOUNT FROM RETWEETING#################################################
    #apis.pop(0)
    #apis_filtered.pop(0)
###########################################################################################################################

    # complete authorization and initialize API endpoint
    accs=len(apis_filtered)
    userss=['@5iiOZuZTr4kWBVY','@kaleabhaile8','@SecondLine18','@EthiopiaResili1','@mare69509315','@OI1LnOY3iWbQlWT']
    #userss.pop(5)
    count=0
    streamListener = StreamListener()
    randd=random.randint(0,len(apis_filtered)-1)
    stream = tweepy.Stream(auth=apis_filtered[randd].auth, listener=streamListener,tweet_mode='extended_tweet')


    tags = ['#AmharaGenocide','#TPLFistheGenocider','#TPLFTerroristGroup','#TplfIsWarCriminal','#DisarmTPLF','#NoNegotiationWithTPLF','#TPLFTerrorists','#Afarunderattack','#AfarGenocide','#AfarMassacre','#AfarCantWait','#AfarIsBleeding','#afar ','#TPLFMustGo','#PermanentUNSCSeat4Africa']
    while True:
        try:
            stream.filter(track=tags)
            print("working")
        except Exception as e:
        	print(e)
        	pass
       # print('pass')

