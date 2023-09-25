from selenium import webdriver
from selenium.webdriver.common.by import By
from extFuncs import parseLog


def getGrades(username, password):


   options = webdriver.EdgeOptions()
   options.add_argument('--headless')
   driver = webdriver.Edge(options=options)
   
   driver.get("https://focus.pcsb.org/focus/Modules.php?modname=misc/Portal.php")
   print('logging in')
   
   driver.find_element(by=By.ID, value="username-input").send_keys(username)
   driver.find_element(by=By.NAME, value="password").send_keys(password)
   driver.find_element(by=By.XPATH, value="/html/body/div/div[3]/div/div[1]/form/div[2]/div[2]/button").click()
   print('signing in...')
   
   
   while (True) :
      
      try :
         if "Permission denied" in driver.find_element(by=By.XPATH, value="/html/body/div/div[3]/div/div[1]/form/div[2]/div[1]/div[2]").text :
            print('Login wrong')
            return
      
      except :
         pass
      
      if len(driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div[2]/div")) > 0 :
         print("found grades")
         break
   


   rawGrades = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div").text
   rawGrades = str(rawGrades).split("\n")
   driver.close
   
   finalGrades = []
   
   for posGrade in rawGrades :
      indexLength = len(posGrade)
      
      if "ABC" in posGrade :
         finalGrades.append(posGrade)
      
      if indexLength != 0 and posGrade[indexLength -1] in ['A', 'B', 'C', 'D', 'F'] and indexLength <= 6 and "," not in posGrade :
         finalGrades.append(posGrade)
         
   return finalGrades
      









print('focus grade checker')
print()

username = input("Enter Username: ")
password = input("Enter Password: ")

grades = getGrades(username, password)

for grade in grades :
   print(grade)
   print()

print()