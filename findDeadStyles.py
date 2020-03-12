import sys, os
# import code # <--- for debugging
# code.interact(local=locals()) # <--- for debugging

def main(pathToDirectory):
    deadStylesList = usedSelectorsList = allSelectorsList = []
    filesList = recursiveList(pathToDirectory)

    exit(0)
    
# recursively build a list of all html, js, and (s)css files in given directory, keep relative path from cwd with each entry
def recursiveList(pathToDir):
    filesList = []
    tmpList = os.listdir(pathToDir)
    for i in tmpList:
        if i.endswith('.html') or i.endswith('.js') or i.endswith('.css') or i.endswith('.scss'):
            filesList.append(os.path.join(pathToDir,i))
        elif os.path.isdir(os.path.join(pathToDir, i)):
            iList = recursiveList(os.path.join(pathToDir, i))
            for f in iList:
                if not f.startswith(pathToDir):
                    filesList.append(os.path.join(pathToDir,f))
                else:
                    filesList.append(f)
    return filesList

# single function wrapping 3 unique file type options (html, js, css)
def getSelectorsList(sourceFile):
    if sourceFile.endswith('.html'):
        return getSelectorsListHTML(sourceFile)
    elif sourceFile.endswith('.js'):
        return getSelectorsListJS(sourceFile)
    else:
        return getSelectorsListCSS(sourceFile)

def getSelectorsListHTML(sourceFile):
    selectorsList = []
    with open(sourceFile, 'r') as f:
        # parse selectors and append to selectorsList
        lines = f.readlines()
    return selectorsList

def getSelectorsListJS(sourceFile):
    selectorsList = []
    with open(sourceFile, 'r') as f:
        # parse selectors and append to selectorsList
        lines = f.readlines()
    return selectorsList

def getSelectorsListCSS(sourceFile):
    selectorsList = []
    with open(sourceFile, 'r') as f:
        # parse selectors and append to selectorsList
        lines = f.readlines()
    return selectorsList

# assumes list1 is already unique
def uniqueJoin(list1, list2):
    for i in list2:
        if not i in list1:
            list1.append(i)
    return list1

# 'clean' a list of all duplicate entries
def removeDuplicates(listToClean):
    resultList = []
    for i in listToClean:
        if not i in resultList:
            resultList.append(i)
    return resultList

if __name__ == "__main__":
    if (sys.argv.__len__() <= 1):
        print("pathToDirectory is required")
        exit(1)
    main(sys.argv[1])