'''import requests
URL = "http://127.0.0.1:8000/api/student/student-list/"

r = requests.get(url = URL)
data = r.json()
print(data)'''

import requests
import json
URL = "http://127.0.0.1:8000/api/student/student-create/"

data = {
    'name' : 'Sonam',
    'roll' : 12,
    'city' : 'Jaipur',
}

json_data = json.dumps(data)
r = requests.post(url = URL,data = json_data)
data = r.json()
print(data)