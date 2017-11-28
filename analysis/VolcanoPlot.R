library(ggplot2)
setwd('...')

path='sign/'
files=list.files(path,'*.tsv')
#[1] "X0909T_vs_ES0416SP.tsv" "X0909T_vs_ES0416SP.tsv"


#plot
for (i in files){
  print(i) #"X0909T_vs_ES0416SP.tsv"
  base=substr(i,1,nchar(i)-4) #字符剪切修改
  data=read.csv(file=paste(path,i,sep = ''),header=T,row.names=1,sep='\t')

  par(mfrow=c(1,1))
  r03 = ggplot(data,aes(log2FoldChange,-1*log10(pvalue)))
  print(r03  + geom_point(aes(color=significant)) + xlim(-12,12) + ylim(0,15)+ labs(title=base,x="log2(FC)")  + labs(title=base,x=expression(log[2](FC)), y=expression(-log[10](FDR)))) #note:ggplot2的需要print

  ggsave(paste(i,'.eps',sep = ''),width = 20,height =20,units = 'cm')#保存为eps格式 #AI打不开pdf问题
  dev.off()
}

