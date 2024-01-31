version = "2.0"
try:
    import os, sys, time, json, uuid, requests, base64, tls_client, random, platform, websocket, webbrowser, threading
    from colorama import init, Fore; init()
except ModuleNotFoundError:
    libs = [
        "requests",
        "tls_client",
        "colorama",
        "websocket-client",
        "uuid",
        "base64",
        "tls_client"
    ]
    for lib in libs:
        print("Installing libs please wait")
        os.system(f"pip install -q {lib}")
        import os, sys, time, json, uuid, requests, base64, tls_client, random, platform, websocket, webbrowser, threading
        from colorama import init, Fore; init()

if platform.system() == 'Windows':
    os.system(f"mode con: cols=170 lines=35")
elif platform.system() == 'Linux':
    os.system(f"resize -s 170 35")

class c:
    r = Fore.RED
    lr = Fore.LIGHTRED_EX
    y = Fore.YELLOW
    ly = Fore.LIGHTYELLOW_EX
    g = Fore.GREEN
    lg = Fore.LIGHTGREEN_EX
    res = Fore.RESET
    p = Fore.LIGHTMAGENTA_EX
    m = Fore.MAGENTA
    o = "\033[38;2;255;165;0m"
    do = "\033[38;2;200;120;0m"
    b = Fore.LIGHTBLACK_EX

class util:
    def clear():
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux':
            os.system('clear')

    def title(tit):
        if platform.system() == 'Windows':
            os.system(f'title {tit}')
        elif platform.system() == 'Linux':
            sys.stdout.write(f"\x1b]0;{tit}\x07")

class files:
    if platform.system() == 'Windows':
        path = os.path.join(os.getenv('APPDATA'))
        main = f"{path}\MoonerV2"
    elif platform.system() == 'Linux':
        path = os.path.join(os.path.expanduser('~'), '.local', 'share')
        main = f"{path}\MoonerV2"

    if not os.path.exists(main): 
        os.makedirs(main)

    for file in ["tokens.txt", "config.json"]:
        if not os.path.exists(f"{main}\{file}"):
            with open(f"{main}\{file}", "w"):
                pass 

    json_data = {
        "comments": [
            "Do not touch the debug if ur not experienced with requests and discord api. Also i made it for myself so the raider may even not work correctly with it on",
        ],
        "settings": {
            "debug": False,
            "check for updates": True,  
        },
    }

    if not os.path.exists(f"{main}\config.json"):            
        with open(f"{main}\config.json", "w") as f:
            json.dump(json_data, f, indent=4)
    try:   
        if os.path.exists(f"{main}\config.json"):
            with open(f"{main}\config.json", "r") as file:
                config_data = json.load(file)

                config_settings = config_data.get('settings', {})
                json_settings = json_data.get('settings', {})

                if config_settings.get('debug') != json_settings.get('debug'):
                    config_settings['debug'] = json_settings.get('debug')
                if config_settings.get('check for updates') != json_settings.get('check for updates'):
                    config_settings['check for updates'] = json_settings.get('check for updates')

            config_data['settings'] = config_settings
            if config_data != json_data:
                input(f"{c.r}Config outdated Press enter to deleate it so a updated one can be made")
                os.remove(f"{main}\config.json")
                time.sleep(1)
                with open(f"{main}\config.json", "w") as f:
                    json.dump(json_data, f, indent=4)

    except json.decoder.JSONDecodeError:
        with open(f"{main}\config.json", "w") as f:
            json.dump(json_data, f, indent=4)

class get:
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9031 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36"

    def debug():
        with open(f"{get.folder()}/config.json", "r") as f:
            cfg = json.load(f)
            return cfg["settings"]["debug"]
        
    def update():
        with open(f"{get.folder()}/config.json", "r") as f:
            cfg = json.load(f)
            return cfg["settings"]["check for updates"]
        
    def folder():
        if platform.system() == 'Windows':
            path = os.path.join(os.getenv('APPDATA'))
            return f"{path}\MoonerV2"
        elif platform.system() == 'Linux':
            path = os.path.join(os.path.expanduser('~'), '.local', 'share')
            return f"{path}\MoonerV2"

    def stars():
        r = requests.get(f"https://api.github.com/repos/R3CI/MoonerV2")
        return r.json().get("stargazers_count")
        
    def build():
        # tak nie umiem tego zrobic wiec takie cos zrobile mxd
        prefix = "254206"[:-2]
        generated = ''.join([str(random.randint(0, 9)) for _ in range(2)])
    
        return prefix + generated
    
    def cookies_s():
        try:
            r = requests.get("https://discord.com")
            return {cookie.name: cookie.value for cookie in r.cookies}
        except Exception as e:
            if get.debug():
                input("COOKIE FETCHER ERROR\n" + e)
            else:
                input("Cookie fetcher failed; the raider will not be usable")


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
    
    def xsup():
        pass
    #    try:
    #        super = {
    #           "os": "Windows",
    #            "browser": "Discord Client",
    #            "system_locale": "en",
    #            "release_channel": "stable",
    #            "client_version": "1.0.0.215",
    #            "os_version": "19045.3803",
    #            "browser_user_agent": fetchers.user_agent,
    #            "client_build_number": fetchers.get.build(),
    #            "native_build_number": 42627,
    #        }
    #        return base64.b64encode(json.dumps(super).encode()).decode()
    #    except Exception as e:
    #        if fetchers.get.debug():
    #            input("XSUPER FETCHER ERROR \n" + e)
    
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

def ss():
    session = tls_client.Session(client_identifier="chrome_108",random_tls_extension_order=True)
    return session

def update_ss():
    cookies = get.cookies_s()
    session = tls_client.Session(client_identifier="chrome_108",random_tls_extension_order=True)
    session.cookies.update(cookies)

update_ss(); session = ss()

if get.update():
    class auto_update:
        try:
            @staticmethod
            def get_info():
                os.system("title MoonerV2 - Searching for updates")
                r = requests.get("https://api.github.com/repos/R3CI/MoonerV2/releases/latest")
                if r.status_code == 200:
                    data = r.json()
                    changelog = data.get('body', '')
                    version = float(data['tag_name'].lstrip('v'))
                    return version, changelog
                else:
                    return None, None

            @staticmethod
            def update(local, github, changelog):
                local = float(local)
                github = float(github)
                if local == github:
                    pass
                else:
                    if local < github:
                        size = os.get_terminal_size().columns
                        os.system("title MoonerV2 - Update found")
                        os.system("cls")
                        banner = f"""{c.r}
                        {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗".center(size)}
                        {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝".center(size)}
                        {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══".center(size)}
                        """
                        print(banner)
                        print(f"{c.r}Change log\n{changelog}")
                        input(f"\n{c.r}Enter to open GitHub on the newest release")
                        webbrowser.open("https://github.com/R3CI/MoonerV2/releases")
                        exit()

            gh_version, changelog = get_info()
            update(version, gh_version, changelog)
        except Exception as e:
            input(f"UPDATE ERROR: {e}")


class log:
    def ask(pyt):
        return input(f"{c.r}║{c.res}{pyt}{c.r}║ {c.res}> ")
    def askyn(pyt):
        return input(f"{c.r}║{c.res}{pyt}{c.r}║ {c.b}(y/n) {c.res}> ")

class run:
    def guild_info(invite):
        try:
            r = requests.get(
                f"https://discord.com/api/v9/invites/{invite}?inputValue={invite}&with_counts=true&with_expiration=true",
                )
            
            data = r.json()
            guild = data['guild']
            inviter = data['inviter']
            info = [
                "Invite: " + data["code"],
                "Inviter ID: " + inviter["id"],
                "Inviter name: " + inviter["username"],
                "Guild ID: " + data["guild_id"],
                "Guild name: " + guild["name"],
                "Channel ID: " + data["channel"]["id"],
                "Channel name: " + data["channel"]["name"],
                "Member count: " + str(data["approximate_member_count"]),
                "Online member count: " + str(data["approximate_presence_count"]),
            ]

        
            return '\n'.join(info)
        except Exception as e:
            if get.debug:
                input(f"GUILD INFO FETCHER: {e}")
            else:
                return "Unknown"
    
    def join(token, invite):
        session = ss()
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
            
    def bypass_join(token, invite):
        session = ss()
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
                input(f"BYP JOINER: {r.status_code}") 
                input(f"BYP JOINER: {r.text}") 

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
                input(f"BYP JOINER ERROR: {e}")
            else:
                return "failed"
            
    def leave(token, guildid):
        session = ss()
        try:
            payload = {
                "lurking": False,
            }

            r = session.delete(
                f"https://discord.com/api/v9/users/@me/guilds/{guildid}",
                json=payload,
                headers=headers(token)
            )

            if get.debug():
                input(f"LEAVER: {r.status_code}") 
                input(f"LEAVER: {r.text}") 

            if r.status_code == 204:
                return "succes"
            else:
                return "failed"
        except Exception as e:
            if get.debug():
                input(f"LEAVER ERROR: {e}")
            else:
                return "failed"
            

    def check(token):
        session = ss()
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
        
    def send_message(token, message, channel_id):
        session = ss()
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

    def get_reactions(channel_id, message_id):
        global found_emojis
        found_emojis = False
        session = ss()
        tokens = get.tokens()
        found = False
        emojis = []
        for token in tokens:
            if not found:
                try:
                    r = session.get(
                        f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=50",
                        headers=headers(token),
                    )
                    if get.debug():
                        input(f"REACTION FETCHER: {r.status_code}") 
                        input(f"REACTION FETCHER: {r.text}") 
                    if r.status_code == 200:
                        found == True
                        for entry in r.json():
                            if entry["id"] == message_id and entry["channel_id"] == channel_id:
                                found_emojis = True
                                break
                            for message in r.json():
                                for reaction in message.get("reactions", []):
                                    emoji_name = reaction["emoji"]["name"]
                                    count = reaction["count"]
                                    emojis.append(f"{emoji_name}:{count}")
                                return emojis
                        else:
                            return "No emojis found"
                    else:
                        pass
                except Exception as e:
                    if get.debug():
                        input(f"RACTION FETCHER: {e}") 

    def react(token, channel_id, message_id, emoji):
        session = ss()
        encoded_emoji = ''.join(['%' + format(char, '02X') for char in emoji.encode('utf-8')])
        try:
            r = session.put(
                f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/%40me?location=Message&type=0",
                headers=headers(token)
            )
            if get.debug():
                input(f"REACTONER: {r.status_code}")
                input(f"REACTONER: {r.text}")
            if r.status_code == 200:
                return "succes" 
            elif r.status_code == 403:
                return "locked"
            elif r.status_code == 429:                          
                return "ratelimit", r.json().get('retry_after')
            elif r.status_code == 401:
                return "invalid"  
            else:
                return "failed"
        except Exception as e:
            if get.debug():
                input(f"REACTON ERROR {e}")


    def get_rules(guildid):
        session = ss()
        tokens = get.tokens()
        found = False
        for token in tokens:
            if not found:
                try:
                    r = session.get(
                        f"https://discord.com/api/v9/guilds/{guildid}/member-verification?with_guild=false",
                        headers=headers(token)
                    )
                    if get.debug():
                        input(f"RULE FETCHER: {r.status_code}") 
                        input(f"RULE FETCHER: {r.text}") 
                    if r.status_code == 200:
                        rules_list = r.json()["form_fields"][0]["values"]
                        rules = '\n'.join(rules_list)
                        found == True
                        return rules
                    else:
                        pass
                except Exception as e:
                    if get.debug():
                        input(f"RULE FETCHER: {e}") 

    def bypass_rules(token, guildid):
        session = ss()
        try:
            r = session.put(
                f"https://discord.com/api/v9/guilds/{guildid}/requests/@me",
                headers=headers(token)
            )
            if get.debug():
                input(f"RULE BYPASS: {r.status_code}")
                input(f"RULE BYPASS: {r.text}")
            if r.status_code == 201:
                return "succes" 
            elif r.status_code == 403:
                return "locked"
            elif r.status_code == 429:                          
                return "ratelimit", r.json().get('retry_after')
            elif r.status_code == 401:
                return "invalid"  
            else:
                return "failed"
        except Exception as e:
            if get.debug():
                input(f"RULE BYPASS: {e}")
            

    def online(token):
        try:
            ws = websocket.WebSocket()

            ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")

            ws.send(
                json.dumps(
                    {
                        "op": 2,
                        "d": {
                            "token": token,
                            "properties": {
                                "$os": "Windows",
                            },
                        },
                    }
                )
            )
        except:
            pass

    def join_vc(token, guild, channel, mute, deaf):
        try:
            for _ in range(1):
                ws = websocket.WebSocket()

                ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")

                ws.send(json.dumps({
                    "op": 2,
                    "d": {
                        "token": token,
                        "properties": {
                            "$os": "windows",
                            "$browser": "Discord",
                            "$device": "desktop"
                        }
                    }
                }))

                ws.send(json.dumps({
                    "op": 4,
                    "d": {
                        "guild_id": guild,
                        "channel_id": channel,
                        "self_mute": False,
                        "self_deaf": False
                    }
                }))
                return "succes"
        except:
            return "failed"

class modules:
    def joiner():
        if log.askyn("DISCORD ANTI RAID BYPASS") == "y": discord_bypass = True
        invite = log.ask("INVITE")
        guild_info = run.guild_info(invite)
        succes, cap, ratelimit, r_time, fail = 0, 0, 0, 0, 0
        if discord_bypass:
            for token in get.tokens():
                try:
                    status, r_time = run.bypass_join(token, invite)
                except ValueError:
                    status = run.bypass_join(token, invite)
                    r_time = "0s"
                if status == "succes": succes += 1
                elif status == "captcha": cap += 1
                elif status == "failed": fail += 1
                elif status == "ratelimit": 
                    ratelimit += 1
                    time.sleep(float(r_time))
                    run.bypass_join(token, invite)
                util.clear()
                banner = f"""{c.r}
                {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗".center(size)}
                {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝".center(size)}
                {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══".center(size)}
                """
                print(banner)
                print(f"{c.r}Discord bypass is enabled joining will take ~ {get.token_amt() / 2}m")
                input("")
                print(f"{c.r}Joined - {succes} Capched - {cap} Ratelimited - {ratelimit} ({r_time}s) Failed - {fail}")
                print(f"{c.r}\n{guild_info}")
        else:
            for token in get.tokens():
                try:
                    status, r_time = run.join(token, invite)
                except ValueError:
                    status = run.join(token, invite)
                    r_time = "0s"
                if status == "succes": succes += 1
                elif status == "captcha": cap += 1
                elif status == "failed": fail += 1
                elif status == "ratelimit": 
                    ratelimit += 1
                    time.sleep(float(r_time))
                    run.join(token, invite)
                    succes += 1
                util.clear()
                banner = f"""{c.r}
                {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗".center(size)}
                {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝".center(size)}
                {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══".center(size)}
                """
                print(banner)
                print(f"{c.r}Joined - {succes} Capched - {cap} Ratelimited - {ratelimit} ({r_time}s) Failed - {fail}")
                print(f"{c.r}\n{guild_info}")

    def leaver():
        guildid = log.ask("GUILD ID")
        succes, fail = 0, 0
        for token in get.tokens():
            status = run.leave(token, guildid)
            if status == "succes": succes += 1
            elif status == "failed": fail += 1
            util.clear()
            banner = f"""{c.r}
            {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗".center(size)}
            {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝".center(size)}
            {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══".center(size)}
            """
            print(banner)
            print(f"{c.r}Left - {succes} Failed - {fail}")

    def checker():
        if log.askyn("KEEP VALID ONLY") == "y": onlyvalid = True
        valid = []
        i = 0
        tkn_amt = get.token_amt()
        succes, lock, ratelimit, r_time, fail, invalid = 0, 0, 0, 0, 0, 0
        for token in get.tokens():
            i += 1
            try:
                status, r_time = run.check(token)
            except ValueError:
                status = run.check(token)
                r_time = "0s"
            if status == "succes": succes += 1; valid.append(token)
            elif status == "locked": lock += 1
            elif status == "failed": fail += 1
            elif status == "invalid": invalid += 1
            elif status == "ratelimit": 
                ratelimit += 1
                time.sleep(float(r_time))
                run.check(token)
                succes += 1
            util.clear()
            banner = f"""{c.r}
            {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗".center(size)}
            {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝".center(size)}
            {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══".center(size)}
            """
            print(banner)
            print(f"{c.r}Valid - {succes} Locked - {lock} Invalid - {invalid} Ratelimited - {ratelimit} ({r_time}s) Failed - {fail} {i}/{tkn_amt}")
            if onlyvalid:
                with open(f"{files.main}/tokens.txt", "w") as f:
                    for token in valid:
                        f.write(token + "\n")

    def spammer():
        message = log.ask("MESSSAGE")
        channelid = log.ask("CHANNEL ID")
        #leave_on_fail = log.askyn("LEAVE ON FAIL")
        succes, ratelimit, r_time, fail = 0, 0, 0, 0
        try:
            print(f"{c.r}Controll + C to stop")
            while True:
                for token in get.tokens():
                    try:
                        status, r_time = run.send_message(token, message, channelid)
                    except ValueError:
                        status = run.send_message(token, message, channelid)
                        r_time = "0s"
                    if status == "succes": succes += 1
                    elif status == "failed": fail += 1
                    elif status == "ratelimit": 
                        ratelimit += 1
                        time.sleep(float(r_time))
                        run.send_message(token, message, channelid)
                        succes += 1
                util.clear()
                banner = f"""{c.r}
                {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗".center(size)}
                {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝".center(size)}
                {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══".center(size)}
                """
                print(f"{c.r}Controll + C to stop")
                print(banner)
                print(f"{c.r}Sent - {succes} Ratelimited - {ratelimit} ({r_time}s) Failed - {fail}")
        except KeyboardInterrupt:
            pass

    def reactor():
        channelid = log.ask("CHANNEL ID")
        messageid = log.ask("MESSAGE ID")
        emojis = run.get_reactions(channelid)
        i = 0
        succes, ratelimit, r_time, fail = 0, 0, 0, 0, 0
        if found_emojis:
            for emoji in emojis:
                i += 1
                print(f"{c.r}{i} - {emoji.split(':')[0]}")
            choice = log.ask("EMOJI")
            try:
                selected_index = int(choice) - 1
                if 0 <= selected_index < len(emojis):
                    selected_emoji = emojis[selected_index].split(":")[0]
                    for token in get.tokens():
                        try:
                            status, r_time = run.react(token, channelid, messageid, selected_emoji)
                        except ValueError:
                            status = run.react(token, channelid, messageid, selected_emoji)
                            r_time = "0s"
                        if status == "succes": succes += 1
                        elif status == "failed": fail += 1
                        elif status == "ratelimit": 
                            ratelimit += 1
                            time.sleep(float(r_time))
                            run.react(token, channelid, messageid, selected_emoji)
                            succes += 1
                        util.clear()
                        banner = f"""{c.r}
                        {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗".center(size)}
                        {"║║║║ ║║ ║║║║║╣ ╠╦╝".center(size)}
                        {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═".center(size)}
                        """
                        print(banner)
                        print(f"{c.r}Reacted - {succes} Ratelimited - {ratelimit} ({r_time}s) Failed - {fail}")
                else:
                    print(f"{c.r}Invalid emoji index")
            except ValueError:
                print(f"{c.r}Not a valid number")
        print(f"{c.r}No emojis ware found")
    
    def rule_bypasser():
        guildid = log.ask("GUILD ID")
        rules = run.get_rules(guildid)
        succes, ratelimit, r_time, fail = 0, 0, 0, 0, 0
        for token in get.tokens():
            try:
                status, r_time = run.bypass_rules(token, guildid)
            except ValueError:
                status = run.bypass_rules(token, guildid)
                r_time = "0s"
            if status == "succes": succes += 1
            elif status == "failed": fail += 1
            elif status == "ratelimit": 
                ratelimit += 1
                time.sleep(float(r_time))
                run.bypass_rules(token, guildid)
                succes += 1
            util.clear()
            banner = f"""{c.r}
            {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗".center(size)}
            {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝".center(size)}
            {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══".center(size)}
            """
            print(banner)
            print(f"{c.r}Bypassed - {succes} Ratelimited - {ratelimit} ({r_time}s) Failed - {fail}")
            print(f"{c.r}\n{rules}")

    def button_clicker():
        guildid = log.ask("GUILD ID")
        rules = run.get_rules(guildid)
        succes, cap, fail = 0, 0, 0
        for token in get.tokens():
            status = run.bypass_rules(token, guildid)
            if status == "succes": succes += 1
            elif status == "captcha": cap += 1
            elif status == "failed": fail += 1
            util.clear()
            banner = f"""{c.r}
            {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗".center(size)}
            {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝".center(size)}
            {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══".center(size)}
            """
            print(banner)
            print(f"{c.r}Bypassed - {succes} Capched - {cap} Failed - {fail}")
            print(f"{c.r}\n{rules}")

def open_tokens():
    os.startfile(f"{get.folder()}/tokens.txt")

def open_config():
    os.startfile(f"{get.folder()}/config.json")

def change_debug_state():
    with open(f"{get.folder()}/config.json", "r") as f:
        cfg = json.load(f)
        if "settings" in cfg and "debug" in cfg["settings"]:
            cfg["settings"]["debug"] = not cfg["settings"]["debug"]

        with open(f"{get.folder()}/config.json", "w") as f:
            json.dump(cfg, f, indent=4)


def TEST():
    for token in get.tokens():
        rules = run.send_message(token, "xd", "1189982026858766458")
        input(rules)

stars = get.stars(); util.title("MoonerV2 - Fetching stars")
version_info = sys.version_info
while __name__ == "__main__":
    util.title(f"MoonerV2 - [PY {version_info.major}.{version_info.minor}.{version_info.micro}]")
    size = os.get_terminal_size().columns
    menu = f"""{c.r}
{"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗".center(size)}
{"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝".center(size)}
{"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══".center(size)}
{f"[Discord] dsc.gg/moonerv2 [Discord]".center(size)}
{f"[Stars] {stars} [Stars] ------- [Tokens] {get.token_amt()} [Tokens] ------- [Debug] {get.debug()} [Debug]".center(size)}

{"║!║ - Manage tokens       ║$║ - Edit config       ║#║ - Change debug state".center(size)}
{"! Most features are still in development".center(size)}       
{"╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗".center(size)}
{"║                                                                                                                                     ║".center(size)}
{"║  ║01║ - Joiner                ║07║ - Rule bypass           ║13║ - VC rapper                                                         ║".center(size)}
{"║  ║02║ - Leaver                ║08║ - Onboard bypass        ║14║ - Invite info                                                       ║".center(size)}
{"║  ║03║ - Checker               ║09║ - Bot authier           ║15║                                                                     ║".center(size)}
{"║  ║04║ - Spammer               ║10║ - Onliner               ║16║                                                                     ║".center(size)}
{"║  ║05║ - Reactor               ║11║ - Typier                ║17║                                                                     ║".center(size)}
{"║  ║06║ - Button clicker        ║12║ - VC joiner             ║18║                                                                     ║".center(size)}
{"║                                                                                                                                     ║".center(size)}
{"╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝".center(size)}
"""
    for x in ["═","╚","╔","╝","╗","-"]:
        menu = menu.replace(x, f"{c.lr}{x}{c.r}")
    print(menu)

    choice = input(f"""
╔══MoonerV2@{os.getlogin()}
╚══════{c.res}> """)
    options = {
        "!": open_tokens,
        "$": open_config,
        "#": change_debug_state,
        "1": modules.joiner,
        "2": modules.leaver,
        "3": modules.checker,
        "4": modules.spammer,
        "5": modules.reactor,
        "6": modules.button_clicker,
        "7": modules.rule_bypasser,
        #"10": modules.onliner,
        "test": TEST,
    }

    if choice in options:
        util.clear()
        banner = f"""{c.r}
{"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗".center(size)}
{"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝".center(size)}
{"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══".center(size)}
"""

        print(banner)
        options[choice]()
        if choice not in ["#", "$", "!"]:
            input(f"{c.g}\nFinished, waiting")
        util.clear()
    else:
        print(f"{c.r}[Invalid option]")
        time.sleep(2)
        util.clear()
