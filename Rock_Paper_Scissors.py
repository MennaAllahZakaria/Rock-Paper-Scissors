from tkinter import *
from PIL import Image,ImageTk
from random import randint
root =Tk()
root.title=("Rock Paper Scissors")
root.configure(background="#9b56b9")

choices=['rock','paper','scissor']

rock_img=ImageTk.PhotoImage(Image.open("images//rock.png"))
paper_img=ImageTk.PhotoImage(Image.open("images//paper.png"))
scissors_img=ImageTk.PhotoImage(Image.open("images//scissors.png"))
help_img=ImageTk.PhotoImage(Image.open("images//Rock - Paper - Scissors _ With Restaurant Napkins!.jpeg"))

#-----------------------------------------------------
user_lab= Label(root,image=scissors_img,bg="#9b56b9")
user_lab.grid(row=1,column=4)
comp_lab= Label(root,image=scissors_img,bg="#9b56b9")
comp_lab.grid(row=1,column=0)
help_lab= Label(root,image=help_img,bg="#9b56b9")
help_lab.grid(row=1,column=6)


#-----------------------------------------------------
def updateImageUser(x):
    if x==choices[0]:
        user_lab.configure(image=rock_img)
    elif x==choices[1]:
        user_lab.configure(image=paper_img)
    else:
        user_lab.configure(image=scissors_img)
    
    com=choices[randint(0,2)]
    if com=='rock':
        comp_lab.configure(image=rock_img)
    elif com=='paper':
        comp_lab.configure(image=paper_img)
    else:
        comp_lab.configure(image=scissors_img)
        
    winner(x,com)
#-----------------------------------------------------

def updateScoreplayer():
    playerScore['text']= str(int(playerScore["text"])+1)
    
def updateScoreComputer():
    compScore['text']= str(int(compScore["text"])+1)

def updatemsg(x):
    msg=Label(root,font=70,bg="#9b59b6",fg="white",text=' ').grid(row=3,column=2)
        
    if x==0:
        msg=Label(root,font=70,bg="#9b59b6",fg="white",text='TIE').grid(row=3,column=2)
        del(msg)
    elif x==1:
        msg=Label(root,font=70,bg="#9b59b6",fg="white",text='YOU LOSS :(').grid(row=3,column=2)
        del(msg)
    else:
        msg=Label(root,font=70,bg="#9b59b6",fg="white",text='YOU WIN :)').grid(row=3,column=2)
        del(msg)
    
    
#-----------------------------------------------------
def winner(player,computer):
    if player==computer:
        updatemsg(0)
    elif player=='rock' and computer=='paper':
        updateScoreComputer()
        updatemsg(1)
    elif player=='rock' and computer=='scissor':
        updateScoreplayer()
        updatemsg(2)
    elif player=='paper' and computer=='rock':
        updateScoreplayer()
        updatemsg(2)
    elif player=='paper' and computer=='scissor':
        updateScoreComputer()
        updatemsg(1)
    elif player=='scissor' and computer=='rock':
        updateScoreComputer()
        updatemsg(1)
    elif player=='scissor' and computer=='paper':
        updateScoreplayer()
        updatemsg(2)
    
        


#-----------------------------------------------------
playerScore=Label(root,text=0,font=100,bg="#9b56b9",fg="white")
playerScore.grid(row=1,column=3)
compScore=Label(root,text=0,font=100,bg="#9b56b9",fg="white")
compScore.grid(row=1,column=1)

#-----------------------------------------------------
rockButton = Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command=lambda:updateImageUser("rock")).grid(row=2,column=1)
peperButton=Button(root,width=20,height=2,text="PEPER",bg="#FAD02E",fg="white",command=lambda:updateImageUser("paper")).grid(row=2,column=2)
scissorsButton=Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command=lambda:updateImageUser("scissor")).grid(row=2,column=3)

#-----------------------------------------------------
user_ind=Label(root,text="USER",font=70,bg="#9b56b9",fg="white").grid(row=0,column=3)
comp_ind=Label(root,text="COMPUTER",font=70,bg="#9b56b9",fg="white").grid(row=0,column=1)
#-----------------------------------------------------

msg=Label(root,font=70,bg="#9b59b6",fg="white",text=' ').grid(row=3,column=2)


root.mainloop() 