# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

istenilengun = 'Dec 28'

caps = {}
caps["platformName"] = "android"
caps["appium:platformVersion"] = "13"
caps["appium:appPackage"] = "com.grubhub.driver"
caps["appium:appActivity"] = "com.grubhub.driver.startup.SplashScreenActivity"
caps["appium:deviceName"] = "pixel_5_API_33"
caps["appium:udid"] = "emulator-5554"
caps["appium:enablePerformanceLogging"] = "true"
caps["appium:appWaitDuration"] = "30000"
caps["appium:automationName"] = "UiAutomator2"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element(by=AppiumBy.ID, value="com.grubhub.driver:id/log_in_button")
el1.click()
sleep(1)
el2 = driver.find_element(by=AppiumBy.ID, value="com.grubhub.driver:id/username")
el2.click()
sleep(1)
el2.send_keys("i.cengiz13@gmail.com")
el3 = driver.find_element(by=AppiumBy.ID, value="com.grubhub.driver:id/password")
el3.click()
sleep(1)
el3.send_keys("ismail8513")
el3.click()
el4 = driver.find_element(by=AppiumBy.ID, value="com.grubhub.driver:id/loginBtn")
el4.click()
sleep(2)
el5 = driver.find_element(by=AppiumBy.ID, value="com.grubhub.driver:id/actionBtn")
el5.click()
sleep(1)
el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Open navigation drawer")
el6.click()
sleep(1)
el7 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.view.ViewGroup[2]")
el7.click()
sleep(1)
el8 = driver.find_element(by=AppiumBy.ID, value="com.grubhub.driver:id/skip_button")
el8.click()
sleep(1)
el9 = driver.find_element(by=AppiumBy.ID, value="com.grubhub.driver:id/button")
el9.click()
sleep(1)
els1 = driver.find_elements(by=AppiumBy.XPATH, value="//*[@text= 'Update schedule']")
els1[0].click()
sleep(1)
els2 = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text, istenilengun)]")
els2[0].click()
sleep(1)
driver.quit()