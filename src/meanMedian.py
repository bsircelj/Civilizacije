'''
Created on 10 Aug 2018

@author: benos
'''

def meanMedian(final, xaxis):
    mean = 0
    summ = 0
    median = [0]*len(final)
    sumNo = 0
    for p in range(1,len(final)):
        print(xaxis[p]," - ",final[p])
        #mean += p*final[p]*(xaxis[p]-xaxis[p-1])
        summ += final[p]*(xaxis[p]-xaxis[p-1])
        if final[p]!=0 :
            median[sumNo]=xaxis[p]
            sumNo+=1
    half = summ/2
    tempSum = 0
    for p in range(1,len(final)):
        if tempSum>half:
            

    return (mean,median[int(sumNo/2)])