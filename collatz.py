# The number we will perform the Collatz operations on. 

n = int(input("enter a number \n"))
# Keep looping until we reach 1.
# Note: this assumes the Collatz conjecture is true.
while n != 1:
  # prent the curretn value of n
  print(n)
  # check if n is event
  if n % 2 == 0: 
    # if n is even, divide it by two
    n = n // 2
  else:
    # if n is odd, multiply by three and add 1. 
    n = int((3 * n) + 1)
# Finally, print 1
print(n)      