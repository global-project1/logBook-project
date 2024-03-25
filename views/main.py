from tkinter import *
import signIn
import admin
import student
import shared_data

# Global variable to store the user info

if __name__ == "__main__":

  signIn.SignIn()
  if shared_data.studInfo:

    if shared_data.studInfo['role_id'] == 1:
      admin.adminHome()
    else:
      student.studentHome()
