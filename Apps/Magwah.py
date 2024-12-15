import os

ready = True

print('Try typing the help command.')

Ibe = '<<. '

while ready:
    operation = input(Ibe)
    if operation == 'help':
        print('del: deletes a file')
        print('help: open this menu')
        print('add: creates a file')
        print('mov: moves a file')
        print('Also use mov for renaming')
        print('read: read a text file')
        print('wri: write to a text file')
        print('rb: read binary code (may take a few minutes)')

    if operation == 'del':
        print('use / instead of \\')
        file = input('file Path? ')
        print('deleting')
        os.remove(file)
        print('deleted!')

    if operation == 'mov':
        file = input('file Path? ')
        print('use / instead of \\')
        dest = input('destination? ')
        print('moving')
        os.replace(file, dest)
        print('moved!')

    if operation == 'add':
        fi = open((input('File name? '))+'.'+(input('Format? ')),'w+')
        print('Creating New file')
        print('DONE!!')

    if operation == 'read':
        fileW = open(input('file Path? '),'r')
        content = fileW.read()
        print(content)
        fileW.close()
        
    if operation == 'wri':
        with open(input('file Path? '), 'w') as Txfile:
            # Write some text to the file
            text = input('Text? ')
            Txfile.write(text)

    if operation == 'rb':
        fileW = open(input('file Path? '),'rb')
        content = fileW.read()
        print(content)
        fileW.close()

    if operation == 'ibe':
        Ibe = input('Ibe Settings ')
        if Ibe == 'def':
            Ibe = '>>.'
        Ibe = Ibe+' '