#!/usr/bin/python
import sys

from prettytable import PrettyTable

input_file_name = sys.argv[1]
input_file = open(input_file_name, "r")

content = input_file.read().splitlines()
it  = iter(content)

input_file.close()

line = next(it).split(" ")
num_elems = int(line[0])
num_subgroups = int(line[1])

subgroups = []
for line in it:
    line = line.split(" ")
    aux_subgroup = []
    aux_subgroup.append(int(line[0]))
    aux_subgroup.append(int(line[1]))
    aux_subgroup.append(int(line[2]))
    subgroups.append(aux_subgroup)

x = PrettyTable()

field_names = [" "]
for n in range(1,num_elems+1):
    field_names.append(str(n))
x.field_names = field_names

for s in range(1,num_subgroups+1):
    row = []
    row.append("C" + str(s))
    for n in range(0,num_elems):
        if n in subgroups[s-1]:
            row.append("1")
        else:
            row.append("0")
    x.add_row(row)

print(x)
