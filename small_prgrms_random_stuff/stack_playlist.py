def enqueue(stack,item):
    stack.append(item)
    print("Song {} added succesfully".format(item))
def dequeue(stack):
    if len(stack)!=0:
        a=stack.pop()     
        print("Enjoy {}  song now ".format(a))
    else:
        print("Oops looks like you need to add more songs 😉")

def nextinqueue(stack):
    if len(stack):
        print(stack[-1])
    else:
        print("Nothing to play next 🎵")

stack=[]
while True:
    row = len("Playlist Options")
    dash=len("|||||||||||| |")
    right=len("| ||||||||||")
    h = ''.join([' '] + [dash* " "] + ['-' *row] + [right*' ']+[' '])
    b=''.join(['|||'] + [(dash-2)* " "] + ['-' *row] + [(right-2)*' ']+['|||'])
    result= h + '\n'"|"+"|||||||||||| |Playlist Options| ||||||||||"+"|"'\n' + b
    result='\033[1m' + result
    print()
    print()
    print(result)
    print("|||                                      |||")
    print("||| Choose one of the following options  |||" )
    print("||| 1. Add song to queue                 |||")
    print("||| 2. Next Song                         |||")
    print("||| 3. Upcoming song                     |||")
    print("||| 4. All songs in queue                |||")
    print("||| 5. To Exit                           |||")
    print("|||                                      |||")
    print("||||||||||||||||||||||||||||||||||||||||||||")
    print()
    print()
    print('\033[1m')
    choice = int(input())
    if choice==1:
        item=input("Enter Song you wants to add : ")
        enqueue(stack,item)
    elif choice == 2:
        dequeue(stack)
    elif choice==3:
        nextinqueue(stack)
    elif choice==4:
        if len(stack):
            for i in stack[::-1]:
                print(i,end=", ")
            print("are all upcoming songs")
        else:
            print("There is no song in playlist")
    elif choice ==5 :
        print("We hope you enjoyed your music")
        break
    else:
        print("Wrong Choice")



