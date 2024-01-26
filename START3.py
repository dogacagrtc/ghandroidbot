# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
while 3<4 :
    try:

        from fonksiyonlar import *
        from time import sleep
        from appium import webdriver
        from appium.webdriver.common.appiumby import AppiumBy
        from appium.webdriver.common.touch_action import TouchAction

        # For W3C actions
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.actions import interaction
        from selenium.webdriver.common.actions.action_builder import ActionBuilder
        from selenium.webdriver.common.actions.pointer_input import PointerInput

        a=0
        kaydirmadeger=0

        istenilengun = 'Dec 28'
        currentmonth = 'asdasd'
# EXAMPLE HOURS AND DAYS WANTED

        gun0 = 'Jan 3'
        gun1 = 'Jan 4'
        gun2 = 'Jan 5'
        gun3 = 'Jan 6'
        gun4 = 'Jan 7'
        gun5 = 'Jan 8'
        gun6 = 'Jan 3'

        is0= 0
        is1= 0
        is2= '3:30pm–5:00pm'
        is3= '5:00pm–7:00pm'
        is4= '5:00pm–7:30pm'
        is5= '5:00pm–8:00pm'
        is6= '8:00pm–11:00pm'
        is7= '8:30pm–11:30pm'
        is8= '9:00pm–10:30pm'
        is9= '9:00pm–11:30pm'
        is0=is1=is2=is3=is4=is5=is6=is7=is8=is9=0

        is1_0= '2:30pm–4:00pm'
        is1_1= '2:00pm–4:30pm'
        is1_2= '3:30pm–5:00pm'
        is1_3= '4:30pm–6:00pm'
        is1_4= 0
        is1_5= 0
        is1_6= '7:30pm–10:30pm'
        is1_7= '8:00pm–11:00pm'
        is1_8= '8:30pm–11:30pm'
        is1_9= '9:30pm–11:00pm'

        is2_0= '10:00pm–11:30pm'
        is2_1= '10:00pm–12:00am'
        is2_2= 0
        is2_3= 0
        is2_4= '11:00pm–12:30am'
        is2_5= '11:00pm–1:30am'
        is2_6= '11:00pm–2:00am'
        is2_7= 0 
        is2_8= 0 
        is2_9= 0

        is3_0= '2:30pm–4:00pm'
        is3_1= '3:00pm–4:30pm'
        is3_2= '8:00pm–11:00pm'
        is3_3= '9:30pm–11:00pm'
        is3_4= '10:00pm–11:30pm'
        is3_5= 0
        is3_6= 0
        is3_7= 0
        is3_8= 0
        is3_9= 0

        is4_0= '3:00pm–5:30pm'
        is4_1= '3:30pm–5:00pm'
        is4_2= '8:00pm–11:00pm'
        is4_3= '8:00pm–10:30pm'
        is4_4= 0
        is4_5= 0
        is4_6= 0
        is4_7= 0
        is4_8= 0
        is4_9= 0

        is5_0= '1:00pm–3:30pm'
        is5_1= '1:30pm–4:30pm'
        is5_2= '2:00pm–5:00pm'
        is5_3= '5:00pm–7:30pm'
        is5_4= '5:30pm–8:00pm'
        is5_5= 0
        is5_6= '8:30pm–11:00pm'
        is5_7= '8:30pm–10:00pm'
        is5_8= '9:00pm–11:30pm'
        is5_9= '9:30pm–11:00pm'

        is6_0= '1:30pm–3:00pm'
        is6_1= '22:00pm–4:30pm'
        is6_2= '3:30pm–5:00pm'
        is6_3= '4:30pm–6:00pm'
        is6_4= '5:00pm–7:30pm'
        is6_5= '5:30pm–8:00pm'
        is6_6= '8:00pm–11:00pm'
        is6_7= '8:30pm–10:00pm'
        is6_8= '9:00pm–11:30pm'
        is6_9= '9:30pm–11:00pm'

        gunler = [gun2]


        istenilensaatler_0 = [is0, is1,is2,is3,is4,is5,is6,is7,is8,is9]
        istenilensaatler_1 = [is1_0, is1_1,is1_2,is1_3,is1_4,is1_5,is1_6,is1_7,is1_8,is1_9]
        istenilensaatler_2 = [is2_0, is2_1,is2_2,is2_3,is2_4,is2_5,is2_6,is2_7,is2_8,is2_9]
        istenilensaatler_3 = [is3_0, is3_1,is3_2,is3_3,is3_4,is3_5,is3_6,is3_7,is3_8,is3_9]
        istenilensaatler_4 = [is4_0, is4_1,is4_2,is4_3,is4_4,is4_5,is4_6,is4_7,is4_8,is4_9]
        istenilensaatler_5 = [is5_0, is5_1,is5_2,is5_3,is5_4,is5_5,is5_6,is5_7,is5_8,is5_9]
        istenilensaatler_6 = [is6_0, is6_1,is6_2,is6_3,is6_4,is6_5,is6_6,is6_7,is6_8,is6_9]





        istenilensaatler_ = [ istenilensaatler_2 ]




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


        appopenlogin1()
        sleep(5)
        scheduleagidis2()

        els1 = driver.find_elements(by=AppiumBy.XPATH, value="//*[@text= 'Update schedule']")
        els1[0].click()
        sleep(0.5)
        denemesayisi=0
        print('noldu şimdi')
        gundegeri=0
        ilkgunvarmi = 1
        while 1<2:
            while gundegeri!=len(gunler):


                guntarihi = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text, '"+str(gunler[gundegeri]) +"')]")
                while len(guntarihi) == 0:
                    driver.swipe(150, 800, 150, 200, 200)
                    sleep(0.5)
                    guntarihi = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text, '"+str(gunler[gundegeri]) +"')]")
                    print('looking for the specific day')
                print('looking for the specific day')
                print(gunler[gundegeri])

                
                while a!=len(istenilensaatler_[gundegeri]) : 
                

                    if istenilensaatler_[gundegeri][a] != 0:

                        istenilensaatblock=driver.find_elements(by=AppiumBy.XPATH, value="//*[@text= '"+str(istenilensaatler_[gundegeri][a]) +"']")
                        while len(istenilensaatblock) == 0 :
                            driver.swipe(150, 800, 150, 200, 200)
                            kaydirmadeger+=1
                            istenilensaatblock=driver.find_elements(by=AppiumBy.XPATH, value="//*[@text= '"+str(istenilensaatler_[gundegeri][a]) +"']")
                            if kaydirmadeger>24:
                                break
                        if kaydirmadeger<24:
                            kaydirmadeger=0
                            istenilensaatblock[0].click()
                            sleep(0.2)
                            nevermind=driver.find_elements(by=AppiumBy.XPATH, value="//*[@text= 'Nevermind']")

                            if len(nevermind)==1:
                                nevermind[0].click()
                                print(str(istenilensaatler_[gundegeri][a])+'this block is/was added')
                                istenilensaatler_[gundegeri][a] = 0
                            print(a)
                        else :
                            kaydirmadeger=0
                            print(str(istenilensaatler_[gundegeri][a])+'this block is not true')
                            #istenilensaatler_[gundegeri][a] = 0
                            done = driver.find_elements(by=AppiumBy.XPATH, value="//*[@text= 'Done updating']")
                            done[0].click()
                            sleep(2)
                            els1 = driver.find_elements(by=AppiumBy.XPATH, value="//*[@text= 'Update schedule']")
                            els1[0].click()
                            guntarihi = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text, '"+str(gunler[gundegeri]) +"')]")
                            while len(guntarihi) != 1:
                                driver.swipe(150, 800, 150, 200, 200)
                                guntarihi = driver.find_elements(by=AppiumBy.XPATH, value="//*[contains(@text, '"+str(gunler[gundegeri]) +"')]")
                                print('looking for the specific day')
                            print('specific day found')
                            print(gunler[gundegeri])
                    else :
                        print(f' {a}. saat off')
                    a+=1




                gundegeri+=1
                a=0
            gundegeri=0
            sleep(2)
            done2 = driver.find_elements(by=AppiumBy.XPATH, value="//*[@text= 'Done updating']")
            done2[0].click()
            sleep(2)
            el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Open navigation drawer")
            el6.click()
            sleep(0.5)
            el6.click()
            els1 = driver.find_elements(by=AppiumBy.XPATH, value="//*[@text= 'Update schedule']")
            els1[0].click()
            denemesayisi+=1
            print(str(denemesayisi)+'. Deneme')
    except:
        pass