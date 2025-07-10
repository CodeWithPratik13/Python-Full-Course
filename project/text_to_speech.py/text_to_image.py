from monsterapi import client
import requests
import webbrowser

# monster api key

api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjcxM2ExOTgzMmI4NjE4MGZjMzdkNzliMzI2MGMwYmJjIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDctMDZUMTM6NDY6MzIuNjUzMjIxIn0.fMpwpB05LhDXtFyWY2d41pKARhGya6H_JBLhLk8oOjs'

#initilize client
monster_client = client(api_key)

# prompt
prompt = input("prompt: ")
# model
model = 'txt2img'

# input data
input_data ={
    'prompt':f'{prompt}',
    'negprompt': 'bad anatomy',
    'samples' :1,
    'steps' : 50,
    'aspect_ratio': 'square',
    'guidance_scale' : 7.5,
    'seed' : 2414,
}

result = monster_client.generate(model, input_data)

img_url = result["output"] [0]

file_name = "generated_image.jpg"

# download the image
response = requests.get(img_url)

if response.status_code == 200:
    with open(file_name,'wb') as file:
        file.write(response.content)
    print("image downloaded")

# open the image
    webbrowser.open(file_name)