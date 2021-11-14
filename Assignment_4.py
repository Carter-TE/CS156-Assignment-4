"""Assignment 4B

Aurthors:   Carter Edmond
            Kengo Kobayashi
            Dustin Nguyen
"""
import re
import os
import numpy as np
import pandas as pd
import math


def split_train_test (folder_path):
    """Split the data into training and testing data
    """
    files = os.listdir(os.path.abspath(folder_path))
    file_names = list(filter(lambda file: file.endswith('.txt'), files))
    
    df = pd.DataFrame(file_names)
    # approximate 9:1 ratio between training and test split
    mask = np.random.rand(len(df)) <=.9
    training_data = df[mask] #90% extracted
    testing_data = df[~mask] #remaining 10% extracted

    print(f"No. of training examples : {training_data.shape[0]}")
    print(f"No. of testing examples: {testing_data.shape[0]}")
    return training_data, testing_data


def count_words(df, word_dict, dir_path):
    """Counts the total occurences of words given a text file path
    
    :param file_path: Path to text file location
    :param word_dict: Dictionary containing words and accumulated occurrences
    :return dict: Returns dictionary with updated word occurence values
    """

    # Combines all text of files into single string
    text = str()
    for i in range(df.shape[0]):
        try:
            with open(os.path.join(dir_path, df.at[i, 0]), 'r') as f:
                text += f.read()
        except KeyError:
            continue
    
    # Parses text removing punctuation
    chars = re.compile(r"[^a-zA-Z0-9-\s]")
    text = chars.sub("",text)
    
    # Counts the word occurrneces line by line 
    words = text.split()
    for word in words:
        if len(word) < 4:
            continue
        if word in word_dict:
            word_dict[word] += 1
        else: 
            word_dict[word] = 1
    
    return word_dict


def mutual_information(a, b, c, d):
    first_part = ((a*b)/(c*d))
    return (math.log(first_part,2))
           

# Main to test functionality of tokenizer counter
if __name__ == '__main__':
    pos_file_path = input("Input positive file path: ")
    neg_file_path = input("Input negative file path: ")

    # Splits data
    pos_train_data, pos_test_data = split_train_test(pos_file_path)     # data type: dataframe
    neg_train_data, neg_test_data = split_train_test(neg_file_path)

    # Pre Processing
    pos_counts = dict()
    neg_counts = dict()
    pos_ev = dict() 
    neg_ev = dict()

    pos_counts = count_words(pos_train_data, pos_counts, pos_file_path)
    neg_counts = count_words(neg_train_data, neg_counts, neg_file_path)

    pos_word_count = sum(pos_counts.values())
    neg_word_count = sum(neg_counts.values())
    total_words = neg_word_count + pos_word_count

    # Calculates mutual independence of each attribute
    for word in pos_counts:
        if word in(neg_counts.keys()):
            pos_occs = pos_counts[word]
            neg_occs = neg_counts[word]
            pos_mi = mutual_information(pos_occs, total_words, (pos_occs+neg_occs), pos_word_count)
            neg_mi = mutual_information(neg_occs, total_words, (pos_occs+neg_occs), neg_word_count)
            pos_ev[pos_mi] = word 
            neg_ev[neg_mi] = word

    top_pos_ev = list()
    top_neg_ev = list()
    i=0
    while i < 5:
        top_pos_ev.append(pos_ev.pop(max(pos_ev.keys())))
        top_neg_ev.append(neg_ev.pop(max(neg_ev.keys())))
        i+=1
    
    print(top_pos_ev)
    print(top_neg_ev)

            
    


    
    



