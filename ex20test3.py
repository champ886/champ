from sys import argv

script, input_file = argv

def print_all(file):
    print(file.read)

def rewind(file):
    file.seek(2)

def print_a_line(line_count, file):
    print(line_count, file.readline())

current_file = open(input_file)

print("First, let's print the whole file: \n")

print(current_file)

print ("Now let's rewind the whole file")
rewind(current_file)

print("Let's print 3 lines")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
