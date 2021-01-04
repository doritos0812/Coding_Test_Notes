string = "this is string example....wow!!!";
print(string.startswith( 'this' ))
print(string.startswith( 'is', 2, 4 ))
print(string.startswith( 'this', 2, 4 ))

'''
str.startswith(str, beg=0,end=len(string))

str − This is the string to be checked.

beg − This is the optional parameter to set start index of the matching boundary.

end − This is the optional parameter to end start index of the matching boundary.

'''