from socket import create_connection
from collections import namedtuple

MAZE_SERVER = ('54.69.145.229', 16000)
RECV_SIZE = 8192
Dir = namedtuple("Dir", ["char", "dy", "dx"])

class Maze:
    START = "#>"
    END   = "X"
    WALL  = "#"
    PATH  = " "
    OPEN  = {PATH, END}  # map locations you can move to (not WALL or already explored)

    RIGHT = Dir(">",  0,  1)
    DOWN  = Dir("V",  1,  0)
    LEFT  = Dir("<",  0, -1)
    UP    = Dir("^", -1,  0)
    DIRS  = [RIGHT, DOWN, LEFT, UP]
    data = ""
    @classmethod
    def load_maze(cls, fname):
        with open(fname) as inf:
            lines = (line.rstrip("\r\n") for line in inf)
            maze  = [list(line) for line in lines]
        return cls(maze)

    def __init__(self, maze):
        self.maze = maze

    def __str__(self):
        return "\n".join(''.join(line) for line in self.maze)

    def find_start(self):
        for y,line in enumerate(self.maze):
            try:
                x = line.index(">")
                return y, x
            except ValueError:
                pass

        # not found!
        raise ValueError("Start location not found")

    def solve(self, y, x):
        if self.maze[y][x] == Maze.END:
            # base case - endpoint has been found
            return True
        else:
            # search recursively in each direction from here
            for dir in Maze.DIRS:
                nx, ny = x + dir.dx , y + dir.dy





                if self.maze[ny][nx] in Maze.OPEN:  # can I go this way?
                    if self.maze[y][x] != Maze.START: # don't overwrite Maze.START
                        self.maze[y][x] = dir.char

                                                    # mark direction chosen
                    if self.solve(ny, nx):          # recurse...
                        return True                 # solution found!
                Maze.data += dir.char
            # no solution found from this location
            if self.maze[y][x] != Maze.START:       # don't overwrite Maze.START
                self.maze[y][x] = Maze.PATH         # clear failed search from map
            return False

def main():

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
                data = Maze.data
                fo = data[0]
                fo += data
                print (fo)
                print (data)
            else:
                print("    no solution found")
        except ValueError:
            print("No start point found.")


if __name__ == '__main__':
    main()
