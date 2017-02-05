import tweepy
from textblob import TextBlob

consumer_key = '9QCcbB1H06623O0jcZs0fFh3W'
consumer_secret = 'VKRX3iLmewqr07fz066J7gisYQoKMXPcMtV45pXqwebcB2FndT'

access_token = '1262219683-BRhwVmBtPvPP5ssXV9yFsvLoIvpjx8BsXOsZpUE'
access_token_secret = 'DmtbwZnWXGWmvp1VSPTvthctR4SSun25nx2tifxZcjz7U'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print("-------")
	print(analysis.subjectivity)
	print("-------")
	print("\n")
