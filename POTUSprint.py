#DEPENDENCIES:
	#sudo pip install tweepy
		#www.tweepy.org
	#sudo pip install textblob
		#https://textblob.readthedocs.io/en/dev

import tweepy
from textblob import TextBlob

consumer_key = '9QCcbB1H06623O0jcZs0fFh3W'
consumer_secret = 'VKRX3iLmewqr07fz066J7gisYQoKMXPcMtV45pXqwebcB2FndT'

access_token = '1262219683-BRhwVmBtPvPP5ssXV9yFsvLoIvpjx8BsXOsZpUE'
access_token_secret = 'DmtbwZnWXGWmvp1VSPTvthctR4SSun25nx2tifxZcjz7U'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

POTUS = api.get_user('POTUS')  #POTUS is now a user object for POTUS
print(POTUS.screen_name)
print(POTUS.followers_count)
for friend in POTUS.friends():
	print friend.screen_name
print("\n\n")

numOfTweets = 0
for status in tweepy.Cursor(api.user_timeline, id="POTUS").items():
	#process status here
	print(status.text)
	print("\n------\n")
	numOfTweets += 1
print("Total number of POTUS tweets:")
print(numOfTweets)

POTUSsentiment = []
POTUSsentimentMax = 0
POTUSsentimentMin = 0
POTUSsubjuctivity = []
count = 0
for status in tweepy.Cursor(api.user_timeline, id="POTUS").items():
	#process status here
	analysis = TextBlob(status.text)
	POTUSsentiment.append(analysis.sentiment.polarity)
	POTUSsubjuctivity.append(analysis.sentiment.subjectivity)
	count += 1

	#check for min&max sentiment
	if analysis.sentiment.polarity > POTUSsentimentMax:
		POTUSsentimentMax = analysis.sentiment.polarity
	if analysis.sentiment.polarity < POTUSsentimentMin:
		POTUSsentimentMin = analysis.sentiment.polarity

	#TODO check for min&max subjuctivity
#TODO average sentiments.
anotherCount = 0
totalSentiment = 0
for sentiments in POTUSsentiment:
	POTUSsentiment[anotherCount] += totalSentiment
	anotherCount += 1
print(totalSentiment)
print(totalSentiment/len(POTUSsentiment))


#PROGRAM GOALS:
#	Read all POTUS tweets
#	Conduct sentiment and subjuctivity analysis on all tweets
#	Print out average sentiment (& high and low?)
#	Print out average subjuctivity (& high and low?)

# public_tweets = api.search('Trump')

# for tweet in public_tweets:
# 	print(tweet.text)
# 	analysis = TextBlob(tweet.text)
# 	print("-------")
# 	print(analysis.sentiment)
# 	print("-------")
# 	print("\n")
