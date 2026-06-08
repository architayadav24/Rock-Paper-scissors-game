import tkinter as tk
import random
#main window
window=tk.Tk()
window.title("R-P-S GAME")
window.geometry("600x600")
window.configure(bg="black")

#scores
user_score=0
comp_score=0
time_left=10

#top Frame score-
top_Frame=tk.Frame(window,bg="")
top_Frame.pack(fill="x",pady=10)

user_label =tk.Label(top_Frame,text="YOU: 0", font=("Arial",14),bg="blue")
user_label.pack(side="left", padx=20)

comp_label =tk.Label(top_Frame,text="COMPUTER: 0", font=("Arial",14),bg="red")
comp_label.pack(side="right", padx=20)


#label
result_label=tk.Label(window,text="Choose Your Move!",font=("Arial",16),bg="pink")
result_label.pack(pady=20)

timer_label=tk.Label(window, text="time:30", font=("Arial", 12))
timer_label.pack()

#symbol Frame-
symbol_Frame=tk.Frame(window, bg="black")
symbol_Frame.pack(pady=10)
#image load
rock_img=tk.PhotoImage(file="first.png")
rock_label=tk.Label(symbol_Frame,image=rock_img,bd=2,width=300,height=300)
rock_label.image=rock_img
rock_label.grid(row=0,column=0,padx=20)

paper_img=tk.PhotoImage(file="third.png")
paper_label=tk.Label(symbol_Frame,image=paper_img,bd=2,width=300,height=300)
paper_label.image=paper_img
paper_label.grid(row=0,column=1,padx=20)

scissors_img=tk.PhotoImage(file="second.png")
scissors_label=tk.Label(symbol_Frame,image=scissors_img,bd=2,width=300,height=300)
scissors_label.image=scissors_img
scissors_label.grid(row=0,column=2,padx=20)

#sound function-
def play_sound():
    window.bell()
#game logic-
def game(user_choice):
    global user_score, comp_score
    if(time_left <=0):
        return
    choices=["Rock","Paper","Scissors"]
    comp_choices = random.choice(choices)
    if(user_choice==comp_choices):
        result="draw!"
        result_label.config(fg="blue")
    elif(user_choice=="Rock" and comp_choices=="Scissors")or\
                              (user_choice=="Scissors" and comp_choices=="Paper")or\
                              (user_choice=="Paper" and comp_choices=="Rock"):
        result="You Win!"
        user_score+=1
        result_label.config(fg="green")
        user_label.config(text=f"YOU: {user_score}") 
    else:
        result="computer wins!"
        comp_score+=1
        result_label.config(fg="red")
        comp_label.config(text=f"COMPUTER:{comp_score}")
    play_sound()
    result_label.config(text=f"YOU:{user_choice}\n\n COMPUTER:{comp_choices}\n\n{result}")
   
   

#BOTTONS-
btn_Frame=tk.Frame(window,bg="black")
btn_Frame.pack(pady=20)

tk.Button(btn_Frame,text="Rock", width=20,command=lambda: game("Rock")).grid(row=0,column=0,padx=20)
tk.Button(btn_Frame,text="Paper", width=20,command=lambda: game("Paper")).grid(row=0,column=1,padx=20)
tk.Button(btn_Frame,text="Scissors", width=20,command=lambda: game("Scissors")).grid(row=0,column=2,padx=20)


#TIMER FUNCTION-
time_left=30
def countdown():
    global time_left
    if(time_left)>0:
        time_left-=1
        timer_label.config(text=f"Time: {time_left}")
        window.after(1000,countdown)
    else:
        if(user_score>comp_score):
            result_label.config(text="Time's Up! Game over.\n you win!",fg="green")
        elif(comp_score>user_score):
            result_label.config(text="Time's Up! Game over.\n computer win!",fg="red")
        else:
            result_label.config(text="Time's Up! Game over.\n match draw!",fg="blue")

                


#start timer
countdown()

#run app
window.mainloop()

        
        
        
