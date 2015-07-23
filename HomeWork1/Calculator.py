__author__ = 'kehao'
import sys
# sys.argv 0 is the filename 1.. are argv
exec("result = ("+sys.argv[1]+")")
# exec a string....
print(result)
