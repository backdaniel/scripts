#!/usr/bin/env python3

import argparse, csv

parser = argparse.ArgumentParser(
	description = 'print the contents of a csv file to stdout using \
	               database-like ascii table format.'
)
parser.add_argument(
	'file',
	help = 'csv file name'
)
parser.add_argument(
	'-n',
	'--noheader',
	action = 'store_true',
	help = 'explicitly informs that the first line is not a header'
)
parser.add_argument(
	'-t',
	'--tabular',
	action = 'store_true',
	help = 'show data in tabular form'
)
parser.add_argument(
	'-r',
	'--rows',
	action = 'store_true',
	help = 'show number of rows in table'
)
args = parser.parse_args()

with open(args.file) as csvfile:
    reader = csv.reader(csvfile)
    ncol = len(next(reader))
    space = [0] * ncol
    csvfile.seek(0)
    row_number = sum(1 for line in csvfile)
    csvfile.seek(0)

    for i in range(ncol):
        for row in reader:
            space[i] = max(space[i], len(row[i]))
        csvfile.seek(0)

    print('+-'+'-+-'.join(''.center(num, '-') for num in space)+'-+')
    for i, row in enumerate(reader):
        print('| '+' | '.join(row[j].ljust(num) for j, num in enumerate(space))+' |')
        if i == 0 and not args.noheader and not args.tabular:
            print('+-'+'-+-'.join(''.center(num, '-') for num in space)+'-+')
        if args.tabular:
            print('+-'+'-+-'.join(''.center(num, '-') for num in space)+'-+')
    if not args.tabular:
        print('+-'+'-+-'.join(''.center(num, '-') for num in space)+'-+')
    if args.rows:
        if args.noheader:
            print('({} rows)'.format(row_number))
        else:
            print('({} rows)'.format(row_number - 1))
