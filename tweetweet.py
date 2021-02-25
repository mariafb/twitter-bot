import tweepy
import time

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('key', 'secret')

api = tweepy.API(auth)
user = api.me()

# Tweeter - Like tweets based on search key

search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite
        print('I liked that tweet!')

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# Tweeter - follows back
def limit_handler(Cursor):
    try:
        while True:
            yield Cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


for follower in tweepy.Cursor(api.followers).items():
    if follower.followers_count > 1000:
        follower.follow()
    break
