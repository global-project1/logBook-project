
import sys
sys.path.append(r'C:\Users\Uzer\Desktop\python\logBook')

from models.courses import Courses

cour = Courses()

def load_courses():
  return cour.read()
