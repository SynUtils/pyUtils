import os, shutil, sys
import time


def fileMove(srcDir,extension,dstDir):
    i= 0
    for root, dirs, files in os.walk(srcDir):
        for file_ in files:
            if file_.endswith(extension):
                shutil.move(os.path.join(root, file_), os.path.join(dstDir, file_))
                print "file path::", os.path.join(root, file_)
                i = i + 1 
                print i
                if i > 1999:
                    break

def main():
    srcDir = '/home/synerzip/RT/UnprocessedFiles/' 
    todaynm = time.strftime("%d_%b")
    print todaynm
    dstDir = todaynm + '/Point/pptx'
    print dstDir
    extensions = ['.doc', '.docx','.xls', '.xlsx','.pptx','.ppt']
    fileType = ['/Word/Doc_Docx','/Sheet/Xls_Xlsx','/Point/Ppt_Pptx']
    x= 0
    for i in range(0, 3):
        for j in range(0, 2):
           
            dstDir = "/home/synerzip/RT/Files/" + todaynm + fileType[i]
            print extensions[x]
            extension = extensions[x]
            print ("Dest dir: %s " % dstDir) 
            fileMove(srcDir, extension , dstDir)
            x = x + 1
            
 #Start of execution
if __name__ == '__main__':
    main() 
