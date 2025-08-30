def content():
    
    print("Press 1 if you want to print")
    print("Press 2 if you are done")
    print("Press 3 if you want to turn the printer off")
    temp=input()
    return temp


queue=[]
printer=0
while True:
    
    status=content()
    
    if status=="1":
        if printer==0:
            print("Enter your name")
            temp=input()
            print()
            queue.append(temp)
            printer=1
            continue
        else:
            print()
            print("sorry printer is busy")
            print("Enter your name to add yourself to waiting list or press 1 to exit")
            a=input()
            if a=="1":
                continue
            else:
                queue.append(a)
                print()
                print('{}, your number in queue is {}'.format(a,(queue.index(a)+1)))
                print()    
    elif status=="2":
        if len(queue)!=0:
            a=queue.pop(0)
            print("Thank you {} for using the printer".format(a))
            print()
            print()
        else:
            print("Sorry there is nothing to remove")
            print()
        if len(queue)==0:
            printer=0
            continue
        print(queue[0],"your wait is up you can print now")
        print()
    elif status=="3":
        break
    else:
        print("Invalid input")