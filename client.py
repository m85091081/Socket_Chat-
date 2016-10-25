import socket, select, string, sys

from config import ip as host
from config import port as port

if __name__ == "__main__":
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
     
    try :
        s.connect((host, port))
    except :
        print('connect who sure!?')
        sys.exit()

    print('connect!')
     
    while 1:
        socket_list = [sys.stdin, s]
         
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print('you dead')
                    sys.exit()
                else :
                    print(data)
             
            else :
                msg = sys.stdin.readline()
                s.send(msg.encode())
                

