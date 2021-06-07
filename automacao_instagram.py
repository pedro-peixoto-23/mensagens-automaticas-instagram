# Objetivo: criar um bot para enviar mensagens no instagram. O programa recebe o
# seu usuário e senha e uma quantidade de contatos, após isso manda a mensagem 
# antes definida para essa lista de contatos.

# Importando as bibliotecas necessárias
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class InstagramMessages:
    def __init__(self):
        # Recebendo os dados essenciais para entrar no instagram
        self.username = input('\nUsername: ')
        self.password = input('Password: ')
        
        # Mensagem que será enviada para os contatos
        self.mensagem = 'Hello! How are you?'
        
        # Abrir o google chrome e entrar no instagram
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://instagram.com')
    
    def login(self):
        time.sleep(3)
        # Encontrar o campo de inserir o nome de usuário
        xpath = '//input[@name="username"]'
        username_block = self.driver.find_element_by_xpath(xpath)
        # Clicar no elemento
        username_block.click()
        time.sleep(1)
        # Inserir o email ou usuário
        username_block.send_keys(self.username)

        # Encontrar o campo de inserir a senha
        xpath = '//input[@name="password"]'
        password_block = self.driver.find_element_by_xpath(xpath)
        # Clicar no campo
        password_block.click()
        # Inserir a senha
        password_block.send_keys(self.password)
        
        # Encontrar o botão de fazer login
        xpath = '//*[@id="loginForm"]'
        login_button_block = self.driver.find_element_by_xpath(xpath)
        # Clicar no botão
        login_button_block.click()
    
    # Quando chamar esse método, usar o @ da pessoa para quem quer enviar
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
        message_block.send_keys(self.mensagem)
        # Clicar ENTER para enviar
        message_block.send_keys(Keys.ENTER)


instagram_messages = InstagramMessages()
instagram_messages.login()
# Observação: podem ser colocados mais de uma pessoa e até mesmo apenas uma
instagram_messages.seek_contact(['contact_1', 'contact_2'])
