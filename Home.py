
from telethon.sessions import StringSession
from telethon import TelegramClient, events, sync

# replace these values with your own api_id, api_hash, and session name
api_id = 6
api_hash = 'eb06d4abfb49dc3eeb1aeb98ae0f581e'
session_name = 'YOUR_SESSION_NAME'
SESSION = '1ApWapzMBuxnxUHxe-hALnT9r0mCe_uUR8-fdMVuSWfO8xyVL18PUHjdr37Cbq8XJUGkXJeqBqypfpxp5JApT4xWg1Ac6-UznAx_EMnhZJ4JFmaYl1PoRbD8_oClvj9lkD-ItkVW23Pfi_VFswCEha8KOQgts3wCduGZJzuokdb4-263G_fchji72I6T3g4nDC8JZ-wiXJXR__9BW0MTmIs8dZ6ixkygVu9pGHh2Iwdb-3auDGmqxe8T-FMwU3Q7tgVQJyD4rbucfhjDDhAOL2B9PHINucfVrIo0kvj0HhWdxljnYS6_T8Yk5viYdAH-fY0heIe2bp6YlGh6HX4sTX2zd_9v1cbM='
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
