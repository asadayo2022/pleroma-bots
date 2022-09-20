# pleroma-bots
Some python scripts that post and do polling on the fediverse, made for the Mastodon and Pleroma APIs

check image-bot and polling-bot for comments explaning how it works, the rest of the files are not commented WIPs

the scripts are meant to be executed by crontab, you can execute them manually as well or however you want.
in order to have crontab do it this is a cron job example:

```
*/30 * * * * /usr/bin/python3 /home/myuser/files/bots/supercoolbot/supercoolbot.py >> /home/myuser/files/bots/supercoolbot/supercoolbot_cron.log 2>&1
```

This will execute it every 30 mins and save the logs to the specified file
