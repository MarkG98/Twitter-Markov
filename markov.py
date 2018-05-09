import string
import random
from pickle import load
import os

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

        for i in range(len(data) - prefix_length - 1):
            self.prefix = data[i:i + prefix_length]
            try:
                self.pref_to_suff[tuple(self.prefix)].append(data[i + prefix_length])
            except KeyError:
                self.pref_to_suff[tuple(self.prefix)] = [data[i + prefix_length]]

        for key in self.pref_to_suff:
            if key[1][-1] == '.' or key[1][-1] == '!' or key[1][-1] == '?':
                self.end_dict[key] = self.pref_to_suff[key]

    def next_choice(self, current):

        """
        This function chooses the next prefix for the chain at random.

        current: the last suffix added to the chain

        return: key of next key value pair to add to chain
        """

        next_keys_list = list()
        for key in self.pref_to_suff:
            if key[0] == current:
                next_keys_list.append(key)

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

        start_list = list()
        for key in self.pref_to_suff:
            if key[0][0].isupper() and key[0][-1] not in self.end_punctuation:
                start_list.append(key)

        start = start_list[random.randint(0,len(start_list) - 1)]

        for word in start:
            chain += word + " "
        chain += self.pref_to_suff[start][0] + " "
        current = self.pref_to_suff[start][0]

        while True:
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

            if length < 1:
                for key in self.end_dict:
                    if key[0] == current:
                        chain += key[1]
                        return chain

    def markov(self, user):

        """
        This function attempts to create the chain of the specified length. If in the process, there
        are no first words in keys that match the previous suffix it tries again.
        """

        scrape = TwitterScraper(user)
        f = open(user + 'Tweets.pickle', 'rb')
        new_tweets = load(f)

        tweets = [tweet.full_text for tweet in new_tweets]

        for i in range(len(tweets)):
            tweets[i] = tweets[i].split()

        for i in range(len(tweets)):
            self.generate_markov_list(tweets[i])

        result = None
        while result == None:
            result = self.create_chain()
        print(result)


if __name__ == "__main__":
    M = Markov()
    M.markov('@debcha')
