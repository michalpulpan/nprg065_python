
import sys

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def workWithLine(line):
    try:
        queue = []
        data = line.split()
        for i in data:
            if is_number(i): #add number to queue
                queue.append(str(i))
            elif i in ['+', '-', '/', '*']:
                num2 = queue.pop()
                num1 = queue.pop()
                if i is '/' and num2 is '0':
                    print('Zero division')
                    return
                expr = str(num1) + str(i) + str(num2)
                queue.append( int(eval(expr)) )
            else:
                raise
        if len(queue) is not 1:
            raise
        print(queue.pop())
    except:
        print("Malformed expression")
        return


if __name__ == '__main__':

    for line in sys.stdin:
        if line.rstrip():
            workWithLine(line.rstrip())

