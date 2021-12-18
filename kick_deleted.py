from telethon import types, errors
from telethon.sync import TelegramClient
import time
api_id = 'Insert API ID'
api_hash = 'Insert API HASH'
chat_id = -1003213123123 #(insert chat id: Example: -1003123123121)
client = TelegramClient('user', api_id, api_hash)
client.start()
print('Fetching Members...')
all_participants = []
all_participants = client.get_participants(chat_id, aggressive=True)

def kick(user):
    try:
        client.kick_participant(chat_id, user)
    except errors.FloodWaitError as e:
        print('Have to sleep', e.seconds, 'seconds')
        time.sleep(e.seconds)

print('Saving In file...')
for user in all_participants:
    if user.deleted: 
        print("Kicking: " + user.id)
        kick(user)

print('Deleted accounts kicked!')

