def bubble(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                temp=a[j];
                a[j]=a[j+1]
                a[j+1]=temp
    return a

import time
for i in range(1,11):
    sum1=0
    sum2=0
    sum3=0
    k=i
    filename='File ',str(i),'.txt'
    s=''
    fname=s.join(filename)
    print(fname)
    lineList = [line.rstrip('\n') for line in open(fname)]
    print('Lenght of a:',len(lineList))
    for i in range(10):

        b=[int(i) for i in lineList]
        #bubble sort
        #avg case
        start = time.time()
        bubble(b)
        end = time.time()
        sum1=sum1+end - start
        b.sort()
        #best case
        start = time.time()
        bubble(b)
        end = time.time()
        sum2=sum2+end - start

        #worst time
        b.reverse();
        start = time.time()
        bubble(b)
        end = time.time()
        sum3=sum3+end - start
        print('Best Case :',sum2/10)

        print('Worst Case :',sum3/10)
        print('Average Case:',sum1/10)