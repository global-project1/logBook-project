import sys
sys.path.append(r'C:\Users\Uzer\Desktop\python\logBook')

from models.students import Students

obj = Students()

def load_students(cond = None):
  if cond is None:
    return obj.read()
  else:
    return obj.read(cond)