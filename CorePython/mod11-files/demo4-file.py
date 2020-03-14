import sys

f = open(sys.argv[1], mode='rt', encoding='utf-8')
for line in f:
    sys.stdout.write(line)
    # print(line)
f.close()

# python demo4-file.py wasteland.txt
