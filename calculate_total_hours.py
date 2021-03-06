import os
import pandas as pd
import datetime


def make_delta(entry):
    hm = entry.split(':')
    h = hm[0]
    if len(hm) == 1:
        m = 0
    else:
        m = hm[1]
    
    return datetime.timedelta(hours=int(h), minutes=int(m), seconds=0)

if __name__ == '__main__':

	import sys
	filename = sys.argv[1]
	df = pd.read_csv(filename, sep=";")
	df["time"] = df[" hours"].apply(make_delta)
	times = df["time"].sum()
	print(times.total_seconds() / 3600)
