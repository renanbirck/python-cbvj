#
#

import tweepy
import logging
import keys, store


#### Autenticação
def authenticate_oauth():
    auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
    auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET_KEY)
    api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)
    return api

#### Iniciar 
def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    storage = store.TweetStorage()

    twitter_API = authenticate_oauth()  # Instanciar a API do Twitter

    # Pegar os tweets
    logger.info("Começando a pegar os tweets.")
    cbvj_tweets = twitter_API.user_timeline(screen_name='bvsc_joinville', tweet_mode='extended')
   
    for tweet in cbvj_tweets: 
        # Jogar os tweets pegos numa base SQLite.
        try:
            storage.add_tweet(tweet.id, tweet.full_text, tweet.created_at)
        except:
            logger.info(f"O tweet de ID {tweet.id} já existia na base.")
        
if __name__ == "__main__":
    main()