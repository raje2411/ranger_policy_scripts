```json
   // code for coloring
```
```html
   // code for coloring
```
```js
   // code for coloring
```
```css
   // code for coloring
```


## Script to Take Export Policy / Dump

##### This script will take export / policy dump of given ranger service(like hive, hdfs, kafka, hbase, yarn etc.) and also export the each policy into a seaparate file.  Which you can move to another cluster and import it.

## How to use:

git clone https://github.com/raje2411/ranger_policy_scripts.git

cd ranger_policy_scripts

#### python python_script_to_dump_ranger_policies.py

```
Ranger host name(default localhost): c349-node4
Ranger port(default : 6080):
Ranger SSL enabled ? (True or False): False
Ranger admin username (default : admin): admin
Ranger admin password :
Enter the exact Ranger service name to be exported(as shown in Ranger URI) :c349_hive
Do you want a full policy dump in a single file (y or n)? : y
Policies are now getting exported to policy_dumps directory....It should take a while depending on the number of policies
```

### To verify:-
```
# ls -lrt
total 196744
-rw-r--r--      1 rraman  staff      2113 Mar 29 00:49 python_script_to_dump_ranger_policies.py
-rw-r--r--      1 rraman  staff  90550962 Mar 29 00:54 c349_hive_policy_full_dump.json
drwxr-xr-x  22649 rraman  staff    724768 Mar 29 00:54 policy_dumps

# du -sh *
 96M	c349_hive_policy_full_dump.json
111M	policy_dumps
4.0K	python_script_to_dump_ranger_policies.py
```

Policy_dumps directory will have individual files for each policy
