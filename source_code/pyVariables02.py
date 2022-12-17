# pyVariables02.py
# global variables
# and function(s)

# these are globals
x = y = "fagoto"

def change_instruments():
  global x
  global z

  x = "oboe"
  y = "klarineto"
  z = "piano"
  k = "flaouto"

change_instruments()

print(x)
print(y)
print(z)
# print(k) # error!!!
