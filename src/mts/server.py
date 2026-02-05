from socket import socket as Socket, AF_INET, SOCK_STREAM
from threading import Thread
from json import loads

"""

{
    "from": "nicolas",
    "to": [
        "Kylian",
        "Lois"
    ],
    "message": "Bonjour !"
}

{
    "command": "list-users"
}

"""

class Server:
    def __init__(self, bind_host: str, bind_port: int):
        self.bind_host: str = bind_host
        self.bind_port: int = bind_port
        self.client_connections: dict[str, Socket] = {}
    
    def start(self):
        with Socket(AF_INET, SOCK_STREAM) as server_socket:
            print(f"Trying to bind socket to {self.bind_host}:{self.bind_port}")
            try:
                server_socket.bind((self.bind_host, self.bind_port))
            except:
                print(f"Failed to bind to {self.bind_host}:{self.bind_port}")
            else:
                server_socket.listen(5)
                self.__accept_and_process(server_socket)
    
    def __accept_and_process(self, server_socket: Socket):
        print(f"Server is listening on: tcp://{self.bind_host}:{self.bind_port}")
        while True:
            print("Waiting for new client connection...")
            client_socket, client_socket_info = server_socket.accept()
            try:
                username_message = client_socket.recv(1024).decode()
            except:
                print("Client's connection lost.")
            else:
                print(f"A new client is connected: {username_message} from {client_socket_info}")
                self.client_connections[username_message] = client_socket
                MessageDisptacher(client_socket, self.client_connections).start()

class MessageDisptacher(Thread):
    def __init__(self, client_socket: Socket, client_connections: dict[str, Socket]):
        Thread.__init__(self)
        self.client_socket: Socket = client_socket
        self.client_connections: dict[str, Socket] = client_connections
    
    def run(self):
        while True:
            try:
                message: str = self.client_socket.recv(4096).decode()
            except:
                client_username: str = [key for key, value in self.client_connections.items() if value is self.client_socket]
                print(f"Connection lost with client: {client_username}")
                break
            else:
                message_as_json: dict[str, any] = loads(message)
                if "to" in message_as_json.keys():
                    users_destination: list[str] = message_as_json["to"]
                    for user in users_destination:
                        user_socket: Socket = self.client_connections[user]
                        user_socket.send(message.encode())
                elif "command" in message_as_json.keys():
                    command: str = message_as_json["command"]
                    if command == "list-users":
                        self.client_socket.send(",".join(self.client_connections.keys()).encode())


server = Server("127.0.0.1", 4466)
server.start()