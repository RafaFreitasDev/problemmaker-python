from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

import os
import dotenv

from selenium.webdriver.common.action_chains import ActionChains

dotenv.load_dotenv()

class SendMessage:    
    def open_website(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        link = 'https://web.whatsapp.com'
        self.driver.get(link)
        sleep(15)

    def enviar_problemas(self, msn_problemas):
        CONTATO = os.getenv("CONTACT")
        sleep(5)

        campo_buscar_contato = self.driver.find_elements(By.XPATH, '//p[@class="selectable-text copyable-text iq0m558w g0rxnol2"]')[0]
        campo_buscar_contato.send_keys(CONTATO)
        campo_buscar_contato.send_keys(Keys.ENTER)
        sleep(2)

        campo_msn = self.driver.find_elements(By.XPATH, '//p[@class="selectable-text copyable-text iq0m558w g0rxnol2"]')[1]
        campo_msn.send_keys(msn_problemas)
        sleep(2)

        campo_msn = self.driver.find_elements(By.XPATH, '//p[@class="selectable-text copyable-text iq0m558w g0rxnol2"]')[1]
        campo_msn.send_keys("---POR HOJE É SÓ---\n")
        sleep(2)
        
    def enviar_resultados(self,msn_result_mult, msn_result_div1,msn_result_div2,msn_result_div3):
        MYSELF = os.getenv("MYSELF")
        sleep(2)

        campo_buscar_contato = self.driver.find_elements(By.XPATH, '//p[@class="selectable-text copyable-text iq0m558w g0rxnol2"]')[0]
        campo_buscar_contato.send_keys(MYSELF)
        campo_buscar_contato.send_keys(Keys.ENTER)
        sleep(2)

        campo_msn = self.driver.find_elements(By.XPATH, '//p[@class="selectable-text copyable-text iq0m558w g0rxnol2"]')[1]
        campo_msn.send_keys("---RESULTADOS---\n")
        sleep(5)

        campo_msn = self.driver.find_elements(By.XPATH, '//p[@class="selectable-text copyable-text iq0m558w g0rxnol2"]')[1]
        campo_msn.send_keys(msn_result_mult)
        sleep(5)

        campo_msn = self.driver.find_elements(By.XPATH, '//p[@class="selectable-text copyable-text iq0m558w g0rxnol2"]')[1]
        campo_msn.send_keys(msn_result_div1)
        sleep(5)

        campo_msn = self.driver.find_elements(By.XPATH, '//p[@class="selectable-text copyable-text iq0m558w g0rxnol2"]')[1]
        campo_msn.send_keys(msn_result_div2)
        sleep(5)

        campo_msn = self.driver.find_elements(By.XPATH, '//p[@class="selectable-text copyable-text iq0m558w g0rxnol2"]')[1]
        campo_msn.send_keys(msn_result_div3)
        sleep(5)

        