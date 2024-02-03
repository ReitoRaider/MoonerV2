from src import *
import uuid

def join(token, invite, jonson=False):
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

        if jonson: return r.status_code, r.json()
        else: return r.status_code, r.text

    except Exception as e:
        if get.debug():
            input(f"JOINER ERROR: {e}")
        else:
            pass