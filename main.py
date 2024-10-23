from turtle import Turtle,Screen
import random
tim=Turtle()
ram=Turtle()
sham=Turtle()
timmy=Turtle()
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
tim.color('red')
ram.color('yellow')
sham.color('green')
timmy.color('blue')
tim.shape('turtle')
sham.shape('turtle')
ram.shape('turtle')
timmy.shape('turtle')
tim.penup()
timmy.penup()
sham.penup()
ram.penup()
tim.goto(-230,80)
timmy.goto(-230,40)
ram.goto(-230,00)
sham.goto(-230,-40)
tim.penup()


print("You lose, ")







screen.exitonclick()