import os,re,warnings,configparser,sys

from attr import field

my_os = sys.platform
print("Currently on ",my_os)
try :
    assert sys.version_info >= (3,)
    print("Python version check: ok")
except:
    print("Version de Python < 3")
    print("Mettre a jour la version !")
    time.sleep(4)
    sys.exit()

if my_os != "linux":
    try:
        import time,praw,random
    except:
        os.system("pip install requests")
        os.system("pip install praw")
        os.system("cls")
    else:
        print("time,praw,random : OK")
    try:
        from pystyle import Center, Anime, Colors, Colorate  # pip install pystyle
    except:
        os.system("pip install pystyle")
        os.system("cls")
    else:
        print("pystyle: OK")
    try:
        from colorama import init, Fore  # pip install colorama
    except:
        os.system("pip install colorama")
        os.system("cls")
    else:
        print("colorama: OK")
    try:
        from psaw import PushshiftAPI
    except:
        os.system("pip install psaw")
    else:
        print("psaw: OK")
    try:
        from datetime import datetime
    except:
        os.system("pip install datetime")
    else:
        print("datetime: OK")
    print(f"{Fore.LIGHTCYAN_EX}Pip install's with window: OK")
else:
    try:
        import time,praw,random
    except:
        os.system("pip3 install requests")
        os.system("pip3 install praw")
        os.system("reset")
    else:
        print("time,praw,random: OK")
    try:
        from pystyle import Center, Anime, Colors, Colorate  # pip install pystyle
    except:
        os.system("pip3 install pystyle")
        os.system("reset")
    else:
        print("pystyle: OK")
    try:
        from colorama import init, Fore  # pip install colorama
    except:
        os.system("pip3 install colorama")
        os.system("reset")
    else:
        print("colorama: OK")
    try:
        from psaw import PushshiftAPI
    except:
        os.system("pip3 install psaw")
    else:
        print("psaw: OK")
    try:
        from datetime import datetime
    except:
        os.system("pip3 install datetime")
        print("datetime: OK")
    else:
        print(f"{Fore.LIGHTCYAN_EX}Pip install's with linux: OK")


init()
warnings.filterwarnings("ignore")
cfg = configparser.RawConfigParser()
if my_os != "linux":
    cfg.read("tools\config.ini")
else:
    cfg.read("tools/config.ini")

banner = r"""

                    ,----------------,              ,---------,
               ,-----------------------,          ,"        ,"|
             ,"                      ,"|        ,"        ,"  |
            +-----------------------+  |      ,"        ,"    |
            |  .-----------------.  |  |     +---------+      |
            |  |                 |  |  |     | -==----'|      |
            |  |  I LOVE NFT!    |  |  |     |         |      |
            |  |  Bad command or |  |  |/----|`---=    |      |
            |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
            |  |     Press ENTER |  |  |  // |(((( [33]|    ,"
            |  `-----------------'  |," .;'| |((((     |  ,"
            +-----------------------+  ;;  | |         |,"
                /_)______________(_/  //'   | +---------+
        ___________________________/___  `,
       /  oooooooooooooooo  .o.  oooo /,   \,"-----------
      / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
     /_==__==========__==_ooo__ooo=_/'   /___________,"
     `-----------------------------'

        ██████╗  ██████╗ ████████╗    ███╗   ██╗███████╗████████╗
        ██╔══██╗██╔═══██╗╚══██╔══╝    ████╗  ██║██╔════╝╚══██╔══╝
        ██████╔╝██║   ██║   ██║       ██╔██╗ ██║█████╗     ██║   
        ██╔══██╗██║   ██║   ██║       ██║╚██╗██║██╔══╝     ██║   
        ██████╔╝╚██████╔╝   ██║       ██║ ╚████║██║        ██║   
        ╚═════╝  ╚═════╝    ╚═╝       ╚═╝  ╚═══╝╚═╝        ╚═╝   
"""[1:]

Anime.Fade(Center.Center(banner), Colors.blue_to_purple,
           Colorate.Horizontal, enter=True)
print(banner)


class fontS:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


Ncompte = ["", "COMPTE1", "COMPTE2", "COMPTE3"]

x = 0
while x != 1:
    try:
        compte = int(input(f"{Fore.LIGHTCYAN_EX}Choisir le bot n° {Fore.LIGHTYELLOW_EX}| {Fore.CYAN}1 {Fore.LIGHTYELLOW_EX}| {Fore.CYAN}2 {Fore.LIGHTYELLOW_EX}| {Fore.CYAN}3 {Fore.LIGHTYELLOW_EX}| : {Fore.LIGHTMAGENTA_EX}"))
        compte = Ncompte[compte]
        API_REDDIT_CLIENT_ID = eval(cfg[compte]["API_REDDIT_CLIENT_ID"])
    except KeyError:
        print(f"{Fore.RED}[{Fore.LIGHTWHITE_EX}!{Fore.RED}] {Fore.LIGHTRED_EX}Le compte n'existe pas ! {fontS.END}")
        print(f"{Fore.RED}__"*60)
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTWHITE_EX}!{Fore.RED}] {Fore.LIGHTRED_EX}Saisie invalide, il faut saisir un chiffre ! {fontS.END}")
        print(f"{Fore.RED}__"*60)
    else:
        x = 1
if my_os != "linux":
    os.system("cls")
else:
    os.system("reset")

NoCompte = f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}] {Fore.LIGHTCYAN_EX}Account : {fontS.BOLD}{Fore.WHITE}{compte}"
print(NoCompte)

API_REDDIT_CLIENT_ID = eval(cfg[compte]["API_REDDIT_CLIENT_ID"])
API_REDDIT_CLIENT_SECRET = eval(cfg[compte]["API_REDDIT_CLIENT_SECRET"])
API_REDDIT_USERNAME = eval(cfg[compte]["API_REDDIT_USERNAME"])
API_REDDIT_USER_AGENT = eval(cfg[compte]["API_REDDIT_USER_AGENT"])
API_REDDIT_PASSWORD = eval(cfg[compte]["API_REDDIT_PASSWORD"])

REDDIT_SUBS = eval(cfg["Reddit"]["REDDIT_SUBS"])
REDDIT_COMMENTS = eval(cfg["Reddit"]["REDDIT_COMMENTS"])
REDDIT_EMOJIS = ["🤞","🙏","❤️","💯","💸"]

OPENSEA_WALLET = eval(cfg["Bot"]["OPENSEA_WALLET"])
MAX_GIVEAWAYS = eval(cfg["Bot"]["MAX_GIVEAWAYS"])
MIN_GIVEAWAYS = eval(cfg["Bot"]["MIN_GIVEAWAYS"])
MIN_SECS_SLEEP = eval(cfg["Bot"]["MIN_SECS_SLEEP"])
MAX_SECS_SLEEP = eval(cfg["Bot"]["MAX_SECS_SLEEP"])
MIN_BIG_SLEEP = eval(cfg["Bot"]["MIN_BIG_SLEEP"])
MAX_BIG_SLEEP = eval(cfg["Bot"]["MAX_BIG_SLEEP"])

if OPENSEA_WALLET != "":
    print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}] {Fore.LIGHTCYAN_EX}Wallet:{Fore.WHITE} OK")
else:
    print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.RED}] {Fore.LIGHTCYAN_EX}Wallet:{Fore.WHITE} No wallet !")
    time.sleep(3)
    sys.exit()

praw_api = praw.Reddit(
    client_id=API_REDDIT_CLIENT_ID,
    client_secret=API_REDDIT_CLIENT_SECRET,
    username=API_REDDIT_USERNAME,
    user_agent=API_REDDIT_USER_AGENT,
    password=API_REDDIT_PASSWORD,
)
psaw_api = PushshiftAPI()
submissions = psaw_api.search_submissions(
    q="nft giveway",
    subreddit=REDDIT_SUBS,
    filter=["id"],
    sort="new", 
)

def isAccountOK():
    try:
        commentd = praw_api.comment("t3_qsj32h")
        commentd.upvote()
    except Exception as err:
        if str(err) == f"received 403 HTTP response":
            print(f"{Fore.RED}---------------------------------\n[{Fore.WHITE}Alerte{Fore.RED}] Compte bannis de Reddit !")
        else:
            print(f"{Fore.RED}---------------------------------\n[{Fore.WHITE}Alerte{Fore.RED}] Les informations du compte ne sont pas valides !")
        time.sleep(2)
        print("---------------------------------")
        time.sleep(2)
        print(f"/{Fore.WHITE}!{Fore.RED}\ Fermeture du programe... /{Fore.WHITE}!{Fore.RED}\ \n--------------------------------- ")
        cd = 5
        print("")
        for i in range(5):
            time.sleep(1)
            if my_os != "linux":
                os.system("cls")
            else:
                os.system("reset")
            print(f"[{Fore.WHITE}!{Fore.RED}] ", cd)
            cd -= 1
        time.sleep(1)
        sys.exit()
    else:
        print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}] {Fore.LIGHTCYAN_EX}Account state:{Fore.WHITE} OK")

isAccountOK()
Nb_Giveaway = random.randint(MIN_GIVEAWAYS, MAX_GIVEAWAYS)

if my_os != "linux":
    with open("misc\COM.txt", "r") as com:
        AllAutors = com.readline()
else:
    with open("misc/COM.txt", "r") as com:
        AllAutors = com.readline()

print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.LIGHTCYAN_EX} Debut de session de {Nb_Giveaway} commentaires !")
print(f"{Fore.RED}__"*60)
cnt = 1

while True:
    while Nb_Giveaway > cnt:
        try:
            print(submission," ", submission.id)
            submission = next(submissions, None)
            if not submission:
                print("no sub")
                break
            submission = praw_api.submission(id=submission.id)
            with open("misc\COM.txt", "r") as com:
                AllAutors = com.readline()
            if (
                not submission.removed_by_category
                and submission.selftext
                and submission.id not in AllAutors
            ):
                text_from_op = submission.selftext

                have_seen_post_before = False
                for comment in submission.comments:
                    if comment.author.name == API_REDDIT_USERNAME:
                        have_seen_post_before = True
                    elif comment.author.name == submission.author.name:
                        text_from_op += comment.body
                
                if have_seen_post_before:
                    continue
                if (
                    "opensea" not in text_from_op.lower()
                    and "opensea" not in submission.subreddit.display_name.lower()
                ):
                    continue
                try:
                    comment = random.choice(REDDIT_COMMENTS)
                    emoji = random.choice(REDDIT_EMOJIS)
                    submission.reply(f"{comment} {OPENSEA_WALLET} {emoji}")
                    submission.upvote()
                except:
                    print("Reply error")
                    isAccountOK()
                    break

                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} Comment {Fore.LIGHTBLACK_EX}#{Fore.LIGHTWHITE_EX} {cnt}")
                print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} Current Time:{Fore.WHITE} {current_time}")
                print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} URL: {Fore.LIGHTBLUE_EX} {submission.url}")
                print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} Title:{Fore.LIGHTBLACK_EX} {submission.title}")

                try:
                    opensea_url = re.search(
                        "(?P<url>https?://opensea.io[^\s]+)", text_from_op
                    ).group("url")
                    if opensea_url:
                        if "]" in opensea_url:
                            opensea_url = opensea_url.split("]")[0]
                        if ")" in opensea_url:
                            opensea_url = opensea_url.split(")")[0]
                        print(
                            f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} OPENSEA: ", opensea_url)
    
                except:
                    print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} No Opensea URL")
    
                secs_to_wait = random.randint(MIN_SECS_SLEEP, MAX_SECS_SLEEP)
                time.sleep(secs_to_wait)
                cnt += 1
                
                if my_os != "linux":
                    try:
                        com = open("misc\COM.txt", "a")
                        com.write(submission.id+"\n")
                        with open("misc\COM.txt", "r") as com:
                            AllAutors = com.readline()
                    except:
                        print("Probleme lors de l'enregistrement de l'id")
                        sys.exit()
                    else:
                        print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} Id:{Fore.WHITE} OK")
                        print(f"{Fore.RED}__"*60)
                else:
                    try:
                        com = open("misc/COM.txt", "a")
                        com.write(submission.id+"\n")
                        with open("misc/COM.txt", "r") as com:
                            AllAutors = com.readline()
                    except:
                        print("Probleme lors de l'enregistrement de l'id")
                        sys.exit()
                    else:
                        print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} Id:{Fore.WHITE} OK")
                        print(f"{Fore.RED}__"*60)
            #else: #DEBUG
            #    print("invalid post")
        except:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"{Fore.WHITE}{current_time} | No Giveaway!")
            print(f"{Fore.RED}__"*60)
            time.sleep(3)
    
    pause = random.randint(MIN_BIG_SLEEP, MAX_BIG_SLEEP)
    print(f"Pause de {pause} secondes")
    time.sleep(pause)
    isAccountOK()
    Nb_Giveaway = random.randint(MIN_GIVEAWAYS, MAX_GIVEAWAYS) 
    print(f"Debut de session de {Nb_Giveaway} commentaires !")
    print(f"{Fore.RED}__"*60)