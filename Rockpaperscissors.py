# Rock paper scissors by NielDmello
import random
a=0
b=0
print("Rock paper scissors by ND")
while a<5 and b<5:
    lis=[1,2,3]
    mov=int(input("Press 1 to make a move"))
    if mov==1:
        amov=random.choice(lis)
        bmov=random.choice(lis)
        if amov==1:
          print("A got Rock")
        elif amov==2:
          print("A got Scissor")
        else:
            print("A got Paper")
        if bmov==1:
          print("B got Rock")
        elif bmov==2:
          print("B got Scissor")
        else:
            print("B got Paper")
        if amov==bmov:
            print("It's a Draw")
            print("User A Score=",a)
            print("User B Score=",b)
        elif amov==1 and bmov==2:
            a=a+1
            print("User A Score=",a)
            print("User B Score=",b)
        elif amov==1 and bmov==3:
            b=b+1
            print("User A Score=",a)
            print("User B Score=",b)
        elif amov==2 and bmov==1:
            b=b+1
            print("User A Score=",a)
            print("User B Score=",b)
        elif amov==2 and bmov==3:
            a=a+1
            print("User A Score=",a)
            print("User B Score=",b)
        elif amov==3 and bmov==1:
            a=a+1
            print("User A Score=",a)
            print("User B Score=",b)
        elif amov==3 and bmov==2:
            b=b+1
            print("User A Score=",a)
            print("User B Score=",b)
        else:
            pass
if a>b:
  print("A is winner")
else:
  print("B is winner")
# Rock paper scissors by NielDmello