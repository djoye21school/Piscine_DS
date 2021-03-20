import sys
import psutil


def generator(path):
    for row in open(path):
        yield row


def main(path):
    for line in generator(path):
        pass
    memory = psutil.Process().memory_info().peak_wset/2.0**30
    cpu = psutil.Process().cpu_times()
    print(f'Peak Memory Usage = {memory:.3} Gb')
    print(f'User Time + System Time = {cpu.user + cpu.system:.2f}s')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
