
# import libs
import pandas as pd
import numpy as np
import glob

path = 'data/*'
folder = ['idle/', 'running/', 'stairs/', 'walking/']

all_files = glob.glob(path + "/*.csv")

print(all_files)
#li = []

# print(all_files)

#for filename in all_files:
#    df = pd.read_csv(filename, index_col=None, header=0)
#    li.append(df)

#print(li)
# frame = pd.concat(li, axis=0, ignore_index=True)

#for i in folder:
 #   all_files = glob.glob(path + i + "*.csv")
  #  print(all_files)

#df = pd.read_csv('data/idle/idle-1.csv')
#df.count()
