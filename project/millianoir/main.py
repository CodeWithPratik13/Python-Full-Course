questions = [
    ["Who is Shah Rukh Khan", "WWE Wrestler", "Actor", "Astronut", "Plumber", 2],
    ["What is the capital of India?", "mumbai", "Delhi", "chennai", "kolkata", 1], 
    ["Who invented the light bulb?", "Nikola Tesla", "Thomas Edison", "Albert Einstein", "Isaac Newton", 2 ]
]

prizes = [1001, 10001,20001, 40001] 
i = 0
for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    #check whether the answer is correct or not

    a= int(input("Enter your answer. 1 for a/ 2 for b/ 3 for c/ 4 for d: ")) 

    if(question[5]==a):
        print("correct answere")
    else:
        print(f"incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break

    print(f"You won {prizes[i]}")
    i += 1