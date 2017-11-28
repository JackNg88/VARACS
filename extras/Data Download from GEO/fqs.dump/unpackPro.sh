#PBS -l walltime=336:00:00
#PBS -l nodes=1:ppn=1
#PBS -q default
#PBS -j oe
#PBS -o ${out}.txt
#PBS -V 
cd $PBS_O_WORKDIR

echo "good"
echo $inp
mkdir $out
/public/home/jianwu/tools/sratoolkit.2.8.2-centos_linux64/bin/fastq-dump --disable-multithreading --gzip --split-3 $inp -O ./$out/
#nice -n 19 ionice -c 3 fastq-dump --disable-multithreading --gzip --split-3 $inp -O ./fqs/
