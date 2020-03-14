import sys


def read_series(filename):
    # series = []
    # try:
    #     f = open(filename, mode='rt', encoding='utf-8')
    #     for line in f:
    #         a = int(line.strip())
    #         series.append(a)
    # finally:
    #     f.close()
    # return series
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        return [int(line.strip()) for line in f]
    finally:
        f.close()


def main(filename):
    series = read_series(filename)
    print(series)


if __name__ == '__main__':
    main('demo5-out.txt')
