from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import socket

# Classe que se comunica com a interface Kivy
class Caixa(BoxLayout):
    def enviar(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = self.ids.ip.text
        port = 12345  
        client_socket.connect((host, port))

        # Envio dos dados
        message = self.ids.pr1.text
        client_socket.send(message.encode('utf-8'))

        # Fechamento do socket
        client_socket.close()

    def receber(self):
        # Cria socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Seta a porta de escuta e o host
        host = '0.0.0.0'
        port = 12345  
        server_socket.bind((host, port))

        # Escuta potenciais conexoes
        server_socket.listen(5)

        # Aceite da conexao e recebimento dos dados
        client_socket, addr = server_socket.accept()
        data = client_socket.recv(1024)
        print(f"Connection from {addr} Mensagem: {data.decode('utf-8')}")
        self.ids.p1.text = f"Connection from {addr} Mensagem: {data.decode('utf-8')}"

        # Fechamento dos sockets
        client_socket.close()
        server_socket.close()

# Classe principal da aplicação
class Teste(App):
    def build(self):
        return Caixa()

Teste().run()
