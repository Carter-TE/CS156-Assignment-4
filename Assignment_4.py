"""Assignment 4B

Aurthors:   Carter Edmond
            Kengo Kobayashi
            Dustin Nguyen
"""

import os

def count_words(dir_path, word_dict):
    """Counts the total occurences of words given a text file path
    
    :param file_path: Path to text file location
    :param word_dict: Dictionary containing words and accumulated occurrences
    :return dict: Returns dictionary with updated word occurence values
    """
    with os.scandir(dir_path) as paths:
        lines = list()
        for path in paths:
            with open(path, 'r') as file:
                lines = lines + [line.strip() for line in file]
        
    # Counts the word occurrneces line by line
    for line in lines:
        words = line.split()
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else: 
                word_dict[word] = 1
    
    return word_dict
           

# Main to test functionality of tokenizer counter
if __name__ == '__main__':
    file_path = 'pos/'
    counts = dict()
    counts = count_words(file_path, counts)

    print(len(counts.keys()))
    print(max(counts, key=counts.get))

    for key in counts.keys():
        if(counts[key] < 50):
            continue
        print(key+ ":\t" + str(counts[key]))

    
    



