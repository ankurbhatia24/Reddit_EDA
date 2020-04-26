import requests
import pprint

files = {'upload_file': open('test.txt','rb')}
f = open('bekar.txt', 'rb')
line = f.readline()
print(line)
f.close()
url = 'http://13.234.217.64/automated_testing'
r = requests.post(url, files=files)
pprint.pprint(r.json())
