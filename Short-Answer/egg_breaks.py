def egg_breaks(n):  #n = 10 -> n=7
     middle = n
     f = middle

     while n <= 1:
          breaks = False
          middle = n//2  #middle = 5

          #throw egg from middle
          if breaks == False:
               # f is higer than middle
               n = middle + middle//2 
               #n = 5 + (5//2)= 5 + 2

               #So we throw the egg from 7th floor
               egg_breaks(n)
          else:
               n = middle // 2
               egg_breaks(n)


