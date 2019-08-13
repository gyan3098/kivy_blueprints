import select,socket,sys

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",9096))
p = "Connect"
s.send(p.encode("utf8"))

rlist = (sys.stdin, s)
while 1:
    read, write ,fail = select.select(rlist,(),())
    for sock in read:
        if sock == s: #receive message from server
            data = s.recv(4096)
            print(data)

        else:
            msg = sock.readline()
            s.send(msg)