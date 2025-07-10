#write to a file called john doe.txt
# It should contain data about john doe

f = open("john doe.txt","w")

string = '''
john doe is a nice guy. he lives in nyc and he work with python
his favorate package is pandas
'''
f.write(string)

f.close()