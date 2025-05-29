with open('example.txt', 'w') as file:
    file.write("Create a new file and write initial content.\n")

with open('example.txt', 'a') as file:
    file.write("Append content to the file.\n")

with open('example.txt', 'r') as file:
    content = file.read()
    print("Read the content of the file:\n",content)