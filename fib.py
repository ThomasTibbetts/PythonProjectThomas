import turtle
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(10)
prevNum = 0
currentNum = 1
nextNum = prevNum + currentNum
number_of_terms = 15
myTurtle.color('red')
while True:

    print(currentNum)
    for f in range(currentNum - prevNum):
        myTurtle.right(360/currentNum)
        myTurtle.forward(10)

    nextNum = prevNum + currentNum
    prevNum = currentNum
    currentNum = nextNum

    
    
