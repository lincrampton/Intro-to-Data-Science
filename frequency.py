import sys, json, re

def check_valid_input():
    if len(sys.argv) != 2:
        sys.exit('\nExiting - inappropriate number arguments.\nUsage: %s sentiment-concordance-file tweets-file' % sys.argv[0])

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
        #print '%f' % (tweet_score)

        for word in tweet_words:
            wordl = word.lower()
            word_score = sentiments[wordl] if wordl in sentiments else (float(tweet_score)/len(tweet_words))
            print '%s %f' % (word, word_score)

def extract_terms(words):
    unique_terms = []
    non_unique_terms = words.split()
    for term in non_unique_terms:
        if term not in unique_terms: 
            unique_terms.append(term)
    return unique_terms

def calculate_frequency(terms, words):
    total_terms = len(words.split())
    for term in terms:
        count = words.count(term)
        frequency = float(count)/total_terms
        print "%s\t%f" % (term, frequency)

def main():
    check_valid_input()
    #concordance_in = open(sys.argv[1])
    #concordance = build_concordance(concordance_in)
    tweets_in = open(sys.argv[1])
    tweets = extract_tweets(tweets_in)
    tweets_joined = ' '.join(tweets)
    #sentiments = eval_sentiment(tweets, concordance)
    terms = extract_terms(tweets_joined)
    calculate_frequency(terms, tweets_joined)

if __name__ == '__main__':
    main()
