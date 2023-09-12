
# library to check if file exists
from os import path

# read filename from command line
filename = input("Enter filename to  read: ")

# validate filename
if not path.isfile(filename):
    print('invalid filename given')
else:
    # read the filename:
    print('--Start of file content--')

    with open(filename, 'r') as f:

        # read content from file
        print(f.read())

    print('-- End  of file content--')

    print('Enter the new content of the file. Enter "EOF" to stop:')

    line_text = ''       # stores the 1 line input of the user
    lines = []           # stores the lines that will be written to file

    while True:
        line_text = input('')

        # stop if input is "EOF"
        if line_text == 'EOF':
            break

        lines.append(line_text)

    # write data to file
    with open(filename, 'w') as f:
        f.write('\n'.join(lines))





