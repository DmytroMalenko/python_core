file_path = 'demo.txt'

#file = open(file_path, 'r')

#file.close()

#with open(file_path, '+a') as file:
#   print("File created successfully!")


file_path = './text_files/text.txt'
'''
with open(file_path, 'r') as f:
    file_content = f.read(10)
    print(file_content)
    print(type(file_content))

with open(file_path, 'r') as f:
    line_1 = f.readline().strip()
    print(line_1)
    line_2 = f.readline().strip()
    print(line_2)
    

with open(file_path, 'r') as f:
    for line in f:
        print(line.strip())

with open(file_path, 'r') as f:
    lines = f.readline()
    print(lines)
    '''
    

with open('text.txt', 'a') as f:
    f.write("\nthis data is written by code\n")
    f.writelines(["line1\n",  "line2\n", "line3\n"])

    

try: 
    with open("demo.txt", 'x'):
        print("file created successfully!")
except FileExistsError:
    print("File already exists!")
