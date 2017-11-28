# 3_post_edgeR
"""

post edgeR clean-up and annotation.


"""

import sys, os, glob
from glbase import *

config.draw_mode = 'pdf'
os.chdir('/Users/wuxiaojian/wujian/5_ChengLin/6_SVA_GSE83765/0_data/1_raw/3_post_edgeR')
arr = expression(filename="../2_gc_norm/rawtags_gc_normed.tsv", format={"force_tsv": True,"ensg": 0}, expn="column[1:]")


#user_path = os.path.expanduser("~")
#ensg = glload(os.path.join(user_path,  "project/pre_ips/normalization/" "mm10_ensembl_enst_entrez_76.glb"))
ensg = genelist(filename='/Users/wuxiaojian/Documents/0_script_all/3_ann/1_human/6_geneAnn/hg38_V87/hg38_ensembl_enst_V87.tsv', format = {'force_tsv': True, 'ensg': 0, 'name': 4})
ensg = ensg.removeDuplicates("ensg")


mapped = ensg.map(key="ensg", genelist=arr)
mapped = mapped.removeDuplicates('name')


print arr.getConditionNames()
#最好条件排序,这样有利于后续分析
#sam_order = ['H1dCsy4.lncRNA', 'H1dCsy4.miRNA', 'RIP_H1dCsy4', 'RIP_H1GFP']
#mapped = mapped.sliceConditions(sam_order)
"""
sam_order = ['Diff_0h',  'Diff_1h', 'Diff_4h', 'Diff_8h', 'Diff_12h']
mapped = mapped.sliceConditions(sam_order)

fcd = mapped.norm_multi_fc({'Diff_0h':['Diff_1h', 'Diff_4h', 'Diff_8h', 'Diff_12h']}, pad=0.1)
fcd = fcd.sliceConditions(sam_order)

fcd.setConditionNames(['fc_0h', 'fc_1h', 'fc_4h', 'fc_8h', 'fc_12h'])

print fcd

total = mapped.map(genelist=fcd, key='ensg')
"""
#mapped.save("genes_cpm_expression.glb")
mapped.saveTSV("genes_cpm_expression.tsv")
mapped.boxplot("genes_cpm_expression.png")

"""
fcd.save("genes_fc_expression.glb")
fcd.saveTSV("genes_fc_expression.tsv")
fcd.boxplot("genes_fc_fcd.png")


total.save("genes_fcpm_expression.glb")
total.saveTSV("genes_fcpm_expression.tsv")
total.boxplot("genes_fcpm_fcd.png")
"""
print 'good jobs'
