import requests
import json
def createObject():
    url="https://api.restful-api.dev/objects"
    headers={'content-type':'application/json'}
    data={"name":"Sandeep",
          "data":{"age":40,"Country":"India"}}
    response=requests.post(url,data=json.dumps(data),headers=headers)
    if response.status_code != 200:
        print("Error 404")
    return response
def getAllObject():
    url="https://api.restful-api.dev/objects"
    response=requests.get(url)
    return response.json()
def getbyID(id):
    url="https://api.restful-api.dev/objects/"+id
    response=requests.get(url)
    return response.json()
response = createObject().json();
id = response['id']
print("id ",id)
print("create response ",createObject().json())
print("get response ",getAllObject())
print("get response ",getbyID(id))
