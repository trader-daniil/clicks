import requests
import os
import argparse

from dotenv import load_dotenv


def check_is_bitlink(token, link):
    url_check = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(url=url_check, headers=headers)
    return response.ok


def shorten_link(token, link):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {
        'long_url': link,
    }
    url_bitlinks = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(
        url_bitlinks,
        headers=headers,
        json=payload,
    )
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(token, link):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    url_clicks = ('https://api-ssl.bitly.com/' +
                  f'v4/bitlinks/{link}/clicks/summary')
    response = requests.get(
        url=url_clicks,
        headers=headers,
    )
    response.raise_for_status
    return response.json()['total_clicks']


def main():
    load_dotenv()
    bitly_token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser(description='Программа сокращает ссылки')
    parser.add_argument('link', help='Переданная вами ссылка')
    args = parser.parse_args()
    try:
        if check_is_bitlink(bitly_token, args.link):
            print('Количество переходов по '
                  f'ссылке битли: {count_clicks(bitly_token, args.link)}')
        else:
            print(shorten_link(bitly_token, args.link))
    except requests.exceptions.HTTPError:
        print('Проверьте введенную вами ссылку')


if __name__ == '__main__':
    main()
