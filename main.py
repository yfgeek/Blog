import string, os, sys

dir = 'blog'

files = os.listdir(dir)

writerList = open("Content.md", "w")
j = 0
filelist = []
for root, dirs, files in os.walk(dir):
    for name in files:
        if "images" in root:
            a =1
        else:
            list =  "| " + name[0:9] + " | [" +name[11:-3] + "](blog/" + name + ") |"
            filelist.append(list)
            j = j +1
j = j -1
while j>0:
    writerList.write(filelist[j] + '\n')
    print filelist[j]
    j=j-1
