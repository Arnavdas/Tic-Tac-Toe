imp = {}; imp['x'], imp['o'] = set(), set()
def check(c, e):
    if 5 in c: 
        c.remove(5)
        for k in c:
            s = 5-k
            if (5+s) in c:
                if e == 1:
                    return 1
                else:
                    return 2
    else :
        if set(range(1,4)).issubset(c) or set(range(7,10)).issubset(c):
            if e == 1:
                return 1
            else:
                return 2
        elif set(range(1,8,3)).issubset(c) or set(range(3,10,3)).issubset(c):
            if e == 1:
                return 1
            else:
                return 2
    return 0
                
def dic(x = None, y = None, z = None):
    p = 1; s = '|'
    
    if y != None :
        if y == 1:
            imp[z].add(x)
        else:
            imp[z].add(x)
            
    print("") 
    
    while p < 10 :
        for t in range(p, 3+p):
            if t < 2+p:
                if t in imp['x']:
                    print('x',end = ' | ')
                elif t in imp['o']:
                    print('o',end = ' | ')
                else:
                    print(t,end = ' | ')
            else:
                if t in imp['x']:
                    print('x',end = '')
                elif t in imp['o']:
                    print('o',end = '')
                else:
                    print(t,end = '')
        print('')
        print(s.rjust(3,' '), end =' ')
        print(s.rjust(3,' '))
        if p < 7:
            print("----------")
        p+=3
        
    if y != None :
        if y == 1:
            if len(imp[z]) > 2 and check(imp[z].copy(), y) == 1:
                return 1
        else:
            if len(imp[z]) > 2 and check(imp[z].copy(), y) == 2:
                return 2
    
    if len(imp['x']) + len(imp['o']) == 9:
        return 0
    else :
        return -1
        
def game():
    ref = {}; i = -1; j = 1
    print("Enter the character you want to play with ( x or o) : ")
    print('')
    p1 = input()
    print('')
    print('Thus your opponent has the character : ',end='')
    if p1 == 'x':
        print('o')
        p2 = 'o'
    else:
        print('x')
        p2 = 'x'
    print('')
    print('who wants to play the first move (enter 1 if you want to play first else enter 2) : ')
    if int(input()) == 1:
        ref[1] = p1
        ref[2] = p2
    else:
        ref[1] = p2
        ref[2] = p1
    print('')
    dic()
    print('')
    while i < 0:
        if j == 1:
            print(" player 1 enter your number : ")
        else:
            print(' player 2 enter your number : ')
        print('')
        i = dic(int(input()), j , ref[j])
        print('')
        j = j%2 + 1
    if i == 1:
        print('Congrats player 1')
    elif i == 2:
        print('Congrats player 2')
    else :
        print("it's draw")
    
    print('')
    
    print(" wanna play again ?(enter 1 ) else exit( enter 0) : ")
    
    print('')
    
    imp['x'].clear(); imp['o'].clear()
    if int(input()) == 1:
        print('')
        game()
    else :
        print("game finished ")
        return 0
game()
