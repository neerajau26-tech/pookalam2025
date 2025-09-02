from turtle import *
import math


# --- Setup ---
speed(0)
bgcolor("black")
title("Full Screen Competition Pookalam ")
screensize(1600,1600)

# Function to draw a petal
def petal(radius, angle, color1):
    color(color1)
    begin_fill()
    circle(radius, angle)
    left(180 - angle)
    circle(radius, angle)
    left(180 - angle)
    end_fill()

# Function to draw a ring of petals
def ring(num_petals, petal_radius, colors):
    for i in range(num_petals):
        petal(petal_radius, 60, colors[i % len(colors)])
        left(360 / num_petals)

# Function to draw circular border
def circular_border(radius, color1, thickness):
    penup()
    goto(0,-radius)
    pendown()
    pensize(thickness)
    color(color1)
    circle(radius)
    pensize(1)
    

        
   


# --- Draw Pookalam ---

circular_border(750, "gold", 12)  # full-screen border


# First Layer
penup()
goto(0,0)
pendown()
ring(12, 160, ["yellow", "orange"])

# Second Layer
penup()
goto(0,0)
pendown()
ring(16, 150, ["green", "red"])

# Third Layer
penup()
goto(0,0)
pendown()
ring(20, 140, ["dark violet", "maroon"])

# Fourth Layer
penup()
goto(0,0)
pendown()
ring(24, 130, ["yellow", "orange"])

# Center Pattern
penup()
goto(0,0)
pendown()
ring(12, 100, ["white", "maroon"])


hideturtle()
done()
