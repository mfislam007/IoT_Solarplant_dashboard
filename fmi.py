#listProducePower = [5.0, 10.0, 7.0, 5.0, 10.0, 0.0, 4.0, 7.0, 7.0, 7.0, 6.0, 4.0, 3.0, 1.0, 1.0, 1.0, 4.0, 2.0, 3.0, 7.0, 6.0, 5.0, 4.0, 2.0, 8.0, 8.087, 2.0, 1.0, 4.0, 4.0, 4.0, 3.0, 4.0, 10.0, 4.0, 9.0]
#----------------------------------------------------------------------------------------------------------


#url = 'https://my.iot-ticket.com/api/v1/process/write/2453589bd5a741dab489e650f9e3a656/'


import requests

'''headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic d2F0ZXJwcm9jZXNzOmtVNndlVGh1',
}

data = '[{"name": "testAlbin","v": "30"}]'

response = requests.post('https://my.iot-ticket.com/api/v1/process/write/2453589bd5a741dab489e650f9e3a656/', headers=headers, data=data, verify=False)'''


import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic d2F0ZXJwcm9jZXNzOmtVNndlVGh1',
}

data = '[{"name": "testAlbin2","v": "20","ts":1575766800000}]'
response = requests.post('https://my.iot-ticket.com/api/v1/process/write/2453589bd5a741dab489e650f9e3a656/', headers=headers, data=data, verify=False)
'''
i = 0
data = []
timestamp = 0
while i <= 24:
    data = [{"name": "testAlbin2","v": "20","ts":1575770400000}]
    response = requests.post('https://my.iot-ticket.com/api/v1/process/write/2453589bd5a741dab489e650f9e3a656/', headers=headers, data=data, verify=False)'''

