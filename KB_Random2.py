from tkinter import *
import random
import time

window = Tk()
#window.title("Kettlebell Randomizer")
window.geometry("400x400")

label1=Label(window, text="Choose number of exercises.")
label1.grid(row=0, column=0)
num=Entry(window, width=35, borderwidth=5)
num.grid(row=1, column=0)
label2=Label(window, text='Choose number of seconds per exercise')
label2.grid(row=2, column=0)
exercise=Entry(window, width=35, borderwidth=5)
exercise.grid(row=3, column=0)
label3=Label(window, text='Choose number of seconds per rest')
label3.grid(row=4, column=0)
rest=Entry(window, width=35, borderwidth=5)
rest.grid(row=5, column=0)

def click():
    res="Number of exercises " + num.get()
    label4.configure(text=res, font=15)

myButton=Button(window, text="Let's go!", padx=40, pady=20, fg="orange", bg="blue", command=click)
myButton.grid(row=6, column=0)

label4=Label(window).grid(row=7, column=0)



exerciseList = ['American Swing',
'Bicep Swings',
'Bob and Weave',
'Bottoms Up Clean'
'Bottoms Up Press',
'Bottom-Up Squat',
'Bridge Leg Spreaders',
'Catcher\'s Squat and Press',
'Clean, Squat and Press',
'Clean',
'Clean and Press',
'Clean and Push Press',
'Clean Ups',
'Curls',
'Deck Squat',
'Double Lunge',
'Farmers Carry',
'Figure 8\'s',
'Goblet Squat',
'Good Morning', 
'Half Get-ups',
'Half Kneeling Press',
'Halo', 
'Hamstring Curls',
'High Pulls',
'Hip Thrust',
'Lateral Swing (Side Swing)',
'Lunge and Press',
'Lunge with Rotation',
'Mason Twist',
'Monkey Grip Pushups',
'One Arm Around',
'One Legged Clean',
'Overhead Press',
'Overhead Reverse Lunge',
'Overhead Squat',
'Overhead Walking Lunge',
'Overhead Warm Up',
'Over the Head',
'Over the Shoulder'
'Pistol Squat',
'Push Press',
'Racked Reverse Lunge',
'Regular Row',
'Renegade Row',
'Side Bends',
'Side Grip Pushups',
'Side Lunge',
'Side Lunge and Clean',
'Side Stepping Swing',
'Single Arm Deadlift', 
'Single Handed Swing', 
'Single Leg Deadlift', 
'Sit and Press',
'Situps',
'Skull Crushers',
'Slingshot (Kettlebell Around the World)', 
'Snatch',
'Squat',
'Static Lunge and Press',
'Straight Arm Sit',
'Suitcase Row Exercise',
'Swing Changing Hands',
'Tactical Lunge',
'Tall Kneeling Press',
'Thruster (Squat and Press)',
'Tricep Extensions'
'Turkish Get Up',
'Turkish Press',
'Two Handed Squat and Press',
'Two Hand Swing', 
'Waiter\'s Squat',
'Windmill',
'Wood Choppers']






#Label("Your " + (num) + " exercises are...").pack()
#sampled_list = random.sample(exerciseList, int(num))
#Label(window, '\n'.join(sampled_list)).grid(row=29, column=0)
#time.sleep(10)

#for x in sampled_list:
#    print(x)
#    for i in range(1, int(exercise)+1):
#        print(i, end=', ')
#        time.sleep(1)
#
#   print("Rest") 
#    for i in range(int(rest), 0, -1):
#        print('Rest time remaining:', i)
#        time.sleep(1)

Label(window, text="Congratulations, Workout Complete!").grid(row=30, column=0)


window.mainloop()