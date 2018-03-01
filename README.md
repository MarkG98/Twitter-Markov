# Tweet Generator For Any Twitter User

## Overview
This program uses markov analysis to generate original tweets for any twitter user. It works best for users who have many original tweets on their profile.

## Required Libraries
The only non-core Python library that is required to run the script is tweepy. One can install it using pip as so: <br /> `pip install tweepy`

## How to Use
To set up this program for use, one simply needs to clone the repo and create a file called `config.py` which contains the variables `CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_TOKEN_KEY`, and `ACCESS_TOKEN_SECRET` which are all obtained by creating a twitter app account. It should also contain a `USER` variable which is the twitter handle of the person you want to use markov analysis on.

Next, one must run the script `twitterScraper.py`, and then `markov.py` which will generate the tweets and print them to the terminal. To adjust he prefix length one can adjust the default parameter value for `prefix_length` in the function `generate_markov_list`, and to adjust the amount of prefix-suffix pairs used to create the chain one can change the `length` parameter in the function `create_chain`.

## Examples
### Donald Trump
* "Congratulations to the Philadelphia Eagles on a great relationship with World leaders like him! He will be missed by Mexico, which has a ridiculous $71 billion dollar trade surplus with the world."

* "Border Wall, Military, Pro Life, V.A., Judges 2nd Amendment and lots of GOOD NEWS for the world."

* "Pledge of Allegiance and smarter, I want to talk and begged for his children, grandchildren, great-grandchildren and all who knowingly writes false information."
