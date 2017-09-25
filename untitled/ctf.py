from socket import create_connection
from collections import namedtuple

MAZE_SERVER = ('tower.chall.polictf.it', 31337)
RECV_SIZE = 1024
Dir = namedtuple("Dir", ["char", "dy", "dx"])


class Maze:
    START = ">"
    END = "X"
    WALL = "#"
    PATH = " "
    OPEN = {PATH, END}

    RIGHT = Dir(">", 0, 1)
    DOWN = Dir("V", 1, 0)
    LEFT = Dir("<", 0, -1)
    UP = Dir("^", -1, 0)
    DIRS = [RIGHT, DOWN, LEFT, UP]
    data = ""

    @classmethod
    def load_maze(cls, fname):
        with open(fname) as inf:
            lines = (line.rstrip("\r\n") for line in inf)
            maze = [list(line) for line in lines]
        return cls(maze)

    def __init__(self, maze):
        self.maze = maze

    def __str__(self):
        return "\n".join(''.join(line) for line in self.maze)

    def find_start(self):
        for y, line in enumerate(self.maze):
            try:
                x = line.index(">")
                return y, x
            except ValueError:
                pass

        # not found!
        raise ValueError("Start location not found")

    def solve(self, y, x):
        if self.maze[y][x] == Maze.END:

            return True
        else:

            for dir in Maze.DIRS:
                ny, nx = y + dir.dy, x + dir.dx

                if self.maze[ny][nx] in Maze.OPEN:
                    if self.maze[y][x] != Maze.START:
                        self.maze[y][x] = dir.char
                        Maze.data += dir.char

                    if self.solve(ny, nx):
                        return True

                        # no solution found from this location
            if self.maze[y][x] != Maze.START:
                self.maze[y][x] = Maze.PATH
            return False


def main():
    conn = create_connection(MAZE_SERVER)
    response = conn.recv(RECV_SIZE)
    while True:
        print response
        if "Now " not in response:
            return

        response_lines = response.splitlines()
        find_delim = [x for x in response_lines if x.startswith('Now')][0]
        maze_lines = response_lines[response_lines.index(find_delim) + 2:-1]
        maze_text = '\n'.join(maze_lines)

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
                if (Maze.DATA[0] == '>') and (Maze.DATA[1] == '>'):
                    data = Maze.DATA[0]
                    data += Maze.DATA
                else:
                    data = Maze.DATA[1]
                    data += Maze.DATA[1::]
            else:
                print("    no solution found")
        except ValueError:
            print("No start point found.")
        # Do your thing here with either maze_text or maze_lines.

        print data
        conn.send(data)

        response = conn.recv(RECV_SIZE)


if __name__ == '__main__':
    main()

