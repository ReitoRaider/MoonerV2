from src import *
import uuid

def join(token, invite):
    session = get.ss()
    try:
        
        payload = {
            "session_id": uuid.uuid4().hex
        }

        r = session.post(
            f"https://discord.com/api/v9/invites/{invite}",
            json=payload,
            headers=headers(token)
            )

        if get.debug():
            input(f"JOINER: {r.status_code}") 
            input(f"JOINER: {r.text}") 
        if r.status_code == 200:
            return "succes" 
        elif r.status_code == 400:
            return "captcha" 
        elif r.status_code == 429:                          
            return "ratelimit", r.json().get('retry_after')
        else:
            return "failed"
    except Exception as e:
        if get.debug():
            input(f"JOINER ERROR: {e}")
        else:
            return "failed"