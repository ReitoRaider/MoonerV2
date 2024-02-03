from src import *
import time
def check(token):
    session = get.ss()
    valid = False
    try:
        r = session.get(
            "https://canary.discordapp.com/api/v9/users/@me/library",
            headers=headers(token)
        )

        if get.debug():
            input(f"CHECKER: {r.status_code}") 
            input(f"CHECKER: {r.text}") 

        if r.status_code == 200:
            log.checker.g(token); valid = True
        elif r.status_code == 403:
            log.checker.l(token)
        elif r.status_code == 401:
            log.checker.i(token)
        elif r.status_code == 429:                          
            log.checker.r(token)
            time.sleep(float(r.json().get('retry_after')))
            check(token)

        return valid

        
    except Exception as e:
        if get.debug():
            input(f"CHECKER ERROR: {e}")
        else:
            return "failed"