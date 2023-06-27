n = int(input("Números Gerados : "))
c = 0
c1 = 1
c2 = 1
c3 = 2
l = [c1,c2,c3]
c1 = l[-1]
c2 = l[-2]
'''c = 0
c1 = 0
c2 = 0
c3 = 1
while c < n:
     c = c + 1
     c2 = c1 + c3
     c3 = c2 + c1
     c1 = c2 + c3
     print(c2, "-> ", c3," -> ", c1,end=" -> " if c <+ n else " --- FIM!!!  ")'''
while c<n-3:
     c = c + 1
     c1 = l[-1]
     c2 = l[-2]
     l.append(c2+c1)
print(l)

confirm = 0
while confirm != "n":
 confirm = input("Continuar[s/n] : ")
 if confirm.lower().strip() == "s":
          for números in range(0,n):

               c1 = l[-1]
               c2 = l[-2]
               l.append(c2 + c1)
 print(l)

























