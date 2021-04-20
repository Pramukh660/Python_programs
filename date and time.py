#to get current date an time 
#we need to use the datetime library 
from datetime import datetime
date = datetime.now()
#the funcn returns a datetime object
print('Today is :' + str(date))