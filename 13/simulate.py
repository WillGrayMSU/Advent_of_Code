from __future__ import print_function
from readInput import readInput
from cart import Cart

def main():
    world = readInput("input.txt")
    carts = []
    y = 0
    for j in world:
        x = 0
        for i in j:
            if (i == ">") or (i == "v") or (i == "^") or (i == "<"):
                if i == ">":
                    carts.append(Cart(x,y,"r", "-"))
                elif i == "<":
                    carts.append(Cart(x,y,"l", "-"))
                elif i == "^":
                    carts.append(Cart(y, x, "u", "|"))
                else:
                    carts.append(Cart(x, y, "d", "|"))
            x += 1
        y+=1

    crash = False
    loopCount = 0
    while not crash:
        loopCount += 1
        for cart in carts:
            cart, world, crash = moveCart(cart, world)
            if crash:
                print("CRASH! First Crash occurred at " + str(cart.x) + ", " + str(cart.y) + " during tick " + str(loopCount) + ".")
                break
        carts = sortCarts(carts)


def moveCart(cart, world):
    crash = False
    if cart.direction == "u":
        print(world[cart.y+1][cart.x])
        if (world[cart.y+1][cart.x] == "|") or (world[cart.y+1][cart.x] == "+"):
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x, cart.y+1, world[cart.y+1][cart.x])
            world[cart.y+1][cart.x] = "^"
        elif (world[cart.y+1][cart.x] == ">") or (world[cart.y+1][cart.x] == "v") or (world[cart.y+1][cart.x] == "^") or (world[cart.y+1][cart.x] == "<"):
            crash = True
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x, cart.y+1, world[cart.y+1][cart.x])
            world[cart.y+1][cart.x] = "X"
        else:
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x, cart.y+1, world[cart.y+1][cart.x], handleTurn(cart.direction, world[cart.y+1][cart.x]))
            world[cart.y+1][cart.x] = "^"
    elif cart.direction == "r":
        print(world[cart.y][cart.x+1])
        if (world[cart.y][cart.x+1] == "-") or (world[cart.y][cart.x+1] == "+"):
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x+1, cart.y, world[cart.y][cart.x+1])
            world[cart.y][cart.x+1] = ">"
        elif (world[cart.y][cart.x+1] == ">") or (world[cart.y][cart.x+1] == "v") or (world[cart.y][cart.x+1] == "^") or (world[cart.y][cart.x+1] == "<"):
            crash = True
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x+1, cart.y, world[cart.y][cart.x+1])
            world[cart.y][cart.x+1] = "X"
        else:
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x+1, cart.y, world[cart.y][cart.x+1], handleTurn(cart.direction, world[cart.y][cart.x+1]))
            world[cart.y][cart.x+1] = ">"
    elif cart.direction == "d":
        print(world[cart.y-1][cart.x])
        if (world[cart.y-1][cart.x] == "|") or (world[cart.y-1][cart.x] == "+"):
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x, cart.y-1, world[cart.y-1][cart.x])
            world[cart.y-1][cart.x] = "v"
        elif (world[cart.y-1][cart.x] == ">") or (world[cart.y-1][cart.x] == "v") or (world[cart.y-1][cart.x] == "^") or (world[cart.y-1][cart.x] == "<"):
            crash = True
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x, cart.y-1, world[cart.y-1][cart.x])
            world[cart.y-1][cart.x] = "X"
        else:
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x, cart.y-1, world[cart.y-1][cart.x], handleTurn(cart.direction, world[cart.y-1][cart.x]))
            world[cart.y-1][cart.x] = "v"
    else:
        print(world[cart.y][cart.x-1])
        if (world[cart.y][cart.x-1] == "-") or (world[cart.y][cart.x-1] == "+"):
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x-1, cart.y, world[cart.y][cart.x-1])
            world[cart.y][cart.x-1] = "<"
        elif (world[cart.y][cart.x-1] == ">") or (world[cart.y][cart.x-1] == "v") or (world[cart.y][cart.x-1] == "^") or (world[cart.y][cart.x-1] == "<"):
            crash = True
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x-1, cart.y, world[cart.y][cart.x-1])
            world[cart.y][cart.x-1] = "X"
        else:
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x-1, cart.y, world[cart.y][cart.x-1], handleTurn(cart.direction, world[cart.y][cart.x-1]))
            world[cart.y][cart.x-1] = "<"
    return cart, world, crash


def handleTurn(direction, track):
    if direction == "u":
        if track == "/":
            return "r"
        else:
            return "l"
    elif direction == "l":
        if track == "/":
            return "u"
        else:
            return "d"
    elif direction == "d":
        if track == "/":
            return "l"
        else:
            return "r"
    else:
        if track == "/":
            return "d"
        else:
            return "u"

def sortCarts(carts):
    swapped = True
    while swapped:
        swapped = False
        for each in range(len(carts)-1):
            if carts[each].y > carts[each+1].y:
                temp = carts[each]
                carts[each] = carts[each+1]
                carts[each+1] = temp
                swapped = True

    swapped = True
    while swapped:
        swapped = False
        for each in range(len(carts)-1):
            if carts[each].x > carts[each+1].x:
                temp = carts[each]
                carts[each] = carts[each+1]
                carts[each+1] = temp
                swapped = True
    return carts

if __name__ == "__main__":
    main()