import function as fn
import time

def findminima(eqn,divisions=2000,times=10,showsteps=1):
    start=time.time()
    divisions+=1
    j=0
    s=0
    minx=0
    prec=0
    while j<times:
        if showsteps or showsteps==2:
            print('No.',j)
        miny=float(fn.solve(eqn,s,0))
        minx=s
        i=1
        while i<divisions:
            x=((i/divisions)*2-1)
            x=(x/(1-abs(x)))
            x/=(2**prec)
            x+=s
            y=float(fn.solve(eqn,x,0))
            if y<miny:
                miny=y
                minx=x
            if showsteps==1:
                print('\tAt ',x,'\tf(x)=',y)
            i+=1
        if showsteps or showsteps==2:
            print('\t=>Min at x=',minx,'\tf(x)=',miny)
        if s==minx:
            prec+=1
        s=minx
        j+=1
    if showsteps==1 or showsteps==2:
        print('time taken=',time.time()-start)
    return minx
    
def findmaxima(eqn,divisions=2000,times=10,showsteps=1):
    start=time.time()
    divisions+=1
    j=0
    s=0
    maxx=0
    prec=0
    while j<times:
        if showsteps or showsteps==2:
            print('No.',j)
        maxy=float(fn.solve(eqn,s,0))
        maxx=s
        i=1
        while i<divisions:
            x=((i/divisions)*2-1)
            x=(x/(1-abs(x)))
            x/=(2**prec)
            x+=s
            y=float(fn.solve(eqn,x,0))
            if y>maxy:
                maxy=y
                maxx=x
            if showsteps==1:
                print('\tAt ',x,'\tf(x)=',y)
            i+=1
        if showsteps or showsteps==2:
            print('\t=>Max at x=',maxx,'\tf(x)=',maxy)
        if s==maxx:
            prec+=1
        s=maxx
        j+=1
    if showsteps==1 or showsteps==2:
        print('time taken=',time.time()-start)
    return maxx       

def evalfindminima(eqn,divisions=2000,times=10,showsteps=1):
    start=time.time()
    divisions+=1
    j=0
    s=0
    minx=0
    prec=0
    while j<times:
        if showsteps or showsteps==2:
            print('No.',j)
        miny=float(fn.solve(eqn,s,0))
        minx=s
        i=1
        while i<divisions:
            x=((i/divisions)*2-1)
            x=(x/(1-abs(x)))
            x/=(2**prec)
            x+=s
            y=float(eval(eqn.replace('x',str(x)).replace('^','**')))
            if y<miny:
                miny=y
                minx=x
            if showsteps==1:
                print('\tAt ',x,'\tf(x)=',y)
            i+=1
        if showsteps or showsteps==2:
            print('\t=>Min at x=',minx,'\tf(x)=',miny)
        if s==minx:
            prec+=1
        s=minx
        j+=1
    if showsteps==1 or showsteps==2:
        print('time taken=',time.time()-start)
    return minx
#print(findminima('(x-2)*(x-1)*(x+1)*(x+3)',3,25,1))
#print(findmaxima('-1*x^2+3*x+3',5,2,1))



    