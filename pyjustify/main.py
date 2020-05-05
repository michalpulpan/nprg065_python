import sys

def lineLenParser():
    try:
        num = sys.argv[1]
        if num.isdigit() and int(sys.argv[1]) > 0:
            return int(sys.argv[1])
        else:
            raise
    except:
        print('Error')
        exit(0)



if __name__ == '__main__':
    line_len = lineLenParser()
    lines = []
    for line in sys.stdin:
        if line.rstrip():
            lines.append(line)