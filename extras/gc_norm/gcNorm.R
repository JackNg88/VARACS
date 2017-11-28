# EDASeq-based GC normlisation of data
# I use DESeq here to get a eset object.
library("EDASeq")

setwd("/Users/wuxiaojian/wujian/5_ChengLin/0_data/2_CTCvsnoCTC/1_raw/norm/2_gc_norm")
count_table <- read.delim("../1_merge/edgeR_input.tsv",row.names="ensg") # 'row.names must equal first item in [0]

# Filtering criteria:
filter_threshold = 10^1.2 # number of tags in <num_conditions> conditions to consider expressed (This number is POST normalisation)
num_conditions = 1 # number of conditions that must be greater than <filter_threshold>

# Filter lowly expressed
keep <- rowSums(count_table > filter_threshold) >= num_conditions # Filtering must be done here BEFORE normalization.
count_table = count_table[keep,]
print(paste("Kept:", dim(count_table)[1]))

# Load data:
#gc = read.delim("Ensemble_hg38_GenesGC.txt", row.names=1) / 100.0
gc=read.csv('/Users/wuxiaojian/Documents/0_script_all/3_ann/1_human/1_GCNorm/Ensemble_hg38_GenesGC.txt',row.names = 1,sep = '\t',header = T)/ 100.0
#gc=read.csv('/Users/wuxiaojian/Documents/0_script_all/3_ann/2_mouse/3_mm10_v79/GC_mm10_ensemble_v79.txt',row.names = 1,sep = '\t',header = T)/ 100.0
design = data.frame(1:dim(count_table)[2], row.names=colnames(count_table))

# Make sure gc and count_table match exactly
common = intersect(rownames(gc), rownames(count_table))
df = data.frame(gc=gc, spaz=gc)
feature = df[common,]
colnames(feature) = c("gc", "fill")
count_table = count_table[common,]

pdf("biasplots.pdf", width=15, height=7)
par(mfrow=c(1,3))
plot(density(log10(count_table[,1])), main="Before Norm")
for (i in 2:dim(count_table)[2]){
  lines(density(log10(count_table[,i])))
}

data <- newSeqExpressionSet(counts=as.matrix(count_table), featureData=feature,phenoData=design) # will only tolerate integers

# normalise
cdswithin = withinLaneNormalization(data, "gc", which="full")

norm_table = exprs(cdswithin)
plot(density(log10(norm_table[,1])), main="withinLaneNormalization")
for (i in 2:dim(norm_table)[2]){
  lines(density(log10(norm_table[,i])))
}

cdsnormed = betweenLaneNormalization(cdswithin, which="full")

norm_table = exprs(cdsnormed)
plot(density(log10(norm_table[,1])), main="betweenLaneNormalization")
for (i in 2:dim(norm_table)[2]){
  lines(density(log10(norm_table[,i])))
}
abline(v=log10(filter_threshold), col="grey")
biasPlot(data, "gc", log=T, ylim=c(-4,8))
biasPlot(cdsnormed, "gc", log=T, ylim=c(-4,8))

par(mfrow=c(1,3))
boxplot(data)
boxplot(cdswithin)
boxplot(cdsnormed)
dev.off()

write.table(norm_table, "rawtags_gc_normed.tsv", sep="\t", col.names=NA)
