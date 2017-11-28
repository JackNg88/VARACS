# This is modified from the 'standard version' which is only suitable for broadly similar samples.
# This version performs filtering based on each cell type and then calls dispersions based on that.

library(DESeq2)

# Filtering is taken care of in EDASeq, I don't do here as DESeq2
# copes with off-sample reps better.

setwd("/Users/wuxiaojian/wujian/5_CTC/2_genes/2_DESeq2/all_fc1.5")

#qval = 0.01
qval=0.05
fc_filter =  0.584962500721156 #fc 1.5
#fc_filter = 1 #fc 2

#count_data <- read.delim("d2_tpm.csv",row.names='name',sep = ',') # 'row.names must equal first item in [0]
count_data <- read.csv("../../1_corr_heatmap/filter_CTCvsnoCTC.tsv",row.names=1,sep = '\t') # 'row.names must equal first item in [0]

design = read.delim("colData.txt", row.names="name")
groups <- data.frame(paste(design$condition, sep="."))# design$day,
colnames(groups) = "treatment"
rownames(groups) = rownames(design)
contrasts = read.delim("contrasts.txt",row.names = 'name', stringsAsFactors=F) # stringsAsFactors=F is super important!
#contrasts = read.delim("/home/jiang/documents/andrew/rnaseq/DE-genes/contrasts.txt", stringsAsFactors=F) # stringsAsFactors=F is super important!
#row.names(contrasts)=contrasts$name

cdsFull <- DESeqDataSetFromMatrix(countData=count_data,colData=groups,design = ~ treatment)

#colData(cdsFull)$treatment = relevel(colData(cdsFull)$treatment, "ctrl")
dds = DESeq(cdsFull, betaPrior=F)

#Pre-filtering
#dds <- dds[rowSums(counts(dds)) > 1,]

res <- results(dds)#, contrast=c(1,0,0,1,0,0,-1,0,0))
res_names = resultsNames(dds)

pdf(file="DESeq2_results.pdf", width=8, height=7)
par(mfrow=c(1,1))
rest = c("type", "up", "dn")

plotDispEsts(dds)

for (i in 1:dim(contrasts)[1]) {
  print(contrasts[i,])

  res = results(dds, contrast=c("treatment", contrasts[i,1], contrasts[i,2]))

  write.table(res, file=paste(row.names(contrasts[i,]), ".all.tsv", sep=""), sep="\t", col.names=NA)

  res = res[complete.cases(res),] # Filter NAs
  pres = res[res$pvalue<qval,] # 按p值
  #pres=res[res$padj<qval,] #按q值 q调整值过滤
  pres = pres[abs(pres$log2FoldChange) > fc_filter, ] # select fold-change here
  dn = pres[pres$log2FoldChange > fc_filter,] # Yes, this is weird, but in DESeq2 the up and dn are not
  up = pres[pres$log2FoldChange < -fc_filter,] # in the orientation that you might expect.

  print(paste("up:", dim(up)[1], "dn:", dim(dn)[1]))
  sub_name = paste(row.names(contrasts[i,]), dim(pres)[1], "DE genes", sep=" ")

  # Roll my own plotMA()
  plot(log(res[,1]), res[,2], ylim=c(-6, 6))
  abline(h=c(-fc_filter, fc_filter), col = "blue")
  abline(h=0, col="grey")
  points(log(up[, 1]), up[ ,2], col="red", pch=16, cex=0.9)
  points(log(dn[, 1]), dn[ ,2], col="green", pch=16, cex=0.9)
  title(row.names(contrasts[i,]), sub=sub_name)

  write.table(pres, file=paste("./", row.names(contrasts[i,]), ".tsv", sep=""), sep="\t", col.names=NA)
  write.table(up, file=paste("./", row.names(contrasts[i,]), ".up", ".tsv", sep=""), sep="\t", col.names=NA)
  write.table(dn, file=paste("./", row.names(contrasts[i,]), ".dn", ".tsv", sep=""), sep="\t", col.names=NA)
}

dev.off()

