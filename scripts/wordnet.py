
# from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
# from sklearn.feature_extraction.text import CountVectorizer

# import pandas, numpy, textblob, string
#xgboost
#from keras.preprocessing import text, sequence
#from keras import layers, models, optimizers

from nltk.corpus import wordnet
import csv
import pandas as pd

with open('CCglossaryWiki.txt', 'r') as f:
    reader = csv.reader(f)
    firstlist = list(reader)

#print(firstlist) # has to stay as it contains original words


seplist = []
for term in firstlist:
    for ele in term:
        seplist.append(str(ele).split(' '))

flatten_list = list(set([item for subl in seplist for item in subl]))
# original words seperated, doubles taken out 

#print(flatten_list)

syn_list = []
for word in flatten_list:
    syns = wordnet.synsets(word)
    listi = [] # synonyms
    for i in range(len(syns)):
        listi.append(syns[i].lemmas()[0].name())
    syn_list.append(list(set(listi)))
        
#print(syn_list) # list with synonymous



# bring all three lists together, save as new csv_file

newlist1 = firstlist + flatten_list + syn_list
newlist2 = list(set([item for subl in newlist1 for item in subl])) # delete duplicates

newlist = []
for i in newlist2:
    if len(i) > 1:
        newlist.append(i)

#print(newlist)

df = pd.DataFrame(newlist)
df.to_csv('CCglossaryComplete.csv', index=False)



print ("Obirgada Carlos | Gracias Neele")