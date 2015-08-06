#import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "8uzyONuamPuBvSn4mqhQ"
consumer_secret="xIN9c7MkXJ6bu1Ux6ZQ8f4eF5SgvSPkT2H0EMw1s"
access_token ="59030345-J7rN96xIrnic2JoAK0LAm3waulKiUoeV5jGRiC3RO"
access_token_secret="U6KoVtXgLgqSWJLox2JGVNXVtNZlexuRFuLK1VrqFA"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
      print data
      return True

    def on_error(self, status):
      print status

if __name__=='__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
  #  stream=Stream(auth,l)

  #  stream.filter(track=['Beer'])

    api =  tweepy.API(auth)
    print api.user_timeline("haathikumari")
