import requests, json, os, random

# Enter absolute paths and trailing slashes at the end
pic_directory = ""
already_posted_pic_directory = ""
# Full URL of the mastodon or pleroma server, username and password, it uses basic HTTP auth
url = ""
user = ""
password = ""

# Creates a list with all the files in a folder
pic_list = os.listdir(pic_directory)

# If the folder is empty it moves all the files from the already posted folder to the main one
# This is to make the distribution of images posted more even than just random
if len(pic_list) == 0:
    os.system("mv " + already_posted_pic_directory + "* " + pic_directory)
    pic_list = os.listdir(pic_directory)

# Choses a file out of all the ones in the list at random
chosen_img = pic_directory + random.choice(pic_list)

# First it uploads the image with one request, then makes a post with another request using the media id
media_id = json.loads(requests.post(url + "/api/v2/media", files={ 'file': open(chosen_img,"rb") }, auth=(user, password)).text)['id']
# You can add more parameters according to the Mastodon/Pleroma API specification
# spoiler_text only works for Pleroma I believe, you can add something there if you want
r = requests.post(url + "/api/v1/statuses", { 'media_ids[]':media_id, "spoiler_text":"" }, auth=(user, password))

# Move posted image to already posted directory
os.system("mv " + chosen_img + " " + already_posted_pic_directory)

# This is just to write something to cron logs at the end of the execution, to see the errors if they happen
print("execution: " ,end="")
print(r)