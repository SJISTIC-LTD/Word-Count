import re
test_string = "Tutorials point is a learning platform"
# original string
print ("The original string is : " + test_string)
# using regex (findall()) function
res = len(re.findall(r'\w+', test_string))
# total no of words
print ("The number of words in string are : " + str(res))
