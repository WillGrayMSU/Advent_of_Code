from __future__ import print_function
from readInput import readInput
from cart import Cart

def main():
    world = readInput("input.txt")
    carts = []
    for j in world:
        for i in j:
            if i == (">" | "v" | "^" | "<"):
                if i == ">":
                    carts.append(Cart(i,j,"r", "-"))
                elif i == "<":
                    carts.append(Cart(i,j,"l", "-"))
                elif i == "^":
                    carts.append(Cart(i, j, "u", "|"))
                else:
                    carts.append(Cart(i, j, "d", "|"))

    crash = False
    while not crash:
        for cart in carts:
            cart = moveCart(cart, world)


def moveCart(cart, world):
    crash = False
    if cart.direction == "u":
        if world[cart.y+1][cart.x] == ("|" | "+"):
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x, cart.y+1, world[cart.y+1][cart.x])
            world[cart.y+1][cart.x] = "^"
        elif world[cart.y+1][cart.x] == (">" | "v" | "^" | "<"):
            crash = True
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x, cart.y+1, world[cart.y+1][cart.x])
            world[cart.y+1][cart.x] = "X"
        else:
            world[cart.y][cart.x] = cart.currentTrack
            cart.move(cart.x, cart.y+1, world[cart.y+1][cart.x], )
            world[cart.y+1][cart.x] = "^"

def handleTurn(direction, track):
    if direction == "u":
        if track == "/":
            return "r"
        else:
            return "l"

##def shouldCartOrderUpdate(cartA, cartB):



if __name__ == "__main__":
    main()