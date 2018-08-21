'''
Created on 8 Aug 2018

@author: benos
'''


def save(x,y,filename):
    file = open('data/'+filename+'.csv', 'w')
    for i in range(0,len(x)):
        file.write(str(x[i])+';'+str(y[i])+'\n')
    file.close()
    
def readFile(filename):
    file = open('data/'+filename,'r')
    lines = file.readlines()
    
    size = len(lines)
    x = [0]*size
    y = [0]*size
    
    for i in range(0,size):
        line = lines[i].split(';')
        x[i] = float(line[0])
        y[i] = line[1]
        y[i] = float(y[i][0:-1])
    
    file.close()
    return (x,y)