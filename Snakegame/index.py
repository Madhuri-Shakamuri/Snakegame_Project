from tkinter import *                    # 1.   It is a  built in module used to create GUI from this statement you can access all the functions to current namespace
import random                                   #used to generate random numbers

GAME_WIDTH=700                           #2.   constants(variables)==uppercase and not intended to change
GAME_HEIGHT=700
SPEED=250                                      #lower the number faster the game
SPACE_SIZE=50
BODY_PARTS=3
SNAKE_COLOR="GREEN"                             #00FF00
FOOD_COLOR="RED"                                #FF0000
BACKGROUND_COLOR="BLACK"                        #000000


class Snake:
    def __init__(self):                         # 9. constructor - by creating an object for this we can easily call and access the class---pic-5  display snake  at left corner
        self.body_size=BODY_PARTS
        self.coordinates=[]                     #list of coordinates
        self.squares=[]                         # list of square graphics

        for i in range(0,BODY_PARTS):           # creating list of coordinates
            self.coordinates.append([0,0])      #snake will be aappear in top left corner
        for x,y in self.coordinates:            # creating square
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
            self.squares.append(square)         # by running this we get snake always at top left corner

class Food:

    def __init__(self):                                              # 8. method used to create food object for us the below lines display food at random places---pic-4
        x=random.randint(0 ,(GAME_WIDTH/SPACE_SIZE)-1)* SPACE_SIZE # TO CREATE FOOD AT RANDOM 0 to 14 positions on x-axis and y-axis and  to make it exclusito -1,and to convert into pixcels * space size(650)
        y=random.randint(0,(GAME_HEIGHT / SPACE_SIZE)-1)*SPACE_SIZE
        self.coordinates=[x,y]                                      # setting coordinates
        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")   #drawing food in canvas
        # by runnig this food appears at random at 650 from width or height
def next_turn(snake,food):
    global direction
    x,y = snake.coordinates[0]                 # 9. snake coordinates will be stored at x,y here we unpacked so in line 56 we packed it

    if direction == "up":
        y -= SPACE_SIZE  # y be the head of the snake and move one space up  as snake head at top left corner initially  down

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE


    snake.coordinates.insert(0, ( x, y))  # upadte snake coordinates  0=head of snake  and x,y are new subcoordianets at new location
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,fill=SNAKE_COLOR)  # new graphic for head of the snake
    snake.squares.insert(0,square)  # update list of square of snake    and then call next_turnin below  and snake is going to move

    if x == food.coordinates[0] and y == food.coordinates[1]:  # here we apcked the coordinates of snake and food      this line smeans both are overlapping
        global score
        score +=1

        label.config(text="Score:{}".format(score))   # changing label by new score

        canvas.delete("food")   #delete our food object

        food=Food()    # creating a new food object
    else:
        del snake.coordinates[-1]             # delete  last body part of snake  at negative index that is last set of coordiantes
        canvas.delete(snake.squares[-1])      # upadating canvas
        del snake.squares[-1]            # after running this we get a moving a snake  with 3 body parts without control of speed
    if check_collisions(snake):               # if  collision occur game over elsewe repeat the else block
         game_over()
    else:
         window.after(SPEED, next_turn, snake, food)  #  calling next_turn without paranthesis

def change_direction(new_direction):
    global direction                # accessing our direction    ====old direction

    if new_direction == 'left' and  direction != 'right':    # the direction we passed as an argument
        direction = new_direction                            # old direction as we dont want to go backwards to turn around 180 degrees
    elif new_direction == 'right' and  direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction   # we have to run and move where we want

def check_collisions(snake):
    x,y= snake.coordinates[0] # unpacking coordinates of snake

    if x < 0 or x >= GAME_WIDTH:     # if ittouches any border of the screen then game over
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for  body_part in snake.coordinates[1:]:   # if snake touches any of its body parts game over
        if x == body_part[0] and y== body_part[1]:
            return True

    return False      # if there are no collisons
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2 ,canvas.winfo_height()/2,font=('consolas',70),text="GAME OVER",fill="red",tag="gameover")   # it makes it center


window=Tk()                                          # 3.  below 3 lines  creates a small window with white background that cannot be changed ----pic-1
window.title("Snake Game")
window.resizable(False,False)                              # window size cannot be changed

score=0                                                # 4.  initial  score and direction
direction='down'

label=Label(window,text="Score:{}".format(score),font=('consolas',40))                      # 5.  just a score label inserted into window
label.pack()                                                                                #  creates a score label   ----pic-2

canvas=Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)               # score label with background black and sized  ----pic-3---game board
canvas.pack()                                                                               # used to pack all the parameters

window.update()     #normal updating the window                                             # 6. center the window label by below steps

window_width=window.winfo_width()                                                            # to  make it center merging window and screen
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width/2)-(window_width/2))                                                   # screen size after removing window size
y=int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")                                 # setting window geometry here we use f string
                                                                                           # upto this alligning the window block  to the ceter..full width and height


window.bind('<Left>',lambda event: change_direction('left'))
window.bind('<Right>',lambda event: change_direction('right'))
window.bind('<Up>',lambda event: change_direction('up'))
window.bind('<Down>',lambda event: change_direction('down'))

snake=Snake()                                                                                # 7. creating snake and food object  by calling Snake  and food constructor
food=Food()

next_turn(snake,food)

window.mainloop()