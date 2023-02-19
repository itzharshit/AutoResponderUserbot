from telethon import TelegramClient, events 
from telethon.sessions import StringSession
# Replace the values below with your own API ID, API Hash and session file name
api_id = 6
string= '1ApWapzMBuxnxUHxe-hALnT9r0mCe_uUR8-fdMVuSWfO8xyVL18PUHjdr37Cbq8XJUGkXJeqBqypfpxp5JApT4xWg1Ac6-UznAx_EMnhZJ4JFmaYl1PoRbD8_oClvj9lkD-ItkVW23Pfi_VFswCEha8KOQgts3wCduGZJzuokdb4-263G_fchji72I6T3g4nDC8JZ-wiXJXR__9BW0MTmIs8dZ6ixkygVu9pGHh2Iwdb-3auDGmqxe8T-FMwU3Q7tgVQJyD4rbucfhjDDhAOL2B9PHINucfVrIo0kvj0HhWdxljnYS6_T8Yk5viYdAH-fY0heIe2bp6YlGh6HX4sTX2zd_9v1cbM='
api_hash = 'eb06d4abfb49dc3eeb1aeb98ae0f581e'
session_name = 'my_session'
# Create a new Telegram client
client = TelegramClient(api_id, api_hash, StringSession(string))
# Define the message to be sent as an auto-reply
auto_reply_message = 'Thanks for your message! I will get back to you as soon as possible.'
# Define the event handler for incoming messages
@client.on(events.NewMessage)
async def handle_incoming_message(event):

    if not await client.is_user_authorized() or event.out:

        # User is not currently authorized or message is outgoing, ignore

        return

    

    # Check if user is online

    me = await client.get_me()

    if me.status == 'online':

        # User is currently online, ignore the message

        return

    

    # Send the auto-reply message to the sender of the incoming message

    await client.send_message(event.chat_id, auto_reply_message)

# Start the client

client.start()

# Run the client until it is disconnected

client.run_until_disconnected()
