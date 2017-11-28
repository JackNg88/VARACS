#gcat.py
#merge SRR*.fastq.gz 成 Hs_Pr11.4.6.fq.gz

import os
import csv

#os.chdir('/Users/wuxiaojian/wujian/5_ChengLin/2_download/1_GSE67980前列腺/geo')

csvfile = file('zlink.sh', mode='rb')
reader = csv.reader(csvfile, dialect= csv.excel_tab)
data = []
for line in reader:
    data.append(line)
csvfile.close()


#keep
keep = {}
for item in data:
    #print item
    #['ln -s fqs/SRR1977992.fastq.gz Hs_Pr11.4.6.fq.gz']
    #bad
    values = item[0].split(' ')
    key = values[-1]
    SRR = values[-2]
    if key not in keep:
        keep[key] = [SRR]
    else:
        keep[key].append(SRR)

#save
oh = open('gcat.sh', mode='w')
for k in keep:
    #print k
    #Hs_PriTum5.fq.gz
    #bad
    mems = keep[k]
    merge = ' '.join(mems)
    oh.write('zcat %s > %s\n' % (merge, k))

oh.close()


print 'good jobs'
