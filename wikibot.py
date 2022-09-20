import requests, random

# Sorry not commenting exhaustively this smaller files
# kinda self-explanatory, check imagebot and pollingbot for documentation

chosen_url = random.choice(open("full-path-textfile.txt").readlines())

url = "" #server full url

user = ""
password = ""

status = chosen_url

r = requests.post(url + "/api/v1/statuses", { 'spoiler_text':'𝓘𝓷𝓽𝓮𝓻𝓮𝓼𝓽𝓲𝓷𝓰 𝓪𝓻𝓽𝓲𝓬𝓵𝓮', 'status':status }, auth=(user, password))

print("wikibot execution: " ,end="")
print(r)
