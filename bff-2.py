# coding:utf-8
import os, sys, time
oh = []

ngen = ("""

HAYO MAU NGAPAIN TOD?

""")


try:
    import requests
except ImportError:
    os.system('''
pip2 install requests ''' + sys.argv[0])


try:
    import bs4
except ImportError:
    os.system('''
pip2 install bs4 ''' + sys.argv[0])


except IOError:
    for x in range(999999999):
        oh.append(sys.argv[0])
    sys.exit()
    

try:
    r = requests.get('https://raw.githubusercontent.com/warba29/server/main/bff.py').text
    if "bff.py" in r:
    	os.system("python2 bff.py")
    
except requests.exceptions.ConnectionError:
    sys.exit('\n\x1b[1;91m• Tidak ada koneksi!')


exit()
