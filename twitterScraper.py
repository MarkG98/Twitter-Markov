import tweepy
from pickle import dump, load
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET


class TwitterScraper(list):

    def __init__(self, user):

        """
        Upon initialization, the class scrapes the twitter account of the user name entered as a parameter. It stores the tweets it finds in a long
        list and saves the file where the class was initialized

        user: twitter user name of account to scrape

        return: list of original tweets from the account holder
        """

        # created api environment with keys
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)
        self.user = user

    def scrape(self):

        try:
            # initialize page counter
            page = 1

            while True:
                tweets = self.api.user_timeline(screen_name=str(self.user), page=page, count=200, tweet_mode='extended', include_rts=False)
                if tweets:
                    for tweet in tweets:
                        # process status here
                        self.append(tweet)
                else:
                    # All done
                    break
                page += 1  # next page

            f = open(str(user) + 'Tweets.pickle', 'wb')
            dump(self, f)
            f.close()

        except tweepy.error.TweepError:
            return -1
