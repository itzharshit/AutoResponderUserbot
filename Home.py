
from telethon.sessions import StringSession
from telethon import TelegramClient, events, sync

# replace these values with your own api_id, api_hash, and session name
api_id = 6
api_hash = 'eb06d4abfb49dc3eeb1aeb98ae0f581e'
session_name = 'YOUR_SESSION_NAME'
SESSION = 'Your_session_here'
# replace this message with the message you want to send to users when you are offline
offline_message = 'Sorry, I am currently offline. I will respond to your message as soon as possible.'

client = TelegramClient(StringSession(SESSION) , api_id, api_hash)

# register an event handler for incoming messages
@client.on(events.NewMessage)
async def handle_new_message(event):
    # check if the message was sent by a user (as opposed to a bot or a group)
    if event.is_private:
        # check if you are currently online
        if client.is_user_authorized():
            # if you are online, do nothing (let the message go through to your account)
            return
        else:
            # if you are offline, send the offline message to the user who sent the message
            await event.respond(offline_message)

# start the client
client.start()
