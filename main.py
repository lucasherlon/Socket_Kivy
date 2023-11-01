from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import socket


class Caixa(BoxLayout):
    def enviar(self):
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        host = '127.0.0.1'  # The server's IP address
        port = 12345  # The server's port
        client_socket.connect((host, port))

        # Send data to the server
        message = self.ids.pr1.text
        client_socket.send(message.encode('utf-8'))

        # Close the socket
        client_socket.close()

    def receber(self):
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to a specific address and port
        host = '127.0.0.1'  # Your server's IP address
        port = 12345  # Choose a free port
        server_socket.bind((host, port))

        # Listen for incoming connections
        server_socket.listen(5)

        # Accept a connection and establish a connection object
        client_socket, addr = server_socket.accept()
        data = client_socket.recv(1024)
        print(f"Connection from {addr} Mensagem: {data.decode('utf-8')}")
        self.ids.p1.text = f"Connection from {addr} Mensagem: {data.decode('utf-8')}"

        # Close the sockets
        client_socket.close()
        server_socket.close()

class Teste(App):
    def build(self):
        return Caixa()

Teste().run()