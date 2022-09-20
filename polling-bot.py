import requests, json, random

# This both does polling on the server to check the user's mentions, by default it checks the last 20
# the idea is to have crontab execute it periodically

# full url of server, username, password for basic http auth
url = ""
user = ""
password = ""
# Full path of directory the python script is in with trailing slash at the end
path = ""

# You should manually create a empty textfile in the path by the name of last_id.txt
# It checks the id of the last recorded mention in order to only request mentions that are newer than that one
rfile = open(path + "last_id.txt","r")
since_id = rfile.read()
rfile.close()

# API request for mentions since the last recorded one
r = requests.get(url + "/api/v1/notifications?include_types[]=mention&since_id=" + since_id, auth=(user, password))
y = json.loads(r.text)

# If there is new mentions, overwrite last_id.txt with the new one
if len(y) != 0:
    if y[0]['id'] != "" and y[0]['id'] != None:
        wfile = open(path + "last_id.txt","w")
        wfile.write(y[0]['id'])
        wfile.close()

# This is just to write something to the cron log to check that it is indeed being executed
print("." ,end="")

# Loop to get the content of the mentions and in case X string is present do whatever you want
# You can do anything here, not just with the content of the status but with all the other info that
# the JSON provides, like account it came from, etc.
# I provide the !roll example
for x in y:
    content = x['status']['pleroma']['content']['text/plain']
    if '!roll' in content: # If the substring !roll is present in the status message
        # create a response aimed at the user that mentioned you with !roll, and answer with a number 0-100
        status = "@" + x['account']['acct'] + " " + str(random.randint(0,100))
        # send the API request to post the response, use same post visibility as the mention
        r2 = requests.post(url + "/api/v1/statuses", { 'in_reply_to_id':x['status']['id'], 'conversation_id':x['status']['pleroma']['conversation_id'], 'direct_conversation_id':x['status']['pleroma']['direct_conversation_id'], 'in_reply_to_account_acct':x['status']['pleroma']['in_reply_to_account_acct'], 'status':status, 'visibility':x['status']['visibility'] }, auth=(user, password))
        print(r2) # record any errors or response 200 to cron log
