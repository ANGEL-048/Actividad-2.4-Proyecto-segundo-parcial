from socket import socket
import socket

try:
    raw_input
except NameError:
    raw_input = input
def main():
    print("CLIENTE\n")
    ipServidor = "127.0.0.1"
    puertoServidor = 9000
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((ipServidor,puertoServidor))
    print("servidor:", (ipServidor, puertoServidor))
    data = cliente.recv(1024)
    print(data.decode(),"\n")

    while True:
        msg = input("CLIENTE: ")
        cliente.send(msg.encode('utf-8'))
        if msg == 'salir':
            break
        else:
            respuesta = cliente.recv(1024)
            print("SERVIDOR", respuesta.decode('utf-8'))  
    cliente.close() 
if __name__ == "__main__":
    main()