"""
Simple demo of a horizontal bar chart.
"""
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import pandas as pd
import os, glob
os.chdir('/Users/wuxiaojian/wujian/5_CTC/2_genes/6_goseq/4_kegg_bar/CTChigh')


#load
#data = pd.read_csv('data/ac/Cip.csv', index_col= 'ensg', sep = '\t')
for f in glob.glob('CTChigh-KEGG.csv'):
    print f
    #bad
    head = os.path.split(f)[1]
    base = head.replace('.csv', '')

    data = pd.read_csv(f, index_col= 0, sep= ',')
    data = data.loc[:, ['PValue']]
    log = -np.log10(data)  #取-log10
    people = log.index
    y_pos = np.arange(len(people))
    performance = np.array(log)


    #plot
    fig, ax = plt.subplots()

    color = {'Cip': 'purple', 'F7': 'blue', 'OKSM': 'yellow', 'OSK': 'green',}

    ax.barh(y_pos, performance, align='center',color= 'red', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people, )  #minor = True
    ax.invert_yaxis()  # labels read top-to-bottom
    #ax.set_xlabel('Performance')
    ax.set_xlabel('-log10(P)')
    ax.set_title('KEGG analysis of %s' % base)


    #save as pdf
    #plt.show()
    fig.savefig('%s.pdf' % base)

print 'good jobs'

