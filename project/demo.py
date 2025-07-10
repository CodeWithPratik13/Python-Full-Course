import pywhatkit as pw

txt = """Theory:  Lists in R language, are the objects which comprise elements of diverse types like numbers, strings, logical values, vectors, 
list within a list and also matrix and function as its element. 
A list is generated using list() function. It is basically a generic vector that contains different objects. 
R allows its users to perform various operations on lists which can be used to illustrate the data in different forms."""

pw.text_to_handwriting(txt,"demo.png",[0,0,138])
print("End")