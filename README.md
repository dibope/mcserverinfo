# mcstatus

This Discord bot helps manage and monitor Minecraft servers using API endpoints.

Before running the bot, ensure you set the following environment variables or repository secrects:

BOT_TOKEN = our_discord_bot_token

API_URL_LIST = https://yourapi.com/servers/list

API_URL_LOGS = https://yourapi.com/servers/logs/

API_URL_INSPECT = https://yourapi.com/servers/inspect/

In the Discord Developer Portal, your bot needs the Message Content Intent enabled under Privileged Gateway Intents. After that, go to OAuth2, and under Scopes, select bot and applications.commands.

In Bot Permissions, ensure you grant Read Messages, Send Messages, and Manage Messages.

After adding the bot to your server, go to Server Settings → Integrations. There, you can assign a moderator role to use the bot's commands.

If the commands do not appear, run the bot to register them.
