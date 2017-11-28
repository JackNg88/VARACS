#my_marker_heatmap
import matplotlib.cm as cm
from glbase import *
import os

os.chdir('/Users/wuxiaojian/wujian/5_CTC/2_genes/12_METmarker_heat')
config.draw_mode = 'pdf'

expn = expression(filename= '../0_data/filter_CTCvsnoCTC.tsv', format = {'force_tsv': True, 'name': 0,}, expn = 'column[1:]')

#sort
samples = ['noCTC_6', 'noCTC_7', 'noCTC_8', 'noCTC_9', 'CTC_2', 'CTC_3', 'CTC_4', 'CTC_5']
expn = expn.sliceConditions(conditions=samples)

gene_list = {
    #"prostate": ['AR', 'KLK3', 'KLK2', 'FOLH1', 'UGT2B15', 'AMACR'],
    #'bloodMarker': ['CD19', 'PTPRC', 'CD3G', 'MS4A1', 'IL3RA', 'CD33', 'CD274', 'CD22'],
    'eplthelial': ['EPCAM', 'CDH1', 'KRT8', 'KRT18', 'KRT19', 'KRT5', 'KRT14'],
    'mesenchymal': ['CDH2', 'SNAI1', 'TWIST1', 'TWIST2', 'CDH11', 'FN1', 'VIM', 'SERPINE1'],
    'stem cell': ['ALDH1A1', 'ALDH1A2', 'ALDH7A1', 'CD44', 'PROM1', 'ABCG2', 'NANOG', 'KIT', 'NES', 'ITGA2', 'POU5F1', 'KLF4', 'SOX2', 'MYC'],
    'proliferation': ['MKI67', 'BIRC5', 'AURKA', 'MYBL2', 'CCNB1','CCND1'],
}

gls = {}
for k in gene_list:
    #print k
    gls[k] = genelist()
    gls[k].load_list([{'name': i} for i in gene_list[k]])

todo = {} # load prepackaged here
todo.update(gls)

for k in todo:
    print k
    #d

    mm = todo[k].map(genelist = expn, key = 'name')
    print len(mm)
    mm.saveTSV('results/%s.tsv' % k)

    mm.convert_to_Z_score()
    #mm.log(2, 1)
    #mm.saveTSV('results/log2_%s.tsv' % k)
    mm.heatmap(filename = 'results/%s.pdf' % k, bracket = [-1.5, 1.5], imshow = False, heat_hei = 0.01 * len(mm), heat_wid = 0.15, col_cluster = False, row_cluster = True, size = (12, 8), colbar_label = 'z-Score', col_font_size = 8, row_font_size = 6, grid = True)


print 'good jobs'
