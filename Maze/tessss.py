import socket

def main():
  Host = '127.0.0.1'
  port = 8000
  Opte_list = ['SAVE', 'LOAD']
  file_list = []
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(Host, port)
  s.listen(1)
  Conection, Adress = s.accept()
  if Conection.recv(1024 == Opte_list[0]):
    fname = Conection.recv(1024)
    fobj = file(fname , 'w' )
    data = Conection.recv(1024)



if __name__=='__main__':
  main()