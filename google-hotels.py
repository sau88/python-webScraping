
import os

import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.action_chains import ActionChains


os.environ['PATH'] = "/usr/local/bin/firefox/" 


cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
google_hotels = "https://www.google.co.in/travel/hotels/London?ap=KigKEgli2gfAn7pJQBEAAJDgIX_HvxISCYNRH5NX1UlAEQAAwH14Z6A_MAJakwMKBQiAfRAAIgNJTlIqFgoHCOMPEAcYAxIHCOMPEAcYBBgBKACwAQBYAZoBCBIGTG9uZG9uogESCggvbS8wNGpwbBIGTG9uZG9uqgEqCgIIIRICCA8SAggIEgIIFRICCA0SAghnEgIIWxICCC8SAghaEgIIVBgBqgEPCgIIEhIDCJsBEgIIaBgBqgEOCgIIFBICCBsSAghSGAGqAQcKAwihAhgAqgESCgIIHBICCFESAghzEgIINhgBqgEKCgIIJRICCHoYAaoBIgoCCBESAggqEgIIQBICCDgSAghXEgIIAhICCH8SAggrGAGqASwKAgguEgIIPBICCDsSAggaEgIISBICCD0SAwiDARICCEsSAggMEgMIiQEYAaoBEQoDCK4BEgMIsAESAwiyARgBqgEHCgMIpwEYAKoBEQoDCKkBEgMIqgESAwisARgBqgEGCgIIYxgAqgEGCgIIRhgAqgEKCgIIUBICCE8YAaoBBwoDCMsBGACqAQYKAgg5GACqAQ4KAgg1EgIIExICCDIYAZIBAiAB&g2lb=2502548%2C4208993%2C4223281%2C4252074%2C4253230%2C4254308%2C4258168%2C4258962%2C4260007%2C4262509%2C4265959%2C4270442%2C4274032%2C4274649%2C4276661%2C4276914%2C4276917%2C4250437%2C4251519%2C4265427%2C4270859&hl=en&gl=in&un=1&q=hotels%20in%20london&rp=OAFAAEgC&ictx=1&ved=2ahUKEwj_wvCG_pXjAhVbVisKHahDA8AQjGp6BAgKEEg&hrf=CgUIgH0QACIDSU5SKhYKBwjjDxAHGAMSBwjjDxAHGAQYASgAsAEAWAGKASgKEgli2gfAn7pJQBEAAJDgIX_HvxISCYNRH5NX1UlAEQAAwH14Z6A_mgEIEgZMb25kb26iARIKCC9tLzA0anBsEgZMb25kb26qASYKAgghEgIICBICCBUSAggNEgIIZxICCFsSAggvEgIIWhICCFQYAaoBDwoCCBISAwibARICCGgYAaoBCgoCCBQSAggbGAGqAQcKAwihAhgAqgESCgIIHBICCFESAghzEgIINhgBqgEKCgIIJRICCHoYAaoBIgoCCBESAggqEgIIQBICCDgSAghXEgIIAhICCH8SAggrGAGqASgKAgguEgIIOxICCBoSAghIEgIIPRIDCIMBEgIISxICCAwSAwiJARgBqgERCgMIrgESAwiwARIDCLIBGAGqAQcKAwinARgAqgEMCgMIqQESAwisARgBqgEGCgIIYxgAqgEGCgIIRhgAqgEKCgIIUBICCE8YAaoBBwoDCMsBGACqAQYKAgg5GACqAQ4KAgg1EgIIExICCDIYAZIBAiAB&tcfs=EiwKCC9tLzA0anBsEgZMb25kb24aGAoKMjAxOS0wNy0wMxIKMjAxOS0wNy0wNFIA"
market_ft = "https://markets.ft.com/data/funds/tearsheet/charts?s=NL0006294175:EUR"

w3schools = "https://www.w3schools.com/howto/howto_js_dropdown.asp"
flipkart = "https://www.flipkart.com/mobiles/smartphones~type/pr?sid=tyy,4io"


google_arrival_class = 'tcAWyf WGMqof'
google_departure_class='eoY5cb MphfQd yJ5hSd'



class DatePickerDateRangeTest(unittest.TestCase):

    def setUp(self):
        #define a driver instance, for example Chrome
        
        self.driver = webdriver.Firefox(capabilities=cap, executable_path='/usr/local/bin/firefox/geckodriver')
        self.driver.maximize_window()
    
    def test_date_picker_date_range_(self):
        driver = self.driver
        driver.get(google_hotels)
         
        
        #_______________________FROM DATE_____________________________________
       
        # Click arrival button, wait until its pop up

        arrival = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/div[1]/div/div[2]/div[2]")
        arrival.click()
        time.sleep(2)

        # select month 
        for x in range(1):
            month = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/div[1]/div/div/div[3]/button")     
            #month = WebDriverWait(arrival, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ow41']/div[2]/div/div[2]/div[3]/div[1]/div/div/div[3]/button")) )
            month.click()
            time.sleep(1)
 

        # google allows upto one month date selection

        # select day 
        for x in range(3):
            day = driver.find_element_by_xpath("//*[@id='dwrFZd0']/div/div[1]/button[2]")     
            day.click()
            time.sleep(1)

        
        #________________________________TO DATE___________________________________________________
        
        # Swith to departure button

        departure = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='dwrFZd0']/div/div[2]")) )
        departure.click()
        time.sleep(2)
        
        
        # select day 

        for x in range(3):
            day = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/button[2]")) )
            day.click()
            time.sleep(2)
            
        # Submit

        submit = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[4]/div/button[2]") 
        submit.click()
        time.sleep(15)
        
   

    def tearDown(self): 
        time.sleep(3)
        self.driver.close()	
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()





