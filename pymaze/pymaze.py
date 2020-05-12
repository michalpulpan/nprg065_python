import sys

class Maze:
    player = {'x': 0, 'y': 0, 'pos': ''}
    pane = []
    steps = 0

    def __init__(self, player, pane, steps):
        self.player = player
        self.pane = pane
        self.steps = steps

    def doStep(self):
        if self.isWallInFrontOfMe() and self.isWallOnMyRight():
            # CORNER, rotate to left
            self.move('L')
        elif not self.isWallInFrontOfMe() and self.isWallOnMyRight():
            #nothing infront of player
            self.move('F')
            self.steps -= 1

        if not self.isWallOnMyRight():
            # nothing below me
            self.move('R')
            self.move('F')
            self.steps -= 1

    def isWallInFrontOfMe(self):  # returns true if next cell (based on player's position) is a wall
        if self.player['pos'] is '>' and self.pane[self.player['y']][self.player['x'] + 1] is False:
            return True
        elif self.player['pos'] is '<' and self.pane[self.player['y']][self.player['x'] - 1] is False:
            return True
        elif self.player['pos'] is '^' and self.pane[self.player['y'] - 1][self.player['x']] is False:
            return True
        elif self.player['pos'] is 'v' and self.pane[self.player['y'] + 1][self.player['x']] is False:
            return True
        else:
            return False

    def isWallOnMyRight(self): # returns true if cell on the right from player is a wall
        if self.player['pos'] is '>' and self.pane[self.player['y'] + 1][self.player['x']] is False:
            return True
        elif self.player['pos'] is '<' and self.pane[self.player['y'] - 1][self.player['x']] is False:
            return True
        elif self.player['pos'] is '^' and self.pane[self.player['y']][self.player['x'] + 1] is False:
            return True
        elif self.player['pos'] is 'v' and self.pane[self.player['y']][self.player['x'] - 1] is False:
            return True
        else:
            return False

    def isWallOnMyLeft(self): # returns true if cell on the left from player is a wall
        if self.player['pos'] is '>' and self.pane[self.player['y'] - 1][self.player['x']] is False:
            return True
        elif self.player['pos'] is '<' and self.pane[self.player['y'] + 1][self.player['x']] is False:
            return True
        elif self.player['pos'] is '^' and self.pane[self.player['y']][self.player['x'] - 1] is False:
            return True
        elif self.player['pos'] is 'v' and self.pane[self.player['y']][self.player['x'] + 1] is False:
            return True
        else:
            return False

    def isWallBehindMe(self):  # returns true if next cell (based on player's position) is a wall
        if self.player['pos'] is '>' and self.pane[self.player['y']][self.player['x'] - 1] is False:
            return True
        elif self.player['pos'] is '<' and self.pane[self.player['y']][self.player['x'] + 1] is False:
            return True
        elif self.player['pos'] is '^' and self.pane[self.player['y'] + 1][self.player['x']] is False:
            return True
        elif self.player['pos'] is 'v' and self.pane[self.player['y'] - 1][self.player['x']] is False:
            return True
        else:
            return False

    def move(self,direction): #Moves with player based on his position
        if self.player['pos'] is '>' and direction is 'L':
            self.player['pos'] = '^'
        elif self.player['pos'] is '>' and direction is 'R':
            self.player['pos'] = 'v'
        elif self.player['pos'] is '>' and direction is 'F':
            self.player['x'] += 1
        elif self.player['pos'] is '<' and direction is 'L':
            self.player['pos'] = 'v'
        elif self.player['pos'] is '<' and direction is 'R':
            self.player['pos'] = '^'
        elif self.player['pos'] is '<' and direction is 'F':
            self.player['x'] -= 1
        elif self.player['pos'] is '^' and direction is 'L':
            self.player['pos'] = '<'
        elif self.player['pos'] is '^' and direction is 'R':
            self.player['pos'] = '>'
        elif self.player['pos'] is '^' and direction is 'F':
            self.player['y'] -= 1
        elif self.player['pos'] is 'v' and direction is 'L':
            self.player['pos'] = '>'
        elif self.player['pos'] is 'v' and direction is 'R':
            self.player['pos'] = '<'
        elif self.player['pos'] is 'v' and direction is 'F':
            self.player['y'] += 1

    def setCorrectPosition(self): #corrects player's position after start of the calcuation
        if self.isWallInFrontOfMe() and not self.isWallBehindMe() and not self.isWallOnMyLeft():
            self.move('L')
        elif self.isWallInFrontOfMe() and self.isWallBehindMe():
            self.move('R')
        elif self.isWallBehindMe() and not self.isWallInFrontOfMe():
            self.move('R')
        elif self.isWallInFrontOfMe() and self.isWallOnMyLeft():
            self.move('R')

        elif self.isWallOnMyLeft():
            self.move('R')
            self.move('R')

    def myPrint(self):
        x = 0
        y = 0
        ret = ''
        for row in self.pane:
            for i, cell in enumerate(row):
                if x is self.player['x'] and y is self.player['y']:
                    print(self.player['pos'], end='')
                    ret += self.player['pos']
                elif cell:
                    print('.', end='')
                    ret += '.'
                else:
                    print('#', end='')
                    ret += '#'
                x += 1
                if i is not len(row) - 1:
                    print(' ', end='')
                    ret += ' '
            y += 1
            x = 0
            print()
            ret += '\n'
        return ret

    def calculate(self):
        if not self.isWallOnMyRight():
            self.setCorrectPosition()
        while self.steps is not 0:
            self.doStep()
        return self.myPrint()


def readPane(border, empty, positions, input):
    ret = []
    player = {'x': 0, 'y': 0, 'pos': ''}
    iters = 0
    for linenum, line in enumerate(input):
        if linenum is 0:
            iters = int(line)
            continue
        row = []
        if line.rstrip():
            line = line.split()
            for word in line:
                if word is border:
                    row.append(False)
                elif word is empty:
                    row.append(True)
                elif word in positions:
                    player['x'] = len(row)
                    player['y'] = len(ret)
                    player['pos'] = word
                    row.append(True)
        ret.append(row)
    maze = Maze(player, ret, iters)
    return maze

if __name__ == '__main__':
    border = '#'
    empty = '.'
    positions = ['^', '>', 'v', '<']

    maze = readPane(border, empty, positions,sys.stdin)
    maze.calculate()


