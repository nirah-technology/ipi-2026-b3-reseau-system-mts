# Module qui gère la couche réseau
from socket import socket as Socket, AF_INET, SOCK_STREAM

# Module qui gère l'héritage
from abc import abstractmethod

# Module qui gère le typage
from typing import Protocol  # Permet à une classe d'être représenté 
                             # comme une fonctionnalité devant être 
                             # ajouter à un objet. 

class ScannerFeature(Protocol):
    @abstractmethod
    def scan(self, *args, **kwargs):
        raise NotImplementedError("'scan' feature is not implemented.")

class PortsScanner(ScannerFeature):
    def __init__(self):
        pass

    def scan(self, target_host: str, start_port_to_scan: int, end_port_to_scan: int):
        opened_ports: list[int] = []
        for port in range(start_port_to_scan, end_port_to_scan+1):
            with Socket(AF_INET, SOCK_STREAM) as scanner_socket:
                try:
                    scanner_socket.settimeout(0.2)
                    scanner_socket.connect((target_host, port))
                except:
                    pass
                else:
                    opened_ports.append(port)
        return opened_ports

scanner = PortsScanner()
ports = scanner.scan("127.0.0.1", 6000, 9000)
print(ports)

