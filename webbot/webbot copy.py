from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from pandas import read_csv
from time import sleep

NUMBEO_LINK = 'https://it.numbeo.com/'
CATEGORIE = {
    'Criminalità': 'Paura che ci rubino l\'automobile',
    'Assistenza Sanitaria': 'Cordialità e gentilezza del personale sanitario',
    'Inquinamento': 'Insoddisfazione per la Nettezza Urbana'
}

df = read_csv('/Users/newmac/Documents/PROG/Pythone/webbot/città_latine.csv', index_col = 0, encoding = 'utf-8')

chrome_driver_path = '/Users/newmac/Documents/PROG/Pythone/webbot/chromedriver'
driver = Chrome(service=Service(chrome_driver_path))
driver.maximize_window()
driver.get(NUMBEO_LINK)

wait = WebDriverWait(driver, 10)  # Imposta il timeout a 10 secondi (puoi modificare questo valore)
wait.until(EC.element_to_be_clickable((By.ID, 'accept-choices'))).click()
print("ok qui tutto apposto")
for luogo in df.index:
    wait.until(EC.visibility_of_element_located((By.ID, 'city_selector_menu_city_id'))).send_keys(luogo)
    print("ho cercato",luogo)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-menu-item'))).click()
    print("ok ora ho fatto invio")
    for categoria, indice in CATEGORIE.items():
        xpath = f'//span[contains(@class, "nobreak")]/a[text()="{categoria}"]'
        print("ora devo selezionare",categoria)
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        indice_tr = wait.until(EC.element_to_be_clickable((By.XPATH, f'//td[text()="{indice}"]/parent::tr')))
        print("ok")
        sleep(2)
        valore_td = indice_tr.find_element(By.CLASS_NAME, 'indexValueTd')
        print("ora ho preso il valore per ",indice)
        df.loc[luogo, categoria] = valore_td.text
        print("ora ho salvato il valore ",valore_td.text)
        
    print("se siamo arrivati fin qui già non ci credo più")

df.to_csv('/Users/newmac/Documents/PROG/Pythone/webbot/città_latine_compilate.csv')
print("ok ora sono felice 🥲")