# Objetivo: criar um bot para enviar mensagens no instagram. O programa recebe o
# seu usuário e senha e uma quantidade de contatos, após isso manda a mensagem 
# antes definida para essa lista de contatos.

# Importando as bibliotecas necessárias
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class InstagramMessages:
    def __init__(self, username, password):
        # Recebendo os dados essenciais para entrar no instagram
        self.username = username
        self.password = password
        
        # Abrir o google chrome e entrar no instagram
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://instagram.com')
    
    def login(self):
        time.sleep(3)
        # Encontrar o campo de inserir o nome de usuário
        path = '//input[@name="username"]'
        username_block = self.driver.find_element_by_xpath(path)
        # Clicar no elemento
        username_block.click()
        time.sleep(1)
        # Inserir o email ou usuário
        username_block.send_keys(self.username)

        # Encontrar o campo de inserir a senha
        path = '//input[@name="password"]'
        password_block = self.driver.find_element_by_xpath(path)
        # Clicar no campo
        password_block.click()
        # Inserir a senha
        password_block.send_keys(self.password)
        
        # Encontrar o botão de fazer login
        path = '//*[@id="loginForm"]'
        login_button_block = self.driver.find_element_by_xpath(path)
        # Clicar no botão
        login_button_block.click()
        
    def seek_contact(self, contact_name):
        time.sleep(3)
        for contact in contact_name:
            self.driver.get(f'https://instagram.com/{contact}/')
            self.send_messages()
            
    def send_messages(self):
        time.sleep(4)
        # Procurar o botão de enviar mensagens
        send_message_button = self.driver.find_element_by_tag_name('button')
        time.sleep(1)
        # Clicar no botão de enviar mensagens
        send_message_button.click()
        # Tempo para apertar em não querer notificações
        time.sleep(20)
        
        # Procurar a caixa de mensagens
        message_block = self.driver.find_element_by_tag_name('textarea')
        # Clicar na caixa de texto
        message_block.click()
        # Inserir a mensagem na caixa
        message_block.send_keys('Durma bem! Tchau!')
        # Clicar ENTER para enviar
        message_block.send_keys(Keys.ENTER)


instagram_messages = InstagramMessages('username', 'password')
instagram_messages.login()
instagram_messages.seek_contact(['contact_1', 'contact_2'])
