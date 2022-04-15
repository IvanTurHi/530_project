import requests
#
#path = '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[3]/div[1]/div[3]/a'
#
#re = requests.get('https://pulkovoairport.ru/passengers/departure/?when=0')
#re =requests.get('https://pulkovoairport.ru/api/?type=departure&when=0&_=1643051394110')
#sssssssssssssss ='https://pulkovoairport.ru/api/?type=departure&when=0&_=1643052596840'
#sssssssssssssss ='https://pulkovoairport.ru/api/?type=departure&when=0&_=1643052661576'
#sssssssssssssss ='https://pulkovoairport.ru/api/?type=departure&when=0&_=1643053239743'
#sssssssssssssss ='https://pulkovoairport.ru/api/?type=departure&when=0&_=1643057673233'
#sssssssssssssss ='https://pulkovoairport.ru/api/?type=departure&when=0&_=1643057953306'
#the_second = 'https://pulkovoairport.ru/api/?type=arrival&when=0&_=1643106690490'
#the_first ='https://pulkovoairport.ru/api/?type=departure&when=0&_=1643058015961'
#re = requests.get(the_second)
#
##
#k = re.json()
#for i in k[0]:
#    print(i, k[0][i])

#for i in range(len(k)):
#    print(k[i]['OD_STD'][11:16], k[i]['OD_FLIGHT_NUMBER'], k[i]['OD_STATUS_RU'])

#for i in k[140]:
#    print(i, k[140][i])


import time

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#
#
#
#driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
#
#driver.get('https://krr.aero/flights/online-schedule/');
#
##time.sleep(2) # Let the user actually see something!
#
#css_selector_flight = 'div.board__td.board__td--bold.board__td--flight-number > a'
#
#search_box_flight = driver.find_elements(By.CSS_SELECTOR, css_selector_flight)
##print(search_box_flight)
##for i in search_box_flight:
##    print(i.get_attribute('text'))
#
##search_box = driver.find_element_by_name('q')
##
##search_box.send_keys('ChromeDriver')
##
##search_box.submit()
##
#
#
##time.sleep(5) # Let the user actually see something!
#
#
##css_selector_time = 'div.board__row-basic > div.board__td.board__td--time.board__td--bold'
##search_box_time = driver.find_elements(By.CSS_SELECTOR, css_selector_time)
##print(search_box_time)
##for i in search_box_time:
##    #print(i.get_attribute('text'))
##    d = i.find_elements(By.TAG_NAME, 'span')
##    for j in d:
##        print(j.get_attribute('text'))
#
#
#selector = 'body > div.wrap > div.main > div.schedule.d-none > div.schedule__tabs-wrapper > div.schedule__tab-content.schedule__tab-content--active > div > div > div > div > div'
#search_box = driver.find_elements(By.CSS_SELECTOR, selector)
#search_box = search_box[2:]
##print(search_box)
#for i in search_box:
#    n1 = i.find_element(By.CLASS_NAME, 'board__row-basic')
#    n2 = n1.find_element(By.CLASS_NAME, 'board__td.board__td--time.board__td--bold')
#    n3 = n2.find_elements(By.TAG_NAME, 'span')
#    n4 = n3[-1]
#    #for j in n4:
#    #    print(j)
#        #n4 = j.find_elements(By.CLASS_NAME, 'board__time')
#        #print(n4)
#    try:
#        #print(n4.find_element(By.CLASS_NAME, 'board__time'))
#        class_ = n4.get_attribute('class')
#        print(class_)
#        print(n4.tag_name)
#        print(n4.text)
#        print(n4.find_elements(By.CLASS_NAME, class_))
#    except BaseException:
#        print('sex')
#
#
#    print('=============================================')
#driver.quit()



import requests

re = requests.get('https://rasp.yandex.ru/station/9623123/?time=all')

print(re.text)