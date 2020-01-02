def solve(eqn='',val=1,showsteps=1):    
    while eqn.find('(')!=-1:
        
        i=0
        flag=0        
        while i<len(eqn):
            if eqn[i:i+1]=='(':
                flag=i
            if eqn[i:i+1]==')':
                eqn=eqn[0:flag]+solve(eqn[flag+1:i],val,showsteps)+eqn[i+1:len(eqn)]
                
                break
            i+=1
    while True:        
        sp=1
        flag=0
        while eqn.find('+',sp)!=-1:            
            if eqn[eqn.find('+',sp)-1:eqn.find('+',sp)]!='e':
                flag=1
                break
            else:
                sp+=1
                
        sm=1
        while eqn.find('-',sm)!=-1:            
            if eqn[eqn.find('-',sm)-1:eqn.find('-',sm)]!='e':
                flag=1
                break
            else:
                sm+=1
        if eqn.find('*')!=-1 or eqn.find('/')!=-1 or eqn.find('^')!=-1:
            flag=1
        if flag==0:
            break
        seqn=eqn
        i=0        
        a=0
        b=0
        o=0
        if eqn.find('^')!=-1:
            o=eqn.find('^')
            i=o+2
            while (eqn[i:i+1]!='+'or eqn[i-1:i]=='e') and (eqn[i:i+1]!='-' or eqn[i-1:i]=='e') and eqn[i:i+1]!='*' and eqn[i:i+1]!='/' and eqn[i:i+1]!='^' and i<len(eqn):
                i+=1
            
            if eqn[o+1:i]=='x':
                b=val
            else:
                b=float(eqn[o+1:i])
            j=i
            i=o-1
            while (eqn[i:i+1]!='+'or eqn[i-1:i]=='e') and (eqn[i:i+1]!='-' or i<1 or eqn[i-1:i]=='e' or eqn[i-1:i]=='*' or eqn[i-1:i]=='/' or eqn[i-1:i]=='+' or eqn[i-1:i]=='^') and eqn[i:i+1]!='*' and eqn[i:i+1]!='/' and eqn[i:i+1]!='^' and i>-1:
                i-=1
            
            if eqn[i+1:o]=='x':
                a=val
            else:
                a=float(eqn[i+1:o])
            try:
                result=a**b
            except:
                result=float('inf')
            eqn=eqn[0:i+1]+str(result)+eqn[j:len(eqn)]
            if showsteps:
                print(seqn,'=',eqn)
            continue
        if eqn.find('/')!=-1:
            o=eqn.find('/')
            i=o+2
            while (eqn[i:i+1]!='+'or eqn[i-1:i]=='e') and (eqn[i:i+1]!='-' or eqn[i-1:i]=='e') and eqn[i:i+1]!='*' and eqn[i:i+1]!='/' and eqn[i:i+1]!='^' and i<len(eqn):
                i+=1
            
            if eqn[o+1:i]=='x':
                b=val
            else:
                b=float(eqn[o+1:i])
            j=i
            i=o-1
            while (eqn[i:i+1]!='+'or eqn[i-1:i]=='e') and (eqn[i:i+1]!='-' or i<1 or eqn[i-1:i]=='e' or eqn[i-1:i]=='*' or eqn[i-1:i]=='/' or eqn[i-1:i]=='+' or eqn[i-1:i]=='^') and eqn[i:i+1]!='*' and eqn[i:i+1]!='/' and eqn[i:i+1]!='^' and i>-1:
                i-=1
            
            if eqn[i+1:o]=='x':
                a=val
            else:
                a=float(eqn[i+1:o])
            if b!=0:
                eqn=eqn[0:i+1]+str((a/b))+eqn[j:len(eqn)]
            else:
                if a<0:
                    eqn=eqn[0:i+1]+str(float('-inf'))+eqn[j:len(eqn)]
                else:
                    eqn=eqn[0:i+1]+str(float('inf'))+eqn[j:len(eqn)]
            if showsteps:
                print(seqn,'=',eqn)
            continue
        if eqn.find('*')!=-1:
            o=eqn.find('*')
            i=o+2
            while (eqn[i:i+1]!='+'or eqn[i-1:i]=='e') and (eqn[i:i+1]!='-' or eqn[i-1:i]=='e') and eqn[i:i+1]!='*' and eqn[i:i+1]!='/' and eqn[i:i+1]!='^' and i<len(eqn):
                i+=1
            
            if eqn[o+1:i]=='x':
                b=val
            else:
                b=float(eqn[o+1:i])
            j=i
            i=o-1
            while (eqn[i:i+1]!='+'or eqn[i-1:i]=='e') and (eqn[i:i+1]!='-' or i<1 or eqn[i-1:i]=='e' or eqn[i-1:i]=='*' or eqn[i-1:i]=='/' or eqn[i-1:i]=='+' or eqn[i-1:i]=='^') and eqn[i:i+1]!='*' and eqn[i:i+1]!='/' and eqn[i:i+1]!='^' and i>-1:
                i-=1
            
            if eqn[i+1:o]=='x':
                a=val
            else:
                a=float(eqn[i+1:o])
            
            eqn=eqn[0:i+1]+str((a*b))+eqn[j:len(eqn)]
            if showsteps:
                print(seqn,'=',eqn)
            continue
        if eqn.find('+',sp)!=-1 and eqn[eqn.find('+',sp)-1:eqn.find('+',sp)]!='e':
            s=1
            while eqn.find('+',s)!=-1:
                if eqn[eqn.find('+',s)-1:eqn.find('+',s)]!='e':
                    o=eqn.find('+',s)
                    break
                else:
                    s+=1
            i=o+2
            while (eqn[i:i+1]!='+'or eqn[i-1:i]=='e')and (eqn[i:i+1]!='-' or eqn[i-1:i]=='e') and eqn[i:i+1]!='*' and eqn[i:i+1]!='/' and eqn[i:i+1]!='^' and i<len(eqn):
                i+=1
            
            if eqn[o+1:i]=='x':
                b=val
            else:
                b=float(eqn[o+1:i])
            j=i
            i=o-1
            while (eqn[i:i+1]!='+'or eqn[i-1:i]=='e') and (eqn[i:i+1]!='-' or i<1 or eqn[i-1:i]=='e' or eqn[i-1:i]=='*' or eqn[i-1:i]=='/' or eqn[i-1:i]=='+' or eqn[i-1:i]=='^') and eqn[i:i+1]!='*' and eqn[i:i+1]!='/' and eqn[i:i+1]!='^' and i>-1:
                i-=1
            
            if eqn[i+1:o]=='x':
                a=val
            else:
                a=float(eqn[i+1:o])
            
            eqn=eqn[0:i+1]+str((a+b))+eqn[j:len(eqn)]
            if showsteps:                
                print(seqn,'=',eqn)
            continue
        if eqn.find('-',sm)!=-1 :
            s=1
            while eqn.find('-',s)!=-1:
                if eqn[eqn.find('-',s)-1:eqn.find('-',s)]!='e':
                    o=eqn.find('-',s)
                    break
                else:
                    s+=1
            i=o+2
            while (eqn[i:i+1]!='+'or eqn[i-1:i]=='e') and (eqn[i:i+1]!='-'or eqn[i-1:i]=='e') and eqn[i:i+1]!='*' and eqn[i:i+1]!='/' and eqn[i:i+1]!='^' and i<len(eqn):
                i+=1
            
            if eqn[o+1:i]=='x':
                b=val
            else:
                b=float(eqn[o+1:i])
            j=i
            i=o-1
            while (eqn[i:i+1]!='+'or eqn[i-1:i]=='e') and (eqn[i:i+1]!='-' or i<1 or eqn[i-1:i]=='e' or eqn[i-1:i]=='*' or eqn[i-1:i]=='/' or eqn[i-1:i]=='+' or eqn[i-1:i]=='^') and eqn[i:i+1]!='*' and eqn[i:i+1]!='/' and eqn[i:i+1]!='^' and i>-1:
                i-=1
            
            if eqn[i+1:o]=='x':
                a=val
            else:
                a=float(eqn[i+1:o])
            
            eqn=eqn[0:i+1]+str((a-b))+eqn[j:len(eqn)]
            if showsteps:
                print(seqn,'=',eqn)
            continue
            
    return eqn  

#y=float(solve('-1e+3+2',0.0004999999999999946,0))