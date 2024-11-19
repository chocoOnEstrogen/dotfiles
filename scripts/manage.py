import os 
import sys
import argparse

# Example: python manage.py --create scripts --name script1
# Example 2: python manage.py --create config --name config1

parser = argparse.ArgumentParser(description='Manage the project')
parser.add_argument('--create', type=str, help='Create a new file')
parser.add_argument('--name', type=str, help='Name of the file')

args = parser.parse_args()

class Converter:
    def __init__(self, name):
        self.name = name
    def from_slug(self):
        return self.name.replace('-', ' ').title()
    def to_slug(self):
        return self.name.lower().replace(' ', '-')

def logger(_from_, message):
    print(f'[{_from_}] {message}')

def create_scripts(name):
    logger('create_scripts', f'Creating script {name}')
    file_ext = name.split('.')[-1]
    name = name.split('.')[0]
    normalized_name = name
    name = Converter(name).to_slug()

    if os.path.exists(f'{name}'):
        logger('create_scripts', f'Script {name} already exists')
        return

    # Make the directory
    os.makedirs(f'{name}')
    logger('create_scripts', f'Created directory for script {name}')

    with open(f'{name}/{name}.{file_ext}', 'w') as f:
        pass
    
    with open(f'{name}/README.md', 'w') as f:
        f.write(f'<h1 align="center">{normalized_name}</h1>\n\n')

    logger('create_scripts', f'Created script file {name}.{file_ext}')

if args.create == 'scripts':
    create_scripts(args.name)
