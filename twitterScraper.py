import tweepy
from pickle import dump, load
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET

def collect_tweets():

    """
    This function scrapes the twitter account of the screen name put in as a parameter to api.user_timeline
    for non-retweeted tweets.

    return: list of original tweets from the account holder
    """

    tweets_list = []
    page = 1

    while True:
        tweets = api.user_timeline(screen_name='@realDonaldTrump', page=page, count=200, tweet_mode='extended', include_rts=False)
        if tweets:
            for tweet in tweets:
                # process status here
                tweets_list.append(tweet)
        else:
            # done
            break
        page += 1  # next page
    return tweets_list

if __name__ == "__main__":
    # created api environment with keys
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweets_list = collect_tweets()

    f = open('donaldTrumpTweets.pickle', 'wb')
    dump(tweets_list, f)
    f.close()
