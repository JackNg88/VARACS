
import sys, os, glob
#import glbase
from glbase import *

os.chdir('/Users/wuxiaojian/wujian/13_DHK_pro/0_datas/1_raw/rsem/human/1_merge')
all = None

conds = []

for f in glob.glob("../0_data/*genes.results"):
    print "ollll"
    #bad
    head = os.path.split(f)[1]
    base = head.replace(".genes.results", "").replace("-", "_")

    tbase = base
    n = 1
    while tbase in conds: # Make sure all condition names are unique.
        tbase = "%s_%s" % (tbase, n)
    base = tbase

    conds.append(base)

    rsem_form = {"name": 0, base: 4,
        "force_tsv": True}

    print "...", base
    #rsem = genelist(filename=f, format=rsem_form)

    # skip the glbase overhead:
    rsem = []
    oh = open(f, "rU")
    for line in oh:
        ll = line.strip().split("\t")
        if not "gene_id" in ll[0]:
            rsem.append({"ensg": ll[0], base: float(ll[4])})

    if not all:
        all = rsem
    else:
        for idx, g in enumerate(all):
            if g["ensg"] == rsem[idx]["ensg"]:
                g[base] = rsem[idx][base]
            else:
                print "Oh dear, not cool"
                sys.exit()
        #all = all.map(key="ensg", genelist=rsem)

cond_names = conds

expn = expression(loadable_list=all, expn=cond_names)
expn.coerce(int)
expn.saveTSV("edgeR_input.tsv")
#expn.save("edgeR_input.glb")

print "Good Jobs!"
