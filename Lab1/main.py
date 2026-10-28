import pandas as pd

# option 2.1.1 read in all at once
data = pd.read_excel("nhanes_matlab.xlsx")

# option 2.1.2 read in chunks
chunksize = 50
reader = pd.read_csv("nhanes_matlab.csv", chunksize=chunksize)

# read the first chunk
first_chunk = next(reader)
print(first_chunk)

# read the second chunk
second_chunk = next(reader)
print(second_chunk)
