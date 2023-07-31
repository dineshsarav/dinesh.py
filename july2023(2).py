## let x be some number
x = int(input("Enter the number :"))

def fibonacci_seq(x):
 fibonacci=[0,1]

 for i in range(2,x):
  fnew = fibonacci[-1] + fibonacci[-2]
  fibonacci.append(fnew)
 return fibonacci

if x >= 0:
 print("Fibonacci sequence : ",fibonacci_seq(x))
else:
 print("Negative number cannot be input Please enter positive number ")
