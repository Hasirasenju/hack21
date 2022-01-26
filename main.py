import os, time, sys
import colorama as C
from colorama import Fore as F

DEFAULT = F.LIGHTWHITE_EX

green = '\033[1;32m'
red ='\33[31;1m'
white = '\33[37;1m'
blue = '\33[36;1m'
yellow = '\33[1;33m'
red2 = '\33[6;31m'

def slowprint(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./50)
		
def __list(k):
	__list__ = {
		"1":"Detect Scatter Get Of Olympus", 
		"2":"Detect Keluaran Aztech", 
		"3":"Detect Sweet Bonanza/Xmas", 
		"4":"Bocoran Jam", 
		"5":"RTP Game", 
		"6":"Auto Scatter (Berbahaya)"
	}
	return __list__[k]
def Menus():
	print("\n")
	print("[01]. " + __list("1"))
	print("[02]. " + __list("2"))
	print("[03]. " + __list("3"))
	print("[04]. " + __list("4"))
	print("[05]. " + __list("5"))
	print("[06]. " + F.RED + __list("6") + DEFAULT)
	print()

def Banner(whereAt):
	whereAt = whereAt.title()
	print(C.Back.CYAN, (f"CLI Version of Hawkeye v.0.4 {whereAt}"))
	print(C.Style.RESET_ALL)
	slowprint("""\33[37;1mWelcome to Hawkeye ® (Open Slot Enchanting Software)\nCopyright ©️ 2021 Copyright Holder.""")
	
def banner(whereAt):
	os.system("clear")
	whereAt = whereAt.title()
	print(C.Back.CYAN, (f"CLI Version of Hawkeye v.0.4 {whereAt}"))
	print(C.Style.RESET_ALL)
	
	print(F.GREEN)
	print(
		F.GREEN +
		"[INFO]\n" +
		F.RED +
		"-> " +
		DEFAULT +
		"Sebelum Menjalankan Script-nya\n" +
		"-> Silahkan baca info dan kebijakan Script\n" +
		F.RED +
		"\n" + F.GREEN + "[Silahkan Deposit Ke]\n" +
		DEFAULT +
		"-> BCA: 4220146478\n" +
		"-> Atas nama: Sri Haryani"  +
		DEFAULT
	)
	
if __name__=="__main__":
	Banner("Main Menu")
	Menus()
	menu = input("Pilih menu: -> ")
	if "1" in menu:
		banner(__list("1"))
	if "2" in menu:
		banner(__list("2"))
	if "3" in menu:
		banner(__list("3"))
	if "4" in menu:
		banner(__list("4"))
	if "5" in menu:
		banner(__list("5"))
	if "6" in menu:
		banner(__list("6"))