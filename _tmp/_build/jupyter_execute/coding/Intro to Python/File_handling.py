# File handling in Python
``` {index} File handling
```
Suppose we have a text file like below, from which we would like to extract temperature and density data:

$$
# Density of air at different temperatures, at 1 atm pressure
# Column 1: temperature in Celsius degrees
# Column 2: density in kg/m^3
  0.0   999.8425
  4.0   999.9750
 15.0   999.1026
 20.0   998.2071
 25.0   997.0479
 37.0   993.3316
 50.0   988.04
100.0   958.3665
# Source: Wikipedia (keyword Density)
$$

## Python

It is usually best to read and write files using the **with statement** which will improve our syntax and do a lot of things automatically for us (like closing the file we opened).

Our file contains 3 lines at the beginning and 1 line at the end which we do not want to extract. Additionally, the temperature and density values are separated by whitespaces. Here is an example of how we could extract the data into two arrays:

with open('density_water.dat', 'r') as file:  # r for read
    # skip extra lines by taking a slice of the file
    lines = file.readlines()[3:-1]
        
    # initialise 2 empty arrays to store our data
    temp, density = np.zeros(len(lines)), np.zeros(len(lines))
    
    for i in range(len(lines)):
        values = lines[i].split()
        temp[i] = float(values[0])
        density[i] = float(values[1])
        
print(temp)
print(density)

The lines variable in the above example is a list which contains our lines with numbers, but they are stored as a string - they are not recognised as numbers at this point. Note that the temperature and density arrays are already initialised as arrays of specific length, rather than empty lists which we will then append numbers to. It is good practice to initalise arrays like this when we know exactly how many elements our final array will have. The for loop is used to cycle through all elements of our data list. Each ith element is a string, which we split into a new list with the same number of elements as the number of values that are separated by whitespaces in the line - in our case 2. Finally we can assign those values to elements in the temperature and density arrays, but first we converted them from a string to a float.

The below example shows how we could write the data into a text file with, for example here, comma separated values.

with open('output.txt', 'w') as file:  # w for write
    file.write('# Temperature and density data\n')
    for i in range(len(temp)):
        file.write('{},{}\n'.format(temp[i], density[i]))

## NumPy

NumPy's [**genfromtxt**](https://numpy.org/doc/1.18/reference/generated/numpy.genfromtxt.html) (generate from text) function provides full control over the file which we are trying to open. It initialises a numpy array from the data. Some of the parameters include:
    - dtype: set a data type. If not set, determines the data type automatically for each column
    - comments: skips every line starting with a string that is set here. '#' by default.
    - skip_header: number of lines to skip at the beginning of the file
    - skip_footer: number of lines to skip at the end of the file
    - delimiter: the string used to separate values. Any whitespaces, by default.
    
For our file, we do not have to change anything since comments are marked by a # at the beginning of the line and the values are separated by whitespaces.

import numpy as np

data = np.genfromtxt('density_water.dat')
print(data)

We can save our array to a file in multiple ways - examples below. If we plan on using the array in another python code, perhaps it is best to save it as a .npy file. We can later easily load the .npy file and reconstruct the original array. The reader is encouraged to read about **pickling** in Python, which allows any object in Python to be saved in this way, not only numpy arrays.

np.savetxt('data.txt', data)  # save data array to a text file
np.save('data.npy', data)  # save data array to a .npy file

A = np.load('data.npy')

print(A)

## Pandas

Despite its name, panda's [**read_csv**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) can read many different types of files, including our .dat file. Pandas DataFrame is the primary data structure in pandas, so this function will generate one such DataFrame. It is a very powerful object with many capabilities not even implemented in NumPy - deserving of its own notebook.

As in the NumPy example, we specify that our comment lines begin with a '#' and that our delimiter is whitespace(s). Furthermore, we can give names (header) to our columns in the DataFrame, where we assign our list col_names using the names parameter. Pandas' read_csv() by default automatically sets this from the header line in our file, which we do not have in our file so we set header=None.

from pandas import read_csv

col_names = ['temperature', 'density']

df = read_csv('density_water.dat', comment='#', delim_whitespace=True, names=col_names, header=None)
print(df)

df.to_csv('data.csv', index=False)