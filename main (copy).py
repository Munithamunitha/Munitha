def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return  n*fact_rec(n-1)
number=int(input("Enter a factorial:")) 
res = fact_rec(number)
print("the factorial of {}.".format(res)) 