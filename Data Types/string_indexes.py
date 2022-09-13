#Example of string indexes, where you are asking the computer to graph the first variable of selfish which is "m"

selfish = 'me me me'
# 01234567
print(selfish[0])

selfish = '01234567'
# 01234567
print(selfish[0])

#Start and Stop default is one by one iteration over a number
selfish = '01234567'
# 01234567
# [start:stop]
print(selfish[0:8])

#Stepover can hopover a # of iterations specified
selfish = '01234567'
# 01234567
# [start:stop:stepover]
print(selfish[0:8:2])

#Start at 1 and stop when there is nothing else there.
selfish = '01234567'
# 01234567
# [start:stop:stepover]
print(selfish[1:])

#Start at default 0 and goes to 5.
selfish = '01234567'
# 01234567
#[start:stop]
print(selfish[:5])

#Start at default 0, ends whenever string ends and stepping over it once.
selfish = '01234567'
#01234567
#[start:stop:stepover]
print(selfish[::1])

#Start at the end of the string when using the negative index number.
selfish = '01234567'
#01234567
#[start:stop:stepover]
print(selfish[-2])

#Start and stop and index from the back, which provides the reverse output of the string index.
selfish = '01234567'
#01234567
#[start:stop:stepover]
print(selfish[::-1])  # common method to reverse the order of a string
