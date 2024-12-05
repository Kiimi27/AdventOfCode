import sys
import requests
import os
import shutil

year = sys.argv[1]
day = sys.argv[2]
no_dl = len(sys.argv) > 3 and sys.argv[3]

os.chdir(os.path.dirname(os.path.realpath(__file__)))

if not os.path.exists(f'../code/{year}'):
    os.mkdir(f'../code/{year}')
if not os.path.exists(f'../code/{year}/day{day}'):
    os.mkdir(f'../code/{year}/day{day}')

with open(f'../code/{year}/day{day}/input.txt', 'w') as f:
    if not no_dl:
        with open('session-cookie.txt', 'r') as cookie:
            f.write(requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': cookie.read()}).text)

shutil.copyfile('template/parts-template.py', f'../code/{year}/day{day}/part1.py')
shutil.copyfile('template/parts-template.py', f'../code/{year}/day{day}/part2.py')
shutil.copyfile('template/runner-template.py', f'../code/{year}/day{day}/runner.py')

print(f'Open created day in browser: https://adventofcode.com/{year}/day/{day}')
