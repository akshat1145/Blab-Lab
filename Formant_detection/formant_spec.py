import csv
import numpy
import matplotlib.pyplot as plt
import pandas
colnames = ['F1', 'F2', 'F3']
data = pandas.read_csv('data/ExamplePredictions2.csv',  skipinitialspace=True, usecols=colnames)

F1 = data.F1.tolist()
F2 = data.F2.tolist()
F3 = data.F3.tolist()	
print(data)
plt.plot(data)
plt.ylabel('formants-F1,F2,F3')
plt.show()
plt.imshow(numpy.transpose(data), extent=[0,2,0,3000], cmap='Greys',
           vmin=00, vmax=3000, origin='lowest', aspect='auto')
plt.colorbar()
plt.show()