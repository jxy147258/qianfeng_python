
with open("logbuffer.txt","r") as f:
    while len(f.readline()) > 0:
        logInfo = f.readline()[60:].split(":",1)[-1]
        for i in range(11):
            indexIP = logInfo.split(",")[i]
            print(indexIP)



