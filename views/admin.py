from tkinter import *
import sys
sys.path.append(r'C:\Users\Uzer\Desktop\python\logBook')
import tkinter.messagebox as messageBox
import shared_data
from models import students, classTab, courses, role, class_courses

stud = students.Students()
cour = courses.Courses()

def adminHome():

  def display_info():
    my_list.delete(0, END)
    for key in shared_data.studInfo:
      my_list.insert(END,shared_data.studInfo[key])


  def printIT(param):
    print(param)
  # GUI 
      
  root = Tk()
  root.geometry("600x600")

  root.title("IAI logBook")

  root.resizable(False, False)

  # studName = shared_data.studInfo['name'] + "(Class Delegate)"
  homeLabel = Label(root, text="Class Delegate", font=('Acumin Variable Concept', 18, 'bold'))
  homeLabel.place(relx=0.22, rely=0.05)

  course_label = Label(root, text="Select Course:", font=('Acumin Variable Concept', 10))
  course_label.place(relx=0.07, rely=0.15)

  status, courses = cour.read() 

  if(status):
    options = [row[1] for row in courses]
  else:
    messageBox.showerror("Error", "Erro loading options")

  sel_opt = StringVar()
  sel_opt.set("None")

  option_menu = OptionMenu(root, sel_opt, *options, command=lambda opt=sel_opt: printIT(opt))
  option_menu.place(relx=0.07, rely=0.2)

  my_list = Listbox(root, height=15, width=60, bg="#fff")
  my_list.place(relx=0.1, rely=0.3)

  display_info()

  root.mainloop()

adminHome()