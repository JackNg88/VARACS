
import matplotlib.cm as cm
from glbase import *
import os

os.chdir('/home/wuj/wujian/hESc_dif/marker_heatmap')
config.draw_mode = "png"

arr = glload("genes_cpm_expression.glb")

arr.log(2,.1)


gene_lists = {
    "Pluripotency Marker": ['NANOG', 'POU5F1', 'N0DAL', 'TDGF1', 'DPPA2', 'DPPA3', 'DPPA4', 'DPPA5', 'SOX2', 'ZFP42', 'LIN28A', 'SSEA3', 'SSEA3', 'SSEA4', 'LEFTY1', 'DNMT3B', 'EPCAM', 'YCL1A', 'ERAS', 'GDF3', 'SOX15', 'KLF4', 'SALL4', 'NR0B1', 'SALL1', 'DNMT3B', 'ESRRB', 'UTF1', 'CDH1', 'PECAM1', 'STAT3' ],
    'neural': ['PAX6', 'FOXG1', 'EMX2', 'NKX2-1', 'DLX1'],
    'neural_induction_marker': ['NES', 'OTX2', 'PAX6', 'ADRA2A', 'DRD5', 'GRM4', 'POU3F2', 'ADRA2A', 'DRD5'],
    'cardiomyocyte': [],   #"H3K36me":["Bcorl1","Kdm2b","C14orf169","Kdm2a","Kdm4a","Kdm8","Phf8","Setd2","Smyd2","MTF2","Brd1","Brpf1","Cul1","Kdm4a","Kdm4c","Msh6","Setd2"],
    #"H4K16ac":["Kat5","Baz2a","Mcrs1","Sirt1","Nsl1","Sirt2","Vdr"],
    #"H3K56ac":["Sirt2","Sirt6"],
    }

gls = {}
for k in gene_lists:
    gls[k] = genelist()
    gls[k].load_list([{"name": i} for i in gene_lists[k]])
    #print gls[k]

todo = {} # load prepackaged here
todo.update(gls)

for k in todo:
    mm = todo[k].map(genelist=arr, key="name")
    print len(mm)
    #for item in mm:
        #print mm
    mm.saveTSV('heat/%s.tsv'%k)

    mm.heatmap(filename="heat/%s_heat.png" % k, bracket=[4,13],imshow=False, heat_hei=0.009*len(mm),col_cluster=False,row_cluster=False, heat_wid=0.9,size=(12,12),colbar_label="log2(expression value)",col_font_size=6,row_font_size=6)

print 'good jobs'
