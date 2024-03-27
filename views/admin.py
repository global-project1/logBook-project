from tkinter import *
import os
import sys
sys.path.append(r'C:\Users\Uzer\Desktop\python\logBook')
import tkinter.messagebox as messageBox
import shared_data
from models import students, classTab, courses, role, class_courses
import ttkbootstrap as tb

stud = students.Students()
cour = courses.Courses()

def adminHome():

  def display_info(sub):

    myFrame = Frame(root, bg="white", width="400", height="400")
    myFrame.grid(row=4, column=0, columnspan=10)

    # Date entry
    # cur_date = tb.DateEntry(myFrame, bootstyle="RoyalBlue1")
    # cur_date.grid(row=5, column=2, columnspan=5)
    
    title = Label(myFrame, text = sub, font=('Acumin Variable Concept', 12, 'bold'), bg="white")
    title.grid(row=1, column=2, columnspan=4)

    btn = Button(myFrame, text="Add Record")
    btn.grid(row=6, column=4)
    

  # GUI 
      
  root = Tk()
  root.geometry("700x700")
  root.title("IAI logBook")
  root.resizable(False, False)

  current_dir = os.getcwd()
  
  # icon
  icon_img = current_dir + '/icon.ico'
  root.iconbitmap(icon_img)

  # studName = shared_data.studInfo['name'] + "(Class Delegate)"
  homeLabel = Label(root, text="Class Delegate", font=('Acumin Variable Concept', 18, 'bold'))
  homeLabel.place(relx=0.22, rely=0.05)

  course_label = Label(root, text="Select Course:", font=('Acumin Variable Concept', 10))
  course_label.place(relx=0.07, rely=0.15)

  status, courses = cour.read() 

  if(status):
    options = [row[1] for row in courses]
  else:
    messageBox.showerror("Error", "Error loading options")

  sel_opt = StringVar()
  sel_opt.set("None")
  option_menu = OptionMenu(root, sel_opt, *options, command=lambda opt=sel_opt: display_info(opt))
  option_menu.place(relx=0.07, rely=0.2)



  root.mainloop()

adminHome()