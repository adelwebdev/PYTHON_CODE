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
