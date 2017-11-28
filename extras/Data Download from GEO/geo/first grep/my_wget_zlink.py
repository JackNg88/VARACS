import time

wget={}
zlink={}
LibraryLayout={}
species={}
o=open('SraRunInfo.csv','rU')
for line in o:
    if 'Run' in line:
        continue
    line=line.strip().split(',')
    #['SRR1145795', '2015/7/22'....]
    #libraryName=line[11].split(':')[1][1:]
    print len(line)
    libraryName=line[29] #use this when the former is empty
    #'GSM1316300'
    #if 'hESC' not in libraryName: # This is because I only need hESCs data
    #    continue
    wget.setdefault(line[9],libraryName)
    #line[9] #'https://sra-download.ncbi.nlm.nih.gov/srapub/SRR1145795'
    #{'https://sra-download.ncbi.nlm.nih.gov/srapub/SRR1145795': 'GSM1316300'}


    sra='SRR'+line[9].split('SRR')[-1]  #'SRR1145795'
    zlink.setdefault(sra,libraryName)
    #zlink
    #{'SRR1145795': 'GSM1316300'}

    LibraryLayout.setdefault(sra,line[15])  #{'SRR1145795': 'SINGLE'}
    #line[15] #'SINGLE'
    species.setdefault(sra,line[28])  #{'SRR1145795': 'Homo sapiens'}
    #line[28] #'Homo sapiens'
    #bad
o.close()

oh=open('wget.sh','w')
for k in wget:
    #wget #{'https://sra-download.ncbi.nlm.nih.gov/srapub/SRR1145795': 'GSM1316300',...}
    #k #'https://sra-download.../SRR1145816'
    oh.write('wget -c %s #%s\n'%(k,wget[k]))
    #wget[k]  #'GSM1316321'
oh.close()

oh=open('zlink.sh','w')
i=0
for k in zlink:
    #zlink #{'SRR1145795': 'GSM1316300', 'SRR1145796': 'GSM1316301',...}
    i+=1
    if LibraryLayout[k] == 'SINGLE':
        #LibraryLayout  #{'SRR1145795': 'SINGLE','SRR1145796': 'SINGLE',...}
        if species[k]=='Homo sapiens':
            #species  #{'SRR1145795': 'Homo sapiens', 'SRR1145796': 'Homo sapiens',...}
            #oh.write('ln -s fqs/%s.fastq.gz Hs_%s_%s.fq.gz\n'%(k,zlink[k],i))
            oh.write('ln -s fqs/%s.fastq.gz Hs_%s.fq.gz\n'%(k,zlink[k]))
        elif species[k]=='Mus musculus':
            #oh.write('ln -s fqs/%s.fastq.gz Mm_%s_%s.fq.gz\n'%(k,zlink[k],i))
            oh.write('ln -s fqs/%s.fastq.gz Mm_%s.fq.gz\n'%(k,zlink[k]))
        else:
            print 'Warning:it is not mouse or huaman'
            raise Error
    elif LibraryLayout[k] == 'PAIRED':
        if species[k]=='Homo sapiens':
            #oh.write('ln -s fqs/%s_1.fastq.gz Hs_%s_%s.p1.fq.gz\n'%(k,zlink[k],i))
            #oh.write('ln -s fqs/%s_2.fastq.gz Hs_%s_%s.p2.fq.gz\n'%(k,zlink[k],i))
            oh.write('ln -s fqs/%s_1.fastq.gz Hs_%s.p1.fq.gz\n'%(k,zlink[k]))
            oh.write('ln -s fqs/%s_2.fastq.gz Hs_%s.p2.fq.gz\n'%(k,zlink[k]))
        elif species[k]=='Mus musculus':
            #oh.write('ln -s fqs/%s_1.fastq.gz Mm_%s_%s.p1.fq.gz\n'%(k,zlink[k],i))
            #oh.write('ln -s fqs/%s_2.fastq.gz Mm_%s_%s.p2.fq.gz\n'%(k,zlink[k],i))
            oh.write('ln -s fqs/%s_1.fastq.gz Mm_%s.p1.fq.gz\n'%(k,zlink[k]))
            oh.write('ln -s fqs/%s_2.fastq.gz Mm_%s.p2.fq.gz\n'%(k,zlink[k]))
        else:
            print 'Warning:it is not mouse or human'
            #raise Error
oh.close()

