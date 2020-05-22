#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)O(n^3) - As the size of the input(n) increases the runtime increases faster.

b)O(n^2)
Two nested loops. uadratic time because for each item in the outer loop we iterate through every item in the inner one. We are accessing n 2 times. n \* n = n^2

c)O(n) In the first part, we are just passing a integer and checking if it's 0. We're not looping through and array for example. But we are returning a call to the same function, recursion, so we have linear time because the function is calling it self n times until it reaches the base case.

## Exercise II

Building with n floors
Eggs get broken if it falls from floor f or higher
Doesn't get broken if it falls from f - 1 and lower

For this exercise I'd propose we throw an egg from n/2 - the floor in the middle of the building. If the egg breaks

middle = n/2
if egg breaks we know that f is somewhere below the current middle floor

So we could discard the half that's greater that middle and update the middle.

the new middle is equal to middle / 2. We throw another egg from that floor which is the result of the new middle.

Suppose the egg doesn't break this time. We know that f is in the greater half.

def egg_breaks(n):
#n number of floors
#f is the floor we know the egg breaks
#everything above f breaks too

     #Base Cases: (while number of floor is above or first)
     #while n >= 0

     #throw egg from middle of building
     middle = n/2

     #if it breaks:
          #f is somewhere below
          #middle is the "total" universe now
          #mark the building in half again
          #middle = middle/2
          #call the function again with n updated -> middle

     #else: (egg doesn't break)
          #f is somewhere above
          #we call the function again with n as m + m/2
