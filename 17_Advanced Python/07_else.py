try:
    a = 345/0

except Exception as e:
    print(e)

#gets executed when there is no error in the try block
else: 
    print("Hey i am good")