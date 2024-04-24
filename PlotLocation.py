import csv
import matplotlib.pyplot as plt
import numpy as np

from class1 import my_class


data = []

with open('gt_5DoF_gnss.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            line_count += 1
            data.append(datapoint(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21]))
    print(f'Processed {line_count} lines.')


xlocpoints = np.array([])
ylocpoints = np.array([])

for obj in data:
    xlocpoints = np.append(xlocpoints, float(obj.xenu))
    ylocpoints = np.append(ylocpoints, float(obj.yenu))
    

print(xlocpoints)

plt.plot(xlocpoints, ylocpoints, 'o')
plt.xlabel("x enu (m)")
plt.ylabel("y enu (m)")
plt.show() 
