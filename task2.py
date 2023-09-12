# parse args
import argparse
import string
import os # to validate path


import json


import re   # for performing operations on string


N = 5


stop_words = [
    'the', 'and', 'in', 'of', 'is', 'a'
]


def analyse_file(file_path):
    '''
    analyse the file with given path

    It is assumed that file_path is valid
    '''


    freqs = {}

    sentences_count = 0
    word_count = 0
    vowels_count = 0
    consonants_count = 0

    # read file
    with open(file_path, 'r') as f:


        content = f.read()

        # every sentence ends with "." There will be space before start of next line
        # so regex will be \.(full stop) then \s+ (1 or more spaces)
        sentences = re.split('\.\s+', content)

        sentences_count = len(sentences)

        word_count = 0


        # split word based on spaces
        words = re.split('\s+', content)

        words_length_sum = 0

        for word in words:


            filtered_word = ''
            # remove all punctuation marks
            for ch in word:
                if ch not in string.punctuation:
                    filtered_word += ch

                    if ch.lower() in 'aeiou':
                        vowels_count += 1
                    elif ch.isalpha():
                        consonants_count += 1

            words_length_sum += len(filtered_word)


            if filtered_word:
                word_count += 1


                if filtered_word.lower() not in stop_words:
                    # increment its frequency
                    if filtered_word in freqs:
                        freqs[filtered_word] += 1

                    # frequency will be zero if occurs first time
                    else:
                        freqs[filtered_word] = 1




    # sort freqs to find most common words
    freqs = dict(sorted(freqs.items(), key=lambda item: item[1]))


    # only chose first N elements
    elements = []

    i = 0

    for word in freqs.keys():
        elements.append(word)

        i += 1
        if i == N:
            break


    return {
        'sentence_count':  sentences_count,
        'word_count': word_count,
        f'most_common_{N}_words': elements,
        'average_word_length': words_length_sum / word_count,
        'vowel_to_consonant_ratio': f'{vowels_count}:{consonants_count}'
    }








if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Perfom analysis on file'
    )

    parser.add_argument(
        '-d', '--directory',
        help='The path to the directory containing the text files for analysis',
        required=True
    )

    parser.add_argument(
        '-o', '--output',
        help='The path to the output report file',
        required=True
    )


    args = parser.parse_args()



    if not os.path.isdir(args.directory):
        print('not a valid directory')
        exit()


    file_count = 0

    results = {}
    for file_name in os.listdir(args.directory):
        file_name = os.path.join(args.directory, file_name)
        results[file_name] = (analyse_file(file_name))
        file_count += 1

    output_file_name = args.output + '.json'
    with open(output_file_name, 'w') as f:
        json.dump({
            'files_analyzed': file_count,
            'result': results
        } , f)


    print('output saved to file ' + output_file_name)






