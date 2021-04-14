from tkinter import *
import random
import time

window = Tk()
#window.title("Kettlebell Randomizer")
window.geometry("400x400")

def number():
    try:
        int(num.get())
        int(exercise.get())
        int(rest.get())
        answer.configure(text="All Good!")
    except ValueError:
        answer.configure(text="Enter only numbers!")

      

answer=Label(window, font=20)
answer.grid(row=20, column=0)


check=Button(window, text="Check", command=number)
check.grid(row=15, column=0)



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
    res1="Time of exercise " + exercise.get()
    label5.configure(text=res1, font=15)
    res2="Time of Rest " + rest.get()
    label6.configure(text=res2, font=15)

myButton=Button(window, text="Let's go!", padx=40, pady=20, fg="orange", bg="blue", command=click)
myButton.grid(row=6, column=0)

label4=Label(window)
label4.grid(row=7, column=0)

label5=Label(window)
label5.grid(row=8, column=0)

label6=Label(window)
label6.grid(row=9, column=0)




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






label7=Label(text="Your " + num.get() + " exercises are...")
label7.grid(row=10, column=0)
#sampled_list = random.sample(exerciseList, int(num))
#lable8=Label(window, '\n'.join(sampled_list))
#lable8.grid(row=29, column=0)
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