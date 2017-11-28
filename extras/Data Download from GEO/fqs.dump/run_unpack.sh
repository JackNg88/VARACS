
for f in ../geo/SRR*
do
    root=`basename $f`
    tf=`echo $root | sed 's/.sra//g'` 
    #af=`echo $tf | sed s/.sra/.fastq/g`
    #bf=`echo $tf | sed s/.sra/_1.fastq/g`
    af=$tf.fastq
    bf=`echo $tf | sed 's/$/_1.fastq/g'`
    if [ ! -f ./fqs/$af ] && [ ! -f ./fqs/$bf ] && [ ! -f ./fqs/$bf.gz ] && [ ! -f ./fqs/$af.gz ]
    then
        echo Convert $tf $af $bf
	qsub -N $bf -v inp=$f,out=$tf do_unpack.sh
        #nice -n 19 ionice -c 3 fastq-dump --disable-multithreading --gzip --split-3 $f -O ./fqs/
        sleep 2
    fi
done

