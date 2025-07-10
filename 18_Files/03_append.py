# append to an existing file called john doe.txt
# It should  add data about john doe's Hometown

f = open("john doe.txt","a")

string = '''
john doe initially lived in phoenix, arizona. He is a very nice 
guy
'''
f.write(string)

f.close()