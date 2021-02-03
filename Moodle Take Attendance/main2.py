from selenium import webdriver #import lib
from time import sleep #import lib
from secrets import username, password, key, evt #import username and password
from datetime import datetime
ImplicitlyWait = 20
WeekdayNum = 3
CurrentHour = 0 #UTC Time
CurrentMin = 0
import requests as req
from urllib import parse


def MoodleWebDriveStart():
	try:
		firefox_profile = webdriver.FirefoxProfile() #Tell the program to use FireFox Driver
		firefox_profile.set_preference("browser.privatebrowsing.autostart", False) #Start FireFox
		driver = webdriver.Firefox(firefox_profile=firefox_profile)
		
		#print("Program Run")
		driver.get("https://moodle.cpce-polyu.edu.hk/my/") #Go to Moodle
		driver.implicitly_wait(ImplicitlyWait)
		driver.find_element_by_name("ctl00$ContentPlaceHolder1$UsernameTextBox").send_keys(username);#Type in username
		driver.find_element_by_name("ctl00$ContentPlaceHolder1$PasswordTextBox").send_keys(password);#Type in password
		driver.find_element_by_name("ctl00$ContentPlaceHolder1$SubmitButton").click()
		print("Logined In!")
		print("")
		driver.implicitly_wait(ImplicitlyWait)
		driver.find_element_by_link_text("Dashboard").click()
		driver.implicitly_wait(ImplicitlyWait)
		b = driver.find_element_by_partial_link_text("Attendance").click()
		driver.implicitly_wait(ImplicitlyWait)
		driver.find_element_by_link_text("Go to activity").click()
		driver.implicitly_wait(ImplicitlyWait)
		WebTitle = driver.title
		CourseName = WebTitle[:8]
		val1 = CourseName  # IFTTT value1參數值
		try:
			driver.find_element_by_link_text("Submit attendance").click()
			driver.implicitly_wait(ImplicitlyWait)
			driver.find_element_by_name("status").click()
			driver.implicitly_wait(ImplicitlyWait)
			driver.find_element_by_name("submitbutton").click()
			#print("Attendance Took!")
			val3 = '🟢 '
			val2 = 'Successfully! 💩 🟢'
		except:
			print("Error 404: Link Not found!")	
			print("")
			val2 = 'Unsuccessfully! 🔴'
			val3 = '🔴 '
	finally:
		driver.quit()
		url = (f'https://maker.ifttt.com/trigger/{evt}' + f'/with/key/{key}?value1={val1}&value2={val2}&value3={val3}')
		r = req.get(url)  # 執行IFTTT平台的webhooks
		val3 = ''
def Mon():
	if CurrentHour == 9 : #Hour Here
		if CurrentMin == 40: #Minute Here
 			MoodleWebDriveStart()

	if CurrentHour == 15 : #Hour Here
		if CurrentMin == 40: #Minute Here
 			MoodleWebDriveStart()

def Tue():	
	# If your course is 0830, then fill 
	if CurrentHour == 8 : #Hour Here
		if CurrentMin == 40: #Minute Here
 			MoodleWebDriveStart()

 	# If your course is 1430, then fill 
	if CurrentHour == 23 : #Hour Here
		if CurrentMin == 51: #Minute Here
 			MoodleWebDriveStart()		

def Wed():
	if CurrentHour == 8 : #Hour Here
		if CurrentMin == 40: #Minute Here
 			MoodleWebDriveStart()
	if CurrentHour == 12 : #Hour Here
		if CurrentMin == 40: #Minute Here
 			MoodleWebDriveStart()
	if CurrentHour == 16 : #Hour Here
		if CurrentMin == 40: #Minute Here
 			MoodleWebDriveStart()
def Thu():
	if CurrentHour == 9 : #Hour Here
		if CurrentMin == 40: #Minute Here
 			MoodleWebDriveStart()
def Fri():
	if CurrentHour == 10 : #Hour Here
		if CurrentMin == 40: #Minute Here
 			MoodleWebDriveStart()
	if CurrentHour == 16 : #Hour Here
		if CurrentMin == 40: #Minute Here
 			MoodleWebDriveStart()

def TimeConvert():
	pass

def DateOfWeekCheck():
	global WeekdayNum
	global CurrentHour
	global CurrentMin
	WeekdayNum = datetime.today().isoweekday()
	CurrentHour = datetime.today().hour
	CurrentMin = datetime.today().minute
	TimeConvert()
	if WeekdayNum == 1:
		Mon()
	elif WeekdayNum == 2:
		Tue()
	elif WeekdayNum == 3:	
		Wed()
	elif WeekdayNum == 4:
		Thu()
	elif WeekdayNum == 5:	
		Fri()	

def SerialPrint():
	print("WeekdayNum :", WeekdayNum)
	print("CurrentHour :", CurrentHour)
	print("CurrentMin :", CurrentMin)

#Main
while(1):
	DateOfWeekCheck()
	#SerialPrint()
	sleep(1)