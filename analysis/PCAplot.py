'''
this is new pca after andrew changed 2016-05
'''

import numpy as np
from glbase import *
import re, os
from scipy import stats
import sys, os, glob

#import shared
os.chdir('/Users/wuxiaojian/wujian/5_ChengLin/5_lungTPM/3_PCA')
config.draw_mode="pdf"

expn = expression(filename="../2_pre_pca/results/DEgenes_1591.tsv",format={'force_tsv':True,'name':1},expn='column[2:]')
expn.log(2, 1)
SampleName = expn.getConditionNames()

pca = expn.get_pca(feature_key_name=SampleName)
pca.train(20)

pca.explained_variance(filename="loading.png")

print expn.getConditionNames()

cols = []

CTC = ['CTC_2', 'CTC_3', 'CTC_4', 'CTC_5']
noCTC = ['noCTC_6', 'noCTC_7', 'noCTC_8', 'noCTC_9']
GSE74639_CTC = ['GSE74639_CTC_1', 'GSE74639_CTC_2', 'GSE74639_CTC_3', 'GSE74639_CTC_4', 'GSE74639_CTC_5', 'GSE74639_CTC_6', 'GSE74639_CTC_7', 'GSE74639_CTC_8', 'GSE74639_CTC_9', 'GSE74639_CTC_10']
GSE74639_primary = ['GSE74639_primary_1', 'GSE74639_primary_2', 'GSE74639_primary_3', 'GSE74639_primary_4', 'GSE74639_primary_5', 'GSE74639_primary_6']
#endothelial = ['GSE54968_H1_Db0', 'GSE54968_H1_D2', 'GSE54968_H1_D4', 'GSE54968_H1_D8', 'GSE54968_Endothelial', 'GSE54968_HUVEC']
#mesenchymal = ['GSE16256_polyA_RNAseq_h1_msc_rp1', 'GSE16256_polyA_RNAseq_h1_msc_rp2' ]
#trophoblast = ['GSE16256_polyA_RNAseq_h1_tro_rp1', 'GSE16256_polyA_RNAseq_h1_tro_rp2']
#cerebellum = ['GSM2072376_cerebellum_19_weeks', 'GSM2072376_cerebellum_37_weeks' ]

for s in expn.getConditionNames():
    if s in CTC:
        cols.append("red")
    elif s in noCTC:
        cols.append("blue")
    elif s in GSE74639_CTC:
        cols.append("green")
    elif s in GSE74639_primary:
        cols.append("purple")
    #elif s in HE:
        #cols.append("yellow")
    #elif s in mac:
        #cols.append("black")
    #elif s in mesenchymal:
        #cols.append("orange")
    #elif s in neural:
        #cols.append("green")
    #elif s in trophoblast:
        #cols.append('lightgreen')
    #elif s in cerebellum:
        #cols.append('red')
    else:
        cols.append("grey")

#cols = ['grey'] * len(expn.getConditionNames())
conds = expn.getConditionNames()
#cols = shared.get_cols(conds)

pca.scatter(filename="scatter12.png" , x=1, y=2, label=True, spot_cols=cols, spot_size=100)
pca.scatter(filename="scatter13.png" , x=1, y=3, label=True, spot_cols=cols, spot_size=10)
pca.scatter(filename="scatter14.png" , x=1, y=4, label=True, spot_cols=cols, spot_size=10)
pca.scatter(filename="scatter23.png" , x=2, y=3, label=True, spot_cols=cols ,spot_size=10)
pca.scatter(filename="scatter34.png" , x=3, y=4, label=True, spot_cols=cols ,spot_size=10)
pca.scatter(filename="scatter24.png" , x=2, y=4, label=True, spot_cols=cols ,spot_size=10)
#pca.scatter(filename="scatter45.png" , x=4, y=5, label=False, spot_cols=cols )
#pca.scatter(filename="scatter67.png" , x=6, y=7, label=False, spot_cols=cols )
pca.scatter3d(filename="scatter3d123.png" , x=1, y=2, z=3, label=True, spot_cols=cols , stem=True, spot_size= 200)
pca.scatter3d(filename="scatter3d124.png" , x=1, y=2, z=4, label=True, spot_cols=cols , stem=True, spot_size=10)
pca.scatter3d(filename="scatter3d234.png" , x=2, y=3, z=4, label=True, spot_cols=cols , stem=True, spot_size=10)
pca.scatter3d(filename="scatter3d345.png" , x=3, y=4, z=5, label=True, spot_cols=cols , stem=True, spot_size=10)
pca.scatter3d(filename="scatter3d234-v2.png" , x=2, y=4, z=3, label=True, spot_cols=cols , stem=True, spot_size=10)
pca.scatter3d(filename="scatter3d234-v3.png" , x=4, y=2, z=3, label=True, spot_cols=cols , stem=True, spot_size=10)


#num = 50
#for pc in [1, 2, 3, 4, 5]:
    #dd=pca.loading(filename="loading_png/loading_pc%s_top%s.png" % (pc, num), PC=pc, label_key="name", top=num, bot=num)
    #dd.saveTSV(filename="loading_tsv/gene_loading_pc%s_top%s.tsv" % (pc, num))
    #dd.convert_to_Z_score()
    #dd.heatmap("heats/heat_pc%s_top%s.png" %(pc, num), heat_hei=0.8, heat_wid=0.6, bracket=[-2.5, 2.5], col_cluster=False, row_cluster = True, col_font_size=5, row_font_size=5, size=[16, 20])


num = 50
for pc in [1, 2, 3, 4, 5]:
    #dd = pca.explained_variance(filename="loading_png/loading_pc%s_top%s.png" % (pc, num), PC=pc, label_key="name", top=num, bot=num)
    dd = pca.loading(filename="loading_png/loading_pc%s_top%s.png" % (pc, num), PC=pc, label_key="name", top=num, bot=num)
    dd.saveTSV(filename="loading_tsv/gene_loading_pc%s_top%s.tsv" % (pc, num))
    dd.heatmap("heats/heat_pc%s_top%s.png" %(pc, num), heat_hei=0.8, heat_wid=0.6, bracket=[4,12], col_cluster=True, col_font_size=5, row_font_size=5, size=[8, 16])

print 'good jobs'


