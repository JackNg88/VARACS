#scatter_color.py
#做带颜色的scatter
import scipy.stats
import seaborn as sns
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

os.chdir('/Users/wuxiaojian/wujian/5_ChengLin/2_genes/5_MAplot/2_MAplot')


def scatter_color(data=None, cond1=None, cond2=None):
    #plot colorful scatter plot
    sns.set_style('ticks')
    fig = plt.figure(figsize=(9,8))
    color = ['grey'] * len(data.index)
    size = [10] * len(data.index)
    up = []
    dn = []
    for idx,g  in enumerate(data.index):
        #g #'Nkg7'
        x = data.ix[g, cond1]  #-3.82
        y = data.ix[g, cond2]  #5.91
        if x - y >= 1 and x >= 4 :
            color[idx] = 'r'
            size[idx] = 20
            up.append(g)
        elif x - y <= -1 and y >= 4:
            color[idx] = 'b'
            size[idx] =20
            dn.append(g)  #dn #['Nkg7']


    #up[0:5]    #['Tgfbr1', 'Mrpl54', '1810032O08Rik', 'Dclre1c', 'Cxcr4']
    #color[0:5] #['b', 'b', 'b', 'b', 'b']
    #size[0:5]  #[20, 20, 20, 20, 20]
    plt.scatter(data.ix[:, cond1], data.ix[:, cond2], color=color, s=size, alpha=.6, edgecolor='none')
    c1 = list(data.ix[:, cond1].values)
    c2 = list(data.ix[:, cond2].values)

    r = scipy.stats.linregress(c1[:100], c2[:100])[2]
    r2 = r**2
    print r2
    plt.xlabel(cond1)
    plt.ylabel(cond2)
    plt.xlim(-1, 16)
    plt.ylim(-1, 16)
    plt.title('R = %.3f'%r2)
    plt.savefig('%s_vs_%s.pdf'%(cond1, cond2))
    plt.close()

    upv = data.ix[up]
    dnv = data.ix[dn]
    print len(up), len(dn)
    #save
    upv.to_csv('up_%s_vs_%s.csv'%(cond1, cond2))
    dnv.to_csv('dn_%s_vs_%s.csv'%(cond1, cond2))
    return upv, dnv


#load data
data = pd.read_csv('../1_pre_MAplot/mean_CTCvsnoCTC.tsv', index_col= 'name', sep = '\t')
#del data['ensg']

#log2 data
#data = np.log2(data.drop('name', axis= 1) +1)
data = np.log2(data +1)

#cond1 = 'X0909SP..KZ_no_rRNA';cond2 = 'X0909T..KZ_no_rRNA'
scatter_color(data= data, cond1='CTC', cond2='noCTC')
#scatter_color(data= data, cond1='X0909T..KZ_no_rRNA', cond2='ES0416SP..NKZ_no_rRNA')


print 'good jobs'

