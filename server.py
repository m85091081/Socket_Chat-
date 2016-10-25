import socket, select 
import config

connlist = []
recv_buffer = 4096

def broadcast(sock , msg):
    for socket in connlist :
        if not socket == ss and not socket == sock :
            try:
                socket.send(msg)
            except:
                socket.close()
                connlist.remove(socket)

if __name__ == "__main__":
    ## TCP Server udp use socket.SOCK_DGRAM
    ss = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    
    ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    ss.bind((config.ip,config.port))
    
    ## conn value
    ss.listen(10) 
    connlist.append(ss)
    print('server run on ' + str(config.ip))

    while 1:
        rdsocket,wrsocket,errsocket = select.select(connlist,[],[])
        for s in rdsocket :
            if s == ss:
                sockfd , addr = ss.accept()
                connlist.append(sockfd)
                print('conn client' + str(addr)) 
                broadcast(sockfd,"[%s:%s] enter \n" % addr)
            else:
                try :
                    data = s.recv(recv_buffer)
                    if data :
                        broadcast(s,"\r" + '<' + str(s.getpeername()) + '> ' + data)
                except:
                    broadcast(s, "(%s, %s) go dead" % addr)
                    s.close()
                    connlist.remove(s)
                    continue
    ss.close()


