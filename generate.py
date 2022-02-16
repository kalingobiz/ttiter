import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import urllib
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
from datetime import datetime
import telegram
tokenn= '5072669226:AAEIJhRsmNCqoY3WATCUuiIhB1L1LTGs4AU'
bot = telegram.Bot(tokenn)


x1=''
x=''
x2=''
import requests
from bs4 import BeautifulSoup
def unity(ur='https://www.unityforethiopia.net/twitter-campaign-33/'):
    proxy = {'https': '127.0.0.1:58732'} 
    # page = requests.get("https://www.unityforethiopia.net/tweets-for-today-2/",proxies=proxy)
    
    uurls=[ur
           ]
    msg=["UNITY FOR ETHIOPIA TWITTER CAMPAIGN"]
    
    
    for uurl in uurls:
        
         page = requests.get(uurl)
    
         soup = BeautifulSoup(page.content, 'html.parser')
         todtweet=soup.find_all('a', class_='ss-ctt-tweet')
    
        
         for tw in todtweet:
            msg.append(tw.get_text() +" ")
            
    return msg
def ettruth(ur='https://ethiopiantruth.com/ethiopia-is-a-sovereign-never-colonized-country/'):
    msg=[]
    proxy = {'https': '127.0.0.1:60889'} 
    # for uurl in uurls:
        
    #     page = requests.get(uurl)
    
    #     soup = BeautifulSoup(page.content, 'html.parser')
    #     todtweet=soup.find_all('a', class_='ss-ctt-tweet')
#    page = requests.get("https://ethiopiantruth.com/2021/07/07/the-gerd-grand-ethiopian-renaissance-dam-is-a-development-project-not-a-peace-security-issue-involving-un-security-council-is-inappropriate-2/")
#
#    soup = BeautifulSoup(page.content, 'html.parser')
#    todtweet=soup.find_all('span', class_='bctt-ctt-text')
##    todtweet=soup.find_all('a', class_='ssctt-tweet')
#        
#    for tw in todtweet:
#        msg.append(tw.get_text() +" ")
#    # # msg=['#GERD is not luxury. #FillTheDam #Ethiopia #ItsMyDam',
#    #      'More than 60 million Ethiopians have no electricity. #Ethiopia #ItsMyDam',
#    #      'In 21 century electricity is not luxury. #Ethiopia #ItsMyDam ']
#    
#        
    uurls=[ur ]
  
    
##    msg=['#TPLFisaTerroristGroup has been recruiting child soldiers as cannon fodders when attacking & massacring #Amhara. It must be clear that recruiting child soldiers is violation of International laws. #WolkaitIsAmhara #RayaIsAmhara #ChildrenNotSoldiers',
#         'Allowing #TPLFisaTerroristGroup to get control of Northern Amhara region means allowing #MaikadraMassacre to happen again. It was recalled that over 1000 ethnic #Amhara were massacred by retreating TPLF forces. Millions of Amhara are in danger again. ',
#         'Amharas are under existential threat as #TPLFisaTerroristGroup continues its expansionist & genocidal war against ethnic Amhara particularly and all Ethiopians in general. Z group vows to attack Amhara time and again. Many have been victims of TPLF attacks.  #WolkaitIsAmhara #RayaIsAmhara ',
#         'Two weeks after unilateral ceasefire on government side, #TPLFisaTerroristGroup has invaded Amhara region & massacred civilians. Where is the media coverage? #WolkaitIsAmhara #RayaIsAmhara #ChildrenNotSoldiers',
#         'Many civilians have been killed by TPLF after z withdrawal of ENDF from Tigray. PM @AbiyAhmedAli & ENDF has made z irresponsible decision to withdrew & abandon civilians to #TPLFisaTerroristGroup.  Both parties need to be held accountable for z massacre. #WolkaitIsAmhara #RayaIsAmhara #Ethiopia',
#         'Spokesperson of #TPLFisaTerroristGroup, Getachew Reda said “Tigray forces will settle a score with Amhara”. This is a genocidal statement from TPLF and no international body has taken any measure or condemned it. #WolkaitIsAmhara #RayaIsAmhara #Ethiopia',
#         'During a brief recapture of #RayaIsAmhara areas, #TPLFisaTerroristGroup has taken retaliation measures against ethic #Amharas by massacring civilians. When will international community draw lessons about TPLF evil actions? Where is the media coverage? #WolkaitIsAmhara #Ethiopia',
#         '#TPLFisaTerroristGroup is not fighting the war, it\'s using civilians as human shield! The international community should understand the true nature of TPLF. Ethiopians said enough to TPLF rule. #WolkaitIsAmhara #RayaIsAmhara #Ethiopia #ChildrenNotSoldiers',
#         'The international community must condemn TPLF\'s evil acts. The terrorist group is using child soldiers. Unfortunately, international media such as The New York Times romanticized those child soldiers as young fighters. #TPLFisaTerroristGroup #ChildrenNotSoldiers',
#         'TPLF, the terrorist group in Ethiopia vows to wipeout Amharas from their ancestral lands #WolkaitIsAmhara and #RayaIsAmhara.  #Ethiopia #TPLFisaTerroristGroup #ChildrenNotSoldiers',
#         'TPLF, the terrorist group in Ethiopia, is abducting and killing Eritrean Refugees in Tigray region. This is violation of international laws. #TPLFisaTerroristGroup #WolkaitIsAmhara #RayaIsAmhara #Ethiopia',
#         '#USA and #EU stop the double standard, and condemn TPLF\'s criminal acts. Ethiopians said enough to #TPLFisaTerroristGroup long ago. #WolkaitIsAmhara #RayaIsAmhara #Ethiopia #ChildrenNotSoldiers',
#         '#TPLFisaTerroristGroup is recruiting arming & deploying child  soldiers and The New York Times @nytimes featured a story by @declanwalsh where pictures of these children were cast \'young recruits\'. This act should be condemned. #WolkaitIsAmhara #RayaIsAmhara #ChildrenNotSoldiers',
#         'Recruiting and using children as soldiers is prohibited under inter\'al humanitarian law – treaty & custom – and is defined as war crime by z ICC. #TPLFisaTerroristGroup  recruited and used children violating inter\'al laws. #WolkaitIsAmhara #RayaIsAmhara #Ethiopia #ChildrenNotSoldiers',
#         'Tekeze river is z natural boundary between Tigray and Gondar of Amhara region. There is no "Western Tigray" in Amhara areas. #TPLFisaTerroristGroup annexed Wolkaite and Raya in 1991 and it wants to reannex again. People said No to TPLF! #WolkaitIsAmhara #RayaIsAmhara #ChildrenNotSoldiers']
#    
    for uurl in uurls:
        
         page = requests.get(uurl)
    
         soup = BeautifulSoup(page.content, 'html.parser')
         todtweet=soup.find_all('span', class_='bctt-ctt-text')
    
        
         for tw in todtweet:
            msg.append(tw.get_text() +" ")
            
    return msg

def defend():
    msg=[]
    ddriver = webdriver.Firefox()
        
    ddriver.get('https://defendethiopia.com/twittercampaign-2')
    
    time.sleep(20)
    ss=ddriver.find_elements_by_class_name('ctt-font-original')

    for tw in ss:
        msg.append(tw.text +" ")
    
    ddriver.quit()
    return msg

 
def zemacham(ur='http://www.zemach-amhara.com/twitter'):
    page = requests.get(ur)
    soup = BeautifulSoup(page.content, 'html.parser')
    todtweet=soup.find_all('div', class_='tweet_container')
    msg=[]

    for tw in todtweet:
            msg.append(tw.find('p').get_text() +" ")
            
    return msg
    
def esleman(ur='http://www.zemach-amhara.com/twitter'):
    page = requests.get(ur)
    soup = BeautifulSoup(page.content, 'html.parser')
    todtweet2=soup.find_all('span', class_='bctt-ctt-text')
    msg=[]

    for tw in todtweet2:
        msg.append(tw.get_text() +" ")
            
    return msg

def amharanet():
    page = requests.get('https://www.amhara.net/tweets')
    soup = BeautifulSoup(page.content, 'html.parser')
    todtweet=soup.find_all('div', class_='_1Q9if')
    msg=[]
    todtweet2=todtweet[5:len(todtweet)]
    for tw in todtweet2:
            msg.append(tw.get_text() +" ")
            
    return msg

def cyberfano():
    msg=[]
    ddriver = webdriver.Firefox()
        
    ddriver.get('https://www.cyberfano.org/twitter')
    time.sleep(10)
    camp=ddriver.find_elements_by_class_name('campaignNameTwitterCampaignTitles')
    print(len(camp))
    while 1:
        options = input('Enter  which campaign to tweet or X to quite: ')
        if options=="X":
            break
        camp[int(options)-1].click()
        
        
        ss=ddriver.find_elements_by_class_name('card-text')
        
        for tw in ss:
            if tw.text!='':
                msg.append(tw.text +" ")
            
    return msg
def lehager():
    page = requests.get("https://lehager.org/click-to-tweet/")
      
    soup = BeautifulSoup(page.content, 'html.parser')
    todtweet=soup.find_all('span', class_='bctt-ctt-text')
    todtweet2=soup.find_all('div', class_='wp-block-ub-content-toggle-accordion')
    melkt=todtweet2[0].find_all('span', class_='bctt-ctt-text')
    arst=todtweet2[0].find_all('p', class_='wp-block-ub-content-toggle-accordion-title ub-content-toggle-title-008ec0a7-e41c-4127-8bb5-a81c07dffede')
##    print(arst[0].get_text())
##    print(melkt[0].get_text())
    msgo=["LEHAGER TWITTER CAMPAIGN " +arst[0].get_text()] 
    for tw in melkt:
        msgo.append(tw.get_text() +" ")
##    print(msgo[0])
    return msgo


def buzz_ethio(ur='https://linktr.ee/buzz_ethio'):
         page = requests.get(ur)
         soup = BeautifulSoup(page.content, 'html.parser')
         todtweet=soup.find_all('div', class_='pkAuV')
         msg=["@buzz_ethio TWITTER CAMPAIGN"]
     
         for tw in todtweet:
             msg.append(tw.find('p').get_text() +" ")
     
         return msg[:len(msg)-4]

def nomorehub(ur='https://linktr.ee/NoMoreHUb'):
         page = requests.get(ur)
         soup = BeautifulSoup(page.content, 'html.parser')
         todtweet=soup.find_all('div', class_='pkAuV')
         msg=[]
     
         for tw in todtweet:
                 msg.append(tw.find('p').get_text() +" ")
     
         return msg
	
print("1. unity for Ethiopia")
print("2. Ethiopian truth")
print("3. defend Ethiopa")
print("4. zemach Amhara")
print("5. Amhara.net")
print("6. CyberFano")
print("7. Esleman")
print("8. from file")
print("9. Lehager")
print("10. buzz_ethio")
print("11. NoMoreHUb")
print("0. Quit")
                                #OPTIONS BLOCK COMMENTED FOR TEST
####################################################################################################################################################
##options = input('Enter  your option: ')
##options=int(options)
##
##ur = input('Enter the url: ')
##msg=[]
##if options==1:
##	msg=unity(ur)
##elif options==2:
##	msg=ettruth(ur)
##elif options==3:
##	msg1=defend()
##	rang=input("How many messages to extract")
##	msg=msg1[:int(rang)]
##elif options==4:
##	msg=zemacham(ur)
##
##elif options==5:
##	msg=amharanet()
##elif options==6:
##	msg=cyberfano()
##    
##elif options==7:
##	msg=esleman(ur)
##elif options==8:
##	file=open('msg.txt', encoding="utf-8")
##	x=file.readlines()
##	for ms in x:
##		msg.append(ms.replace('\n',''))
##elif options==9:
##	msg1=lehager()
##	rang1=input("How many messages to extract start: ")
##	rang2=input("How many messages to extract end: ")
##	msg=msg1[int(rang1):int(rang2)]
##
##elif options==10:
##	msg=buzz_ethio()
##elif options==11:
##	msg=nomorehub()
##############################################################################################################

def savetofile(message):	
    print(len(message))
    # xx=msg[1].replace('\r\n',' ')
    fname=input("insert the file name: ")
    textfile = open(f"{fname}.txt", "a+",encoding="utf-8")
    for element in message:
        # xx=msg[1].replace('\r\n',' ')
        element=element.replace('\r\n',' ')
        element=element.replace('“','"')
        element=element.replace('”','"')
        textfile. write(element + "\n")
    textfile.close()
#textfile.


def executer(message2,web,title):
    ttl=message2[0]
    today=datetime.today().strftime('%Y-%m-%d')

    titlemess=ttl+" "+title+"\
    \n💚💚💚💚💚💚💚💚💚\
    \n💛💛 🕊  ሰላም  🕊 💛💛\
    \n❤️❤️❤️❤️❤️️❤️️❤️️❤️️❤️ \
    \n 👇👇👇👇👇👇\
    \n"+ title+' \n 👆👆👆👆👆 \n '+web
    
    res=bot.send_message('@Twitter_campaign_arch',text=titlemess)
    bot.pin_chat_message(res["chat"]["id"],res["message_id"])
    sleep(3)
    i=1
    
    file=open('today-tweets-'+today+'.txt','a+',encoding="utf-8")
    for element in message2[1:]:
    # xx=msg[1].replace('\r\n',' ')
        element=element.replace('\r\n',' ')
        element=element.replace('“','"')
        element=element.replace('”','"')
        print(element + "\n")
        rl=f'https://twitter.com/intent/tweet?text={element}'
        ur2=urllib.parse.quote_plus(rl,safe="/:?=")
        message2="<b>"+str(i)+ '. '+" </b>" + "\n"+element.replace('\n','')+"\n CLICK 👇 TO TWEET \n" +ur2
        bot.send_message('@Twitter_campaign_arch', message2, parse_mode=telegram.ParseMode.HTML)
        file.write(element+"\n")
        i+=1
        sleep(3)
    file.close()
import gspread
import pandas as pd
from datetime import datetime
import pytz
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('creds-trends.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('trends')

# get the first sheet of the Spreadsheet
sheet_instanceu = sheet.get_worksheet(1)
sheet_instancel = sheet.get_worksheet(2)
sheet_instanceb = sheet.get_worksheet(3)
#sheet_instance = sheet.sheet1
i=0
xs=[]
ys=[]
for item in sheet_instancel.col_values(2):
    if i==0:
        i+=1
        continue
    if int(item)%60<3:
        xs.append(sheet_instancel.col_values(1)[i])
##            print(float(xx[i])+3)
        ys.append(item)
    i+=1


def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)        
##lastdate=datetime.today().strftime('%Y-%m-%d')
lastdate="2022-02-03"
print("Last date: "+lastdate)
prevlehagercount=575
unityprevcamp=178


ur=sheet_instanceu.col_values(1)[1]
status=[]
status.append(sheet_instanceu.col_values(2)[1])
prevlehagercount=int(sheet_instancel.col_values(1)[1])
status.append(sheet_instancel.col_values(2)[1])
status.append(sheet_instanceb.col_values(2)[1])
blasttweet=sheet_instanceb.col_values(3)[1]
llasttweet=sheet_instancel.col_values(3)[1]
ulasttweet=sheet_instanceu.col_values(3)[1]
lastdate=sheet_instanceu.col_values(4)[1]

print(ur)


##message=unity(ur)
##print(len(message))
while(1):
    
    today=datetime.today().strftime('%Y-%m-%d')
    
    print(today==lastdate)
    buzz=buzz_ethio()
    if today!=lastdate:
        print("today date: "+today)
        if int(status[2])==1 and blasttweet != buzz[len(buzz)-1]:
            
            
            web='https://linktr.ee/buzz_ethio'
            print("=====================================================================================")
            print("BUZZ_ETHIO")
            print("=====================================================================================")
##            sheet_instanceb.update_acell("B2", 0)
            sheet_instanceb.update_acell("C2", buzz[len(buzz)-1])
            sheet_instanceb.update_acell("D2", today)
            executer(buzz,web,today)
        
##        lehagerm=lehager()
##        )
        print(llasttweet)
        lehagerm=lehager()
        print(lehagerm[len(lehagerm)-1])
        if llasttweet != lehagerm[len(lehagerm)-1]:
            print(len(lehagerm[0]))
            web="https://lehager.org/click-to-tweet/"
##            print(lehagerm[543])
            message=[lehagerm[0]]
            for lhgr in lehagerm[1:]:
                message.append(lhgr)
##            message=lehagerm[prevlehagercount+1:len(lehagerm)]
            print("=====================================================================================")
            print("LEHAGER")
            print("=====================================================================================")
            executer(message,web,today)
            prevlehagercount=len(lehagerm)
            sheet_instancel.update_acell("A2", prevlehagercount)
##            sheet_instancel.update_acell("B2", 0)
            sheet_instancel.update_acell("C2", lehagerm[len(lehagerm)-1])
            sheet_instancel.update_acell("D2", today)
##        ur="https://www.unityforethiopia.net/twitter-campaign-"+str(unityprevcamp+1)
        try:
            message=unity(ur)
            
            if int(status[0])==1 :
                
                print("=====================================================================================")
                print("UNITY FOR ETHIOPIA")
                print("=====================================================================================")
                web=ur
                executer(message,web,today)
                unityprevcamp+=1
                sheet_instanceu.update_acell("B2", 0)
                sheet_instanceu.update_acell("D2", today)
                sheet_instanceu.update_acell("C2", message[len(message)-1])
        except:
            print("Unity for Ethiopia did not release campaign "+str(unityprevcamp+1))
            pass
        print("*****************************END OF TODAY FETCHING*****************************")
        lastdate=today
    else:
       print("*****************************THERE IS NOTHING TO FETCHING*****************************") 
        

    sleep(3600)
    
