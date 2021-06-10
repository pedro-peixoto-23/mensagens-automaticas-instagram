# Importando as bibliotecas necessárias
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import getpass as get
import time
import titles
import os


class InstagramMessages:
    def __init__(self):
        os.system('cls')
        titles.tit('Automatic messages for Instagram')
        
        # Recebendo os dados essenciais para entrar no instagram
        self.username = input('\nUsername: ')
        self.password = get.getpass('Password: ')
        
        # Mensagem que será enviada para os contatos
        self.message = input('\nMessage: ')
        
        # Chamando o método responsável por receber e armazenar os contatos
        self.contacts()
        
        # Abrir o google chrome e entrar no instagram
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://instagram.com')
    
    def contacts(self):
        while True:
            try:
                contacts_number = int(input('\nHow many contacts will the '
                                            'message be sent to? '))
                break
            except:
                print('\033[1;31m' + 'ERROR: type a number!' + '\033[m')
        print()
        
        # Lista que vai armazenar os contatos
        self.contacts = list()
        # Recebendo os contatos e armazenando na lista chamada "self.contacts"
        for p in range(contacts_number):
            p = input('Insert the {}º contact (@): '.format(p + 1))
            self.contacts.append(p)
    
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
       
    def seek_contact(self):
        time.sleep(3)
        for contact in self.contacts:
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
        time.sleep(10)
        
        # Procurar a caixa de mensagens
        message_block = self.driver.find_element_by_tag_name('textarea')
        # Clicar na caixa de texto
        message_block.click()
        # Inserir a mensagem na caixa
        message_block.send_keys(self.message)
        # Clicar ENTER para enviar
        message_block.send_keys(Keys.ENTER)


instagram_messages = InstagramMessages()
instagram_messages.login()
instagram_messages.seek_contact()
