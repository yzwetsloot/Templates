import json
import random

import requests

with open('config.json') as file:
    parameters = json.loads(file.read())    

with open('proxies.txt') as file:
    proxies = file.read().splitlines()

headers = parameters['headers']
cookies = parameters['cookies']
base_url = parameters['base_url']
targets = []


def main():
    random.shuffle(targets)

    for target in targets:
        rotate_proxies()
        try:
            requests.get(base_url, headers=headers, cookies=cookies, proxies={'https': proxies[0]})
        except requests.RequestException:
            remove_proxy()
            continue


def remove_proxy():
    global proxies
    proxies = proxies[1:]


def rotate_proxies():
    global proxies
    first = proxies[0]
    proxies = proxies[1:]
    proxies.append(first)


if __name__ == '__main__':
    main()
    