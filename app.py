import sys
sys.path.append(r'C:\Users\Uzer\Desktop\python\logBook')
import os

from flask import Flask

from tkinter import *
from views import signIn, student, admin, shared_data

if __name__ == "__main__":

  signIn.SignIn()

  if shared_data.studInfo:

    if shared_data.studInfo['role_id'] == 1:
      admin.adminHome()
    else:
      student.studentHome()
