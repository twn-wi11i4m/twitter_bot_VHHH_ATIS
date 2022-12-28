from secret import *
import tweepy


def api():
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    return client

def tweet(client:tweepy.Client, message:str):
    client.create_tweet(text=message)
    print('Tweeted successfully!')


if __name__ == '__main__':
    client = api()
    tweet(client, 'This was tweeted from Python')
