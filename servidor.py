from socket import socket, error
from threading import Thread
import socket
class Client(Thread):
    def __init__(self, conn, addr):

        Thread.__init__(self)
        
        self.conn = conn
        self.addr = addr
    
    def run(self):
        while True:
            try:

                while True:
                    recibido=self.conn.recv(4096)
                    print("%s:%d CLIENTE: "% self.addr, recibido.decode('utf-8'))
                    if recibido.decode('utf-8') == 'salir':                      
                        break
                    enviar=input("SERVIDOR: ")
                    self.conn.send(enviar.encode('utf-8'))
                self.conn.close()
                print("%s:%d Cliente desconectado" % self.addr)

            except error:
                print("[%s] Error de lectura. "% self.name ,"(Comunicacion cerrada con %s:%d)\n"  % self.addr)
                print("en espera de nuevas conexiones...\n")
                break

def main():    

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 9000))
    print("SERVIDOR")
    print ("El servidor esta a la espera de conexiones en el puerto ", 9000 ,"\n")
    s.listen(15)
    while True:
        msg = ("HOLA SOY EL SERVIDOR")
        conn, addr = s.accept()
        conn.send(msg.encode('utf-8'))
        c = Client(conn, addr)
        c.start()
        print("%s:%d Cliente conectado." % addr)
        print("en espera de nuevas conexiones...\n")
        
if __name__ == "__main__":
    main()