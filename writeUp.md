# Software Design Text Mining Project Write-Up

## Project Overview
The data source I used for this project is Twitter. I took the tweets that I scraped from a chosen user and ran them through markov analysis to autogenerate new tweets that appeared to be written by said user. I hoped to learn about markov analysis and hoped to create a program that could auto generate tweets from any given person with a twitter account that the user chooses.

## Implementation
In terms of my twitter scraper, I used tweepy to get the full text from original twitter statuses on the users twitter timeline (a.k.a. NOT retweets). It scans the profile page by page collecting all the original tweets available until there are no more pages left to scrape. As it does this, it appends each tweet to a list so that, in the end, I have a list of all the tweets as strings.

Next, in `markov.py`, I take that list and generate a dictinoary of prefixes to suffixes one tweet at a time. Then to generate the chain itself, I generate a list of keys whose first word has a capital letter (indicating it is the beginnig of a sentence). I then add this to the variable `chain` (a string), choose a suffix and random and add that to the string, and then choose another prefix whose first word is the suffix I just used using a similar list method to the one I used to pick the start. To determine the length of the chain I use a counter to determine the amount of prefix-suffix pairs I want to be in the chain. Once length is less than one, I start looking for an end prefix whose last word ends in an ending punctuation (., !, or ?).

One design choice I had to make while creating this program was to make the twitter scraper and the markov chain genreator two different scripts and to not import he scraper into the generator. First of all, I decided to make the two operations seperate simply because they were two seperate operations of the process of creating a markov chain. Also, I decided to not import the tweet scraper into the markov chain generator because I did not want to scrape twitter everytime it ran or go through the effort of making it only scrape if the user is not he same. It seems like a fairly logical process of choosing a user, scraping, and then generating. Also, by making the user run the scripts individually, it makes them more aware of how the chain is generated.

## Results
### Donald Trump
* "Congratulations to the Philadelphia Eagles on a great relationship with World leaders like him! He will be missed by Mexico, which has a ridiculous $71 billion dollar trade surplus with the world."

* "Border Wall, Military, Pro Life, V.A., Judges 2nd Amendment and lots of GOOD NEWS for the world."

* "Pledge of Allegiance and smarter, I want to talk and begged for his children, grandchildren, great-grandchildren and all who knowingly writes false information."

Overall, my results produced some fairly realistic tweets. A lot of them mentioned topics that the user talks about frequently (which in the case of Donald Trump is the Senate and House, the wall, etc.) However, sometimes it would only contain one part of a two sided puntuaction (only and opening or closing parenthasis or quotation mark).

The results come out the best if the chosen twitter profile has a lot of original tweets. This will give the best results, for there will be a divese array of choices to slap onto the chain. If a twitter account is fairly vacant of original tweets many of the results will souund the same.

## Reflection
Overall, I think that this project went well. I ended up with a program that could in fact take in a twitter handle and create markov chains based off of their tweets. Places it could imporove are it could be programmed to avoid the one sided punctuation problem, and it could be made more user friendly (a.k.a make it easier to change the parameters of `prefix_length` and `length`. In terms of unit testing, I tested by printing out results at various stages of the project. For example, I printed out the pref-suffix dictionary as I was creating it and printed out the chain as I slowly added to its functionality. Something I learned is that markov chains are better for large texts rather than many small texts. Because I linked all the tweets together into one pref-suff dict sometimes the tweet would jump between differnt topics. To remedy this, I augmented the prefix length, but it can still be abit funky sometime. I feel like I can use this knowledge going foward when trying to emulate certain types of texts. One thing I wish I knew before I started the project that would have helped me succeed was ways to make it more user friendly (explained above) perhaps such as the `sys` module. I did not have time to research AND implement this, and if I were to know this before I started it could have made my user-program interaction a lot more asthetically pleasing. I also think that this project was apropriatly scoped, expecially because I made my own markov chain. It took me a good amount of time to create and debug the markov chain and format the scraped tweets.
