'''
Created on Oct 13, 2016

@author: PShastri
'''
import re
n=raw_input("")
find_n=bool(re.search(r".",n))
find_nn=bool((re.match(r"+-",n))) 
# or bool(re.match(r"-+",n))
print find_nn