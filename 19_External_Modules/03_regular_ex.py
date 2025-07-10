import re

text= "The quick brown fox jumps over the lazy dog"

# # Search for pattern
# match = re.search("brown",text)
# if match:
#     print("match found!")
#     print("Start index:", match.start())
#     print("End index:", match.end())

# # Find all occurrences of a pattern

# matches= re.findall("the",text,re.IGNORECASE)
# print("Matches:", matches)

# replace pattern
new_text = re.sub("fox", "cat", text)
print("New text:",new_text)