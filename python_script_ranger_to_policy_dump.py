import requests
import json
from requests.auth import HTTPBasicAuth
ranger_admin_url ="http://c349-node4:6080/service/public/v2/api/service/c349_hive/policy?pageSize=250000"
username="admin"
password="admin"
ranger_hive_policy=requests.get(ranger_admin_url,auth=HTTPBasicAuth(username,password))
with open("c349_policy_dump.json","w") as write_file:
  json.dump(ranger_hive_policy.json(),write_file)
policie_dump = ranger_hive_policy.json()
for policy_item in policie_dump:
     policy_name_str = str(policy_item["name"])
     with open('%s.json' %policy_name_str,"w") as write_file:
       json.dump(policy_item,write_file)
