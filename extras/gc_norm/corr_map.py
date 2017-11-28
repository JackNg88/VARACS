
from glbase import *
import os
config.draw_mode = 'pdf'
os.chdir('/Users/wuxiaojian/wujian/13_DHK_pro/0_datas/1_raw/rsem/human/4_corr_map')

#arr = glload("../3_post_edgeR/genes_cpm_expression.glb")
arr = expression(filename='../3_post_edgeR/genes_cpm_expression.tsv', format={'force_tsv': True, 'ensg': 0, 'name': 1,}, expn='column[2:]')
print repr(arr)

arr.log(2, pad=1)

arr.boxplot(filename="box.png", size=(15,4))
arr.hist("hist.png", suppress_zeros=False)
arr.tree(filename="tree.png", color_threshold=0.0, label_size=5)
arr.correlation_heatmap(filename="corr_heatmap.png", bracket=(0.0,1), size=(16,12),draw_numbers = True , draw_numbers_fmt='%.2f')


# Do scatters.
for i, c1 in enumerate(arr.getConditionNames()):
    for o, c2 in enumerate(arr.getConditionNames()):
        if o > i:
            arr.scatter(c1, c2, filename = 'scatters/%s_vs_%s.png' % (c1, c2), do_best_fit_line = True, print_correlation = 'r2')

print 'good jobs'
