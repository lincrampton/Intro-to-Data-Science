import sys, json, re

def build_concordance(concordance_in):
    concordance = {}
    for line in concordance_in:
        term, score  = line.split("\t")  
        concordance[term.lower()] = float(score)  
    return concordance

def extract_tweets(tweets_in):
    tweets = []
    for tweet in tweets_in:
        json_tweet = json.loads(tweet)
        if "text" in json_tweet.keys():
            text = json_tweet["text"].encode('utf-8')
            tweets.append(text)
    return tweets

def eval_sentiment(tweets, sentiments):
    for tweet in tweets:
        tweet_score = 0
        tweet_words = re.findall(r"[\w']+", tweet)
        for word in tweet_words:
            wordl = word.lower()
            word_score = sentiments[wordl] if wordl in sentiments else 0
            tweet_score += word_score
        print '%f' % (tweet_score)

def check_valid_input():
    if len(sys.argv) != 3:
        sys.exit('\nExiting - inappropriate number arguments.\nUsage: %s sentiment-concordance-file tweets-file' % sys.argv[0])

def main():
    check_valid_input()
    concordance_in = open(sys.argv[1])
    tweets_in = open(sys.argv[2])

    concordance = build_concordance(concordance_in)
    tweets = extract_tweets(tweets_in)
    sentiments = eval_sentiment(tweets, concordance)

if __name__ == '__main__':
    main()
