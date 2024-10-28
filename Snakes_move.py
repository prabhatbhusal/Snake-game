
from turtle import Turtle
starting_positions=[(0,0),(-20,0),(-40,0)]
move_distance=20
class Snakes:
    def __init__(self):
        self.snakes=[]
        self.create_snake()
    def create_snake(self):
        
       
        for pos in starting_positions:
            snake=Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(pos)
            self.snakes.append(snake)
    def move(self):
        for seg_num in range(len(self.snakes)-1,0,-1):
            new_x=self.snakes[seg_num-1].xcor()
            new_y=self.snakes[seg_num-1].ycor()
            self.snakes[seg_num].goto(new_x,new_y)
        self.snakes[0].forward(move_distance)
    
