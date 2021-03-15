def rw(file):
    with open(file + '.csv') as csv:
        with open(file + '.tsv', 'w') as tsv:
            tmp = csv.read().replace('\",\"', '\"\t\"')\
                            .replace(',true', '\ttrue')\
                            .replace(',false', '\tfalse')\
                            .replace('true,', 'true\t') \
                            .replace('false,', 'false\t')
            tsv.write(tmp)

if __name__ == '__main__':
    rw('ds')