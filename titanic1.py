import numpy as np
import tflearn

from tflearn.datasets import titanic  # taking the dataset for passengers from tflearn database
titanic.download_dataset('titanic_dataset.csv')

from tflearn.data_utils import load_csv
data, labels = load_csv('titanic_dataset.csv', target_column=0,  # target column probably means what network is trying to predict
                        categorical_labels=True, n_classes=2, columns_to_ignore=[2, 7])  # columns_to_ignore is removing name and ticket #, which aren't important
                                    # n_classes is the number of values can choose between -- 0 is die, 1 is live
for p in data:  # converting value of male/female into numbers, 0 = male, 1 = female
    if p[1] == 'female':
        p[1] = 1
    else:
        p[1] = 0

# neural network??
net = tflearn.input_data(shape=[None, 6])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net)  # one type of machine learning

model = tflearn.DNN(net)  # DNN stands for Deep Neural Network model
model.fit(data, labels, n_epoch=100, batch_size=16, show_metric=True)  #  epoch is 1 forward/backward pass with all examples, batch size is # of examples per epoch

dicaprio = [3, 'Jack Dawson', 'male', 19, 0, 0, 'N/A', 5.0000]  # formatted as [class, name, gender, age, sib/sp, par/ch, ticket#, cost]
print ("Person", model.predict([[2, 1, 15, 1, 2, 100.0]])[0][1])  # after learning from the dataset, the network will predict the chance of this person surviving with these stats