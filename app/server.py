import socket
SERVER = "127.0.0.1",5000
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#soc.bind(SERVER)
con = socket.create_connection(SERVER)
con.bind
while True:
    respons = con.recv(1024)
    if "hello" in respons:
        con.send("Hello \nHow are you \n")
        print  respons
    elif "bye" in respons:
        con.close()
        print  respons
    else:
        con.send("I do not understand you \nclear\n")

