class Cart:

    def __init__(self, x, y, direction, currentTrack):
        self.x = x
        self.y = y
        self.direction = direction
        self.currentTrack = currentTrack
        self.nextTurn = "l"

    def getIntersectionDirection(self):
        if self.direction == "u":
            if self.nextTurn == "l":
                self.direction = "l"
            elif self.nextTurn == "r":
                self.direction = "r"
        elif self.direction == "r":
            if self.nextTurn == "l":
                self.direction = "u"
            elif self.nextTurn == "r":
                self.direction = "d"
        elif self.direction == "d":
            if self.nextTurn == "l":
                self.direction = "r"
            elif self.nextTurn == "r":
                self.direction = "l"
        else:
            if self.nextTurn == "l":
                self.direction = "d"
            elif self.nextTurn == "r":
                self.direction = "u"

    def move(self, newX, newY, newTrack, newDirection = False):
        self.x = newX
        self.y = newY
        self.currentTrack = newTrack

        if newDirection:
            self.direction = newDirection

        if self.currentTrack == "+":
            self.getIntersectionDirection()
            self.updateNextTurn()

    def updateNextTurn(self):
        if self.nextTurn == "l":
            self.nextTurn = "f"
        elif self.nextTurn == "f":
            self.nextTurn = "r"
        else:
            self.nextTurn = "l"