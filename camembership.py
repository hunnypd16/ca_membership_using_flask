from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
def detail_of_chartedaccountant(ca_Membershp_number):
    ca_number = ca_Membershp_number
    driver = webdriver.Chrome(ChromeDriverManager().install(), )
    driver.get('http://112.133.194.254/lom.asp')
    import time
    driver.find_element(By.XPATH,"""/html/body/form/table/tbody/tr/td[2]/input""").click()
    driver.find_element(By.XPATH,"""/html/body/form/table/tbody/tr/td[2]/input""").send_keys(ca_number)
    driver.find_element(By.XPATH,"""/html/body/form/p[1]/input[1]""").click()
    name = driver.find_element(By.XPATH,"""/html/body/form/table[2]/tbody/tr[2]/td[2]/b""").text
    gender = driver.find_element(By.XPATH,"""/html/body/form/table[2]/tbody/tr[3]/td[2]/b""").text
    qualification = driver.find_element(By.XPATH,"""/html/body/form/table[2]/tbody/tr[4]/td[2]/b""").text
    address1 = driver.find_element(By.XPATH,"""/html/body/form/table[2]/tbody/tr[5]/td[2]/b""").text
    address2 = driver.find_element(By.XPATH, """/html/body/form/table[2]/tbody/tr[6]/td[2]/b""").text
    address3= driver.find_element(By.XPATH,"""/ html / body / form / table[2] / tbody / tr[9] / td[2] / b""").text
    address4 = driver.find_element(By.XPATH,"""/ html / body / form / table[2] / tbody / tr[7] / td[2] / b""").text
    address6 = driver.find_element(By.XPATH,"""/html/body/form/table[2]/tbody/tr[9]/td[2]/b""").text
    address5 = driver.find_element(By.XPATH,"""/html / body / form / table[2] / tbody / tr[10] / td[2] / b""").text
    thisdict = {
    "Name":name,
    "Gender":gender,
    "Qualification":qualification,
    "Address":address1 +" "+ address2 +" "+ address3 +" "+ address4 +" "+ address6 +"-"+ address5

    }
    print(thisdict)
    return thisdict
# detail_of_chartedaccountant("076895")