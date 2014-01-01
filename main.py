# -*- coding: utf-8 -*-

import config
import requests
from base64 import b64encode


def get_access_token():
    token = config.twitter_key + ':' + config.twitter_secret
    h = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
         'Authorization': b'Basic ' + b64encode(bytes(token, 'utf8'))}
    print()
    r = requests.post('https://api.twitter.com/oauth2/token',
                      data=b'grant_type=client_credentials', headers=h)
    assert r.json()['token_type'] == 'bearer'

    return r.json()['access_token']


def get_latest_tweet(token):
    parameters = {'screen_name': 'TwoHeadlines',
                  'count': 1,
                  'trim_user': True}

    headers = {'Authorization': 'Bearer ' + token}

    r = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json',
                     params=parameters, headers=headers)

    return r.json(encoding='utf8')[0]['text']


def main():
    bearer_token = get_access_token()
    latest_tweet = get_latest_tweet(bearer_token)


if __name__ == '__main__':
    main()
