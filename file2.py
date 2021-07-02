from Question import Question

# -----------------------------------FILES on PYTHON ----------------------------------------
file_python = open("file.txt", "r")
print(file_python.read()) 
file_python.close() 

file_python = open("file.txt", "w")
file_python.write("tobby - human resources")
file_python.close() 

file_python = open("index.html", "w")
file_python.write("<p>some paragraphe in html</p>")
file_python.close() 

question_prompts = [
    "what color are apples? \n(a) Teal\n(b) Magenta "
    "what color are bananas?\n(a) Teal\n(b) Magenta "
    "what color are strawberries?\n(a) Teal\n(b) Magenta "
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"a"),
    Question(question_prompts[2],"b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(question)) + "correct")

run_test(questions)   
