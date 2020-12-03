
import csv
import string



# open sentences of articles, split into single words and remove punctuation
with open('articles.csv', 'r') as f:
    reader = csv.reader(f)
    sentences = list(reader)

table = str.maketrans(dict.fromkeys(string.punctuation))
sent_clean = []
for sentence in sentences:   
    words = str(sentence)  #.split(' ')
    cleanwords1 = words.translate(table)
    cleanwords = cleanwords1.split(' ')
    sent_clean.append(cleanwords)
       
#print(sent_clean)


# load glossary of CC words
with open('CCglossaryComplete.csv', 'r') as f:
    reader = csv.reader(f)
    glossary1 = list(reader)
    
glossary = list(set([item for subl in glossary1 for item in subl]))

#print(glossary)

# count occurence of glossary words in each sentence
countlist = []
for sentence in sent_clean:
    count = 0
    for word in sentence:
        for key in glossary:
            if key == word:
                count += 1
    #print(count)
    countlist.append(count)
    
#print(len(countlist)) # for each sentence we have a count now

# how many words has each sentence?
sent_len = []
for sentence in sent_clean:
    sent_len.append(len(sentence))
    

# get ratio of CC words per sentence
ratio = []
for i in range(len(countlist)):
    ratio.append(countlist[i]/sent_len[i])
        
#print(ratio)

# print the sentences which ratio of CC words > 0.3
for i in range(len(ratio)):
    if ratio[i] > 0.3:
        print(sentences[i])
            

print("goy away corona")