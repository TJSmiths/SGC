import requests
import json
import pandas as pd


HEADERS = {"X-API-Key":'a024733d647c451b9d7fbaa13d526e38'}

print("Insert clanID")
bungie_api = "https://www.bungie.net/Platform"
call = "/GroupV2/" + input() + "/Members/"
response = requests.get(bungie_api + call, headers=HEADERS);

df = pd.read_json(response.text)
results = df.loc['results','Response']
clan = pd.DataFrame(results,columns = ['memberType','isOnline','lastOnlineStatusChange','groupId','destinyUserInfo',
                                           'bungieNetUserInfo','joinDate'])
clan['destinyDisplayName'] = clan.apply(lambda x: x.destinyUserInfo['displayName'],axis=1)
print(clan['destinyDisplayName'].values)
