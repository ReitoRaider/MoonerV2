from src import *

def send_message(token, message, channel_id):
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

        if r.status_code == 200:
            return "succes" 
        elif r.status_code == 403:
            return "locked"
        elif r.status_code == 401:
            return "invalid"  
        elif r.status_code == 429:                          
            return "ratelimit", r.json().get('retry_after')
        else:
            return "failed"
    except Exception as e:
        if get.debug():
            input(f"SEND MESSAGE ERROR: {e}")
        else:
            return "failed"  