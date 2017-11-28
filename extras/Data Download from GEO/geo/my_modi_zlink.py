o=open('sra_result.csv','rU')
keep=[]
for line in o:
    if 'Experiment Accession' in line:
        continue
    line=line.strip().split(',')  #['SRX764814', 'GSM1551473: GTtoH_input; Homo sapiens; ChIP-Seq', 'Homo sapiens',]
    title=line[1].replace('"','').replace(' Mus musculus;','').replace(' Homo sapiens;','')  #'GSM1551473: GTtoH_input; ChIP-Seq'
    #print title
    keep.append(title)
    #bad
o.close()
print keep  #['GSM1551473: GTtoH_input; ChIP-Seq', 'GSM1551472: GTtoH_H3K27ac; ChIP-Seq', ...]

newlink=[]
o=open('zlink.sh','rU')
for rline in o:
    line=rline.strip().split(' ')  #['ln', '-s', 'fqs/SRR1145834.fastq.gz', 'Hs_Islet_H3K27ac_ChIP-Seq.fq.gz']
    gsm=line[3].replace('Mm_','').replace('Hs_','').replace('.fq.gz','').replace('.p1','').replace('.p2','').split('_')[0]  #Islet
    #print gsm
    #bad
    for item in keep:
        #keep
        #['GSM1551473: GTtoH_input; ChIP-Seq', 'GSM1551472: GTtoH_H3K27ac; ChIP-Seq',...]
        #item #'GSM1316300: ES_D0_H3K27ac_rep1; ChIP-Seq'
        if gsm in item:
            new=item.split(': ')[1].replace('; ','_').replace(' ','_').replace('_RNA-Seq','')
            print gsm,new
            #Islet
            #Islet_H3K27ac_ChIP-Seq
    rline=rline.replace('%s'%gsm,'%s'%new)
    newlink.append(rline)
o.close()

o=open('zlink.sh','w')
for item in newlink:
    o.write(item)
o.close()
