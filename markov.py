import string
import random
from pickle import load

f = open('donaldTrumpTweets.pickle', 'rb')
new_tweets = load(f)

tweets = [tweet.full_text for tweet in new_tweets]

for i in range(len(tweets)):
    tweets[i] = tweets[i].split()

pref_to_suff = dict()
end_dict = dict()
prefix = list()

end_punctuation = ".!?"

def generate_markov_list(data, prefix_length=2):

    """
    This function iterates throught the possible prefixes in the data inputed, and puts
    them into a dictionary with the value being a list of words (suffixes) that come after that
    prefix. It also collects all the key value pairs where the last key ends in a sentence-ending
    punctuation mark.

    data: a list of words in the string to be turned into a markov list
    prefix_length: length of prefix in words
    """

    for i in range(len(data) - prefix_length - 1):
        prefix = data[i:i + prefix_length]
        try:
            pref_to_suff[tuple(prefix)].append(data[i + prefix_length])
        except KeyError:
            pref_to_suff[tuple(prefix)] = [data[i + prefix_length]]

    for key in pref_to_suff:
        if key[1][-1] == '.' or key[1][-1] == '!' or key[1][-1] == '?':
            end_dict[key] = pref_to_suff[key]

def next_choice(current):

    """
    This function chooses the next prefix for the chain at random.

    current: the last suffix added to the chain

    return: key of next key value pair to add to chain
    """

    next_keys_list = list()
    for key in pref_to_suff:
        if key[0] == current:
            next_keys_list.append(key)

    if len(next_keys_list) == 0:
        print("No next key, restarating tweet generation..." + '\n')
        return None
    else:
        return next_keys_list[random.randint(0,len(next_keys_list) - 1)]

def markov(length=20):

    """
    This function will iterate through a chain of prefix suffix key value pairs, looking for a next key whose
    first word is equal to the last suffix.

    length:the amount of key value pairs it adds to the chain
    """

    chain = ""

    start_list = list()
    for key in pref_to_suff:
        if key[0][0].isupper() and key[0][-1] not in end_punctuation:
            start_list.append(key)

    start = start_list[random.randint(0,len(start_list) - 1)]

    
    chain += start[0] + " " + start[1] + " " + pref_to_suff[start][0] + " "

    current = pref_to_suff[start][0]

    while True:
        next_key = next_choice(current)

        if next_key == None:
            return None

        if len(pref_to_suff[next_key]) > 0 or pref_to_suff[next_key] == None:
            index = random.randint(0,len(pref_to_suff[next_key]) - 1)
        else:
            index = 0

        chain += next_key[1] + " " + pref_to_suff[next_key][index] + " "
        current = pref_to_suff[next_key][index]
        length -= 1

        if length < 1:
            for key in end_dict:
                if key[0] == current:
                    chain += key[1]
                    return chain


if __name__ == "__main__":
    for i in range(len(tweets)):
        generate_markov_list(tweets[i])

    print(pref_to_suff)
    result = None
    while result == None:
        result = markov()
    print(result)
