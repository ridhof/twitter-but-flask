import requests


def bg_insert_tweet(text, username):
    payload = {'text': text, 'username': username}

    url = 'http://localhost:5000/tweet'
    r = requests.post(url, data=payload)
    print(f'{r.text} {r.status_code}')
