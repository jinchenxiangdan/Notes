# Author: Shawn Jin

###########################################################
# import files in different directory in different way
###########################################################
#
# import multiplication
#
# runner.py and multiplication.py under same directory 
# 1: import whole file
import multiplication                       
# 2: import specific portion
from multiplication import Multiplication   

#
# import my_print
#
# my_print.py is under runner.py's parrent directory
# It also could be used whereever you want to import 

# add system path at run-time
import sys
########### The path MUST be absolute path ###############
sys.path.append('D:/Projects/Notes/python_import_test_locaotion2')
# 1: import specific method (right here, I used it replaced built-in print method)
from my_print import test_my_print as print
# 2: import whole file
import my_print

#
# import subtraction
#
# subtraction.py 
# 1: import whole file
import addition.addition as aa
# 2: import specific portion
from addition.addition import Addition


###########################################################
# main
###########################################################
if __name__ == "__main__":
    a = 3
    b = 2
    # all of them are using print method under my_print.py
    
    # multiplication usage 
    print(multiplication.test_multiplication(a,b))

    # addition usage 
    print(aa.test_add(a,b))



