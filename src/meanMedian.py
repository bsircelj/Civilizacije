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
        #print(xaxis[p]," - ",final[p])
        #mean += p*final[p]*(xaxis[p]-xaxis[p-1])
        summ += final[p]*(xaxis[p]-xaxis[p-1])
        if final[p-1]!=0 :
            median[sumNo]=xaxis[p-1]
            sumNo+=1
    half = summ/2
    tempSum = 0
    for p in range(0,len(final)):
        tempSum+=final[p]
        if tempSum>half:
            mean = final[p]
            break
            

    return (mean,median[int(sumNo/2)])

'''
(mean,median) = meanMedian([1,2,3,4,5,6,7],[1,2,3,4,5,6,7])
print(mean)
print(median)
'''