import io
#f=open('performance.property','r')
f = open('profileData.csv','r')
totalLoadTime = 0
totalTimeInSecond = 0.0
for line in f:
    if "Total Load Time(min-sec.mil) is" in line:
        print
        print "*" * 140
        print "Performance already checked"
        totalLoadTime += int(totalTimeInSecond / 60)
        totalLoadTime = str(totalLoadTime) + '-' + str(totalTimeInSecond % 60)
        print "Total Load Time(min-sec.mil) is :", str(totalLoadTime).rjust(63)
        f.close()
        exit()

    timePart = line.rpartition(':')[2]
    #print timePart.split('-')[1]

    totalLoadTime += int(timePart.split('-')[0])
    totalTimeInSecond += float(timePart.split('-')[1])

    #totalLoadTime = totalLoadTime + float(line.rpartition('-')[2])
    print repr(line.split(':',2)[0]).ljust(80) + "--->    " + (line.rpartition('-')[2]).rjust(10)

f.close()
print
print "*" * 140
print

totalLoadTime += int(totalTimeInSecond / 60)
totalLoadTime = str(totalLoadTime) + '-' + str(totalTimeInSecond % 60)

#for line in reversed(open("profileData.csv").readlines()):
#    print str(line).find("Total Load Time(min-sec.mil) is")
#    break

with open('profileData.csv','a') as pd:
    pd.write("\nTotal Load Time(min-sec.mil) is :"+ totalLoadTime)

print "Total Load Time(min-sec.mil) is :", str(totalLoadTime).rjust(63)

#print(f.read())