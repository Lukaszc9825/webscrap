from selenium import webdriver
import time

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
url = 'https://csgoempire.com'
row = []
filepath1 = 'data.txt'
filepath2 = 'label.txt'

while True:
    f = open(filepath1, "a")
    f2 = open(filepath2, "a")
    driver.get(url)
    time.sleep(5)

    for i in range(10):

        coin = driver.find_element_by_xpath('//*[@id="page-scroll"]/div/section/div/div/div[4]/div/div[1]/div[2]/div[' + str(i+1) +']/div')
        value = coin.get_attribute("class")

        if str(value) == "inline-block w-24 h-24 rounded-full ml-1 coin-t":
            print("T")
            row.append(0)
        elif str(value) == "inline-block w-24 h-24 rounded-full ml-1 coin-ct":
            print("CT")
            row.append(1)
        else:
            print("x14")
            row.append(2)
    last_ct = driver.find_elements_by_xpath('//*[@class="text-light-grey-1 text-xxs font-bold mr-2"]')
    for x in range(3):
        print(last_ct[x+3].text)
        row.append(int(last_ct[x+3].text))

    print(row)
    f.write(str(row))
    f.write(",\n")
    f2.write(str(row[9]) + ", ")
    row.clear()
    print("-------------------------------------------------------------------------------------")
    f.close()
    f2.close()
    time.sleep(23.5)
