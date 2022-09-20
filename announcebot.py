import requests, json, random, os, sqlite3
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
#from transformers import pipeline

url = ""
path = ""
user = ""
password = ""

rfile = open(path + "last_id.txt","r")
since_id = rfile.read()
rfile.close()

r = requests.get(url + "/api/v1/notifications?include_types[]=mention&since_id=" + since_id, auth=(user, password))
y = json.loads(r.text)

if len(y) != 0:
    if y[0]['id'] != "" and y[0]['id'] != None:
        wfile = open(path + "last_id.txt","w")
        wfile.write(y[0]['id'])
        wfile.close()

print("." ,end="")


con = sqlite3.connect("groups.db")
cur = con.cursor()

for x in y:
    content = x['status']['pleroma']['content']['text/plain']
    #if '!roll' in content:
        #status = "@" + x['account']['acct'] + " " + str(random.randint(0,100))
        #r2 = requests.post(url + "/api/v1/statuses", { 'in_reply_to_id':x['status']['id'], 'conversation_id':x['status']['pleroma']['conversation_id'], 'direct_conversation_id':x['status']['pleroma']['direct_conversation_id'], 'in_reply_to_account_acct':x['status']['pleroma']['in_reply_to_account_acct'], 'status':status, 'visibility':x['status']['visibility'] }, auth=(user, password))
        #print(r2)
    #elif '!sentiment' in content:
        #sentiment_pipeline = pipeline("sentiment-analysis")
        #data = [content.replace('@user@server.com', '').replace('!sentiment', '')]
        #output = sentiment_pipeline(data)
        #status = "@" + x['account']['acct'] + " Label:" + output[0]["label"] + " Score:" + str(output[0]["score"])
        #r2 = requests.post(url + "/api/v1/statuses", { 'in_reply_to_id':x['status']['id'], 'conversation_id':x['status']['pleroma']['conversation_id'], 'direct_conversation_id':x['status']['pleroma']['direct_conversation_id'], 'in_reply_to_account_acct':x['status']['pleroma']['in_reply_to_account_acct'], 'status':status, 'visibility':x['status']['visibility'] }, auth=(user, password))
        #print(r2)
    if '!join' in content:
        con = sqlite3.connect("groups.db")
        cur = con.cursor()
        if cur.execute("SELECT account FROM accounts WHERE account=" + account) != None: # Check if account exists

        clean_content = content.replace('@user@server.com','').replace('!register','')
        first_arg = clean_content.split()[0]
        reg_file = open(path + "groups.txt","w")
        reg_file.write(y[0]['id'])
        reg_file.close()
        r2 = requests.post(url + "/api/v1/statuses", { 'in_reply_to_id':x['status']['id'], 'conversation_id':x['status']['pleroma']['conversation_id'], 'direct_conversation_id':x['status']['pleroma']['direct_conversation_id'], 'in_reply_to_account_acct':x['status']['pleroma']['in_reply_to_account_acct'], 'status':status, 'visibility':x['status']['visibility'] }, auth=(user, password))
    elif '!cc' in content:
        # if cc then share the post replied to