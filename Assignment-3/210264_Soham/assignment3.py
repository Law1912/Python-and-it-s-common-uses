import argparse
import regex as re
import os
import sys
import datetime
import pathlib

def mydir(path):
    files = [d for d in os.listdir(path) if os.path.isfile(os.path.join(path, d))]
    dirs = [d for d in os.listdir(path) if not os.path.isfile(os.path.join(path, d))]

    for d in dirs:
        print((datetime.datetime.fromtimestamp(pathlib.Path(os.path.join(path, d)).stat().st_mtime)),'    dir    ',f'{d:50}')

    for d in files:
        print((datetime.datetime.fromtimestamp(pathlib.Path(os.path.join(path, d)).stat().st_mtime)),'    fil    ',f'{d:50}','size:',os.path.getsize(os.path.join(path, d)))

def mymkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def mygrep(list):
    if os.path.isfile(list[0]):
        pattern=re.compile(list[1])
        for i, line in enumerate(open(list[0])):
            for match in re.finditer(list[1], line):
                print('Found on line %s: %s' % (i+1, line))
    else:
        print('%s is not a path to a file' %(list[0]))
        sys.exit()

def access(dirs, input_path, pattern):
    for d in dirs:
        if re.findall(pattern, d):
            print(os.path.join(input_path, d))
        file1=[d1 for d1 in os.listdir(os.path.join(input_path, d)) if os.path.isfile(os.path.join(os.path.join(input_path, d), d1))]
        dir1=[d1 for d1 in os.listdir(os.path.join(input_path, d)) if not os.path.isfile(os.path.join(os.path.join(input_path, d), d1))]
        access(dir1, os.path.join(input_path, d), pattern)
        for f in file1:
            if re.findall(pattern, f):
                print(os.path.join(input_path, f))
    return

def myfind(list):
    input_path = list[0]
    pattern=re.compile(list[1])
    files = [d for d in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, d))]
    dirs = [d for d in os.listdir(input_path) if not os.path.isfile(os.path.join(input_path, d))]

    access(dirs, input_path, pattern)
    for f in files:
        if re.findall(pattern, f):
            print(os.path.join(input_path, f))



parser = argparse.ArgumentParser(description='assignment3')
group = parser.add_mutually_exclusive_group()
group.add_argument('--dir', help='the path to a directory for info of the stuff in it')
group.add_argument('--mkdir', help='the path to a directory to be made')
group.add_argument('--grep', nargs=2, help='the path of file along with the pattern to search for in double quotes is required')
group.add_argument('--find', nargs=2, help='the path of directory along with the pattern to search for in the directory in double quotes is required')
cat = group.add_mutually_exclusive_group()
cat.add_argument('--out', nargs='*', help='the path for files to be output')
cat.add_argument('--new', nargs=2, help='the path for new file along with the content in double quotes')
cat.add_argument('--n', nargs='?', help='print the content of the addressed file along with line number')
cat.add_argument('--o', nargs=2, help='overwriting the contents of second file with the contents of the first file')
cat.add_argument('--a', nargs=2, help='appends the contents of second file with the contents of the first file')

args = parser.parse_args()
if args.dir is not None:
    mydir(args.dir)
elif args.mkdir is not None:
    mymkdir(args.mkdir)
elif args.grep is not None:
    mygrep(args.grep)
elif args.find is not None:
    myfind(args.find)
elif args.out is not None:
    for i in args.out:
        if os.path.isfile(i):
            for line in open(i):
                print(line)
        else:
            print('%s is not a path to a file' %(i))
            sys.exit()
elif args.new is not None:
    if os.path.isfile((args.new)[0]):
        print('%s cannot be a path to a file' %(args.new))
        sys.exit()
    else:
        f = open((args.new)[0], "w")
        f.write((args.new)[1])
        f.close()
elif args.n is not None:
    if os.path.isfile(args.n):
        for i, line in enumerate(open(args.n)):
            print('%s. %s' %(i+1, line))
    else:
        print('%s is not a path to a file' %(i))
        sys.exit()
elif args.o is not None:
    if not (os.path.isfile((args.o)[0])):
        print('wrong path')
        sys.exit()
    else:
        f = open((args.o)[0], "r")
        g = open((args.o)[1], "w")
        g.write(f.read())
        f.close()
        g.close()
elif args.a is not None:
    if not (os.path.isfile((args.a)[0])):
        print('wrong path')
        sys.exit()
    else:
        f = open((args.a)[0], "r")
        g = open((args.a)[1], "a")
        g.write(f.read())
        f.close()
        g.close()