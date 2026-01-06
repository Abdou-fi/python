# bad practice
def read_file(file_path):
    file = open(file_path, 'r') 
    content = file.read()
    file.close() 
    return content
print(read_file('textError.txt'))

# good practice
def read_file(file_path): 
    try: 
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError: 
        return "File not found."
print(read_file('text_Error.txt'))

