from fetch_VHHH_ATIS import get_updated_VHHH_ATIS
from twitter_bot import api, tweet

print('=' * 50)
res = get_updated_VHHH_ATIS()
if res is not None:
    print('ATIS is updated!')
    text = f"""{res['Arrival ATIS']}

{res['Departure ATIS']}"""
    print(len(text))
    api = api()
    tweet(api, text)
    print('Done!!')
else:
    print('ATIS is not updated and no new tweet.')
print('=' * 50)