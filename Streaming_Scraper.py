# == OAuth Authentication ==
#This part of the application uses tweepy's recommended OAuth Authentication
import tweepy
import sys

consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# == End OAuth Authentication ==

class CustomStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print status.text
		
	def on_error(self, status_code):
		print >> sys.stderr, 'Encountered error with status code:', status_cde
		return True
	
	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		return True

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())

sapi.filter(track=['curiosity'])
