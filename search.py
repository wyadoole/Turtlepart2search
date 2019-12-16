import turtle as turtle # imports library as turtle
from random import randint # imports random interger from random library
from time import sleep # imports sleep from time library


def draw_bag(): # draws the bag
  bag = turtle.Turtle() # Draws turtle
  bag.pen(pencolor='brown', pensize=5) # gets oen color and size
  bag.penup()# pen to draw is up -> not able to draw
  bag.goto(-35, 35) # got to position for x and y for start postion
  bag.pendown() # pen to draw is down -> able to draw
  bag.right(90) # turtle right and angle 90
  bag.forward(70) # forward direction and angle 70
  bag.left(90) # left direction and angle 90
  bag.forward(70) # direction forward  and angle 70
  bag.left(90)# left direction and angle 90
  bag.forward(70)# direction forward  and angle 70
  bag.left(90)# left direction and angle 90
  bag.forward(70)# direction forward  and angle 70
  bag.hideturtle() # hides turtle at draw of bag


# draws draw grid -> floor random x and random y
def draw_grid(floor, rand_x, rand_y): # takes in floor and random x & random y
  obj_size = 5 # takes in the size of grid

  grid= turtle.Turtle() # gets location of turtle for grid
  grid.pen(pencolor='black', pensize=3) # gets pen color and size
  grid.penup()# pen up -> not drawing

  grid.goto(-35, 35)# location to start drawing at start

  for i in range(len(floor)): # draws the horizontal portion of the grid
    grid.penup() # pen is up not able to draw
    grid.goto(-35, 35 - 7*i) # location to start drawing horizontal
    grid.pendown() # pen is down able to draw
    grid.forward(70) # direction across to draw

  grid.penup()# pen up not able to draw
  grid.goto(-35, 35)# reset to starting position
  grid.right(90) # direction right and angle 90

  for i in range(len(floor[0])):# for in range for vertical portion of grid
    grid.penup()# pen up not able to draw to grid
    grid.goto(-35 + 7*i, 35) # reposition at location for nect row
    grid.pendown()# pen down able to draw grid
    grid.forward(70)# pen draws forward across vetical

  grid.penup() # penup not able to draw grid
  grid.pencolor('blue') # sets the pen color of the pen

  grid.goto(-35 + 7*rand_x + (7/2 + obj_size/2), 35 - 7*rand_y - (7/2-obj_size/2)) # sets the random location of target to search for
# draws the box that draws to be searched for linear and binary search

  grid.pendown()# pen down to draw
  grid.fillcolor('blue') # fills the color of the object as blue
  grid.begin_fill()# begins fills the square
  for i in range(4):# checks the range that it fills a square
    grid.forward(obj_size)# draws the object the will be used to search for
    grid.left(-90) # angle at where to draw from to form
  grid.end_fill()# ends fill of sqaure
  grid.hideturtle() # hides turtle and show but as a square or box on the grid


# function for linear search
def linear_search(floor):# takes in floor to search from
  searcher = turtle.Turtle()# searcher called to find the box on the grid
  searcher.pen(pencolor='red', pensize=3)# the line that is searching color as red

  searcher.penup() # pen is up not able to draw the visual for searching for the box
  searcher.goto(-35 + 7/2, 35 - 7/2)# location where the search starts from at the top left hand corner

  searcher.pendown() # pen is able to draw the line that searchs through line by line

  x, y, = 0, 0 # start location for search to begin
  obj_found = False# if false keep searching with linear search

  while not obj_found and y < len(floor):# while object is not found keep searching for y location for binary
    while not obj_found and x < len(floor[0])-1:# while object is not found keep searching once y location has been found then check x position
      searcher.goto(-35 + 7*x + (7/2), 35 - 7*y - 7/2)# searcher goes to location of start to continue
      if floor[y][x] == 1:# checks location to be the one that hold the box location
        obj_found = True# if true stops search
      x = x + 1# # checks x and x of box to see if it matches
    if not obj_found:# if not keep checking until found
      y = y + 1# checks y to see if it matches
      x = 0# disregards x since it is only looking for y
      searcher.goto(-35 + 7/2, 35 - 7*y - (7/2))# if not found restart from top of grid in left hand corner


# function that does the Binary Seach
def binary_search(floor, x_coord, y_coord):# takes in floor, x cordantes and y coordinates
  searcher = turtle.Turtle() #Tells the searcher(turtle) to search until the box is found
  searcher.pen(pencolor='red', pensize=3)# searcher color set as red and size
  searcher.penup()# pen up can't draw
  searcher.goto(-35 + 7/2, 35 - 7/2)# reset for the searcher to search from

  guess = 0 # guess inizalized to zero
  low, high = 0, len(floor)-1 # checks low and high of the grid
  obj_found = False # object still not found -> false keep looking

  searcher.pendown() # pen down -> search starts for the searcher

  while obj_found != True:# while the object is not fine
    guess = int((high + low)/2) # to get the location of the new guess
    searcher.goto(-35 + 7/2, 35 - 7*guess - 7/2) # go to next line after searching the previus to reset on the next line
    print ("Guess: " + str(guess) + ", Coord: " + str(y_coord)) # prints the Guess and Coord if opject is foun =d
    if guess == y_coord:# check the y coordinates frist
      obj_found = True# if found prints out found
      print("Found") # prints found but no location
    if guess < y_coord:# checks the y coordinates
      low = guess + 1 # checks low guess that is y
    if guess > y_coord: # checks the y coordinates
      high = guess - 1 # checks the high which is y

  turtle_y = guess # guess for y cords for turtle to find

  guess = 0 # sets the guess to 0 at the start of the application
  low, high = 0, len(floor[0]) - 1 # checsk high and low of the grid/floor
  obj_found = False # and sets the boolean to false so that the application does not exit

  while obj_found != True: # while the object is not fine
    guess = int((high + low)/2) # to get the location of the new guess
    searcher.goto(-35 + 7*guess + 7/2, 35 - 7*turtle_y - 7/2)# go to next line after searching the previus to reset on the next line
    print ("Guess: " + str(guess) + ", Coord: " + str(y_coord)) # prints the Guess and Coord if opject is foun =d
    if guess == x_coord: # check the x coordinates frist
      obj_found = True # if found prints out found
      print("Found") # prints found but not the actual location
    if guess < x_coord: # check the x cordinates frist
      low = guess + 1 # checks the x coordinates
    if guess > x_coord: # checks the x coordinates
      high = guess - 1 # checks the high which is x


# random search -> takes the longest to get a result
def random_search(x_coord, y_coord): # takes in peramaters as x and y coordinates
  is_object_found_using_random_search = False # sets the object found to false so that is can search
  while is_object_found_using_random_search == False: # runs while loop to search for location of random col and row
    rand_col = randint(0, len(floor[0]) - 1) # gets the ramdom row for and to see of that is the answer
    rand_row = randint(0, len(floor) - 1) # gets the random col to search for and to see if that is the answer
    print("")# prints a blank space for readablity
    print("**** START NEW GUESS ****")# prints out start of new guess
    print("-----------") # brake for reablity
    print("-----------")# brake for reability
    print("Random Col=", rand_col)# prints the random col as guess
    print("Random Row=", rand_row)# prints Random row as guess
    print("-----------") # brake for reablity
    print("-----------") # brake for reablity
    if rand_row == x_coord & rand_col == y_coord: # if found prints the location of where it was found
      print("-----------") # brake for reablity
      print("Found Object at:") # prints the location
      print("-----------") # brake for reablity
      is_object_found_using_random_search = True
    else:
      print("Did not find object at:")# prints location not where object is keep searching
      print("-----------")# brake for reablity
      is_object_found_using_random_search = False # keep searching until found -> goes back to the beginning of loop for the search
    print("Object Loc for x:", x_coord)# location for x exist the loop and quits
    print("Object Loc for y:", y_coord) # Location for y exist the loop and quits


# creates the grid 1-100
if __name__ == "__main__":
  floor = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#1--10
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#11-20
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#21-30
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#31-40
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#41-50
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#51-60
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#61-70
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#71-80
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#81-90
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]#91-100
           ]

  rand_col = randint(0, len(floor[0])-1) # gets the random loction for column
  rand_row = randint(0, len(floor)-1) # gets the random location for row

  floor[rand_row][rand_col] = 1 # gets the random loction for the box to spawn/drawn at

  print(floor) #prints the grid

  turtle.setworldcoordinates(-70.,-70.,70.,70.) # gets the worls corfanites for the grid

  #draw_bag()
  print("The application has 3 search function 1) linear, 2) binary and 3) random search along side using the turtle library which draws the graphics")
  draw_grid(floor, rand_col, rand_row) #draws grid
  linear_search(floor) #calls linear search function
  sleep(5) # creates a delay until called next
  turtle.clearscreen() #clears the screen before function runs
  #draw_bag()
  draw_grid(floor, rand_col, rand_row)#draws new grid for binary search
  binary_search(floor, rand_col, rand_row) # runs binary search
  random_search(rand_col, rand_row) # runs random search

  turtle.mainloop() # runs mainloop of application