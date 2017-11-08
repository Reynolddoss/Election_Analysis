# Election-Prediction-using-sentimental-analysis-Twitter
Predicting the election results using the tweets with sentimental analysis and Bayes model.

## An Overview
Twitter a social website where people comment on several on going topics called tweets. If the tweets related to a particular topic a overall sentimental analysis can be drawn out, which would bring out the emotion of people of those who tweet.
This can used to analyse sevaral conclusion.The Election analysis uses the same to drive out the emotion of people.

## Prerequisation
1. Python 2.7
2. Twitter Account
3. re library
4. tweepy library
5. textblob library

	
## Creating an Twitter Api
To create a Api click here [Twitter_Api](https://apps.twitter.com/)

## Installation and Running the program
	Clone the github repository
	git clone https://github.com/
### Main file
1. Running this python file will automatically run all the respective python files for each parties. 
2. Each party files would individually access the tweeter account through the tweeter api for extracting tweets.

### Party files
1. All the party files have the same functioning except the query that is made, the counts are also mentioned here i.e the number of tweets that need to be considered.
2. Initially the main function is called which would, in turn, call the Twitter client finction.
3.Here the credentials are taken and a connection to the api is made.
4. The control is returned to the main function which would next call the next function which would retrive the tweets now.
5. The matching tweets are put in an array and then passed into another function to get it cleaned.
6 Using textblob library the tweets are cleaned and then checked for its sentiment.
7. For cross checking we have put the positive, negative and neutral sentiment into different files geiint a count simultaneously. 
8. Using these counts the individual percentage can be calculated. 
9. This is then graphically visualized.
10. The overall graph is shown below.

![Alt text](a.png?raw=true "Sentimental analysis")



## NAIVE BAYES CLASSIFIER

1. This was used make a classification of the number of seats that a party would possibly get.
2. The source of data for this was from different well-known news channels.
3. A pie chart was also represented to show which party would get how many seats. 

![Alt text](b.png?raw=true "SEATS")


##Note 
	*The sarcasm tweets are not delt accurately
	*Emoji icon are not considered 
	
