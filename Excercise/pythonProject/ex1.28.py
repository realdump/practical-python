import gzip
with gzip.open('/home/abdul/Documents/GitHub/practical-python/Work/Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')