from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
#from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
driver.get("https://pt-br.facebook.com/")

def campos():

    campo = driver.find_element_by_name('firstname')
    campo.send_keys("Lucas José")

    campo_2 = driver.find_element_by_name("lastname")
    campo_2.send_keys('Teixeira')

    email = driver.find_element_by_name("reg_email__")
    email.send_keys("groselha@felicidade.com.aapp")

#esperar para confirmação, na variável 'elemnto' passo o tempo de espera como parâmetro e aplico a função 'esperar'
#ela me retorna o campo atual aguarda para passar ao próximo campo que preciso.

def aguardar (driver): #esperar a aparição do próximo campo
    return  driver.find_element_by_name('reg_email_')
    elemento = WebDriverWait(driver, 5).until(aguardar)

def preencher ():
    confirm = driver.find_element_by_name('reg_email_confirmation__')
    confirm.send_keys("groselha@felicidade.com.aapp")

    senha = driver.find_element_by_id("u_0_v")
    senha.send_keys("123456789**//**")

    dia = Select(driver.find_element_by_id('day'))
    dia.select_by_value('24')

    mes = Select(driver.find_element_by_id('month'))
    mes.select_by_value('8')

def selecionar ():

    ano = Select(driver.find_element_by_id('year'))
    ano.select_by_value('1989')

    gender = Select(driver.find_element_by_id('u_0_a')).click()
    gender.select_by_value('2')

def submeter ():
    buttom = driver.find_element_by_id('u_0_11')
    buttom.send_keys(Keys.ENTER)

campos()
preencher()
selecionar()
submeter()