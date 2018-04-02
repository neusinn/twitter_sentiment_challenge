# See http://www.tweepy.org/
import tweepy
# See https://pypi.python.org/pypi/textblob-de
from textblob_de import TextBlobDE


# Step 1 - Authenticate
#consumer_key= 'CONSUMER_KEY_HERE'
#consumer_secret= 'CONSUMER_SECRET_HERE'

#access_token='ACCESS_TOKEN_HERE'
#access_token_secret='ACCESS_TOKEN_SECRET_HERE'

consumer_key= '2eYbc3q1Xt6XJuzKAYkSW4mZQ'
consumer_secret= 'dvy2S7enpM4dpRCCr3LS7wvGRmZyvvV0Al6W1y1okJiiAQj3lK'

access_token='612923328-OgEMn0JdVBsV3bkPMMol7sv6eSC3l2Uh8rYo0uRe'
access_token_secret='djVUXlaomK5AxQpr1ePr1gcIV5fIFgsKBvN1b9MBsITrk'


print('Starting...')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print('Authenticated.')

#Step 3 - Retrieve Tweets
# Twitter API https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
query = '@uwyss'
public_tweets = api.search(query, lang='de', count=1, result_type='recent')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

for tweet in public_tweets:
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlobDE(tweet.text)
    
    print(tweet.id, tweet.text)
    print(analysis.sentiment)
    print("")
