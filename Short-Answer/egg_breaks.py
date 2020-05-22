def egg_breaks(n):  #n = 10 -> n=7

     while n <= 1:
          breaks = False
          middle = n//2  #middle = 5
          f = middle
          #throw egg from middle
          if breaks == False:
               # f is higer than middle
               n = middle + middle//2 
               #n = 5 + (5//2)= 5 + 2

               #So we throw the egg from 7th floor
               egg_breaks(n)


