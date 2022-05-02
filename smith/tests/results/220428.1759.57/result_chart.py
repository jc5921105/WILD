import pdb, json
import numpy as np
import matplotlib.pyplot as plt


with open('results.json') as fobj:
    data = json.load(fobj)

#pdb.set_trace()

#Get Total Accuracy

jaro_search_accuracy = 0
lcs_search_accuracy  = 0
hd_search_accuracy   = 0
s_search_accuracy    = 0
v_search_accuracy    = 0
cs_search_accuracy   = 0
dld_search_accuracy  = 0
jw_search_accuracy   = 0
search_accuracy      = 0


for x in data.keys():
    jaro_search_accuracy += data[x]['jaro_search_accuracy']
    lcs_search_accuracy  += data[x]['lcs_search_accuracy']
    hd_search_accuracy   += data[x]['hd_search_accuracy']
    s_search_accuracy    += data[x]['s_search_accuracy']
    v_search_accuracy    += data[x]['v_search_accuracy']
    cs_search_accuracy   += data[x]['cs_search_accuracy']
    dld_search_accuracy  += data[x]['dld_search_accuracy']
    jw_search_accuracy   += data[x]['jw_search_accuracy']
    search_accuracy      += data[x]['search_accuracy']

#pdb.set_trace()

jaro_search_accuracy = jaro_search_accuracy / len(data.keys())
lcs_search_accuracy  = lcs_search_accuracy / len(data.keys())
hd_search_accuracy   = hd_search_accuracy / len(data.keys())
s_search_accuracy    = s_search_accuracy / len(data.keys())
v_search_accuracy    = v_search_accuracy / len(data.keys())
cs_search_accuracy   = cs_search_accuracy / len(data.keys())
dld_search_accuracy  = dld_search_accuracy / len(data.keys())
jw_search_accuracy   = jw_search_accuracy / len(data.keys())
search_accuracy      = search_accuracy / len(data.keys())


plt.style.use('ggplot')
search = ['Jaro Similarity',
          'Longest Common Subsequence',
          'Hamming Distance',
          'Levenshtein Distance',
          #'Vague WILD',
          'Cosine Similarity',
          'Damerau Levenshtein',
          'Jaro Winkler',
          'WILD']
          
search = [
          'Levenshtein Distance',
          'Damerau Levenshtein',
          'Hamming Distance',
          'Longest Common Subsequence',
          'Jaro Similarity',
          'Jaro Winkler',
          'Cosine Similarity',
          'W.I.L.D.'
          ]
accuracy = [jaro_search_accuracy,
            lcs_search_accuracy,
            hd_search_accuracy,
            s_search_accuracy,
            #v_search_accuracy,
            cs_search_accuracy,
            dld_search_accuracy,
            jw_search_accuracy,
            search_accuracy,
            ]
            
accuracy = [
            s_search_accuracy,
            dld_search_accuracy,
            hd_search_accuracy,
            lcs_search_accuracy,
            jaro_search_accuracy,
            jw_search_accuracy,
            cs_search_accuracy,
            search_accuracy,
            
            
            ]
#c = ['red','blue','green','purple']
#c = ['b','g','r','c','m','y','k','w']
c = ['b']
# Plot bar chart
ax = plt.subplot()
#plt.grid(True)
plt.bar( search, accuracy,width=.4, color= c)

for i in range(len(search)):
    plt.text(i - .2,accuracy[i],'{:.2f}%'.format(accuracy[i]))


# Rotate labels
ax.set_xticklabels(search, rotation=20, ha='left', rotation_mode='anchor')
#ax.set_xticklabels(activities, rotation='vertical', ha='right', rotation_mode='anchor')
ax.set_xlabel('Search Types', fontsize=12)
ax.set_ylabel('Accuracy Percentage', fontsize=12)
ax.xaxis.tick_top()
# display chart
#plt.legend(['one','two'])
plt.title('Search Accuracy Results')
plt.ylim((0,100))
plt.tight_layout()
plt.show()