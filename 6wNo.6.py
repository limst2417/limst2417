inFp=open("C:/Windows/win.ini","r")
outFp=open("C:/Temp/data3.txt","w")

inList=inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
