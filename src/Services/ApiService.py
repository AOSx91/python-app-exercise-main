import requests
import json
import csv
import os

from datetime import datetime
from sys import stderr


class ApiService:
    def __init__(self):
        pass

    def run(self):
        print('Running ApiService', file=stderr)
        url = 'https://jsonplaceholder.typicode.com/todos/'
        main_path = os.path.dirname(os.path.realpath(__file__))
        storage_path = os.path.join(main_path, '../..')
        try:
            response = requests.get(url)
        except:
            print("Error al realizar la request")
        
        if response.status_code == 200:
            todos = json.loads(response.text)
            for todo in todos:
                date = datetime.now().strftime('%Y%m%d')
                filename = f'storage/{date}{todo["id"]}.csv'
                file_path = os.path.join(storage_path, filename)
                with open(file_path, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=todo.keys())
                    writer.writeheader()
                    writer.writerow(todo)
        