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
        elif '/cd ' in input_:
            destination = ' '.join(input_.split()[1:])
            if os.path.exists(currentPath + '/' + destination ):
                os.chdir(destination)
                if 'pieceDeck' in '/'.join(os.getcwd().split('\\')):
                    currentPath = '/'.join(os.getcwd().split('\\'))
                else:
                    print('Access denied!')
                    os.chdir(currentPath)
            else:
                print('Invalid path!')
            print(currentPath)
        elif '/mkd 'in input_:
            if not os.path.isdir(input_.split()[1]):
                os.mkdir(input_.split()[1])
        elif '/s' in input_:
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
