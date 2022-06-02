import os,re,warnings,configparser,sys
from math import ceil
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
    x = "cls"
else:
    x = "reset"

try:
    import time,praw,random
    from pystyle import Center, Anime, Colors, Colorate
    from colorama import init, Fore
    from psaw import PushshiftAPI
    from datetime import datetime
    from discord_webhook import DiscordWebhook, DiscordEmbed
except:
    os.system("pip install praw")
    os.system("pip install pystyle")
    os.system("pip install colorama")
    os.system("pip install psaw")
    os.system("pip install datetime")
    os.system("pip3 install discord-webhook")
    os.system(x)
    try:
        os.system("python botr.py")
        os.system("exit")
    except:
        try:
            os.system("python3 botr.py")
            os.system("exit")
        except:
            print("reload script")
else:
    print("Installs: OK")


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

Anime.Fade(Center.Center(banner), Colors.blue_to_purple,Colorate.Horizontal, enter=True)
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

webhookurl = eval(cfg["Discord"]["webhookurl"])

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
    
def bot_pause(pause):
    print(f"Pause de {pause} secondes")
    time.sleep(pause)
    isAccountOK()
    Nb_Giveaway = random.randint(MIN_GIVEAWAYS, MAX_GIVEAWAYS) 
    try:
        start()
        print(f"Debut de session de {Nb_Giveaway} commentaires !")
        print(f"{Fore.RED}__"*60)
    except:
        print(f"{Fore.RED}Erreur lors du lancement du giveaway !{Fore.WHITE}")
        sys.exit()
    
isAccountOK()

if my_os != "linux":
    with open("misc\COM.txt", "r") as com:
        AllAutors = com.readline()
else:
    with open("misc/COM.txt", "r") as com:
        AllAutors = com.readline()

def recherche(REDDIT_SUBS):
    subreddit = random.choice(REDDIT_SUBS)
    newF = praw_api.subreddit(subreddit).search(query="nft giveaway",sort="new")
    topD = praw_api.subreddit(subreddit).search(query="nft giveaway",sort="top",time_filter="day")
    topH = praw_api.subreddit(subreddit).search(query="nft giveaway",sort="top",time_filter="hour")
    topW = praw_api.subreddit(subreddit).search(query="nft giveaway",sort="top",time_filter="week")
    hot = praw_api.subreddit(subreddit).search(query="nft giveaway",sort="hot")
    listeR = [newF,topD,topH,hot]
    return random.choice(listeR)

def start():
    
    Nb_Giveaway = random.randint(MIN_GIVEAWAYS, MAX_GIVEAWAYS)
    print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.LIGHTCYAN_EX} Debut de session de {Nb_Giveaway} commentaires !")
    print(f"{Fore.RED}__"*60)

    #WEBHOOK
    webhook = DiscordWebhook(url=webhookurl, username="NFT Bot logger", avatar_url="https://upload.wikimedia.org/wikipedia/commons/2/24/NFT_Icon.png")

    # create embed object for webhook
    embed = DiscordEmbed(title="**[>]** Nouvelle session de commentaires !", description="```Le bot est parti chercher vos NFT's...```", color="f1330a")
    # add gif to embed

    embed.set_thumbnail(url='https://c.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif')
    embed.set_author(name="SohKey's Bot", url="https://github.com/SohKey", icon_url="https://29.recreatiloups.com/wp-content/uploads/sites/2/2018/06/robot-stage-enfant.png")
    embed.add_embed_field(name='Nombre de commentaires: ', value=f'```{Nb_Giveaway}```', inline=False)
    subs=""
    x=0
    while x < len(REDDIT_SUBS)//2:
        subs += f"\n :white_check_mark: {REDDIT_SUBS[x]}"
        x +=1
    embed.add_embed_field(name=f'Nombre de subbredit : ㅤ{len(REDDIT_SUBS)}', value= f'{subs}\nㅤ', inline=True)
    subs=""
    while x < len(REDDIT_SUBS):
            subs += f"\n :white_check_mark: {REDDIT_SUBS[x]}"
            x +=1
    embed.add_embed_field(name='ㅤ', value= f'{subs}\nㅤ', inline=True)
    webhook.add_embed(embed)
    webhook.execute()

    #END WEBHOOK

    cnt = 1
    print("Bot shearching for giveways...")
    while Nb_Giveaway > cnt:
        for submission in recherche(REDDIT_SUBS):
            with open("misc\COM.txt", "r") as com:
                id_com = com.readline()
            try:
                if (
                    not submission.removed_by_category
                    and submission.selftext
                    and submission.id not in id_com
                ):
                    text_from_op = submission.selftext
                    have_seen_post_before = False
                    for comment in submission.comments:
                        if comment.author.name == API_REDDIT_USERNAME:
                            have_seen_post_before = True
                        elif comment.author.name == submission.author.name:
                            text_from_op += comment.body

                    if have_seen_post_before:
                        print(f'LOG: post deja vu {submission.id}') #DEBUG
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
                        continue
                    try:
                        com = open(f"misc/COM.txt", "a")
                        com.write(submission.id+"\n")
                        with open(f"misc/COM.txt", "r") as com:
                            id_com = com.readline()
                    except :
                        print("Probleme lors de l'enregistrement de l'id")
                        sys.exit()
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} Comment {Fore.LIGHTBLACK_EX}#{Fore.LIGHTWHITE_EX} {cnt}")
                    print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} Current Time:{Fore.WHITE} {current_time}")
                    print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} URL: {Fore.LIGHTBLUE_EX} {submission.url}")
                    print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} Title:{Fore.LIGHTBLACK_EX} {submission.title}")
                    print(f"{Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX}]{Fore.MAGENTA} Id: {Fore.LIGHTBLUE_EX}{id_com}{Fore.WHITE}")

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
                    finally:
                        print(f"{Fore.RED}__"*60)
                    #WEBHOOK
                    hexadecimal=""
                    for i in range(6):
                        hexadecimal +=random.choice('ABCDEF0123456789')

                    embed = DiscordEmbed(title="[>] **Le bot a posté un commentaire !**", description="point faible: trop fort !", color=hexadecimal)
                    # add gif to embed
                    listgif = ["https://c.tenor.com/wAW9GrwqeEoAAAAM/domingo-popcorn.gif", "https://c.tenor.com/NgSabDXAUkkAAAAC/messi-messi-bud.gif", "https://c.tenor.com/5tVlz8y2CdYAAAAC/kameto-kcorp.gif", "https://c.tenor.com/wNxWV_SrS1sAAAAd/clin-doeil-wink.gif"]
                    gif = random.choice(listgif)
                    embed.set_thumbnail(url=gif, height=650, width=650)
                    embed.set_author(name="SohKey's Bot", url="https://github.com/SohKey", icon_url="https://29.recreatiloups.com/wp-content/uploads/sites/2/2018/06/robot-stage-enfant.png")
                    embed.add_embed_field(name='Nom du post :', value=f'{submission.title}', inline=False)
                    embed.add_embed_field(name='Lien du post :', value=f'{submission.url}', inline=False)
                    embed.add_embed_field(name='ID du post :', value=f'{submission.id}', inline=True)
                    embed.add_embed_field(name='Commentaire :', value=f'{comment}', inline=True)
                    embed.add_embed_field(name='Nombre de messages envoyés :', value=f'{cnt}', inline=False)
                    webhook.add_embed(embed)
                    webhook.execute()
                    #END WEBHOOK
                    cnt += 1
                    secs_to_wait = random.randint(MIN_SECS_SLEEP, MAX_SECS_SLEEP)
                    time.sleep(secs_to_wait)
                else:
                    print(f"LOG: {submission} is not a valid submission")
            except ValueError as err: #DEBUG
                #print("invalid post")
                #print(err)
                continue
            except: #DEBUG
                print("invalid post")
                continue
            secs_to_wait = random.randint(1, 2)
            time.sleep(secs_to_wait)
    #END POSTED MESSAGES
    pause = random.randint(MIN_BIG_SLEEP, MAX_BIG_SLEEP)
    pauseE = DiscordEmbed(title="[>] **Le bot fait une pause !**", description="Et oui il faut bien le refroidir :snowflake:  ", color="f1330a")
    pauseE.set_thumbnail(url="https://images-ext-2.discordapp.net/external/vDkk1QkR2I39SGV3_UL71Q-2EVvOG95weOjUdgEH5Uc/https/media.tenor.com/hxBBp7yis4sAAAPo/time-out-wait.mp4")
    pauseE.set_author(name="SohKey's Bot", url="https://github.com/SohKey", icon_url="https://29.recreatiloups.com/wp-content/uploads/sites/2/2018/06/robot-stage-enfant.png")
    pauseE.add_embed_field(name='Durée de la pause ', value=f'{pause} secondes !', inline=True)
    webhook.execute()
    
    bot_pause(pause)
start() #First launch