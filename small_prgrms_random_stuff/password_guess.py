def pss_guess():
    _ = 97
    c0,c1,c2,c3,c4,c5 = 97,97,97,97,97,97
    n0,n1,n2,n3,n4,n5=0,1,2,3,4,5
    psswd = input()
    n12 = len(psswd)-1

    guess = []
    guess = len(psswd)*[chr(_)]
    for i in range(26):
        guess[n0]=chr(c0)
        for k in range(26):
            if c1>122:
                c1=97
            guess[n1]=chr(c1)
            for l in range(26):
                if c2>122:
                    c2=97
                guess[n2]=chr(c2)
                for m in range(26):
                    if c3>122:
                        c3=97
                    guess[n3]=chr(c3)
                    for n in range(26):
                        if c4>122:
                            c4=97
                        guess[n4]=chr(c4)
                        for j in range(26):
                            if _>122:
                                _=97
                            guess[n5] = chr(_)
                            print("".join(guess))
                            if "".join(guess) == psswd:
                                print("".join(guess))
                                print("hello")
                                brake = 1
                                return
                            _+=1
                        c4+=1
                    c3+=1
                c2+=1
            c1+=1
        c0+=1
a=pss_guess()