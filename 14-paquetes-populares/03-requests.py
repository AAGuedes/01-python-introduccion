import requests

# GET
url = "https://jsonplaceholder.typicode.com/users"
r = requests.get(url, timeout=10)
r = r.json()
for user in r:
    print(user["name"])


# GET
url = "https://jsonplaceholder.typicode.com/users/1"
r = requests.get(url, timeout=10)
print(r.json())


# POST
url = "https://jsonplaceholder.typicode.com/users"
user = {
    "id": 11,
    "name": "John Doe"
}
r = requests.post(url, timeout=10, data=user)
print(r.status_code)


# PUT y PATCH
url = "https://jsonplaceholder.typicode.com/users/1"
user = {
    "id": 1,
    "name": "John Doe"
}
r = requests.put(url, timeout=10, data=user)
print(r.status_code)
