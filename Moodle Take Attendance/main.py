from selenium import webdriver #import lib
from time import sleep #import lib
from secrets import username, password #import username and password
ImplicitlyWait = 30

def MoodleWebDriveStart():
	try:
		firefox_profile = webdriver.FirefoxProfile() #Tell the program to use FireFox Driver
		firefox_profile.set_preference("browser.privatebrowsing.autostart", False) #Start FireFox
		print("Program Run")
		driver = webdriver.Firefox(firefox_profile=firefox_profile)#Tell the program to use FireFox Driver
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
		try:
			driver.find_element_by_link_text("Submit attendance").click()
			driver.implicitly_wait(ImplicitlyWait)
			driver.find_element_by_name("status").click()
			driver.implicitly_wait(ImplicitlyWait)
			driver.find_element_by_name("submitbutton").click()
			print("Attendance Took!")
		except:
			print("Error 404: Link Not found!")	
			print("")
	finally:
		driver.quit()

MoodleWebDriveStart()		