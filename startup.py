import os
import os.path

config = open('config.txt', 'r', encoding='utf-8')
lines = config.readlines()
debugMode = lines[0][12:][:-1] == 'true'
devMode = lines[1][10:][:-1] == 'true'
versionName = lines[3][14:][:-1]
version = lines[4][10:][:-1]
versionType = lines[5][14:][:-1]
firstTime = lines[2][10:][:-1] == 'INSERT_SYSTEM_PATH_HERE'
print(f'pieceDeck {versionType} {versionName}')
if firstTime:
    print('''IF YOU ARE USING PIECEDECK FOR THE FIRST
TIME ON THIS COMPUTER THEN GO TO config.txt AND
INSERT YOUR PATH TO PIECEDECK EXECUTABLE''')
    input('press ENTER to continiue.')
    config.close()
    exit(0)
rootLib_ = lines[2][10:][:-1].replace('\\\\', '\\')
rootLib = ''.join(rootLib_)
config.close()

UI = {
    'WELCOME_TEXT': 'Welcome to pieceDesk!',
    'PASSWORD_ENTER': 'Enter your password',
    'PASSWORD_ENTER_AGAIN': 'Wrong password!\nTry again!',
    'LOGIN_SUCCESS': 'Welcome ',
    'AUTHORS': 'Authors: Neykshon, 4ewhat',
    'ORIGINAL_IDEA': 'Original idea: Snake\'s SIMP#2396, Glek',
    'CO_AUTHOR': 'Co-author: NeykShon#2648',
    'LEAD_PROGERS': 'Lead progers: The man who doesn\'t know his hair color\n\t\t\t  His main BRO (sits to the right)',
    'SPECIAL_CREDITS': 'Special thanks to: \n\tPunished \"Venom\" Snake\n\tSolid Snake\n\tThe man who sold the world\n\tKazuhira Miller'
}

if debugMode:
    print('debug mode activated')
if devMode:
    print('dev mode activated')
    print(UI['AUTHORS'])
    print(UI['ORIGINAL_IDEA'])
    print(UI['CO_AUTHOR'])
    print(UI['LEAD_PROGERS'])
    print(UI['SPECIAL_CREDITS'])


class User:
    def __init__(self, name, password=''):
        self.name = name
        self.password = password
        self.rights = 'none'
    def login(self):
        if bool(self.password):
            passwordGuess = input(UI['PASSWORD_ENTER'] + '\n')
            while passwordGuess != self.password:
                passwordGuess = input(UI['PASSWORD_ENTER_AGAIN'] + '\n')
            else:
                pass
        print(UI['LOGIN_SUCCESS'] + self.name)
        return self

class DefaultUser(User):
    def __init__(self, name, password=''):
        self.name = name
        self.password = password
        self.rights = 'user'

class AdminUser(User):
    def __init__(self, name, password=''):
        self.name = name
        self.password = password
        self.rights = 'admin'

class GodUser(User):
    def __init__(self, name, password=''):
        self.name = name
        self.password = password
        self.rights = 'god'

def login_screen(users):
    for user in users:
        print(user.name)
    user_logon = input('Select user:')
    for user in users:
        if user.name == user_logon:
            return user.login()

def initUsers():
    users_file = open(r'users_\users', 'r', encoding='utf-8')
    users_ = users_file.readlines()
    user_names = [users_[i].split('#$%^')[0] for i in range(len(users_))]
    user_passwords = [users_[i].split('#$%^')[1].split('\n')[0] for i in range(len(users_))]
    users = [DefaultUser(user_names[i], user_passwords[i]) for i in range(len(users_))]
    users_file.close()
    return users


def Startup(users):
    running = True
    print(UI['WELCOME_TEXT'])
    return login_screen(users)


#Startup(initUsers())