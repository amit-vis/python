s1 = stack()
     s2 = stack()

     for ele in s1:
         s1.push(ele)
     reverse(s1, s2)

     while s1.isEmpty() is False:
          print(s1.pop())
