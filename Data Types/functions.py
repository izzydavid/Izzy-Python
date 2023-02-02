# Functions
def say_hello(): 
  print('helllloooo')

say_hello()

picture = [
  [0,0,0,1,0,0,0], 
  [0,0,1,1,1,0,0], 
  [0,1,1,1,1,1,0], 
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0], 
  [0,0,0,1,0,0,0]
]

# 1 iterate over picture. 
  # if 0 -> print ''
  # if 1 -> print * 
def show_tree(): 
  for row in picture: 
    for pixel in row:
      if (pixel == 1): 
        print('*', end = '')
      else: 
        print(' ', end = '')
    print('')

show_tree()
show_tree()