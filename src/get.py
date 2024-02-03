import platform
import json
import os
import requests
import random
import tls_client

class get:
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9031 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36"

        
    def folder():
        if platform.system() == 'Windows':
            path = os.path.join(os.getenv('APPDATA'))
            return f"{path}\MoonerV2"
        elif platform.system() == 'Linux':
            path = os.path.join(os.path.expanduser('~'), '.local', 'share')
            return f"{path}\MoonerV2"
        

    def debug():
        with open(f"{get.folder()}/config.json", "r") as f:
            cfg = json.load(f)
            state = cfg["settings"]["debug"]
            return state
        
    def update():
        with open(f"{get.folder()}/config.json", "r") as f:
            cfg = json.load(f)
            return cfg["settings"]["check for updates"]
        
    def ss():
        session = tls_client.Session(client_identifier="chrome_108",random_tls_extension_order=True)
        return session

    def stars():
        r = requests.get(f"https://api.github.com/repos/R3CI/MoonerV2")
        return r.json().get("stargazers_count")
        
    def build():
        # tak nie umiem tego zrobic wiec takie cos zrobile mxd
        prefix = "254206"[:-2]
        generated = ''.join([str(random.randint(0, 9)) for _ in range(2)])

        return prefix + generated


    # to nie skid spierdalaj
    def cookies():
        try:
            r = requests.get("https://canary.discord.com")
            if r.status_code == 200:
                return "; ".join(f"{cookie.name}={cookie.value}" for cookie in r.cookies) + "; locale=en-US"
            else:
                return "__dcfduid=4e0a8d504a4411eeb88f7f88fbb5d20a; __sdcfduid=4e0a8d514a4411eeb88f7f88fbb5d20ac488cd4896dae6574aaa7fbfb35f5b22b405bbd931fdcb72c21f85b263f61400; __cfruid=f6965e2d30c244553ff3d4203a1bfdabfcf351bd-1699536665; _cfuvid=rNaPQ7x_qcBwEhO_jNgXapOMoUIV2N8FA_8lzPV89oM-1699536665234-0-604800000; locale=en-US"
        except Exception as e:
            input(f"Cookie fetcher failed the radier will not be usable {e}")

    def finger():
        r = requests.get("http://discord.com/api/v9/experiments")
        finger = r.json().get("fingerprint", {})
        return finger

    def tokens():
        with open(f"{get.folder()}/tokens.txt", "r") as f:
            return f.read().splitlines()

    def token_amt():
        with open(f"{get.folder()}/tokens.txt", "r") as f:
            return sum(1 for _ in f)

cookie = get.cookies()
def headers(token):
    headers = {
        "accept-language": "en-GB",
        "authorization": token,
        "cookie": cookie,
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9031 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "pl",
        "x-discord-timezone": "Europe/Warsaw",
        "x-failed-requests": "1",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDMxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMzEgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNjE5NzMsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQyODk5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
    }
    if token is False:
        del headers["authorization"]
    return headers  