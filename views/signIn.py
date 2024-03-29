import sys
import os
sys.path.append(r'C:\Users\Uzer\Desktop\python\logBook')
from tkinter import *
import tkinter.messagebox as messageBox
import controllers.coursectrl as courCT
import controllers.classCT as clsCT
import controllers.stud_ctrl as studCT
from . import shared_data
from PIL import Image, ImageTk
from tkinter import filedialog


# Functions

def SignIn():

  def on_enter(event):
    if nameEntry.get() == 'Enter Full Names':
      nameEntry.delete(0,END)

  def checkValues():
    
    if nameEntry.get() == "" or nameEntry.get() == 'Enter Full Names':
      messageBox.showerror('Name error', "Name entry required")
      return
    elif sel_opt.get() == 'None':
      messageBox.showerror("Class", "Class required")
    else:
      name = nameEntry.get().lower()
      opt = sel_opt.get()

      for op in allOptions:
        if op[1] == opt:
          id = op[0]
          break
      condition =  f"class_id = {id} AND name = '{name}'"
      status, names = studCT.load_students(condition)

      if(status):
        if(names):
          row = names[0]
          keys = ['id', 'name', 'dob', 'gender', 'Tel', 'role_id', 'class_id']

          shared_data.studInfo = {key: value for key, value in zip(keys, row)}
      
          window.destroy()
        else:
          messageBox.showinfo('Error', f"student {name} doesn't exist in {opt}")
      else:
        messageBox.showinfo('Data', names)

          
  # GUI part

  window = Tk()

  window.geometry("500x500")
  window.title("IAI logBook")

  window.resizable(False, False)

  current_dir = os.getcwd()
  
  icon_img = current_dir + '/icon.ico'
  # icon
  window.iconbitmap(icon_img)

  # image
  img_path = current_dir + '/views/Images/tagging photo.png'
  image = Image.open(img_path) 

  img_size = (100, 100)
  image = image.resize(img_size, Image.Resampling.LANCZOS)

  image_tk = ImageTk.PhotoImage(image)

  label = Label(window, image=image_tk)
  label.place(relx=0.4, rely=0.025)

  myFrame = Frame(window, bg="#fff", width="400", height="300")
  myFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

  loginLabel = Label(myFrame, text="Welcome Back", font=('Acumin Variable Concept', 18, 'bold'), bg="#fff")
  loginLabel.place(relx=0.3, rely=0.1)

  nameEntry = Entry(myFrame, width=45, font=('Acumin Variable Concept', 10), bg="#fff", bd=0)
  nameEntry.place(relx=0.1, rely=0.3)
  nameEntry.insert(3, 'Enter Full Names')
  nameEntry.bind('<FocusIn>', on_enter)

  nameFrame = Frame(myFrame, width=320, height=1.5, bg="RoyalBlue1")
  nameFrame.place(relx=0.09, rely=0.38)

  status, allOptions = clsCT.load_classes()

  if(status):
    options = [row[1] for row in allOptions]
  else:
    messageBox.showerror("Error", "Erro loading options")

  sel_opt = StringVar()
  sel_opt.set('None')

  sel_input = OptionMenu(myFrame, sel_opt, *options)
  sel_input.place(relx=0.37, rely=0.5)  

  classLabel = Label(myFrame, text="Choose class:", font=('Acumin Variable Concept', 10), bg="#fff")
  classLabel.place(relx=0.1, rely=0.5)

  loginBtn = Button(myFrame, bg="RoyalBlue1", height=2, width=17, font=('Helvetica', 12, 'bold'), fg="alice blue", text="Login", bd=0, command = checkValues)
  loginBtn.place(relx=0.25, rely=0.7)

  window.mainloop()
