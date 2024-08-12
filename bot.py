import pandas as pd
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions

driver = webdriver.Edge()

driver.get('https://api-seguridad.sunat.gob.pe/v1/clientessol/b3639111-1546-4d06-b74f-de2c40629748/oauth2/login?originalUrl=https://apps.trabajo.gob.pe/si.segurovida/index.jsp&state=m1ntr4')

login_caja = {'ruc': '20100209641', 'user': 'ER5DELYP', 'psw': 'ER5DELCa'}

driver.find_element(By.ID, 'txtRuc').send_keys(login_caja['ruc'])
driver.find_element(By.ID, 'txtUsuario').send_keys(login_caja['user'])
driver.find_element(By.ID, 'txtContrasena').send_keys(login_caja['psw'])
driver.find_element(By.ID, 'btnAceptar').click()

#accept=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//area[@coords='250,20,464,68']")))
#accept.click()

#print(accept.text)
input()
driver.execute_script('f_segurovida();')
input()

lista = Select(driver.find_element(By.NAME, 'v_ruc_ase'))

input()

driver.quit()




