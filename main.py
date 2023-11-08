from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import socket


class Caixa(BoxLayout):
    def enviar(self):
        # Cria socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Conecta com lado servidor
        host = '127.0.0.1'  # The server's IP address
        port = 12345  # The server's port
        client_socket.connect((host, port))

        # Envio dos dados
        message = self.ids.pr1.text
        client_socket.send(message.encode('utf-8'))

        #Fechamento do socket
        client_socket.close()

    def receber(self):
        # Cria socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Seta a porta de escuta e o host
        host = '127.0.0.1'  
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

class Teste(App):
    def build(self):
        return Caixa()

Teste().run()
