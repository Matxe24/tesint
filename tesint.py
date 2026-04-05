import os
import subprocess as sub
import time as tm
from colorama import Fore, Style
import requests
import random
import socket
from concurrent.futures import ThreadPoolExecutor
import json
import shutil
import threading
import time
import sys

aka = sub.run(['whoami'], capture_output=True, text=True)
username = aka.stdout.strip()

while True:
    try:
        def clear():
            os.system('cls' if os.name == 'nt' else 'clear')

        def banner():
            banner = r"""

                       *@@@@@@@@@
                      #@@@@@@@@@@@@%
                     -@@@@- %   %@@@@
                    @@             @@
                    @                =
                   *@                @
             @@   : @  @     @              @@
             @@     @@ @  @  @    @ ** %  @ @@
             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

   ___________. ____       _____  __      ______  ___                          ______________________ _________.___ __________________
    \_   _____/|    |     /  _  \/  \    /  \   \/  /                          \__    ___/\_   _____//   _____/|   |\      \__    ___/
     |    __)  |    |    /  /_\  \   \/\/   /\     /                             |    |    |    __)_ \_____  \ |   |/   |   \|    |
     |     \   |    |___/    |    \        / /     \                             |    |    |        \/        \|   /    |    \    |
     \___  /   |_______ \____|__  /\__/\  / /___/\  \                            |____|   /_______  /_______  /|___\____|__  /____| V 0.0.1 BETA
        \/            \/       \/      \/        \_/                                             \/        \/             \/


                @@@@@@@           @@                                           ╭─────────────────────────────────────────────────────────────────────────────────╮
              :@@@@@@  @@@     @@@ *@@                                         │ 1. Username finder                       │  2. Github email puller              │
             @@@@@@@+     @@@@@@    @@@@                                       │ 3. Ip tracker                            │  4. Roblox username info             │
            @@@@@@@@%               @@@@@                                      │ 5. Coming soon...                        │  6. Coming soon...                   │
             @@@@@@@@               @@@@@@@                                    │ 7. Coming soon...                        │  8. Coming soon...                   │
         +@@@@@@@@@@@@             @@@@@@@@@                                   │ 9. Coming soon...                        │ 10. Coming soon...                   │
     @@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@@@@=                               │ 11. Coming soon...                       │ 12. Coming soon...                   │
   @@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@+                            │ 13. Coming soon...                       │ 14. Coming soon...                   │
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                           │ 15. Coming soon...                       │ 16. Coming soon...                   │
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          │ 17. Coming soon...                       │ 18. Coming soon...                   │
@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@                         │ 19. Coming soon...                       │ 20. Exit                             │
                                                                               ╰─────────────────────────────────────────────────────────────────────────────────╯




"""
            print(Fore.MAGENTA + banner)

        def terminal(username):
            command = input(Fore.BLUE + f"""\n
╭─({username}㉿tesint)-[~]
╰─❯❯ """ + Fore.GREEN)
            choice(command, username)

        def get_commit_author(username, repo):
            res = requests.get(f"https://api.github.com/repos/{username}/{repo}/commits")
            if res.status_code != 200:
                return None, None
            data = res.json()
            if not isinstance(data, list) or len(data) == 0:
                return None, None
            author = data[0].get('commit', {}).get('author', {})
            return author.get('name', 'N/A'), author.get('email', 'N/A')

        def get_user_location(username):
            res = requests.get(f"https://api.github.com/users/{username}")
            if res.status_code != 200:
                return 'N/A'
            return res.json().get('location', 'N/A')

        def githubpuller():
            Username = input(Fore.LIGHTMAGENTA_EX + "GitHub username --> ").strip()
            repos = input(Fore.LIGHTMAGENTA_EX + "Insert a repository --> ").strip()

            User, Email = get_commit_author(Username, repos)
            location = get_user_location(Username)

            if not User or not Email:
                print(Fore.RED + "[!] Username not found or no avaible commits.")
                input(Fore.WHITE + "Press enter to continue...")
                uniqe()
                return

            print("\n")

            if "noreply" in Email:
                print(Fore.YELLOW + "⚠️ Hidden email\n")
            else:
                print(Fore.GREEN + "✅ Real email found\n")

                print(Fore.CYAN + f"""\n+----+------------------------------------+---------------------------+----------------------+
| ID | Username             | Email                                   | Paese/Location       |
+----+----------------------+-----------------------------------------+----------------------+
| 1  | {User:<20} | {Email:<25}             | {location or 'N/A':<20} |
+----+----------------------+-----------------------------------------+----------------------+\n""")

            input("\nContinue...")
            uniqe()

        def get_random_user_agent():
            user_agents =  [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Linux; Android 11; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux i645 ) AppleWebKit/601.39 (KHTML, like Gecko) Chrome/52.0.1303.178 Safari/600",
    "Mozilla/5.0 (Windows; U; Windows NT 6.2; x64; en-US) AppleWebKit/603.16 (KHTML, like Gecko) Chrome/49.0.3596.149 Safari/602",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_12_8) AppleWebKit/537.8 (KHTML, like Gecko) Chrome/51.0.3447.202 Safari/533",
    "Mozilla/5.0 (U; Linux x86_64; en-US) AppleWebKit/535.12 (KHTML, like Gecko) Chrome/54.0.2790.274 Safari/601",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 7_5_1) AppleWebKit/534.29 (KHTML, like Gecko) Chrome/54.0.2941.340 Safari/602",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_4_2) AppleWebKit/602.18 (KHTML, like Gecko) Chrome/47.0.1755.159 Safari/600",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_6_4; like Mac OS X) AppleWebKit/601.29 (KHTML, like Gecko)  Chrome/47.0.1661.149 Mobile Safari/536.4",
    "Mozilla/5.0 (Linux; Android 5.1; SM-G9350T Build/LMY47X) AppleWebKit/602.21 (KHTML, like Gecko)  Chrome/50.0.1176.329 Mobile Safari/535.9",
    "Mozilla/5.0 (Linux; U; Android 6.0.1; HTC One M8 Build/MRA58K) AppleWebKit/600.36 (KHTML, like Gecko)  Chrome/53.0.3363.154 Mobile Safari/537.2",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_8_3) Gecko/20100101 Firefox/50.7",
    "Mozilla/5.0 (U; Linux i671 x86_64) AppleWebKit/535.27 (KHTML, like Gecko) Chrome/54.0.1417.286 Safari/537",
    "Mozilla/5.0 (iPad; CPU iPad OS 9_4_4 like Mac OS X) AppleWebKit/536.12 (KHTML, like Gecko)  Chrome/55.0.1687.155 Mobile Safari/600.8",
    "Mozilla/5.0 (Linux; Android 4.4.1; LG-V510 Build/KOT49I) AppleWebKit/535.28 (KHTML, like Gecko)  Chrome/52.0.2705.296 Mobile Safari/602.9",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/54.0.2084.216 Safari/603.3 Edge/8.91691",
    "Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.0; WOW64; en-US Trident/7.0)",
    ]

            return random.choice(user_agents)

        def usersearch(nick):

            urls = {
                "Facebook": f"https://www.facebook.com/{nick}",
                "Telegram": f"https://t.me/{nick}",
                "Reddit": f"https://www.reddit.com/user/{nick}",
                "Twitch": f"https://www.twitch.tv/{nick}",
                "Pinterest": f"https://www.pinterest.com/{nick}",
                "Snapchat": f"https://www.snapchat.com/add/{nick}",
                "Threads": f"https://www.threads.net/@{nick}",
                "Mastodon": f"https://mastodon.social/@{nick}",
                "TruthSocial": f"https://truthsocial.com/@{nick}",
                "Gettr": f"https://gettr.com/user/{nick}",
                "Gab": f"https://gab.com/{nick}",
                "VK": f"https://vk.com/{nick}",
                "Odysee": f"https://odysee.com/@{nick}",
                "Rumble": f"https://rumble.com/user/{nick}",
                "Dailymotion": f"https://www.dailymotion.com/{nick}",
                "Keybase": f"https://keybase.io/{nick}",
                "AboutMe": f"https://about.me/{nick}",
                "Patreon": f"https://www.patreon.com/{nick}",
                "OnlyFans": f"https://onlyfans.com/{nick}",
                "KoFi": f"https://ko-fi.com/{nick}",
                "BuyMeACoffee": f"https://www.buymeacoffee.com/{nick}",
                "GitLab": f"https://gitlab.com/{nick}",
                "Bitbucket": f"https://bitbucket.org/{nick}",
                "SourceForge": f"https://sourceforge.net/u/{nick}",
                "StackOverflow": f"https://stackoverflow.com/users/{nick}",
                "Kaggle": f"https://www.kaggle.com/{nick}",
                "Replit": f"https://replit.com/@{nick}",
                "CodePen": f"https://codepen.io/{nick}",
                "Dev.to": f"https://dev.to/{nick}",
                "Hashnode": f"https://hashnode.com/@{nick}",
                "HuggingFace": f"https://huggingface.co/{nick}",
                "JSFiddle": f"https://jsfiddle.net/user/{nick}",
                "HackerRank": f"https://www.hackerrank.com/{nick}",
                "LeetCode": f"https://leetcode.com/{nick}",
                "TopCoder": f"https://www.topcoder.com/members/{nick}",
                "Codewars": f"https://www.codewars.com/users/{nick}",
                "Exercism": f"https://exercism.org/profiles/{nick}",
                "StackExchange": f"https://stackexchange.com/users/{nick}",
                "npm": f"https://www.npmjs.com/~{nick}",
                "PyPI": f"https://pypi.org/user/{nick}",
                "DockerHub": f"https://hub.docker.com/u/{nick}",
                "RubyGems": f"https://rubygems.org/profiles/{nick}",
                "CPAN": f"https://metacpan.org/author/{nick}",
                "Arduino": f"https://create.arduino.cc/users/{nick}",
                "Hackaday": f"https://hackaday.io/{nick}",
                "Steam": f"https://steamcommunity.com/id/{nick}",
                "EpicGames": f"https://www.epicgames.com/id/{nick}",
                "Xbox": f"https://xboxgamertag.com/search/{nick}",
                "PlayStation": f"https://psnprofiles.com/{nick}",
                "Roblox": f"https://www.roblox.com/user.aspx?username={nick}",
                "Minecraft": f"https://namemc.com/profile/{nick}",
                "Speedrun": f"https://www.speedrun.com/user/{nick}",
                "Chess.com": f"https://www.chess.com/member/{nick}",
                "Lichess": f"https://lichess.org/@/{nick}",
                "GameJolt": f"https://gamejolt.com/@{nick}",
                "ModDB": f"https://www.moddb.com/members/{nick}",
                "Itch.io": f"https://itch.io/profile/{nick}",
                "Valorant": f"https://tracker.gg/valorant/profile/riot/{nick}/overview",
                "Fortnite": f"https://fortnitetracker.com/profile/all/{nick}",
                "ApexLegends": f"https://apex.tracker.gg/apex/profile/origin/{nick}/overview",
                "PUBG": f"https://pubg.op.gg/user/{nick}",
                "CSGO": f"https://csgostats.gg/player/{nick}",
                "Dota2": f"https://www.dotabuff.com/players/{nick}",
                "Overwatch": f"https://overbuff.com/players/{nick}",
                "Hearthstone": f"https://www.hearthstonetopdecks.com/player/{nick}",
                "GOG": f"https://www.gog.com/u/{nick}",
                "Medium": f"https://medium.com/@{nick}",
                "WordPress": f"https://{nick}.wordpress.com",
                "Blogger": f"https://{nick}.blogspot.com",
                "Tumblr": f"https://{nick}.tumblr.com",
                "Wattpad": f"https://www.wattpad.com/user/{nick}",
                "Substack": f"https://{nick}.substack.com",
                "Ghost": f"https://{nick}.ghost.io",
                "LiveJournal": f"https://{nick}.livejournal.com",
                "Quora": f"https://www.quora.com/profile/{nick}",
                "Goodreads": f"https://www.goodreads.com/{nick}",
                "Letterboxd": f"https://letterboxd.com/{nick}",
                "MyAnimeList": f"https://myanimelist.net/profile/{nick}",
                "AniList": f"https://anilist.co/user/{nick}",
                "LastFM": f"https://www.last.fm/user/{nick}",
                "Discogs": f"https://www.discogs.com/user/{nick}",
                "SoundCloud": f"https://soundcloud.com/{nick}",
                "Bandcamp": f"https://{nick}.bandcamp.com",
                "Mixcloud": f"https://www.mixcloud.com/{nick}",
                "Spotify": f"https://open.spotify.com/user/{nick}",
                "Genius": f"https://genius.com/{nick}",
                "Amazon": f"https://www.amazon.it/{nick}",
                "Ebay": f"https://www.ebay.it/{nick}",
                "Doxbin": f"https://doxbin.com/{nick}",
                "VoidBin": f"https://voidbin.rf.gd/{nick}",
                "Youtube": f"https://youtube.com/@{nick}",
                "Github": f"https://github.com/{nick}"
            }

            print(f"{Fore.BLUE}➤ Scanning '{nick}':\n{Style.RESET_ALL}")
            found = []

            for name, url in urls.items():
                try:
                    response = requests.get(url, headers={'User-Agent': get_random_user_agent()}, timeout=5)
                    code = response.status_code
                    if code == 200:
                        print(f"{Fore.WHITE}➤ {name}: {url} - {Fore.GREEN}Found!{Style.RESET_ALL}")
                        found.append(f"{name}: {url}")
                    elif code in [301, 302, 403]:
                        print(f"{Fore.WHITE}➤ {name}: {url} - {Fore.YELLOW}Possible match (status {code}){Style.RESET_ALL}")
                    else:
                        print(f"{Fore.WHITE}➤ {name}: {url} - {Fore.RED}Not found (status {code}){Style.RESET_ALL}")
                except requests.RequestException as e:
                    print(f"{Fore.WHITE}➤ {name}: {url} - {Fore.RED}Error: {e}{Style.RESET_ALL}")


            input(f"\n{Fore.CYAN}➤ Press enter to continue...{Style.RESET_ALL}")
            uniqe()


        def roblox():
            username = input("Roblox usernames: ")
            headers = {"Content-Type": "application/json"}
            r = requests.post("https://users.roblox.com/v1/usernames/users", json={"usernames": [username]}, headers=headers)
            data = r.json().get("data", [])
            if not data:
                print("❌ Username not found or roblox not responding")
                return

            user_id = data[0]["id"]
            profile = requests.get(f"https://users.roblox.com/v1/users/{user_id}").json()
            groups = requests.get(f"https://groups.roblox.com/v2/users/{user_id}/groups/roles").json()
            friends = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/friends").json()
            badges = requests.get(f"https://badges.roblox.com/v1/users/{user_id}/badges").json()
            games = requests.get(f"https://games.roblox.com/v2/users/{user_id}/games?accessFilter=Public&sortOrder=Asc&limit=50").json()
            presence = requests.post("https://presence.roblox.com/v1/presence/users", json={"userIds": [user_id]}, headers=headers).json()
            thumbnails = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=720x720&format=Png&isCircular=false").json()
            aliases = requests.get(f"https://users.roblox.com/v1/users/{user_id}/username-history?limit=50&sortOrder=Desc").json()

            print("\Roblox Profile")
            print(f"  • Username: {username}")
            print(f"  • Display Name: {profile.get('displayName')}")
            print(f"  • User ID: {user_id}")
            print(f"  • Created on: {profile.get('created')[:10]}")
            print(f"  • Bio: {profile.get('description') or '(vuota)'}")
            print(f"  • Status: {'Offline' if presence.get('userPresences', [{}])[0].get('userPresenceType') == 0 else 'Online'}")
            print(f"  • Avatar: {thumbnails.get('data', [{}])[0].get('imageUrl')}\n")

            print("Obtained badges")
            badge_list = [b["name"] for b in badges.get("data", [])]
            if badge_list:
                for b in badge_list:
                    print(f"  • {b}")
            else:
                print("  • None or hidden")

            print("\nPublished games")
            game_list = [g["name"] for g in games.get("data", [])]
            if game_list:
                for g in game_list:
                    print(f"  • {g}")
            else:
                print("  • None")

            print("\nGroups")
            group_list = [g["group"]["name"] for g in groups.get("data", [])]
            if group_list:
                for g in group_list:
                    print(f"  • {g}")
            else:
                print("  • No groups")

            print("\nLast usernames")
            alias_list = [a["name"] for a in aliases.get("data", [])]
            if alias_list:
                for a in alias_list:
                    print(f"  • {a}")
            else:
                print("  • No other usernames")

            print(f"\nFriends: {len(friends.get('data', []))}\n")
            cua = input(Fore.WHITE + "\nVuoi fare una ricerca approfondita per cercare collegamenti con l'account?(Y/n)")
            if cua == 'yes' or cua == 'YES' or cua == 'y' or cua == 'Y' or cua == 's' or cua == 'S':
                nick = input(f'\n{Fore.WHITE}[?] Enter nickname -> {Fore.RED}').strip()
                usersearch(nick)
            else:
                main()

        def ip_tracker():
            ip = input(Fore.WHITE + "IP to track: ")
            r = requests.get(f"https://ipwhois.app/json/{ip}")
            data = r.json()

            print("\n IP Localization")
            print(f"  • IP: {data.get('ip')}")
            print(f"  • Country: {data.get('country')} ({data.get('country_code')})")
            print(f"  • Region: {data.get('region')}")
            print(f"  • City: {data.get('city')}")
            print(f"  • Postal Code: {data.get('postal')}")
            print(f"  • Latitude: {data.get('latitude')}")
            print(f"  • Longitude: {data.get('longitude')}")
            print(f"  • ISP: {data.get('isp')}")
            print(f"  • ASN: {data.get('asn')}")
            print(f"  • Organization: {data.get('org')}")
            print(f"  • Type: {data.get('type')}")
            print(f"  • Continent: {data.get('continent')} ({data.get('continent_code')})")
            print(f"  • Timezone: {data.get('timezone_gmt')} ({data.get('timezone_name')})")
            print(f"  • Mobile Connection: {'Yes' if data.get('mobile') else 'No'}")
            print(f"  • Proxy/VPN: {'Yes' if data.get('proxy') else 'No'}")
            print(f"  • Hosting: {'Yes' if data.get('hosting') else 'No'}")
            input("\nContinue...")
            uniqe()

        def update():
            CURRENT_VERSION = "0.1.0"
            PASTEBIN_URL = "https://pastebin.com/raw/HbaEe6BP"
            REPO_URL = "https://github.com/Matxe24/tesint"

            try:
                response = requests.get(PASTEBIN_URL, timeout=5)
                latest_version = response.text.strip()

                if latest_version != CURRENT_VERSION:
                    print(f"\n🔔 New update available! Current: {CURRENT_VERSION} → Latest: {latest_version}")
                    choice = input("Do you want to download and install the new version? (Y/n): ").strip().lower()

                    if choice in ["y", ""]:
                        clone_dir = f"tesint_{latest_version}"
                        if os.path.exists(clone_dir):
                            print(f"Folder '{clone_dir}' already exists. Removing it first...")
                            try:
                                sub.run(["rm", "-rf", clone_dir], check=True)
                            except Exception:
                                print("Could not remove old folder, please delete manually.")
                                return

                        print(f"Cloning repository into '{clone_dir}'...")
                        sub.run(["git", "clone", REPO_URL, clone_dir], check=True)

                        setup_path = os.path.join(clone_dir, "setup.py")
                        print("Running setup.py...")
                        try:
                            sub.run(["python3", setup_path], check=True)
                        except Exception:
                            print(f"Failed to run setup.py in {clone_dir}. Please run it manually.")
                    else:
                        clear()
                        banner()
                        terminal(username)
                else:
                    clear()
                    banner()
                    terminal(username)

            except Exception as e:
                print(f"\n⚠️ Could not check for updates: {e}")


        def cookies():
            pass

        def choice(command, username):
            if command == '1':
                nick = input("Username: ")
                usersearch(nick)
            elif command == '2':
                githubpuller()
            elif command == '3':
                ip_tracker()
            elif command == '4':
                roblox()
            elif command == '20' or command == 'exit' or command == 'EXIT':
                print(Fore.RED + f"\nExiting... Stay stealthy {username}.\n")
                tm.sleep(0.7)
                exit()
            else:
                print(Fore.YELLOW + f"\n[!] Unkown command: {command}.\n")
                tm.sleep(0.7)
                uniqe()

        def uniqe():
            main()

        def main():
            update()
            clear()
            banner()
            terminal(username)

        main()

    except KeyboardInterrupt:
        print(Fore.MAGENTA + f"\n\nExiting, stay stealthy {username}")
        tm.sleep(0.6)
        exit()
