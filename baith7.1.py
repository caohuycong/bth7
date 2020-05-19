#câu 7.1:
input_file=open('D:/a.txt','r')
for line in input_file:
    l=len(line)
    s=' '
    while(l>=1):
        s=s+line[1-1]
        l=l-1
    print(s)
input_file.close()
#cau 7.2
k=open('D:/a.txt','r')
char,wc,lc=0,0,0
for line in k:
    for k in range(0,len(line)):
        char +=1
        if(line[k]==' '):
            wc+=1
        if(line[k]=='\n'):
            wc,lc=wc+1,lc+1
print("the no.of chars is %d\n the no.of words is %d\n the no.of lines is %d"%(char,wc,lc))
#câu 7.3:
file=open("tep.txt","r")
a=file.read()
print("noi dung file la: ",a)
file.close()
#cau 7.4:
def file_read_from_dead(fname,nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f,nlines):
            print(line)
file_read_from_head('test.txt',2)
#cau 7.5:
def file_read(fname):
    from itertools import islice
    with open(fname,'w') as myfile:
        myfile.write("Python Exercises\n")
        mylife.write("Java Exercises")
    txt = open(fname)
    print(txt.read())
file_read('abc.txt')
#cau 7.6:
import sys
import os
def file_read_from_tail(fname,lines):
        bufsize = 8192
        fsize = os.stat(fname).st_size
        iter = 0
        with open(fname) as f:
            if bufsize > fsize:
                bufsize = fsize-1
                data = []
                while True:
                    iter +=1
                    f.seek(fsize-bufsize*iter)
                    data.extend(f.readlines())
                    if len(data) >= lines or f.tell() == 0:
                        print(' ' .join(data[-lines:]))
                        break
file_read_from_tail('test.txt'2)
#câu 7.7:
file=open("tep.txt","r")
s=0
for line in file:
    s=s+1
print("so dong cua file la: ",s)
file.close()
#cau 7.8
a=input('nhap noi dung danh sach: ')
file=open("tep.txt","a")
file.write(a)
file.close()
#cau 7.9
file=open("tep.txt","r")
a=file.read()
fi=open("abc.txt","a")
fi.write(a)
fi.close()
file.close()
#cau 7.10
file=open("tep.txt","r")
a=file.read()
b=[x for x in a.split(' ')]
c=b[0]
for i in b:
    if i>c:
        c=i
print('chu dai nhat trong van ban la: ',c)
