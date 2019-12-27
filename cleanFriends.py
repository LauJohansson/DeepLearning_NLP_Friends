import os
import glob
import ftfy
from collections import Counter
# Preprocess FRIENDS data

# Get a list of all file paths
file_list = glob.glob(os.path.join(os.getcwd(), r"C:\Users\Bruger\Desktop\02456-deep-learning-with-PyTorch-master (2)\02456-deep-learning-with-PyTorch-master\projektet\data", "*.txt"))

corpus = ''

for file_path in file_list:
    with open(file_path) as f_input:
        episode = f_input.read() 
        # Remove unicode-errors
        #episode = unicodedata.normalize("NFKD", episode)
        # Remove newline indicators
        episode = episode.replace('\n', ' ')
        # Remove random backslahses (might not work correctly?)
        episode = episode.replace("\\", '')
        # Make everything lowercase
        episode = episode.lower()
        episode=episode.replace('...',' DRAMATICPAUSE ')
        #Make spaces between characters
        episode=''.join((' {} '.format(el) if el in '()!-[]?' else el for el in episode))
        episode=''.join((' {} '.format(el) if el in '-' else el for el in episode))
        #only space before punktum og komma
        episode=''.join((' {}'.format(el) if el in '.,?!)]' else el for el in episode))
        #only space after
        episode=''.join(('{} '.format(el) if el in '.([' else el for el in episode))
        #Removes double whitespaces
        episode=episode.replace('  ',' ')
        #Removes double whitespaces
        episode=episode.replace('  ',' ')
        
        episode = episode.replace('=', '')
        
        episodestart = episode.find('[ scene')
        episode = episode[episodestart:]
        print(str(episodestart) +'  '+ file_path[-15:])
        # Try fixing UNICODE errors..
        episode = ftfy.fix_text(episode,  normalization='NFKC')
        episode = ftfy.fix_encoding(episode)
        episode = episode.encode('unicode-escape').decode('utf-8')
        
        # Append to big friends corpus
        corpus = corpus + episode


allepisodes = open("allepisodes.txt","w")
allepisodes.write(corpus)


## BELOW PART OF CODE IS ALSO IN COLAB, JUST EASIER TO WORK WITH IN SPYDER
# Add 'unk' to infrequent words (words which only occur once)
corpuslist_nounk = corpus.split()
multiset = Counter(corpuslist_nounk)
singlewords = [x for x in corpuslist_nounk if multiset[x] == 1]

# words and frequencies
common_words_nounk = multiset.most_common()
# Vocab size (before making unk)
len(set(corpuslist_nounk))

corpuslist_withunk = corpuslist_nounk.copy()
for singleword in singlewords:    
    singlewordidx = corpuslist_withunk.index(singleword)
    corpuslist_withunk[singlewordidx] = '<unk>'

multiset_withunk = Counter(corpuslist_withunk)
# words and frequencies
common_words_withunk = multiset_withunk.most_common()
# Vocab size (before making unk)
len(set(corpuslist_withunk))

# Partition Data into training, validation and testing (no leak from training to validation in above code since
# only 1 word frequencies were chosen, would map to 'unk' anyway from code below)
lencorpus = len(corpuslist_withunk)
friends_train = corpuslist_withunk[:int(lencorpus * 0.8)]
friends_valid = corpuslist_withunk[int(lencorpus * 0.8): int(lencorpus*0.9)]
friends_test = corpuslist_withunk[int(lencorpus*0.9):]

# Remove words that don't occur in training from validation and testing
for wordidx in range(len(friends_valid)):
    if friends_valid[wordidx] not in friends_train:
        friends_valid[wordidx] = '<unk>'
        
for wordidx in range(len(friends_test)):
    if friends_test[wordidx] not in friends_train:
        friends_test[wordidx] = '<unk>' 


space = " "
friends_train = space.join(friends_train)
friends_valid = space.join(friends_valid)
friends_test = space.join(friends_test)

friends_traintxt = open("friends_train.txt","w")
friends_validtxt = open("friends_valid.txt","w")
friends_testtxt = open("friends_test.txt","w")
friends_traintxt.write(friends_train)
friends_validtxt.write(friends_valid)
friends_testtxt.write(friends_test)
