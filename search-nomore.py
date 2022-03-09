import tweepy
import telegram
import urllib
from time import sleep
from time import sleep
from googletrans import Translator
import googletrans
from langdetect import detect
##print(googletrans.LANGUAGES)
translator = Translator()



# authorization tokens
consumer_key = "sTIlpB6wz9HCTXAA3SBmWGJES"
consumer_secret = "F5IF1cmnAADOydZJxGDijuk9yqCwfTPXiyMJaHv569ROro174s"
access_key = "1428032855901360130-SaJUkxqVUa93L8GOutFKbOHKiRdd3G"
access_secret = "ByvofuTomsJgDRtqThHhlQS7BZ1d6E3G8pCaapg4gO8e2"
tokenn= '5033218035:AAETIDgJnW16KxHG2hzDbhyC2lvk784Kr4o'
bot = telegram.Bot(tokenn)


# StreamListener class inherits from tweepy.StreamListener and overrides on_status/on_error methods.
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
##        print(status.id_str)
        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        try:
            is_retweet = hasattr(status, "retweeted_status")
            is_reply = hasattr(status, "replied_status")
    ##        print("repling text: "+str(is_reply))

            # check if text has been truncated
            if hasattr(status,"extended_tweet"):
                text = status.extended_tweet["full_text"]
            else:
                text = status.text

            # check if this is a quote tweet.
            is_quote = hasattr(status, "quoted_status")
            quoted_text = ""
            if is_quote:
                # check if quoted tweet's text has been truncated before recording it
                if hasattr(status.quoted_status,"extended_tweet"):
                    quoted_text = status.quoted_status.extended_tweet["full_text"]
                else:
                    quoted_text = status.quoted_status.text

            # remove characters that might cause problems with csv encoding
            remove_characters = [",","\n"]
            for c in remove_characters:
                text.replace(c," ")
                quoted_text.replace(c, " ")
                urr="https://twitter.com/"+status.user.screen_name+"/status/"+str(status.id)

            with open("out.csv", "a", encoding='utf-8') as f:

                if ("@"+status.user.screen_name in userss) and not(status.in_reply_to_screen_name):
                    print("==========================================")
                    print(status.text)
                    print(status.user.name)
                    print(is_retweet)
                    tex=text
                    if is_retweet==True:
                        tex=""
                    srl=""
                    print("replying to: "+str(status.in_reply_to_screen_name))
                    try:
                        srl=detect(text)
                    except:
                        pass
                    dest="am"
                    print(srl)
                    if srl!="":
                        result = translator.translate (text, src=srl, dest=dest)
                        bot.send_message('@Twitter_campaign_arch', "<b>"+status.user.name+"</b>"+"\n"+text+"\n"+"\n<b>ትርጉም-በጉግል </b>\n"+result.text+"\n"+urr,
                  parse_mode=telegram.ParseMode.HTML)
                    else:
                        bot.send_message('@Twitter_campaign_arch', "<b>"+status.user.name+"</b>"+"\n"+text+"\n"+urr,
                  parse_mode=telegram.ParseMode.HTML)

                    sleep(5)
                    print(urr)
                    print("==========================================")
                f.write("%s,%s,%s,%s,%s,%s\n" % (status.created_at,status.user.screen_name,is_retweet,is_quote,text,quoted_text))
        except tweepy.TweepError as e:
            print("found error and passing")
            print(e.reason)
            pass

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        pass
        #sys.exit()

if __name__ == "__main__":
    # complete authorization and initialize API endpoint
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    userss=[]
    tags=[]
    list_id ='1464623954174304267'
    members = api.list_members(list_id = list_id, count = 5000)
    print(len(members))
    for member in members:
        userss.append("@"+member.screen_name)
        tags.append(member.id_str)
##        print(member.screen_name)
##    userss=['@EthiopiaResili1','@iyoba4u',  '@eslemanabayy','@suleimanabdell7','@PMEthiopia','@SahleWorkZewde','@FdreService']

    # initialize stream
    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended_tweet')
    with open("out.csv", "w", encoding='utf-8') as f:
        f.write("date,user,is_retweet,is_quote,text,quoted_text\n")

##    tags = ["1446212160737136647",' 3740334387','1040994514280886272','1398373401434206209','1059015168263417858','2862321934','1451174958021873664']
    while(1):
        try:
            stream.filter(follow=tags)
        except:
            print('pass')
            pass