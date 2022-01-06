import numpy as np
import pandas as pd

stime = time.time()
data = pd.read_csv('/content/Dataset_1.csv', delimiter='    ', header=None, engine='python')
sostream_data = SOStream()
c = 0
for r in data.values:
    c += 1
    sostream_data.process(r)
    if c%100:
      fadingAll(sostream_data.M[-1], sos)
x = []
for i in sostream_data.M[-1]:
  x.append(i.centroid)
result = np.array(x)

print(f"process time : {time.time() - stime)} second")
print(f"cluster numbers : {len(sos.M[-1])}")
print(f"faded cluster : {sostream_data.merge_number}")
print(f"merged cluster : {sostream_data.fade_number}")
