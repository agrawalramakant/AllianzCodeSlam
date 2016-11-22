import requests
apiRoot = "https://api.api.ai/v1/"

data = {}
headers = {"Authorization":"Bearer c4606158f27643f58e0e66d940ffb8e7"}
print requests.get(apiRoot+"intents",headers=headers, data=data).json()