#falsifieds
#Fake News classification project
#Michael Fedell - Robert Monaco

import csv
import sklearn
import numpy as np 

def read_data(path):
    #Initialize empty dataset
    data = []

    #Open csv specified by path
    with open(path, 'r') as csvf:
        #Read csv file, comma delimeted
        read_file = csv.reader(csvf,delimeter=',')
        
        #append each row in file to dataset
        for row in read_file:
            data.append(row)

    #Return dataset
    return data

def split_data(data):
    #Partition 20% of dataset for testing
    test_data = data[0:int((.2)*len(data))]

    #Set remaining dataset after removing testing examples
    remain_data = data[len(test_data): -1]

    #Set training data to 75% of remaining dataset
    train_data = remain_data[0:int(.75 * len(remain_data))]

    #Set validation data to 25% of remaining dataset
    valid_data = remain_data[len(train_data) : -1]

    #Return train, validation, and test data
    return train_data, valid_data, test_data 

def main():
    #Load news data
    news_data = read_data('data/train.csv')

    #partition data into train, validation, and testing data
    train, valid, test = split_data(news_data)


if __name__ =='__main__':
    main()