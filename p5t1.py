# CTI 110
# P5 T1 - Simple Graphics
# smiths
# 11/8

def drawTop(width):
    print("#" * width)

def drawSides(width):
    width = width - 2
    print("#" + " " * width + "#")

def drawMiddle(width, height):
    for line in range(height):
        drawSides(width)
                  

def main():
    # program starts here
    print("This program draws a rectangle")
    width = int(input("How wide?"))
    height = int(input("How tall?"))
    # draw the top of the box
    drawTop(width)
    # draw the middle
    drawMiddle(width, height)
    # draw the bottom
    drawTop(width) 



# start program
main()
