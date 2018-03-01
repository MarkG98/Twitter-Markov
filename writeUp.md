# Software Design Text Mining Project Write-Up

## Project Overview
The data source I used for this project is Twitter. I took the tweets that I scraped from a chosen user and ran them through markov analysis to autogenerate new tweets that appeared to be written by said user. I hoped to learn about markov analysis and hoped to create a program that could auto generate tweets from any given person with a twitter account that the user chooses.

## Implementation
In terms of my twitter scraper, I used tweepy to get the full text from original twitter statuses on the users twitter timeline (a.k.a. NOT retweets). It scans the profile page by page collecting all the original tweets available until there are no more pages left to scrape. As it does this, it appends each tweet to a list so that, in the end, I have a list of all the tweets as strings.

Next, in `markov.py`, I take that list and generate a dictinoary of prefixes to suffixes one tweet at a time. Then to generate the chain itself, I generate a list of keys whose first word has a capital letter (indicating it is the beginnig of a sentence). I then add this to the variable `chain` (a string), choose a suffix and random and add that to the string, and then choose another prefix whose first word is the suffix I just used using a similar list method to the one I used to pick the start. To determine the length of the chain I use a counter to determine the amount of prefix-suffix pairs I want to be in the chain. Once length is less than one, I start looking for an end prefix whose last word ends in an ending punctuation (., !, or ?).

## Results
### Donald Trump
* "Congratulations to the Philadelphia Eagles on a great relationship with World leaders like him! He will be missed by Mexico, which has a ridiculous $71 billion dollar trade surplus with the world."

* "Border Wall, Military, Pro Life, V.A., Judges 2nd Amendment and lots of GOOD NEWS for the world."

* "Pledge of Allegiance and smarter, I want to talk and begged for his children, grandchildren, great-grandchildren and all who knowingly writes false information."
