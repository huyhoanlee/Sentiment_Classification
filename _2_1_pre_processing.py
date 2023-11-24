import underthesea
import string
from _2_0_dictionary import emotion2wordform_dict, wordform2vnese_dict, mispelling_dict, translate_dict, number_dict

#10 Remove stopwords 
def remove_stopwords(input_text, stopwords_file='stopword.txt'):
    # Read the custom stop words from the file
    with open(stopwords_file, 'r', encoding='utf-8') as file:
        stopwords = set(line.strip() for line in file)

    cleaned_words = [word for word in input_text.split() if word.lower() not in stopwords]
    cleaned_text = ' '.join(cleaned_words)

    return cleaned_text

#9 word segmentation
def word_segment(text):
    return underthesea.word_tokenize(text, format="text")

#8 Remove numbers
def remove_numbers(input_string):
    # Use the isalpha() method to filter out numeric characters
    cleaned_string = ''.join(char for char in input_string if not char.isdigit())
    return cleaned_string

#7 
def remove_extra_whitespace(input_string):
    words = input_string.split()
    return ' '.join(words)

#6 Tranform Number to text (8 - tám)
def number2text(sentence):
    words = sentence.split()
    converted_words = [number_dict.get(word, word) for word in words]
    converted_sentence = ' '.join(converted_words)
    return converted_sentence

#5 Transform mispelling words, acronyms, .....(include translate english words)
def translate2word(sentence, dictionary = translate_dict):
    sentence = " " + sentence.strip() + " "
    for key, value_list in dictionary.items():
        for value in value_list:
            sentence = sentence.replace(value, key)
    return sentence

def mispell2word(sentence, dictionary = mispelling_dict):
    sentence = " " + sentence.strip() + " "
    for key, value_list in dictionary.items():
        for value in value_list:
            sentence = sentence.replace(value, key)
    return sentence

#4 Transform word from into vietnamese (colonsmile - cười)
def word_form2Vnese(sentence):
    words = sentence.split()
    converted_words = [wordform2vnese_dict.get(word, word) for word in words]
    converted_sentence = ' '.join(converted_words)
    return converted_sentence

#3 f
def remove_punctuation(input_string):
    # Create a translation table to remove all punctuation characters
    translator = str.maketrans('', '', string.punctuation)
    
    # Use the translate method to remove punctuation
    cleaned_string = input_string.translate(translator)
    
    return cleaned_string

#2 emoticon to word form  ( :) - colonsmile )
def emoticon2word(sentence):
    words = sentence.split()
    converted_words = [emotion2wordform_dict.get(word, word) for word in words]
    converted_sentence = ' '.join(converted_words)
    return converted_sentence

#1 lower case
def lower_case(text):
    return text.lower()

def data_preprocessing(text):
    return word_segment(remove_numbers(remove_extra_whitespace(number2text(translate2word(mispell2word(word_form2Vnese(remove_punctuation(emoticon2word(lower_case(text))))))))))

def remove_white_space_punctuation(text):
    for i in [',','.',':']:
        text = text.replace(' ' + i,i)
    return text
def data_preprocessing_to_txt(text):
    for i in [',','.',':']:
        text = text.replace(i,' ' + i)
    return remove_white_space_punctuation(remove_extra_whitespace(mispell2word(lower_case(text))))

def read_data(data): #hàm cuối cùng khi đọc và xử lí data
    for x in ['train', 'validation', 'test']:
        data[x] = data[x].map(lambda example: {'sentence': data_preprocessing(example['sentence'])})

def read_input(input): #hàm cuối cùng khi đọc và xử lí input sentence
    return data_preprocessing(input)
# sentence = 'cơ hoi'
# print(read_input(sentence))