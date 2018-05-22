import random
from pickle import load

from twitterScraper import TwitterScraper

class Markov(object):

    def __init__(self):
        self.pref_to_suff = dict()
        self.end_dict = dict()
        self.prefix = list()

        self.end_punctuation = ".!?"

    def generate_markov_list(self, data, prefix_length=5):

        """
        This function iterates throught the possible prefixes in the data inputed, and puts
        them into a dictionary with the value being a list of words (suffixes) that come after that
        prefix. It also collects all the key value pairs where the last key ends in a sentence-ending
        punctuation mark.

        data: a list of words in the string to be turned into a markov list
        prefix_length: length of prefix in words
        """

        # creates overall list of prefix-suffix pairs
        for i in range(len(data) - prefix_length - 1):
            self.prefix = data[i:i + prefix_length]
            try:
                self.pref_to_suff[tuple(self.prefix)].append(data[i + prefix_length])
            except KeyError:
                self.pref_to_suff[tuple(self.prefix)] = [data[i + prefix_length]]

        # creates dictionary of possible endings
        for key in self.pref_to_suff:
            if key[1][-1] in self.end_punctuation:
                self.end_dict[key] = self.pref_to_suff[key]

    def next_choice(self, current):

        """
        This function chooses the next prefix for the chain at random.

        current: the last suffix added to the chain

        return: key of next key value pair to add to chain
        """

        # creates list of possible next orefixes given current suffix
        next_keys_list = list()
        for key in self.pref_to_suff:
            if key[0] == current:
                next_keys_list.append(key)

        # picks next random key or returns None is none available
        if len(next_keys_list) == 0:
            print("No next key, restarating tweet generation..." + '\n')
            return None
        else:
            return next_keys_list[random.randint(0,len(next_keys_list) - 1)]

    def create_chain(self, length=5):

        """
        This function will iterate through a chain of prefix suffix key value pairs, looking for a next key whose
        first word is equal to the last suffix.

        length:the amount of key value pairs it adds to the chain
        """

        chain = ""

        # creates list of possible starts by picking prefixes that are capital
        start_list = list()
        for key in self.pref_to_suff:
            if key[0][0].isupper() and key[0][-1] not in self.end_punctuation:
                start_list.append(key)

        # picks random start from start list
        start = start_list[random.randint(0,len(start_list) - 1)]

        # adds start prefix and suffix to chain, and assigns new current
        for word in start:
            chain += word + " "
        chain += self.pref_to_suff[start][0] + " "
        current = self.pref_to_suff[start][0]

        # build chain
        while True:
            # gets next keys or returns None if none
            next_key = self.next_choice(current)

            if next_key == None:
                return None

            if len(self.pref_to_suff[next_key]) > 0:
                index = random.randint(0,len(self.pref_to_suff[next_key]) - 1)
            else:
                index = 0

            for word in next_key:
                if word != next_key[0]:
                    chain += word + " "
            chain += self.pref_to_suff[next_key][index] + " "

            current = self.pref_to_suff[next_key][index]
            length -= 1

            # once length reaches optimal value, check to see if it's possible to stop
            if length < 1:
                for key in self.end_dict:
                    if key[0] == current:
                        chain += key[1]
                        return chain

    def markov(self, user):

        """
        This function attempts to create the chain of the specified length. If in the process, there
        are no first words in keys that match the previous suffix it tries again.

        user: desired twitter account to scrape
        """

        # scrape and organize tweets
        result = ""
        error = False

        TS = TwitterScraper(user)
        scrape = TS.scrape()
        if scrape == -1:
            error = True
            return result, error
        f = open(user + 'Tweets.pickle', 'rb')
        new_tweets = load(f)

        tweets = [tweet.full_text for tweet in new_tweets]

        for i in range(len(tweets)):
            tweets[i] = tweets[i].split()

        # generate global lists/dictionaries
        for i in range(len(tweets)):
            self.generate_markov_list(tweets[i])

        # run the markov algorithm
        result = None
        while result == None:
            result = self.create_chain()

        # reset global lists/dictionaries and return result
        self.__init__()
        return result, error


if __name__ == "__main__":
    M = Markov()
    res = M.markov('@debcha')

    print(res)
