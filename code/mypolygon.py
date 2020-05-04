import turtle

bob = turtle.Turtle()
print(bob)

for i in range(4):

    # move forward, a distance in pixel
    bob.fd(100)
    # left turn, an angle in degree
    bob.lt(90)

turtle.mainloop()