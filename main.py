#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import config
import requests
from requests_oauthlib import OAuth1
from base64 import b64encode


def get_access_token():
    token = config.twitter_app_key + ':' + config.twitter_app_secret
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


def do_translations(tweet, i=0):
    i += 1
    if i > config.run_limit:
        return tweet

    ko_parameters = {'q': tweet,
                     'target': 'ko',
                     'source': 'en',
                     'key': config.google_key}

    ko_r = requests.get('https://www.googleapis.com/language/translate/v2',
                        params=ko_parameters)

    ko_result = ko_r.json()['data']['translations'][0]['translatedText']

    en_parameters = {'q': ko_result,
                     'target': 'en',
                     'source': 'ko',
                     'key': config.google_key}

    en_r = requests.get('https://www.googleapis.com/language/translate/v2',
                        params=en_parameters)

    en_result = en_r.json()['data']['translations'][0]['translatedText']

    print('Translation #{} is: {}'.format(i, en_result))

    return do_translations(en_result, i) if tweet != en_result else en_result


def post_tweet(tweet):
    auth = OAuth1(config.twitter_app_key, config.twitter_app_secret,
                  config.twitter_user_key, config.twitter_user_secret)

    r = requests.post('https://api.twitter.com/1.1/statuses/update.json',
                      auth=auth, data={'status': tweet})

    return r.json()


def main():
    bearer_token = get_access_token()
    latest_tweet = get_latest_tweet(bearer_token)
    print('Latest Original is: ' + latest_tweet)

    translation = do_translations(latest_tweet)
    print('Translation is: ' + translation)

    post_tweet(translation)


if __name__ == '__main__':
    main()
