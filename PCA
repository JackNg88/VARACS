#pre_filter.py
#filter low

import os
from glbase import *
config.draw_mode = 'pdf'

os.chdir('/Users/wuxiaojian/wujian/5_CTC/2_genes/1_corr_heatmap')

expn = expression(filename='filter_CTCvsnoCTC.tsv', format={'force_tsv': True, 'name': 0,}, expn='column[1:]')


#expn = expn.sliceConditions(['CTC_2', 'CTC_3', 'CTC_4', 'CTC_5', 'noCTC_6', 'noCTC_7', 'noCTC_8', 'noCTC_9'])
base = expn.name
expn = expn.filter_low_expressed(min_expression = 16, number_of_conditions = 1)
expn = expn.removeDuplicates('name')



#corr_heatmap
expn.log(2, 1)
expn.correlation_heatmap(filename='corr_heatmap.pdf', bracket=(0.5,1.0), size = (16, 12), draw_numbers = True, draw_numbers_fmt = '%.2f')
#tree
expn.tree(filename='tree.pdf', color_threshold=0.0,  label_size= 5)
#boxplot
expn.boxplot(filename="box.pdf", size=(15,4))

print 'good jobs'
