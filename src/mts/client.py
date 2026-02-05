from socket import socket as Socket, AF_INET, SOCK_STREAM
from threading import Thread
from json import loads, dumps

class Client:
    def __init__(self, server_host: str, server_port: int):
        self.server_host: str = server_host
        self.server_port: int = server_port
        self.socket: Socket|None = None
        self.username: str|None = None
    
    def connect(self, username: str):
        self.username = username
        self.socket = Socket(AF_INET, SOCK_STREAM)
        try:
            self.socket.connect((self.server_host, self.server_port))
            self.socket.send(self.username.encode())
        except:
            print(f"Unable to connect to server: tcp://{self.server_host}:{self.server_port}")
            self.socket = None
        else:
            MessageReceiver(self.socket).start()

    def list_users(self) -> list[str]:
        users: list[str] = []
        message: dict[str, str] = {"command": "list-users"}
        message_as_string: str = dumps(message)
        try:
            self.socket.send(message_as_string.encode())
            users = self.socket.recv(4096).decode().split(",")
        except:
            print("Disconnected from server.")

        return users

    def send_message(self, message: str, to_users: list[str]):
        message: dict[str, any] = {
            "from": self.username,
            "to": to_users,
            "message": message
        }
        message_as_string: str = dumps(message)
        try:
            self.socket.send(message_as_string.encode())
        except:
            print("Disconnected from server.")

class MessageReceiver(Thread):
    def __init__(self, socket: Socket):
        Thread.__init__(self)
        self.socket: Socket = socket
    
    def run(self):
        while True:
            try:
                self.socket.settimeout(0.2)
                message: str = self.socket.recv(4096).decode()
            except TimeoutError:
                pass
            except:
                print("Disconnected from server.")
                break
            else:
                message_as_json: dict[str, any] = loads(message)
                print(f"{message_as_json["from"]} send: {message_as_json["message"]}")

client = Client("127.0.0.1", 4466)
client.connect("Nicolas")
print(client.list_users())
while True:
    message_to_send = input("> ")
    client.send_message(message_to_send, ["Nicolas"])