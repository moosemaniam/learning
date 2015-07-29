import urllib
import urllib2
import json

#defining handleError
def handleError(e):
    #Error Handling code goes here

def getData(keyword):
    url = 'http://search.twitter.com/search.json'
    data = {'q': keyword, 'lang': 'en', 'result_type': 'recent'}
    params = urllib.urlencode(data)
    try:
        req = urllib2.Request(url, params)
        response = urllib2.urlopen(req)
        jsonData = json.load(response)
        tweets = []
        for item in jsonData['results']:
            tweets.append(item['text'])
        return tweets
    except urllib2.URLError, e:
        handleError(e) #removed self.
    return tweets

tweets = getData("moosemaniam")
print tweet
