import tweepy
from secret_apis import TWIT_CONS_KEY, TWIT_CONS_SECRET, TWIT_ACC_KEY, TWIT_ACC_SECRET

consumer_key = TWIT_CONS_KEY
consumer_secret = TWIT_CONS_SECRET
access_token = TWIT_ACC_KEY
access_token_secret = TWIT_ACC_SECRET 

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


search_query = "market"
no_of_tweets =10


try:
    #The number of tweets to retrieve from the search
    tweets = api.search_tweets(q=search_query, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.likes_count, tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))