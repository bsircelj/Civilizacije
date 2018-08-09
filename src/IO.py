'''
Created on 8 Aug 2018

@author: benos
'''


def save(x,y,time,filename):
    file = open(filename+'.csv', 'w')
    for i in range(0,len(x)):
        file.write(str(x[i])+';'+str(y[i])+'\n')
    file.close()
    logFile = open(filename+'.log','w')
    logFile.write(filename+'\n')
    logFile.write('Time spent: '+str(time)+'s')
    logFile.close()
    
def readFile(filename):
    file = open(filename,'r')
    lines = file.readlines()
    
    size = len(lines)
    x = [0]*size
    y = [0]*size
    
    for i in range(0,size):
        line = lines[i].split(';')
        x[i] = int(line[0])
        y[i] = line[1]
        y[i] = int(y[i][0:-1])
    
    file.close()
    return (x,y)