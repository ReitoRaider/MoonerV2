from src import *

def send_message(token, message, channel_id, jonson=False):
    session = get.ss()
    try:
        r = session.post(
            f"https://discord.com/api/v9/channels/{channel_id}/messages",
            headers=headers(token),
            json={"content": message}
        )

        if get.debug():
            input(f"MESSAGE SENDER: {r.status_code}") 
            input(f"MESSAGE SENDER: {r.text}") 

        if jonson: return r.status_code, r.json()
        else: return r.status_code, r.text
    
    except Exception as e:
        if get.debug():
            input(f"SEND MESSAGE ERROR: {e}")
        else:
            return 69, "failed lol imagine"