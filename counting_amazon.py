def count_arara(n):
    if n==1:
        return 'anane'
    elif n%2==0:
        return ' '.join(int(n/2)*['adak'])  
    elif n%2!=0:
        return ' '.join(int(n/2)*['adak'])+' anane'