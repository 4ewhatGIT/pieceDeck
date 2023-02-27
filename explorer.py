from startup import *
import os
import os.path


def explorer(user):
    currentUser = user
    currentPath = rootLib

    running = True
    while running:
        input_ = input()
        if '/dir' in input_:
            print(f'Contents of {currentPath}:')
            dirs = [d for d in os.listdir(currentPath) if os.path.isdir(d)]
            files = [d for d in os.listdir(currentPath) if os.path.isfile(d)]
            print(*dirs, sep=' (dir)\n', end=' (dir)\n')
            print(*files, sep='\n')
            continue
        elif '/open ' in input_:
            name = ''.join(input_.split()[1:])
            osCommandString = "notepad.exe " + name
            os.system(osCommandString)
        elif '/del ' in input_:
            os.remove(''.join(input_.split()[1:]))
        elif '/help' in input_:
            help = open('README.txt', 'r', encoding='utf-8')
            help_ = help.readlines()
            for i in range(1, 8):
                print(help_[i], end='')
        elif '/cd ' in input_:
            destination = ' '.join(input_.split()[1:])
            if os.path.exists(currentPath + '/' + destination ):
                os.chdir(destination)
                if rootLib in '/'.join(os.getcwd().split('\\')):
                    currentPath = '/'.join(os.getcwd().split('\\'))
                else:
                    print('Access denied!')
                    os.chdir(currentPath)
            else:
                print('Invalid path!')
            print(currentPath)
        elif '/mkd ' in input_:
            if not os.path.isdir(input_.split()[1]):
                os.mkdir(input_.split()[1])
                print('Folder created successfully!')
            else:
                print('Folder already exists!')
        elif '/rmd ' in input_:
            if os.path.isdir(input_.split()[1]):
                os.rmdir(input_.split()[1])
                print('Folder deleted successfully!')
            else:
                print('Folder already doesn\'t exist!')
        elif '/echo ' in input_:
            if ' > ' in input_:
                file = open(input_.split(' > ')[1], 'w+', encoding='utf-8')
                file.write(''.join(''.join(input_.split(' > ')[0]).split()[1:]))
                file.close()
            else:
                print(*input_.split()[1:], sep=' ')
        elif '/exit' in input_:
            if debugMode:
                print('********************DEBUG********************')
                print(f'users = {initUsers()}')
                print(f'debugMode = {debugMode}')
                print(f'devMode = {devMode}')
                print(f'rootLib = {rootLib}')
                print(f'versionName = {versionName}')
                print(f'version = {version}')
                print(f'versionType = {versionType}')
            exit('pisDesk has been shutdown')
