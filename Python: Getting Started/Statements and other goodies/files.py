'''
    open(file, mode, encoding)

'''
import sys


def main(filename):
    f = open(filename, mode="rt", encoding='utf-8')
    for line in f:
        sys.stdout.write(line)
    f.close()


if __name__ == '__main__':
    # main(sys.argv[1])
    pass


f = open('wasteland.txt', mode='wt', encoding='utf-8')
f.write('Test this shit \n')
f.write('this is the second line \n\n')
f.write('fin\n')
f.close()

g = open('wasteland.txt', mode='rt', encoding='utf-8')
print(g.readlines())
g.close()


h = open('wasteland.txt', mode='at', encoding='utf-8')
h.writelines(["This is one \n", "This is scnd \n"])
h.close();

# Alternativ Schließt den Handle automatisch wieder:

with open('wasteland.txt', mode='rt', encoding='utf-8') as f:
    print(f.readlines())