lis1=[' ']*3
lis2=[' ']*3
lis3=[' ']*3
def main():
    l=input("enter length of board")
    w=input("enter width of board")
    i=1
    list1=[]
    for i in range(0,int(l)):
        print_horiz_line(int(w))
        print_vert_line(int(w))
    print_horiz_line(int(w))

    for j in range(0,int(l)*+2):

        while True:
            try:
                if(lis1.count("x")==3):
                    print("Congratualtions,player 1 won")
                    break
                if(lis1.count("o")==3):
                    print("Congratulations,player 2 won")
                    break
                else:
                    st=input("enter player 1 position")
                    if not st in list1:
                      list1.append(st)

                      call(st,l,w,"x")

                      break
                    else:
                       print("This position already filled")
                       continue
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
        while True:
            try:
                if (lis1.count("x") == 3):
                    print("Congratualtions,player 1 won")
                    break
                if (lis1.count("o") == 3):
                    print("Congratulations,player 2 won")
                    break
                else:
                    if(j==4):
                        print("no more positions available")
                        break
                    st2=input("enter player 2 position")
                    if not st2 in list1:
                      list1.append(st2)

                      call(st2, l, w,"o")
                      break
                    else:
                      print('This position already filled')
                      continue
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue


def print_horiz_line(b):
    for i in range(1,b*3+1):
        if(i%3==1):
            print(" ",end="")
        print("-",end="")
    print("\n")
def print_vert_line(b):
    for i in range(1,b*4):
        if(i%3==1):
            print("|",end="")
        print(" ",end="")
    print("\n")

def dis(l,w):

    for i in range(1,int(l)+1):
        print_horiz_line(int(w))
        print_vert(i,int(w))
    print_horiz_line(int(w))

def print_vert(a,b):
    p=0
    for i in range(1,b*4):
        if(i%3==1):
            print("|",end="")
        if (i % 3 == 0):
            if(a==1):
                print(lis1[p],end="")
                p=p+1
            if (a == 2):
                print(lis2[p], end="")
                p = p + 1
            if (a == 3):
                print(lis3[p], end="")
                p = p + 1
        else:
           print(" ",end="")
    print("\n")
def call(list,l,w,name):
        a,b=list.split(",")
        if(int(a)==1):
            lis1.insert(int(b)-1,name)
        if(int(a)==2):
            lis2.insert(int(b)-1,name)
        if(int(a)==3):
            lis3.insert(int(b)-1,name)
        dis(l, w)


if __name__ == '__main__':
    main()

