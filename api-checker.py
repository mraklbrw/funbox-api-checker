import time
import requests
from datetime import datetime

def main():
    servers = ["maria.ru", "rose.ru", "sina.ru"]
    
    while True:
        for server in servers:
            url = 'http://' + server + '/api/count'
            response = requests.get(url).json()
            #response = {"count": 42}

            date_ = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{date_} {server} {response["count"]}')

        time.sleep(60)


if __name__ == '__main__':
    main()

