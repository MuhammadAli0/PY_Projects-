from socket import create_connection
from test2 import Maze, fix_start, fix_answer
MAZE_SERVER = ('54.69.145.229', 16000)
RECV_SIZE = 8192


def main():
    conn = create_connection(MAZE_SERVER)
    response = conn.recv(RECV_SIZE)
    while True:
        print response
        if "Now " not in response:
            return

        response_lines = response.splitlines()
        find_delim = [x for x in response_lines if x.startswith('Now')][0]
        maze_lines = response_lines[response_lines.index(find_delim)+2:-1]
        maze_text = '\n'.join(maze_lines)

        # Do your thing here with either maze_text or maze_lines.
        try:
            with open('Maze.txt', 'w') as f:
                f.write('\n'.join(maze_lines))

        except ValueError:
            print("File not found.")

        zzz = Maze.load_maze("Maze.txt")

        try:
            sy, sx = zzz.find_start()
            print("solving...")
            if zzz.solve(sy, sx):
                print(zzz)
                answer = fix_start()


            else:
                print("    no solution found")
        except ValueError:
            print("No start point found.")
        conn.send(answer)

        response = conn.recv(RECV_SIZE)


if __name__ == '__main__':
    main()
