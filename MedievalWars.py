import requests, json, random, sqlite3
from PIL import Image, ImageDraw, ImageFont

# Config variables
url = ""

user = ""
password = ""


# Polling server
rfile = open("/home/asa/bots/medievalwars/last_id.txt","r")
since_id = rfile.read()
rfile.close()

r = requests.get(url + "/api/v1/notifications?include_types[]=mention&since_id=" + since_id, auth=(user, password))
y = json.loads(r.text)

if len(y) != 0:
    if y[0]['id'] != "" and y[0]['id'] != None:
        wfile = open("/home/asa/bots/medievalwars/last_id.txt","w")
        wfile.write(y[0]['id'])
        wfile.close()


# Defining game functions

def send_reply(reply):
    r2 = requests.post(url + "/api/v1/statuses", { 'spoiler_text':'MedievalWars 0.1alpha', 'status':reply }, auth=(user, password))

def register(): # remember to escape values
    try:
        if cur.execute("SELECT account FROM accounts WHERE account=" + account) != None:
            reply = "Account already exists."
        else:
            cur.execute("INSERT INTO accounts VALUES (" + account +")")
            reply = "You have been registered. use !help for a guide on how to play."
    except:
        reply = "Server error. @antichrist_hater@shitposter.club fix this."
    send_reply(reply)

def help():
    send_reply("Help message")

def attack():
    # respond with the units selected and time that it will take, ask for confirmation, expire after 2 minutes, overwrite
    try:
    except:
        reply = "Server error. @antichrist_hater@shitposter.club fix this."

def show_map():
    try:
        img = Image.new('RGB', (900, 900), color = (119, 221, 119))
        #fnt = ImageFont.truetype('arial.ttf', 15)
        d = ImageDraw.Draw(img)

        cur.execute("SELECT rowid, user, x, y FROM users")
        user_query = cur.fetchall()

        for x in user_query:
            d.rectangle((x[2] + 9, x[2] + 9, x[2] + 18, x[2] + 18), fill=(0, 192, 192), outline=(0, 0, 0))
            d.text((x[2] + 11, x[2] - 3), x[0], fill=(0,0,0))
            #d.line((54, 54, 464, 464), fill=(255, 255, 0), width=2)
            img.save('map.png')
        # respond with list of towns ranked by distance from user's town and image
        # delete image after using it
    except:
        reply = "Server error. @antichrist_hater@shitposter.club fix this."

def overview():
    # respond with overview
    try:
        # reply with resources, resource gain per hour, population, pop capacity
    except:
        reply = "Server error. @antichrist_hater@shitposter.club fix this."

def ranking():
    # respond with ranking list by points
    try:
        cur.execute("SELECT user, x, y, points FROM users")
        user_query = cur.fetchall()
        for x in user_query:
            # add row to reply with ranking

    except:
        reply = "Server error. @antichrist_hater@shitposter.club fix this."

def build():
    # 
    try:
    except:
        reply = "Server error. @antichrist_hater@shitposter.club fix this."

def recruit():
    try:
    except:
        reply = "Server error. @antichrist_hater@shitposter.club fix this."

def research():
    try:
    except:
        reply = "Server error. @antichrist_hater@shitposter.club fix this."

def delete_account():
    try:
    except:
        reply = "Server error. @antichrist_hater@shitposter.club fix this."

def battle():
    # calculate battle, respond with reports
    try:
    except:
        reply = "Server error. @antichrist_hater@shitposter.club fix this."

def militia():
    # respond with militia activated or deactivated, remind this will affect resources
    try:
    except:
        reply = "Server error. @antichrist_hater@shitposter.club fix this."

def confirm():
    try:
    except:
        reply = "Server error. @antichrist_hater@shitposter.club fix this."

# Connecting to DB
con = sqlite3.connect("medievalwars.db")
cur = con.cursor()

# Controller
status = x['status']['pleroma']['content']['text/plain']

for x in y:
    if '!register' in status:
        register()
        continue
    if cur.execute("SELECT account FROM accounts WHERE account=" + account) != None: # Check if account exists
        if '!confirm' in status:
            confirm()
        elif '!attack' in status:
            attack()
        elif '!map' in status:
            show_map()
        elif '!overview' in status:
            overview()
        elif '!ranking' in status:
            ranking()
        elif '!build' in status:
            build()
        elif '!recruit' in status:
            recruit()
        elif '!research' in status:
            research()
        elif '!delete-account' in status:
            delete_account() 
            # your town and 
            # you can re-register after deleting an account
        elif '!militia' in status:
            militia()
    else:
        reply("Account doesn't exist, use !register")

# Commiting and closing connection to DB
con.commit()
con.close()


# Check tasks by date and execute if neccesary



#TO-DO: add the ability for the user to select their timezone
