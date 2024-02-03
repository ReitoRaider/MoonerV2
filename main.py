version = "2.3"
print("Importing libs")
try:
    import os, sys, time, json, uuid, requests, base64, tls_client, random, platform, websocket, webbrowser, threading, datetime
    from colorama import init, Fore; init()
except ModuleNotFoundError:
    libs = [
        "requests",
        "tls_client",
        "colorama",
        "websocket-client",
        "uuid",
        "base64",
        "tls_client",
        "datetime"
    ]
    print("Installing libs please wait")
    for lib in libs:
        os.system(f"pip install -q {lib}")
        import os, sys, time, json, uuid, requests, base64, tls_client, random, platform, websocket, webbrowser, threading, datetime
        from colorama import init, Fore; init()

print("Importing modules")
from src import *
from src.modules import *


if platform.system() == 'Windows':
    os.system(f"mode con: cols=170 lines=35")
elif platform.system() == 'Linux':
    os.system(f"resize -s 170 35")


class files:
    main = get.folder()

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
 
if get.update():
    try:
        @staticmethod
        def get_info():
            print(f"{c.r}Searching for updates")
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

class run:
    def joiner():
        if log.askyn("DISCORD ANTI RAID BYPASS") == "y": 
            discord_bypass = True
        else:
            discord_bypass = False
        invite = log.ask("INVITE")
        guild_info = fetch_guild(invite)

        if discord_bypass:
            input(f"{c.r}Not sure if this even works if it works tell me")
            util.clear()
            banner = f"""{c.r}
            {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗"}
            {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝"}
            {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══"}
            """
            bprint(banner)
            print(f"{c.r}Discord bypass is enabled joining will take ~ {get.token_amt() / 2}m")
            print(f"{c.r}\nGuild info:\n{guild_info}")
            for token in get.tokens():
                status, text = join(token, invite, True)
                if status == 200:
                    log.g(status, text, token)
                elif status == 400:
                    log.c(status, text, token)
                elif status == 429:
                    log.r(status, text, token)
                    slip = float(text.get('retry_after'))
                    time.sleep(slip)
                else:   
                    log.un(status, text, token)

        else:
            util.clear()
            banner = f"""{c.r}
            {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗"}
            {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝"}
            {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══"}
            """
            bprint(banner)
            print(f"{c.r}\nGuild info:\n{guild_info}")
            for token in get.tokens():
                status, text = join(token, invite, True)
                if status == 200:
                    log.g(status, text, token)
                elif status == 400:
                    log.c(status, text, token)
                elif status == 429:
                    log.r(status, text, token)
                    slip = float(text.get('retry_after'))
                    time.sleep(slip)
                else:   
                    log.un(status, text, token)

    def leaver():
        guildid = log.ask("GUILD ID")
        util.clear()
        banner = f"""{c.r}
        {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗"}
        {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝"}
        {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══"}
        """
        bprint(banner)
        for token in get.tokens():
            status, text = leave(token, guildid)
            if status == 204:
                log.g(status, text, token)
            else:
                log.un(status, text, token)

    def checker():
        if log.askyn("KEEP VALID ONLY") == "y": onlyvalid = True   
        util.clear()
        banner = f"""{c.r}
        {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗"}
        {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝"}
        {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══"}
        """
        bprint(banner)
        for token in get.tokens():
            r = check(token)
            if r:
                if onlyvalid:
                    open(f"{files.main}/tokens.txt", "w")
                    with open(f"{files.main}/tokens.txt", "a") as f:
                        f.write(token + "\n")


    def spammer():
        message = log.ask("MESSSAGE")
        channelid = log.ask("CHANNEL ID")
        if log.askyn("LEAVE ON UNKNOWN CHANNEL (ANTI TOKEN BAN)") == "y": 
            leave_on_unknown = True
            guild_id = log.ask("GUILD ID")
        else:
            leave_on_unknown = False
            guild_id = "69420"

        def leave_on_unknown_func(guildid):
            if leave_on_unknown:
                for token in get.tokens():
                    status, text = leave(token, guildid)
                    if status == 204:
                        log.g(status, text, token)
                    else:
                        log.un(status, text, token)

        util.clear()
        banner = f"""{c.r}
        {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗"}
        {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝"}
        {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══"}
        """
        bprint(banner)
        print(f"{c.r}Controll + C to stop")
        for token in get.tokens():
            try:
                while True:
                    status, text = send_message(token, message, channelid, True)
                    if status == 200:
                        log.g(status, text, token)
                    elif status == 400:
                        log.c(status, text, token)
                    elif status == 429:
                        log.r(status, text, token)
                        slip = float(text.get('retry_after'))
                        time.sleep(slip)
                    elif status == 404:
                        print(f"{c.r}BAN DETECTED LEAVING")
                        leave_on_unknown_func(guild_id)
                        print(f"{c.r}Left")
                        break
                    else:   
                        log.un(status, text, token)

            except KeyboardInterrupt:
                pass

    def reactor():
        channelid = log.ask("CHANNEL ID")
        messageid = log.ask("MESSAGE ID")
        emojis, state, found_msg = get_reactions(channelid, messageid)
        i = 0
        util.clear()
        banner = f"""{c.r}
        {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗"}
        {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝"}
        {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══"}
        """
        bprint(banner)

        if state:
            if not found_msg:
                input(f"{c.r}Message not found")
                pass
            for emoji in emojis:
                i += 1
                print(f"{c.r}{i} - {emoji.split(':')[0]}")
            choice = log.ask("EMOJI")
            try:
                selected_index = int(choice) - 1
                if 0 <= selected_index < len(emojis):
                    selected_emoji = emojis[selected_index].split(":")[0]
                    for token in get.tokens():
                        status, text = react(token, channelid, messageid, selected_emoji)
                        if status == 204:
                            log.g(status, text, token)
                        elif status == 400:
                            log.c(status, text, token)
                        elif status == 429:
                            log.r(status, text, token)
                            slip = float(text.get('retry_after'))
                            time.sleep(slip)
                        else:   
                           log.un(status, text, token)
                else:
                    print(f"{c.r}Invalid emoji index")
            except ValueError:
                print(f"{c.r}Not a valid number")
        else:
            print(f"{c.r}No emojis ware found")

    def rule_bypasser():
        guildid = log.ask("GUILD ID")
        rules = get_rules(guildid)
        util.clear()
        banner = f"""{c.r}
        {"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗"}
        {"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝"}
        {"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══"}
        """
        bprint(banner)
        print(f"{c.r}\nRules:\n{rules}")
        for token in get.tokens():
            status, text = bypass_rules(token, guildid, True)
            if status == 201:
                log.g(status, text, token)
            elif status == 400:
                log.c(status, text, token)
            elif status == 429:
                log.r(status, text, token)
                slip = float(text.get('retry_after'))
                time.sleep(slip)
            else:   
                log.un(status, text, token)

    # in work
    def button_clicker():
        guildid = log.ask("GUILD ID")
        rules = get_rules(guildid)
        succes, cap, fail = 0, 0, 0
        for token in get.tokens():
            status = bypass_rules(token, guildid)
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

    def in_work():
        print(f"{c.r}This feature is still in work ")

    def no_token_check():
        if get.token_amt() == 0:
            print(f"{c.r}No tokens found please input your tokens in the opened file")
            os.startfile(f"{files.main}/tokens.txt")
            input(f"{c.res}~> Enter to continue")
            run.no_token_check()

def TEST():
    pass

print(f"{c.r}Fetching stars"); util.title("MoonerV2 - Fetching stars"); stars = get.stars()
version_info = sys.version_info
while __name__ == "__main__":
    util.clear()
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
{"║  ║01║ - Joiner                ║07║ - Rule bypass           ║13║ - VC rapper         ║19║ - ???                  ║25║ - ???          ║".center(size)}
{"║  ║02║ - Leaver                ║08║ - Onboard bypass        ║14║ - Invite info       ║20║ - ???                  ║26║ - ???          ║".center(size)}
{"║  ║03║ - Checker               ║09║ - Bot authier           ║15║ - ???               ║21║ - ???                  ║27║ - ???          ║".center(size)}
{"║  ║04║ - Spammer               ║10║ - Onliner               ║16║ - ???               ║22║ - ???                  ║28║ - ???          ║".center(size)}
{"║  ║05║ - Reactor               ║11║ - Typier                ║17║ - ???               ║23║ - ???                  ║29║ - ???          ║".center(size)}
{"║  ║06║ - Button clicker        ║12║ - VC joiner             ║18║ - ???               ║24║ - ???                  ║30║ - ???          ║".center(size)}
{"║                                                                                                                                     ║".center(size)}
{"╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝".center(size)}
"""
    for x in ["═","╚","╔","╝","╗","-"]:
        menu = menu.replace(x, f"{c.lr}{x}{c.r}")
    bprint(menu)

    run.no_token_check()

    choice = input(f"""{c.r}
╔══MoonerV2@{os.getlogin()}
╚══════{c.res}> """)
    options = {
        "!": run.open_tokens,
        "$": run.open_config,
        "#": run.change_debug_state,
        "1": run.joiner,
        "2": run.leaver,
        "3": run.checker,
        "4": run.spammer,
        "5": run.reactor,
        "6": run.button_clicker,
        "7": run.in_work,
        "8": run.in_work,
        "9": run.in_work,
        "10": run.in_work,
        "11": run.in_work,
        "12": run.in_work,
        "13": run.in_work,
        "14": run.in_work,
        "test": TEST,
    }

    if choice in options:
        util.clear()
        banner = f"""{c.r}
{"╔╦╗╔═╗╔═╗╔╗╔╔═╗╦═╗ ╦  ╦╔══╗"}
{"║║║║ ║║ ║║║║║╣ ╠╦╝ ╚╗╔╝╔══╝"}
{"╩ ╩╚═╝╚═╝╝╚╝╚═╝╩╚═  ╚╝ ╚═══"}
"""

        bprint(banner)
        options[choice]()
        if choice not in ["#", "$", "!"]:
            input(f"\n{c.res}~> Enter to continue")
        util.clear()
    else:
        print(f"{c.r}[Invalid option]")
        time.sleep(2)
        util.clear()
