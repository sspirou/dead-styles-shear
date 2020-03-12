import sys, os
# import code # <--- for debugging
# code.interact(local=locals()) # <--- for debugging

def main(pathToDirectory, ignoreJS=False):
    deadStylesList = usedSelectorsList = allSelectorsList = []
    
    # list all css, scss, js, and html files in desired directory tree
    filesList = recursiveList(pathToDirectory)

    # build all & used selectors lists based on retrieved files list
    for fileToCheck in filesList:
        if fileToCheck.endswith('css') and os.path.isfile(fileToCheck):
            allSelectorsList = uniqueJoin(allSelectorsList, getSelectorsList(fileToCheck))
        elif os.path.isfile(fileToCheck):
            usedSelectorsList = uniqueJoin(usedSelectorsList, getSelectorsList(fileToCheck))
    # these lists are built to contain unique sets within, usedSelectorsList may not be a subset of allSelectorsList

    # build dead styles list by comparing all & used selectors lists from above
    for selector in allSelectorsList:
        if not selector in usedSelectorsList:
            deadStylesList.append(selector + ' {}')

    # write output file with selectors from deadStylesList
    with open('deadStyles.css', 'w') as outputFile:
        outputFile.writelines(deadStylesList)

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
    selectorsList = []
    if sourceFile.endswith('.html'):
        selectorsList = getSelectorsListHTML(sourceFile)
    elif sourceFile.endswith('.js'):
        selectorsList = getSelectorsListJS(sourceFile)
    else:
        selectorsList = getSelectorsListCSS(sourceFile)
    return removeDuplicates(selectorsList)

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
    ignoreJS = False
    if len(sys.argv) < 2:
        print("pathToDirectory is required")
        exit(1)
    elif len(sys.argv) > 2:
        arg2 = sys.argv[2].lower()
        if arg2 == 'true' or arg2 == 'ignorejs':
            ignoreJS = True
    main(sys.argv[1], ignoreJS)