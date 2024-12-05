import os

from part1 import main as p1
from part2 import main as p2

cwd = os.path.dirname(os.path.realpath(__file__))
if '\\' in cwd:
    cwd = cwd.replace('\\', '/')
year = cwd.split('/')[-2]
day = cwd.split('/')[-1].replace('day', '')

with open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt', 'r') as input_file:
      input_text = input_file.read()

results = [p1(input_text), p2(input_text)]

print(f'Year {year}, Day {day}',
      f'------------------------------------',
      f'part 1 result: {results[0]}',
      f'------------------------------------',
      f'part 2 result: {results[1]}',
      f'------------------------------------', sep='\n')
