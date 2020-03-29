#Python Libraries used in this program
import os
import requests
import json
import getpass 
from requests.auth import HTTPBasicAuth


#Example:- ranger_admin_url ="http://c349-node4:6080/service/public/v2/api/service/c349_hive/policy?pageSize=250000"

#User input to collect Environment details

ranger_host= str(raw_input("Ranger host name(default localhost): ") or "localhost")
ranger_port= str(raw_input("Ranger port(default : 6080): ") or "6080")
ssl_enabled= str(raw_input("Ranger SSL enabled ? (True or False): ") or "False") 
if ssl_enabled == True:
  protocol="https"
else:
  protocol="http"
ranger_adm_username = str(raw_input("Ranger admin username (default : admin): ") or "admin")
#ranger_adm_passwd = str(raw_input("Ranger admin password (default : admin): ") or "admin")
ranger_adm_passwd = getpass.getpass(prompt='Ranger admin password : ')
ranger_service_name = str(raw_input("Enter the exact Ranger service name to be exported(as shown in Ranger URI) :"))
ranger_admin_url = protocol + "://"+ ranger_host + ":" + ranger_port + "/service/public/v2/api/service/" + ranger_service_name + "/policy?pageSize=250000"
need_full_dump = str(raw_input("Do you want a full policy dump in a single file (y or n)? : ") or "n")

#Pull all policies from Ranger admin for a given service

ranger_policy_pull = requests.get(ranger_admin_url,auth=HTTPBasicAuth(ranger_adm_username,ranger_adm_passwd))

# Full policy dump
if (need_full_dump == "y" or need_full_dump == "Y"):
  with open("%s_policy_full_dump.json" %ranger_service_name,"w") as write_file:
    json.dump(ranger_policy_pull.json(),write_file, indent=4)

# Exporting each policies in to a single file.  File name will be same name as policy name.
 
policy_dump = ranger_policy_pull.json()

print("Policies are now getting exported to policy_dumps directory....It should take a while depending on the number of policies")  
os.mkdir("policy_dumps")

for policy_item in policy_dump:
     policy_name = "policy_dumps/"+str(policy_item["name"])
     with open('%s.json' %policy_name,"w") as write_file:
       json.dump(policy_item,write_file, indent=4)
