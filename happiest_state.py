import sys, json, re

def check_valid_input():
    if len(sys.argv) != 3:
        sys.exit('\nExiting - inappropriate number arguments.\nUsage: %s sentiment-concordance-file tweets-file' % sys.argv[0])

def build_concordance(concordance_in):
    concordance = []
    for line in concordance_in.readlines():
        term, score = line.split("\t")
        concordance.append((term, float(score)))
    return concordance

# only bother to save tweets that have state info
def get_state_tweets(concordance_in, tweets_in):
    state_tweets = []
    for tweet in tweets_in.readlines():
        jsond_tweet= json.loads(tweet)
        if jsond_tweet.has_key("place"):
            if jsond_tweet["place"] != None and ( jsond_tweet["place"]["country"] == "United States" or jsond_tweet["place"]["country_code"] == "US" ):
               state= (jsond_tweet["place"]["full_name"]).split(",")[1]
               text = jsond_tweet["text"].encode("utf-8")
               state_tweets.append((text,state))
    return state_tweets

def find_happy_state(state_tweets, concordance):
    states={}
    for (tweet, senti_val) in state_tweets:
        val= 0.0
        for (x,y) in concordance:
            if ((x + " " ) or (" " + x)) in tweet:
                val= val + float(y)
                if senti_val in states:
                    states[senti_val] += val
                else:
                    states[senti_val] = val

    cumulative_state_senti = 0.0
    happiest_state = ""
    for key, value in states.iteritems():
        if value > cumulative_state_senti:
            happiest_state = key
            cumulative_state_senti = value
    return happiest_state.strip()

def main():
    check_valid_input()
    concordance_in = open(sys.argv[1])
    tweets_in = open(sys.argv[2])
    state_tweets = get_state_tweets(concordance_in, tweets_in)
    concordance = build_concordance(concordance_in)
    happiest_state = find_happy_state(state_tweets,concordance)
    print happiest_state

if __name__ == '__main__':
	main()
