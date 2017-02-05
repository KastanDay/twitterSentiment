#DEPENDENCIES:
	#sudo pip install tweepy
		#www.tweepy.org
	#sudo pip install textblob
		#https://textblob.readthedocs.io/en/dev

import sys
import tweepy
from textblob import TextBlob

cmdArgs = []
for arg in sys.argv:
	cmdArgs.append(arg)

if len(cmdArgs) > 2:
	raise runtime_error("Please only input one command line argument!")
if len(cmdArgs) <  2:
	raise runtime_error("Please input one (1) command line argument!\nInput a twitter handle!")


consumer_key = '9QCcbB1H06623O0jcZs0fFh3W'
consumer_secret = 'VKRX3iLmewqr07fz066J7gisYQoKMXPcMtV45pXqwebcB2FndT'

access_token = '1262219683-BRhwVmBtPvPP5ssXV9yFsvLoIvpjx8BsXOsZpUE'
access_token_secret = 'DmtbwZnWXGWmvp1VSPTvthctR4SSun25nx2tifxZcjz7U'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


POTUS = api.get_user(cmdArgs[1])  #POTUS is now a user object for POTUS
print "User being examined:", POTUS.screen_name
print "Number of followers:", POTUS.followers_count
#print list of people whom POTUS follows
print "20 accounts whom %s follows:" % POTUS.screen_name
for friend in POTUS.friends():
	print "    ", friend.screen_name


POTUSsentiment = []
POTUSsentimentMax = -1
POTUSsentimentMin = 1
sentimentMaxText = ""
sentimentMinText = ""

POTUSsubjectivity = []
subjectivityMin = 1
subjectivityMax = -1
subjectivityMaxText = ""
subjectivityMinText = ""

print "Please be patient.  Users with many tweets will take longer during this step...\n"

count = 0
for status in tweepy.Cursor(api.user_timeline, id=cmdArgs[1]).items():
	#process status here
	analysis = TextBlob(status.text)
	POTUSsentiment.append(analysis.sentiment.polarity)
	POTUSsubjectivity.append(analysis.subjectivity)
	count += 1

	#check for min&max sentiment
	if (analysis.sentiment.polarity) > POTUSsentimentMax:
		POTUSsentimentMax = analysis.sentiment.polarity
		sentimentMaxText = status.text
	if analysis.sentiment.polarity < POTUSsentimentMin:
		POTUSsentimentMin = analysis.sentiment.polarity
		sentimentMinText = status.text

	#TODO check for min&max subjuctivity
	if analysis.subjectivity > subjectivityMax:
		subjectivityMax = analysis.sentiment.subjectivity
		subjectivityMaxText = status.text
	if analysis.subjectivity < subjectivityMin:
		subjectivityMin = analysis.subjectivity
		subjectivityMinText = status.text
print "Total number of %s tweets:" % POTUS.screen_name
print(count+1)

#TODO average sentiments.
anotherCount = 0
totalSentiment = 0
totalSubjectivity = 0
for sentiments in POTUSsentiment:
	totalSentiment += POTUSsentiment[anotherCount]
	totalSubjectivity += POTUSsubjectivity[anotherCount]
	anotherCount += 1

print "Average sentiment per tweet =", totalSentiment/len(POTUSsentiment)
print "Max sentiment:", POTUSsentimentMax
print "    Most positive tweet:", sentimentMaxText
#TODO print the tweet with the highest sentiment.
print "Min sentiment:", POTUSsentimentMin
print "    Most negetive tweet:", sentimentMinText

print "average subjuctivity per tweet = ", totalSubjectivity/len(POTUSsubjectivity)
print "Max subjuctivity:", subjectivityMax
print "    Most subjuctive teweet:", subjectivityMaxText
print "Min subjuctivity", subjectivityMin
print "    Least subjuctive tweet:", subjectivityMinText


#PROGRAM GOALS:
#	Read all POTUS tweets
#	Conduct sentiment and subjuctivity analysis on all tweets
#	Print out average sentiment (& high and low?)
#	Print out average subjuctivity (& high and low?)