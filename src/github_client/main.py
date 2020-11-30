
import requests


def request_branches():
    base_url = 'http://127.0.0.1:3000'
    endpoint = '/branches'

    response = requests.get(base_url + endpoint)
    json = response.json()

    return json['branches']


def run_loop():
    result = input('Press q to quit, anything else to continue: ')
    result = result.strip().lower()

    if result == 'q' or result == 'quit':
        return False
    else:
        print(request_branches())
        return True


def main():
    while run_loop():
        pass


if __name__ == '__main__': main()
