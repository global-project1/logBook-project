import sys
sys.path.append(r'C:\Users\Uzer\Desktop\python\logBook')

from models.classTab import classTab

obj = classTab()

def load_classes():
  return obj.read()