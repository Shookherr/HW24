import requests
url = "http://127.0.0.1:25000/perform_query"
payload = {
   'file_name': 'data/apache_logs.txt',
   'queries': [
      {
         'cmd': 'regex',
         'value': 'images/\\w+\\.png',
      },
      {
         'cmd': 'sort',
         'value': 'asc'
      }
   ]
}
response = requests.post(url, json=payload)

print(response.text.replace(r'"\n",', '\n'))
