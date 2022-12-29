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
    print(client.create_tweet(text=message))
    print('Tweeted successfully!')

def tweet_double(client:tweepy.Client, first_message:str, second_message:str):
    f_t = client.create_tweet(text=first_message)
    print(f_t)
    print(client.create_tweet(text=second_message, in_reply_to_tweet_id=f_t.data['id']))
    print('Tweeted (2) successfully!')


if __name__ == '__main__':
    client = api()
    tweet(client, 'This was tweeted from Python')
