#Auther nmap
#create json file
import json
admin_data={'name':'admin','password':'admin'}
with open('admin.json','w') as f:
    f.write(json.dumps(admin_data))