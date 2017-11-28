#first grep/cut samples
less zlink.sh | \grep -v matched > NSCLC.sh

#second
less NSCLC.sh |sort -t ' '  -k4,4n >reorder.sh

mv reorder.sh NSCLC.sh

