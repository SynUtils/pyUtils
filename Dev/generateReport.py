# Copyright 2011, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import os
import sys
import fileinput
from os import listdir
from os.path import isfile, join
from time import gmtime, strftime
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
#divString = '<div class="entryDiv"><a class="fileDiv" href="$imagePath">$file</a><span class="numDiv" style="font-size:1.0em;">$slideNum</span><a class="diffDiv" onclick="showMontage(this)">diff</a></div>'
divString = '<tr class="entryDiv"><td><a class="fileDiv" href="$imagePath">$file</a></td><td><a class="numDiv" onclick="showMontage(this)">$slideNum</a></td></tr>'
CL = {'lt50':'','50to70':'','70to85':'','85to95':'','95to99':'', 'match':''}
CatCnt = {'lt50':'','50to70':'','70to85':'','85to95':'','95to99':'', 'match':''}
propArray = []
def getFileList (dir):
    if os.path.isdir(dir):
        list = [ f for f in listdir(dir) if isfile(join(dir,f)) ]
    return list

def updateHtml ():
    numFiles = 0
    numImages = 0
    numFailedFiles = 0
    numFailedImages = 0
    blessedDir = propArray[2] + '/images/blessedImages'
    #check for existence
    if os.path.isdir(blessedDir):
        list = [ f for f in listdir(blessedDir) if not isfile(join(blessedDir,f)) ]
        numFiles = len(list)
        for item in list:
            numImages += len(getFileList (blessedDir + '/' + item + '/'))

    failedDir = propArray[2] + '/images/slideImages'
    #check for existence
    if os.path.isdir(failedDir):
        list = [ f for f in listdir(failedDir) if not isfile(join(failedDir,f)) ]
        numFailedFiles = len(list)
        for item in list:
            numFailedImages += len(getFileList (failedDir + '/' + item + '/'))

    with open(propArray[2] + '/index.html', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            if '$lt50_content' in line:
                if 'lt50' in CL:
                    line = line.replace('$lt50_content', CL['lt50'])
                else:
                    line = line.replace(line, '')
                f.write(line)
            elif '$50to70_content' in line:
                if '50to70' in CL:
                    line = line.replace('$50to70_content', CL['50to70'])
                else:
                    line = line.replace(line, '')
                f.write(line)
            elif '$70to85_content' in line:
                if '70to85' in CL:
                    line = line.replace('$70to85_content', CL['70to85'])
                else:
                    line = line.replace(line, '')
                f.write(line)
            elif '$85to95_content' in line:
                if '85to95' in CL:
                    line = line.replace('$85to95_content', CL['85to95'])
                else:
                    line = line.replace(line, '')
                f.write(line)
            elif '$95to99_content' in line:
                if '95to99' in CL:
                    line = line.replace('$95to99_content', CL['95to99'])
                else:
                    line = line.replace(line, '')
                f.write(line)
            elif '$match_content' in line:
                if 'match' in CL:
                    line = line.replace('$match_content', CL['match'])
                else:
                    line = line.replace(line, '')
                f.write(line)
            elif '$oldBuild' in line:
                line = line.replace('$oldBuild', propArray[0])
                f.write(line)
            elif '$newBuild' in line:
                line = line.replace('$newBuild', propArray[1])
                f.write(line)
            elif '$numFiles' in line:
                line = line.replace('$numFiles', str(numFiles))
                f.write(line)
            elif '$numImages' in line:
                line = line.replace('$numImages', str(numImages))
                f.write(line)
            elif '$numFailedFiles' in line:
                line = line.replace('$numFailedFiles', str(numFailedFiles))
                f.write(line)
            elif '$numFailedImages' in line:
                line = line.replace('$numFailedImages', str(numFailedImages))
                f.write(line)
            elif '$lt50Cnt' in line:
                line = line.replace('$lt50Cnt', str(CatCnt['lt50']))
                f.write(line)
            elif '$50to70Cnt' in line:
                line = line.replace('$50to70Cnt', str(CatCnt['50to70']))
                f.write(line)
            elif '$70to85Cnt' in line:
                line = line.replace('$70to85Cnt', str(CatCnt['70to85']))
                f.write(line)
            elif '$85to95Cnt' in line:
                line = line.replace('$85to95Cnt', str(CatCnt['85to95']))
                f.write(line)
            elif '$95to99Cnt' in line:
                line = line.replace('$95to99Cnt', str(CatCnt['95to99']))
                f.write(line)
            elif '$matchCnt' in line:
                line = line.replace('$matchCnt', str(CatCnt['match']))
                f.write(line)
            else:
                f.write(line)

def fillDiv (filename,slide):
    imgDir = 'images/testFiles/'
    divStr = divString.replace("$imagePath",imgDir + filename).replace("$file",filename).replace("$slideNum",slide)
    return divStr+'\n'

def createCatList (catPath, category):
    dirList = [ d for d in listdir(catPath) if not isfile(join(catPath,d)) ]
    L = ''
    count = 0
    for dirs in dirList:
        dirInCat = catPath + '/' + dirs
        diffList = [ f for f in listdir(dirInCat) if isfile(join(dirInCat,f)) ]
        for item in diffList:
            splitList = item.split('_image_',1)
            if len(splitList) == 2:
                #sldExt = splitList[1].split('_',1)
                sldExt = splitList[1].split('.',1)
                sld = sldExt[0]
                #fname = splitList[0] + '.' +sldExt[1].split('.',1)[0]
                fname = splitList[0] + '.' + dirs.split('_').pop()
                L = L + fillDiv(fname,sld)
                count += 1
    CatCnt[category] = count
    return L

def readDir ():
    diffDir = propArray[2] + '/images/diffImages'
    #check for existence
    if os.path.isdir(diffDir):
        list = [ f for f in listdir(diffDir) if not isfile(join(diffDir,f)) ]
        for item in list:
            CL[item] = createCatList (diffDir + '/' +item, item)
    updateHtml ()

ins = open( sys.argv[1], "r" )
for line in ins:
    propArray.append(line.strip().split(':',1)[1])

mode = 'ALL'
if len(sys.argv) > 2:
   mode = sys.argv[2]

#currDir = os.getcwd()
if mode == 'ALL' or mode == 'BLESSED':

    e2eDir = propArray[0] + '/e2eTests/'
    print 'Cleaing source'

    print 'Cleaning Dest blessedImages'
    cmd = 'rm -rf ' + e2eDir + 'newBlessedImages'
    os.system(cmd)
    cmd = 'rm -rf ' + propArray[4]
    os.system(cmd)

    if propArray[5] != e2eDir + 'c2cTests/testFiles':
        print 'Removing old test files'
        cmd = 'rm -rf ' + e2eDir + 'c2cTests/testFiles/*'
        os.system(cmd)

        print 'Copy new test files'
        cmd = 'cp -rf ' + propArray[5] + '/*' + ' ' + e2eDir + 'c2cTests/testFiles/'
        os.system(cmd)

    print 'Changing to old build dir'
    os.chdir(e2eDir)

    print 'run monkey to get blessed image'
    cmd = 'node monkey.js pageSets/c2c.json -s newBlessedImages'
    os.system(cmd)

    if propArray[4] != e2eDir + 'newBlessedImages':
        print 'copy blessedImages to Dest'
        cmd = 'mv -f ' + e2eDir + 'newBlessedImages' + ' ' + propArray[4]
        os.system(cmd)

#os.chdir(currDir)
if mode == 'ALL' or mode == 'DIFF':
    e2eDir = propArray[1] + '/e2eTests/'
    if propArray[4] != e2eDir + 'blessedImages':
        print 'Removing old blessedImages'
        cmd = 'rm -rf ' + e2eDir + 'blessedImages'
        os.system(cmd)
        print 'Copy new blessedImages'
        cmd = 'cp -rf ' + propArray[4] + ' ' + e2eDir + 'blessedImages'
        os.system(cmd)

    print 'Removing old chrome images'
    cmd = 'rm -rf ' + e2eDir + 'slideImages'
    os.system(cmd)

    print 'Removing old diff images'
    cmd = 'rm -rf ' + e2eDir + 'diffImages'
    os.system(cmd)

    if propArray[5] != e2eDir + 'c2cTests/testFiles':
        print 'Removing old test files'
        cmd = 'rm -rf ' + e2eDir + 'c2cTests/testFiles/*'
        os.system(cmd)

        print 'Copy new test files'
        cmd = 'cp -rf ' + propArray[5] + '/*' + ' ' + e2eDir + 'c2cTests/testFiles/'
        os.system(cmd)

    print 'Changing to new build dir '
    os.chdir(e2eDir)

    print 'run monkey to get diff images'
    cmd = 'node monkey.js pageSets/c2c.json'
    os.system(cmd)

    print 'Cleaing dest'
    cmd = 'rm -rf ' + propArray[2] + '/images/*'
    os.system(cmd)

if mode == 'ALL' or mode == 'DIFF' or mode == 'REPORT':
    e2eDir = propArray[1] + '/e2eTests/'
    cmd = 'rm -rf ' + propArray[2] + '/index.html'
    os.system(cmd)

    print 'copy blessed image to dest'
    cmd = 'mkdir -p ' + propArray[2] + '/images'
    os.system(cmd)
    cmd = 'cp -rpf ' + propArray[4] + ' ' + propArray[2] + '/images/'
    os.system(cmd)

    print 'copy test files to dest'
    cmd = 'cp -rf ' + propArray[5] + ' ' + propArray[2] + '/images/testFiles'
    os.system(cmd)

    print 'move chrome images to dest'
    cmd = 'mv -f ' + e2eDir + '/slideImages' + ' ' + propArray[2] + '/images/'
    os.system(cmd)

    print 'move diff images to dest'
    cmd = 'mv -f ' + e2eDir + '/diffImages' + ' ' + propArray[2] + '/images/'
    os.system(cmd)

    print 'copy ms images to dest'
    cmd = 'cp -rf ' + propArray[3] + ' ' + propArray[2] + '/images/'
    os.system(cmd)

    print 'copy report viewer to dest'
    cmd = 'cp -rf ' + propArray[1] + '/e2eTests/c2cTests/c2c.html ' + propArray[2] + '/index.html'
    os.system(cmd)

    print 'generating report'
    readDir()
print strftime("%Y-%m-%d %H:%M:%S", gmtime())
