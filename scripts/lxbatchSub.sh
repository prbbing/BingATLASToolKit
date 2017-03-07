#!/bin/sh 
for i in {0..49}
do
  bsub -q 8nh -r -oo /afs/cern.ch/user/b/biliu/FourJetsAnalysis/4b/run/FourBSignal_Feb13th/batchSignalProd/lxbatchFeb13th_$i.log /afs/cern.ch/user/b/biliu/FourJetsAnalysis/4b/run/FourBSignal_Feb13th/batchSignalProd/lxbatchRunEXO.sh $i 
# change lxbatchRunEXO.sh to the one you want
done
echo "Finished submitting 50 jobs." 
