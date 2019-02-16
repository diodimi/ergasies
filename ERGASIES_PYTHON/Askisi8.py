import tweepy
import sys


consumer_key = "ZCYgdNKycYTWUB6IReeqmqish"
consumer_secret = "xm4gKvCaQVxTnAHlbXmH46MhqJbw0FCVAq72hsayMSo06rdndP"
access_key="1426498003-PMr1Fds4lCJulrjRMd3wsYZfKLXXeIez0uOveqt"
access_secret="3JmD7iedgX2auVOsQQPdEF5E0mlZsLp6mtPsJZ8nWxwar"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api=tweepy.API(auth)

def gnm(name):
    try:
        user =api.get_user(name)
        foll=(user.friends_count)
        stuff = api.user_timeline(id = name, count = 10, include_rts = False,tweet_mode='extended')
        sum_tweet=0
        for tweet in stuff:
            text=(tweet.full_text).split()#Spao to kathe post se lekseis 
            sum_tweet+=len(text)
        return(sum_tweet*foll)
    except:
        print('The username "%s" is not valid.'%(name))
        return(1)
        


name1=input("First user: ")
name2=input("Second user: ")
ginomeno1=gnm(name1)
ginomeno2=gnm(name2)
if((ginomeno1!=1) or (ginomeno2!=1)): #Elegxo an iparxei to username
    if(ginomeno1>ginomeno2):
        print("Ο χρήστης %s έχει μεγαλύτερο γινόμενο από τον χρήστη %s."%(name1,name2))
    elif(ginomeno1==ginomeno2):
        print("Οι δύο χρήστες έχουν το ίδιο γινόμενο.")
    else:
        print("Ο χρήστης %s έχει μεγαλύτερο γινόμενο από τον χρήστη %s."%(name2,name1))
