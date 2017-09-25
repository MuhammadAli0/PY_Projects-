from socket import create_connection
from collections import namedtuple

MAZE_SERVER = ('34.253.165.46', 11223)
RECV_SIZE = 1024

def main():
    conn = create_connection(MAZE_SERVER)
    response = conn.recv(RECV_SIZE)

    while True:
        print response
        if "Level" in response:


        # answer = raw_input("enter the answer")
        # conn.send(answer)

        response = conn.recv(RECV_SIZE)


if __name__ == '__main__':
    main()
