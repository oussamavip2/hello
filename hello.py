import requests,instaloader,os,re
from user_agent import generate_user_agent

A = "\033[1;91m" #red
B = "\033[1;90m" #black
C = "\033[1;97m" #white
E = "\033[1;92m" #green
H = "\033[1;93m" #yellow
K = "\033[1;94m" #violate
Z = "\033[1;95m" #purple
M = "\033[1;96m" #cyan

baner = f"""{A}                                                                   
@@@  @@@  @@@   @@@@@@   @@@@@@@   @@@@@@      @@@  @@@  @@@@@@@   
@@@  @@@@ @@@  @@@@@@@   @@@@@@@  @@@@@@@@     @@@  @@@  @@@@@@@@  
@@!  @@!@!@@@  !@@         @@!    @@!  @@@     @@!  @@@  @@!  @@@  
!@!  !@!!@!@!  !@!         !@!    !@!  @!@     !@!  @!@  !@!  @!@  
!!@  @!@ !!@!  !!@@!!      @!!    @!@!@!@!     @!@  !@!  @!@@!@!   
!!!  !@!  !!!   !!@!!!     !!!    !!!@!!!!     !@!  !!!  !!@!!!    
!!:  !!:  !!!       !:!    !!:    !!:  !!!     !!:  !!!  !!:       
:!:  :!:  !:!      !:!     :!:    :!:  !:!     :!:  !:!  :!:       
 ::   ::   ::  :::: ::      ::    ::   :::     ::::: ::   ::       
:    ::    :   :: : :       :      :   : :      : :  :    :        
                                                                   
                                                                      {E}V-5"""

def followers():
	os.system("clear")
	print(baner)
	print(f"{H}========================================\n   {Z}CREATOR OF THE TOOL : {M}time.sleep(∞)\n   {Z}TELEGRAM : {M}@lprlp & @f898f\n   {Z}CHANNEL : {M}@ff898ff{H}\n========================================\n")
	L = instaloader.Instaloader()
	username=input(E+"("+C+"⌯"+E+") "+C+" FAKE USERNAME TO LOGIN "+A+" : "+E)
	password=input(E+"("+C+"⌯"+E+") "+C+" PASSWORD TO LOGIN "+A+" : "+E)
	getuser=input(E+"("+C+"⌯"+E+") "+C+" USERNAME TO GET HIS FOLLOWERS "+A+" : "+E)
	print(E+"PLEASE WAIT.....")
	os.system('rm -rf done.txt')
	L.login(username,password)
	profile = instaloader.Profile.from_username(L.context, getuser)
	follow_list = []
	count=0
	ok=0
	for followee in profile.get_followers():
		user=str(followee)
		idd=user.split('(')[1]
		id=idd.split(')')[0]
		follow_list.append(id)
		file = open("done.txt","a")
		file.write(follow_list[count])
		file.write("\n")
		file.close()
		ok+=1
		print(E+"["+C+f" {ok} "+E+"] "+str(id))
		count=count+1

def following():
	os.system("clear")
	print(baner)
	print(f"{H}========================================\n   {Z}CREATOR OF THE TOOL : {M}time.sleep(∞)\n   {Z}TELEGRAM : {M}@lprlp & @f898f\n   {Z}CHANNEL : {M}@ff898ff{H}\n========================================\n")
	L = instaloader.Instaloader()
	username=input(E+"("+C+"⌯"+E+") "+C+" FAKE USERNAME TO LOGIN "+A+" : "+E)
	password=input(E+"("+C+"⌯"+E+") "+C+" PASSWORD TO LOGIN "+A+" : "+E)
	getuser=input(E+"("+C+"⌯"+E+") "+C+" USERNAME TO GET HIS FOLLOWING "+A+" : "+E)
	print(E+"PLEASE WAIT.....")
	os.system('rm -rf done.txt')
	L.login(username,password)
	profile = instaloader.Profile.from_username(L.context, getuser)
	follow_list = []
	count=0
	ok=0
	for followee in profile.get_followees():
		user=str(followee)
		idd=user.split('(')[1]
		id=idd.split(')')[0]
		follow_list.append(id)
		file = open("done.txt","a")
		file.write(follow_list[count])
		file.write("\n")
		file.close()
		ok+=1
		print(E+"["+C+f" {ok} "+E+"] "+str(id))
		count=count+1

def search():
	os.system("clear")
	print(baner)
	print(f"{H}========================================\n   {Z}CREATOR OF THE TOOL : {M}time.sleep(∞)\n   {Z}TELEGRAM : {M}@lprlp & @f898f\n   {Z}CHANNEL : {M}@ff898ff{H}\n========================================\n")
	file = "done.txt"
	sessionid = input(E+"("+C+"⌯"+E+") "+C+" Sessionid  "+A+" : "+E)
	username = input(E+"("+C+"⌯"+E+") "+C+" Word Search  "+A+" : "+E)
	os.system('rm -rf done.txt')
	print (50 * '\033[1;97m~')
	print (E)
	print  (E + "[~] USERNAME  ...\t " + A+str(username)) 
	ok = 0
	users = []
	userx = []
	use = ['.','_','fira','fans','love','singer','2020','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','__','___','____','_____','______','1','2','3','4','5','6','7','8','9','10','..','hot','sexy','news','new','music','song','old','new','forever','q','w','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','11','12','13','14','15','16','17','18','19','20']

	cookies = {"sessionid": sessionid}
	headers={
    "Host": "www.instagram.com",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "Android",
    "upgrade-insecure-requests": "1",
    "origin": "https://www.instagram.com",
    "user-agent": str(generate_user_agent()),
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "same-origin","sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1","sec-fetch-dest": "document",
    "referer": "https://www.instagram.com/",
    "accept-language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "ContentType" : "application/x-www-form-urlencoded",
    "X-Requested-With" : "XMLHttpRequest",
    "X-IG-App-ID": "936619743392459",
    "X-Instagram-AJAX" : "missing",
    "X-CSRFToken" : "missing"}
	response = requests.get("https://www.instagram.com/web/search/topsearch/?context=blended&query="+str(username)+"&rank_token=0.43773004634682566&include_reel=true",headers=headers, cookies=cookies)
	asx = re.compile(r'"pk":"(.*?)"')
	asn = asx.findall(response.text)
	for node in asn:
		ok+=1
		print (E+"["+C+str(ok)+E+"] " + E + str(node))
	for tag in use :
		response = requests.get("https://www.instagram.com/web/search/topsearch/?context=blended&query="+str(username)+str(tag)+"&rank_token=0.43773004634682566&include_reel=true",headers=headers, cookies=cookies)
		asx = re.compile(r'"pk":"(.*?)"')
		asn = asx.findall(response.text)
		for node in asn:
			ok+=1
			print (E+"["+C+str(ok)+E+"] " + E + str(node))
			users.append(node)
				
	for user in users :
		if user not in userx :
			userx.append(user)
			
	print (E)
	tm = (len(userx))
	print (len(users))
	print (H)
	print (len(userx))
	print (E)
	filename = ("done.txt").strip()
	with open (filename,'a+') as file :
		for uesx in userx:
			file.write(str(uesx)+'\n')
			
			
	print (E+"  > Done Save  >  : "+H+str(filename))



def instaup():
	os.system("clear")
	print(baner)
	print(f"{H}========================================\n   {Z}CREATOR OF THE TOOL : {M}time.sleep(∞)\n   {Z}TELEGRAM : {M}@lprlp & @f898f\n   {Z}CHANNEL : {M}@ff898ff{H}\n========================================\n")
	combo = input(E+"("+C+"⌯"+E+") "+C+" FILE NAME "+A+" : "+E)
	user = input(E+"("+C+"⌯"+E+") "+C+" USERNAME TO SEND FOLLOWERS "+A+" : "+E)
	
	L = instaloader.Instaloader()
	profile = str(instaloader.Profile.from_username(L.context,user))
	idd=str(profile.split(')>')[0])
	target=idd.split(' (')[1]

	fi = open(combo,"r")
	ok=0
	while True:
		fil = fi.readline().split('\n')[0]
		curl = f"https://v1-check-up.herokuapp.com/?oid={fil}&submit=submit"
		ct= requests.get(curl).text
		try:
			c1 = ct.split('Message:-{"coins":"')[1]
			c2 = (c1.split('"}')[0])
		
			
			if int(c2) < 800:
					ok+=1
					print(f"{E}[{C}{ok}{E}]{A}[❌] THE ID DONT HAVE ENOUGH COINS\n   ID ==> {H}{fil}\n   {A}COINS ==> {H}{c2}\n")
		
			elif int(c2) > 800 and int(c2) < 1200:
				ourl200 = f"https://v2-order-instaup.herokuapp.com/?target={fil}&userid={target}&order=200&submit=submit"
				ot200 = requests.get(ourl200).text
				o1200 = ot200.split('"message":"')[1]
				o2200 = (o1200.split('","return"')[0])
			
				ok+=1
				if ('Sucess!') in o2200:
					print(f"{E}[{C}{ok}{E}]{E}[✅] DONE SENT 200 FOLLOWERS TO ==> {H}{user}\n{E}   ID ==> {H}{fil}\n   {E}COINS BEFOR ORDER ==> {H}{c2}")
					ct1= requests.get(curl).text
					c11 = ct1.split('Message:-{"coins":"')[1]
					c21 = (c11.split('"}')[0])
					print(f"{E}   COINS AFTER ORDER ==> {H}{c21}\n")
				else:
					print(f"{E}[{C}{ok}{E}]{A}[❌] {o2200}\n   ID ==> {H}{fil}\n   {A}COINS ==> {H}{c2}\n")
		
			elif int(c2) > 1200 and int(c2) < 1600:
				ourl300 = f"https://v2-order-instaup.herokuapp.com/?target={fil}&userid={target}&order=300&submit=submit"
				ot300 = requests.get(ourl300).text
				o1300 = ot300.split('"message":"')[1]
				o2300 = (o1300.split('","return"')[0])
			
				ok+=1
				if ('Sucess!') in o2300:
					print(f"{E}[{C}{ok}{E}]{E}[✅] DONE SENT 300 FOLLOWERS TO ==> {H}{user}\n{E}   ID ==> {H}{fil}\n   {E}COINS BEFOR ORDER ==> {H}{c2}")
					ct1= requests.get(curl).text
					c11 = ct1.split('Message:-{"coins":"')[1]
					c21 = (c11.split('"}')[0])
					print(f"{E}   COINS AFTER ORDER ==> {H}{c21}\n")
				else:
					print(f"{E}[{C}{ok}{E}]{A}[❌] {o2300}\n   ID ==> {H}{fil}\n   {A}COINS ==> {H}{c2}\n")
		
			elif int(c2) > 1600 and int(c2) < 2000:
				ourl400 = f"https://v2-order-instaup.herokuapp.com/?target={fil}&userid={target}&order=400&submit=submit"
				ot400 = requests.get(ourl400).text
				o1400 = ot400.split('"message":"')[1]
				o2400 = (o1400.split('","return"')[0])
			
				ok+=1
				if ('Sucess!') in o2400:
					print(f"{E}[{C}{ok}{E}]{E}[✅] DONE SENT 400 FOLLOWERS TO ==> {H}{user}\n{E}   ID ==> {H}{fil}\n   {E}COINS BEFOR ORDER ==> {H}{c2}")
					ct1= requests.get(curl).text
					c11 = ct1.split('Message:-{"coins":"')[1]
					c21 = (c11.split('"}')[0])
					print(f"{E}   COINS AFTER ORDER ==> {H}{c21}\n")
				else:
					print(f"{E}[{C}{ok}{E}]{A}[❌] {o2400}\n   ID ==> {H}{fil}\n   {A}COINS ==> {H}{c2}\n")
		
			elif int(c2) > 2000 and int(c2) < 2400:
				ourl500 = f"https://v2-order-instaup.herokuapp.com/?target={fil}&userid={target}&order=500&submit=submit"
				ot500 = requests.get(ourl500).text
				o1500 = ot500.split('"message":"')[1]
				o2500 = (o1500.split('","return"')[0])
		
				ok+=1
				if ('Sucess!') in o2500:
					print(f"{E}[{C}{ok}{E}]{E}[✅] DONE SENT 500 FOLLOWERS TO ==> {H}{user}\n{E}   ID ==> {H}{fil}\n   {E}COINS BEFOR ORDER ==> {H}{c2}")
					ct1= requests.get(curl).text
					c11 = ct1.split('Message:-{"coins":"')[1]
					c21 = (c11.split('"}')[0])
					print(f"{E}   COINS AFTER ORDER ==> {H}{c21}\n")
				else:
					print(f"{E}[{C}{ok}{E}]{A}[❌] {o2500}\n   ID ==> {H}{fil}\n   {A}COINS ==> {H}{c2}\n")
		
			elif int(c2) > 2400 and int(c2) < 2800:
				ourl600 = f"https://v2-order-instaup.herokuapp.com/?target={fil}&userid={target}&order=600&submit=submit"
				ot600 = requests.get(ourl600).text
				o1600 = ot600.split('"message":"')[1]
				o2600 = (o1600.split('","return"')[0])
			
				ok+=1
				if ('Sucess!') in o2600:
					print(f"{E}[{C}{ok}{E}]{E}[✅] DONE SENT 600 FOLLOWERS TO ==> {H}{user}\n{E}   ID ==> {H}{fil}\n   {E}COINS BEFOR ORDER ==> {H}{c2}")
					ct1= requests.get(curl).text
					c11 = ct1.split('Message:-{"coins":"')[1]
					c21 = (c11.split('"}')[0])
					print(f"{E}   COINS AFTER ORDER ==> {H}{c21}\n")
				else:
					print(f"{E}[{C}{ok}{E}]{A}[❌] {o2600}\n   ID ==> {H}{fil}\n   {A}COINS ==> {H}{c2}\n")
		
			elif int(c2) > 2800 and int(c2) < 3200:
				ourl700 = f"https://v2-order-instaup.herokuapp.com/?target={fil}&userid={target}&order=700&submit=submit"
				ot700 = requests.get(ourl700).text
				o1700 = ot700.split('"message":"')[1]
				o2700 = (o1700.split('","return"')[0])
			
				ok+=1
				if ('Sucess!') in o2700:
					print(f"{E}[{C}{ok}{E}]{E}[✅] DONE SENT 700 FOLLOWERS TO ==> {H}{user}\n{E}   ID ==> {H}{fil}\n   {E}COINS BEFOR ORDER ==> {H}{c2}")
					ct1= requests.get(curl).text
					c11 = ct1.split('Message:-{"coins":"')[1]
					c21 = (c11.split('"}')[0])
					print(f"{E}   COINS AFTER ORDER ==> {H}{c21}\n")
				else:
					print(f"{E}[{C}{ok}{E}]{A}[❌] {o2700}\n   ID ==> {H}{fil}\n   {A}COINS ==> {H}{c2}\n")
		
			elif int(c2) > 3200 and int(c2) < 3600:
				ourl800 = f"https://v2-order-instaup.herokuapp.com/?target={fil}&userid={target}&order=800&submit=submit"
				ot800 = requests.get(ourl800).text
				o1800 = ot800.split('"message":"')[1]
				o2800 = (o1800.split('","return"')[0])
			
				ok+=1
				if ('Sucess!') in o2800:
					print(f"{E}[{C}{ok}{E}]{E}[✅] DONE SENT 800 FOLLOWERS TO ==> {H}{user}\n{E}   ID ==> {H}{fil}\n   {E}COINS BEFOR ORDER ==> {H}{c2}")
					ct1= requests.get(curl).text
					c11 = ct1.split('Message:-{"coins":"')[1]
					c21 = (c11.split('"}')[0])
					print(f"{E}   COINS AFTER ORDER ==> {H}{c21}\n")
				else:
					print(f"{E}[{C}{ok}{E}]{A}[❌] {o2800}\n   ID ==> {H}{fil}\n   {A}COINS ==> {H}{c2}\n")
		
			elif int(c2) > 3600 and int(c2) < 4000:
				ourl900 = f"https://v2-order-instaup.herokuapp.com/?target={fil}&userid={target}&order=900&submit=submit"
				ot900 = requests.get(ourl900).text
				o1900 = ot900.split('"message":"')[1]
				o2900 = (o1900.split('","return"')[0])
			
				ok+=1
				if ('Sucess!') in o2900:
					print(f"{E}[{C}{ok}{E}]{E}[✅] DONE SENT 900 FOLLOWERS TO ==> {H}{user}\n{E}   ID ==> {H}{fil}\n   {E}COINS BEFOR ORDER ==> {H}{c2}")
					ct1= requests.get(curl).text
					c11 = ct1.split('Message:-{"coins":"')[1]
					c21 = (c11.split('"}')[0])
					print(f"{E}   COINS AFTER ORDER ==> {H}{c21}\n")
				else:
					print(f"{E}[{C}{ok}{E}]{A}[❌] {o2900}\n   ID ==> {H}{fil}\n   {A}COINS ==> {H}{c2}\n")
		
			elif int(c2) > 4000:
				ourl1000 = f"https://v2-order-instaup.herokuapp.com/?target={fil}&userid={target}&order=1000&submit=submit"
				ot1000 = requests.get(ourl1000).text
				o11000 = ot1000.split('"message":"')[1]
				o21000 = (o11000.split('","return"')[0])
			
				ok+=1
				if ('Sucess!') in o21000:
					print(f"{E}[{C}{ok}{E}]{E}[✅] DONE SENT 1000 FOLLOWERS TO ==> {H}{user}\n{E}   ID ==> {H}{fil}\n   {E}COINS BEFOR ORDER ==> {H}{c2}")
					ct1= requests.get(curl).text
					c11 = ct1.split('Message:-{"coins":"')[1]
					c21 = (c11.split('"}')[0])
					print(f"{E}   COINS AFTER ORDER ==> {H}{c21}\n")
				else:
					print(f"{E}[{C}{ok}{E}]{A}[❌] {o21000}\n   ID ==> {H}{fil}\n   {A}COINS ==> {H}{c2}\n")
		
		except IndexError:
			ok+=1
			print(f"{E}[{C}{ok}{E}]{A}[❌] THE ACCOUNT IS BANNED\n   ID ==> {H}false\n")
		
		
		
		
			
def follow():
	os.system("clear")
	print(baner)
	print(f"{H}========================================\n   {Z}CREATOR OF THE TOOL : {M}time.sleep(∞)\n   {Z}TELEGRAM : {M}@lprlp & @f898f\n   {Z}CHANNEL : {M}@ff898ff{H}\n========================================\n")
	print(E+"("+C+"1"+E+") "+C+" GET IDS FROM FOLLOWERS ")
	print(E+"("+C+"2"+E+") "+C+" GET IDS FROM FOLLOWING ")
	print(E+"("+C+"3"+E+") "+C+" GET IDS FROM SEARCH ")
	print(A+" ---------------------------")
	fol = input(E+"("+C+"⌯"+E+") "+C+" ENTER YOUR CHOISE "+A+" : "+E)
	
	if fol == '1':
		followers()
	elif fol == '2':
		following()
	elif fol =='3':
		search()
	
	
def home():
	os.system("clear")
	print(baner)
	print(f"{H}========================================\n   {Z}CREATOR OF THE TOOL : {M}time.sleep(∞)\n   {Z}TELEGRAM : {M}@lprlp & @f898f\n   {Z}CHANNEL : {M}@ff898ff{H}\n========================================\n")
	print(E+"("+C+"1"+E+") "+C+" GET ID LIST ")
	print(E+"("+C+"2"+E+") "+C+" START INSTAUP ")
	print(A+" ---------------------------")
	tools = input(E+"("+C+"⌯"+E+") "+C+" ENTER YOUR CHOISE "+A+" : "+E)

	if tools == '1':
		follow()
	elif tools == '2':
		instaup()
	
home()
