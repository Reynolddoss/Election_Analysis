## Election-Prediction-using-sentimental-analysis-Twitter
Predicting the election results using the tweets with sentimental analysis and Bayes model.

## An Overview
The following code is to get the tweets from the twitter(A social Network).These tweets are then passeed into the program which gives out the polarity-positive,Negative and neutral. This is used to generate a graph which clearly displays the outcome of the election results.

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
1. All the party file function the same way as mentioned bellow
2. The twitter api authentication credentials obtained from the twitter account for the api are to be mentioned
3. The OAuthHandler module will handle accessing the twitter account throught the api.
4. Later a query is made with the parties name and the counts are mentioned.
5. The tweets that matches the query are stored in an array.
## Note 
	*The sarcasm tweets are not delt accurately
	*Emoji icon are not considered 
	
