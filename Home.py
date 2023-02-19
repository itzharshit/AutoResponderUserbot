from telethon import TelegramClient, events

# Replace the values below with your own API ID, API Hash and session file name

api_id = YOUR_API_ID

api_hash = 'YOUR_API_HASH'

session_name = 'my_session'

# Create a new Telegram client

client = TelegramClient(session_name, api_id, api_hash)

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
