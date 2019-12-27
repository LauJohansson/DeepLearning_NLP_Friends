import ftfy
from collections import Counter
# load seinfeld data
seinfeldall = open(r'C:\Users\Bruger\Desktop\02456-deep-learning-with-PyTorch-master (2)\02456-deep-learning-with-PyTorch-master\projektet\seinfelddata.txt', encoding="utf8").read()

def cleanDataLikeFriends(txtdata):
      ## Clean data in the same way as for friends
    txtdata = txtdata.replace('\n', ' ')
    # Remove random backslahses (might not work correctly?)
    txtdata = txtdata.replace("\\", '')
    # Make everything lowercase
    txtdata = txtdata.lower()
    txtdata=txtdata.replace('...',' DRAMATICPAUSE ')
    #Make spaces between characters
    txtdata=''.join((' {} '.format(el) if el in '()!-[]?' else el for el in txtdata))
    txtdata=''.join((' {} '.format(el) if el in '-' else el for el in txtdata))
    #only space before punktum og komma
    txtdata=''.join((' {}'.format(el) if el in '.,?!)]' else el for el in txtdata))
    #only space after
    txtdata=''.join(('{} '.format(el) if el in '.([' else el for el in txtdata))
    #Removes double whitespaces
    txtdata=txtdata.replace('  ',' ')
    #Removes double whitespaces
    txtdata=txtdata.replace('  ',' ')
    # Remove '='
    txtdata = txtdata.replace('=', '')
    # Try fixing UNICODE errors..
    txtdata = ftfy.fix_text(txtdata,  normalization='NFKC')
    txtdata = ftfy.fix_encoding(txtdata)
    txtdata = txtdata.encode('unicode-escape').decode('utf-8')
    return txtdata

# Clean the data
seinfeldall = cleanDataLikeFriends(seinfeldall).split()

# replace one-time occuring words with <unk>
corpuslist_nounk = seinfeldall
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


# Partition into training, validation and testing
seinfeldtrain = corpuslist_withunk[:int(len(corpuslist_withunk)*0.8)]
seinfeldvalid = corpuslist_withunk[int(len(corpuslist_withunk)*0.8) : int(len(corpuslist_withunk)*0.9)]
seinfeldtest = corpuslist_withunk[int(len(corpuslist_withunk)*0.9):]


# Remove words that don't occur in training from validation and testing
for wordidx in range(len(seinfeldvalid)):
    #print(wordidx)
    if seinfeldvalid[wordidx] not in seinfeldtrain:
        print(seinfeldvalid[wordidx])
        seinfeldvalid[wordidx] = '<unk>'

# Remove words that don't occur in training from validation and testing
for wordidx in range(len(seinfeldtest)):
    if seinfeldtest[wordidx] not in seinfeldtrain:
        print(seinfeldtest[wordidx])
        seinfeldtest[wordidx] = '<unk>'
space = " "
seinfeldtrain = space.join(seinfeldtrain)
seinfeldvalid = space.join(seinfeldvalid)
seinfeldtest = space.join(seinfeldtest)

seinfeld_traintxt = open("seinfeldtrainclean.txt","w")
seinfeld_validtxt = open("seinfeldvalidclean.txt","w")
seinfeld_testtxt = open("seinfeldtestclean.txt","w")
seinfeld_traintxt.write(seinfeldtrain)
seinfeld_validtxt.write(seinfeldvalid)
seinfeld_testtxt.write(seinfeldtest)


