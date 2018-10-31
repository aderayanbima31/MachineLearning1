from sklearn import preprocessing


label_encoder = preprocessing.LabelEncoder()

input_classes = ['suzuki', 'ford', 'suzuki', 'toyota', 'ford', 'bmw']

label_encoder.fit(input_classes)

print "\Class mapping:"
for i, item in enumerate(label_encoder.classes_):
    print item, '-->', i