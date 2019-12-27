import ftfy

# load wiki data
wikitrain = open(r'C:\Users\Bruger\Desktop\02456-deep-learning-with-PyTorch-master (2)\02456-deep-learning-with-PyTorch-master\projektet\wikitext-2\wikitrain.txt', encoding="utf8").read()
wikivalid = open(r'C:\Users\Bruger\Desktop\02456-deep-learning-with-PyTorch-master (2)\02456-deep-learning-with-PyTorch-master\projektet\wikitext-2\wikivalid.txt', encoding="utf8").read()
wikitest = open(r'C:\Users\Bruger\Desktop\02456-deep-learning-with-PyTorch-master (2)\02456-deep-learning-with-PyTorch-master\projektet\wikitext-2\wikitest.txt', encoding="utf8").read()

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

# Clean training, testing and validation wiki data
wikitrain = cleanDataLikeFriends(wikitrain).split()
wikivalid = cleanDataLikeFriends(wikivalid).split()
wikitest = cleanDataLikeFriends(wikitest).split()

# Remove words that don't occur in training from validation and testing
#for wordidx in range(len(wikivalid)):
#    #print(wordidx)
#    if wikivalid[wordidx] not in wikitrain:
#        print(wikivalid[wordidx])
        #wikivalid[wordidx] = '<unk>'

# Remove words that don't occur in training from validation and testing
#for wordidx in range(len(wikitest)):
#    if wikitest[wordidx] not in wikitrain:
#        print(wikitest[wordidx])
        #wikitest[wordidx] = '<unk>'
space = " "
wikitrain = space.join(wikitrain)
wikivalid = space.join(wikivalid)
wikitest = space.join(wikitest)

wiki_traintxt = open("wikitrainclean.txt","w")
wiki_validtxt = open("wikivalidclean.txt","w")
wiki_testtxt = open("wikitestclean.txt","w")
wiki_traintxt.write(wikitrain)
wiki_validtxt.write(wikivalid)
wiki_testtxt.write(wikitest)


for  i in range(10):
    print (i > 0)