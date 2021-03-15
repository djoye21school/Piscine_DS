import sys


def encode(string, shift):
    try:
        string.encode('ascii')
    except UnicodeEncodeError:
        raise ValueError("the string contains more than just ascii")

    lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    result = ""
    for i in string:
        if i in lower:
            result += lower[(lower.index(i) + shift) % 26]
        elif i in upper:
            result += upper[(upper.index(i) + shift) % 26]
        else:
            result += i
    return result


if __name__ == '__main__':
    if len(sys.argv) == 4:
        if sys.argv[1] == 'encode':
            print(encode(sys.argv[2], int(sys.argv[3])))
        elif sys.argv[1] == 'decode':
            print(encode(sys.argv[2], -int(sys.argv[3])))
        else:
            print('incorrect operation or option')
    else:
        print('invalid number of arguments', len(sys.argv))
