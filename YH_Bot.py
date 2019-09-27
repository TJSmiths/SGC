import requests
import json
import pandas as pd

# Load API Key
creds = pd.read_csv('API_Key.csv').set_index('key').transpose()

# Header for GET Request
HEADERS = {"X-API-Key" : creds.bungie_api[0]}

# Input Clan ID and fulfill GET request
print("Insert clanID")
bungie_api = "https://www.bungie.net/Platform"
call = "/GroupV2/" + input() + "/Members/"
response = requests.get(bungie_api + call, headers=HEADERS);

df = pd.read_json(response.text)
results = df.loc['results','Response']
clan = pd.DataFrame(results,columns = ['memberType','isOnline','lastOnlineStatusChange','groupId','destinyUserInfo',
                                           'bungieNetUserInfo','joinDate'])
clan['destinyDisplayName'] = clan.apply(lambda x: x.destinyUserInfo['displayName'],axis=1)

#Print the names!
print(clan['destinyDisplayName'].values)
