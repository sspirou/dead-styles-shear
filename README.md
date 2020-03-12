# dead-styles-shear
Py scripts for identifying and trimming dead style rules from a website directory. Written in python 2.7

----------
### Identify Dead Style Rules

`findDeadStyles.py pathToDirectory [ignoreJS]`
  -  recursively search the input directory for html and javascript files to build a list of all selectors being used
  -  pass `ignoreJS` to optionally only crawl html files when building used selectors list
  -  recursively search the input directory for css and scss files to build a list of all style rules
  -  write output file, deadStyles.css, listing all dead styling rules in input directory
  
##### Output:
- deadStyles.css - valid css file containing each unused selector listed on its own line followed by `{}`
----------
### Trim Dead Style Rules [TODO]

`trimStyles.py pathToDirectory [ignoreJS]`
  -  mimics behavior above to generate list of dead style rules, then finds each dead rule in the list and removes it from input directory's css files.
