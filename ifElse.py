# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

n = 4

# solusi 1
# if  n%2 == 0 & n > 20:
#     print("Not Weird")
# elif n%2 == 0 & n >= 2 & n <=5 :
#     print("Not Weird")
# elif n%2 == 0 & n >= 6 & n <=20 :
#     print("Weird")
# else:
#     print("Weird")

# solusi 2
if  (n%2 == 0) and (n > 20 or (n >= 2 and n <=5)):
    print("Not Weird")
else:
    print("Weird")