# -*- coding: utf-8 -*-
"""
Created on Tue May  3 12:14:43 2022

@author: HP
"""

from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Working on canvas using functions")
root.geometry("600x600")

color_label=Label(root,text="Enter a color ")
color_label.place(relx=0.6,rely=0.9,anchor=CENTER)

input_box=Entry(root)
input_box.insert(0,"black")
input_box.place(relx=0.8,rely=0.9,anchor=CENTER)

canvas=Canvas(root,width=500,height=510,bg="white",highlightbackground="grey")
canvas.pack()

img=ImageTk.PhotoImage(Image.open("start_point1.png"))
my_img=canvas.create_image(50,50,image=img)

direction=""
old_x=50
old_y=50
new_y=50
new_x=50

def right_dir(event):
    global direction
    global old_x
    global old_y
    global new_x
    global new_y
    old_x=new_x
    old_y=new_y
    new_x=new_x+5
    direction="right"
    draw(direction,old_x,old_y,new_x,new_y)
    
def left_dir(event):
    global direction
    global old_x
    global old_y
    global new_x
    global new_y
    old_x=new_x
    old_y=new_y
    new_x=new_x-5
    direction="left"
    draw(direction,old_x,old_y,new_x,new_y)
    
def up_dir(event):
    global direction
    global old_x
    global old_y
    global new_x
    global new_y
    old_x=new_x
    old_y=new_y
    new_y=new_y-5
    direction="up"
    draw(direction,old_x,old_y,new_x,new_y)    
    
def down_dir(event):
    global direction
    global old_x
    global old_y
    global new_x
    global new_y
    old_x=new_x
    old_y=new_y
    new_y=new_y+5
    direction="down"
    draw(direction,old_x,old_y,new_x,new_y)    
    
def draw(direction,old_x,old_y,new_x,new_y):
    fill_color=input_box.get()
    if(direction=="right"):
        right_line=canvas.create_line(old_x,old_y,new_x,new_y,width=3,fill=fill_color)
    if(direction=="left"):
        left_line=canvas.create_line(old_x,old_y,new_x,new_y,width=3,fill=fill_color)
    if(direction=="up"):
        up_line=canvas.create_line(old_x,old_y,new_x,new_y,width=3,fill=fill_color)
    if(direction=="down"):
        down_line=canvas.create_line(old_x,old_y,new_x,new_y,width=3,fill=fill_color)
        
root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)    

root.mainloop()