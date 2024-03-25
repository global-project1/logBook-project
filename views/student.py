from tkinter import *
import sys
sys.path.append(r'C:\Users\Uzer\Desktop\python\logBook')
import tkinter.messagebox as messageBox
import shared_data


def studentHome():

  def display_info():
    my_list.delete(0, END)
    
    for key in shared_data.studInfo:
      my_list.insert(END,shared_data.studInfo[key])

  root = Tk()
  root.geometry("600x600")

  root.title("IAI logBook")

  root.resizable(False, False)

  studName = shared_data.studInfo['name']
  homeLabel = Label(root, text="IAI Student", font=('Acumin Variable Concept', 18, 'bold'))
  homeLabel.place(relx=0.3, rely=0.1)

  my_list = Listbox(root, height=15, width=60, bg="#fff")
  my_list.place(relx=0.1, rely=0.3)

  display_info()

  root.mainloop()
