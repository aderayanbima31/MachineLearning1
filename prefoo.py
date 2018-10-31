import numpy as np

from sklearn import preprocessing

# We imported a couple of packages. Let's create some sample data and add the line to this file:

input_data = np.array([[3, -1.5, 3, -6.4], [0, 3, -1.3, 4.1], [1, 2.3, -2.9, -4.3]])

# Process standarisasi
data_standarized = preprocessing.scale(input_data)
print "\nMean =", data_standarized.mean(axis=0)
print "Std deviation =", data_standarized.std(axis=0)

# Binarization Process
data_binarized = preprocessing.Binarizer(threshold=1.4).transform(input_data)
print "\nBinarized data =", data_binarized


# One Hot Encoding
encoder = preprocessing.OneHotEncoder()

encoder.fit([[0, 2, 1, 12], [1, 3, 5, 3], [2, 3, 2, 12], [1, 2, 4, 3]])

encoded_vector = encoder.transform([[2, 3, 5, 3]]).toarray()

print "\nEncoded vector =", encoded_vector
