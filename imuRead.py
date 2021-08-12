import numpy as np
import time

a = []


with open('imu_data.txt') as f:
    x = f.read().split('\n')[2:]
    splited_data = [[j.strip() for j in jy] for jy in [i.split('\t') for i in x]]
    splited_data = splited_data[:len(splited_data)-1]
    

# print(splited_data[0])

time_list =[]
feature_list = [[],[],[],[],[],[],[],[],[]]

for s in splited_data:
    time_list.append(time.strftime(s[1]))
    for i in range(2,11):
        feature_list[i-2] = float(s[i])

feature_list.append(time_list)
# print(time.strftime('14:08:06.818'))

np.save('imu_data.npy',feature_list)

# s = splited_data[:len(splited_data)-1]
# print(s[len(s)-1])
    