import re

def give_vars(ster):
    #   ster = 'many 10 mail to rahulmala@gmail.com about@MY MESSAGE@for every 100sec'
        #str= "some text to test"    
    try:
        tms = re.findall('many ([0-9]+)',ster)
        times = int(tms[0])
    except:
        if ster[0:4] in ['many'] : times = 4 
        else: times = 1
    #email parse
    mal = re.findall('to ([^ ]+)',ster)
    mail = mal[0]
    #sleep parse
    try:
        slp = re.findall('@for every ([^ ]+)',ster)
        count = 0
        slep = 0
        srh=''
        for l in slp[0]:
            try:
                #print(l)
                slep =int(l)+(slep*10) 
                count+=1
            except:
                srh+=l
            if srh in ['sec']:  sleep = slep
            if srh in ['min']:  sleep = slep*60
            #print (srh)
    except :
        sleep = 40
    mb = re.findall('about@([^@]+)',ster)
    mbody = mb[0]
    lst = list()
    lst.append(times)
    lst.append(mail)
    lst.append(mbody)
    lst.append(sleep)
    return (lst)


def give_vars2(ster):
    mb = re.findall('message@([^@]+)',ster)
    #if mb[0]==None : mb[0]='hello'
    mal = re.findall('to ([^ ]+)',ster)
    try : 
        mal.append(mb[0])
    except :
        mb = re.findall('msg@([^@]+)',ster)
        try : 
            mal.append(mb[0])
        except :
            mal.append('hello')
        
    finally : return mal
    #print(re.search("text",str))
