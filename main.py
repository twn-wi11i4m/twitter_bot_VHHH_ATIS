from fetch_VHHH_ATIS import get_updated_VHHH_ATIS
from twitter_bot import api, tweet, tweet_double

print('=' * 50)
res = get_updated_VHHH_ATIS()
if res is not None:
    print('ATIS is updated!')
    text = f"""{res['Arrival ATIS']}

{res['Departure ATIS']}"""
    print(len(text))
    api = api()
    if len(text) >= 270:
        first_text = f"{res['Arrival ATIS']}"
        second_text = f"{res['Departure ATIS']}"
        tweet_double(api, first_message=first_text, second_message=second_text)
    else:
        tweet(api, text)
    print('Done!!')
else:
    print('ATIS is not updated and no new tweet.')
print('=' * 50)