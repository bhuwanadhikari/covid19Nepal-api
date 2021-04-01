import json
import re

data = '''
jmufasdjfl;asdkfj
<script> var jsonString = "{"maal": "muji", "bhuwan": "lado"}"

next = "{"hawa": "muji"}"
''' 

regex = r'next = "({.*})"'

json_string = re.findall(regex, data)[0]

# data = json.loads(json_string)
# print(data['maal'])
print(json_string)