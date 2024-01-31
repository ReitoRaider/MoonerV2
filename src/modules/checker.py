from src import *

def check(token):
    session = get.ss()
    try:
        r = session.get(
            "https://canary.discordapp.com/api/v9/users/@me/library",
            headers=headers(token)
        )

        if get.debug():
            input(f"CHECKER: {r.status_code}") 
            input(f"CHECKER: {r.text}") 

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
            input(f"CHECKER ERROR: {e}")
        else:
            return "failed"