import sys, json

def check_valid_input():
    if len(sys.argv) != 2:
        sys.exit('\nExiting - inappropriate number arguments.\nUsage: %s tweets-file' % sys.argv[0])

def get_hashtags(tweet_file):
    hashtag_dict = {}
    for line in tweet_file:
        tweet=json.loads(line)
        if "entities" in tweet.keys() and "hashtags" in tweet["entities"]:
            for i in range(len(tweet['entities']['hashtags'])):
                hashtags=tweet['entities']['hashtags']
                if hashtag_dict.has_key((hashtags[i])['text']):
                    hashtag_dict[(hashtags[i])['text']] += 1                        
                else:
                    hashtag_dict[(hashtags[i])['text']] = 1
    return hashtag_dict

def print_top_ten(hashtags):
    hashtags_list=[]
    for item in hashtags:
        hashtags_list.append([hashtags[item],item])
    hashtags_list=sorted(hashtags_list)
    for i in range(1,11):
        print "%s %f" % (hashtags_list[-i][1], hashtags_list[-i][0])

def main():
    tweet_file = open(sys.argv[1])
    hashtags=get_hashtags(tweet_file)
    print_top_ten(hashtags)


if __name__ == '__main__':
    main()
