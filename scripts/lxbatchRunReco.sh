#!/bin/sh 
cd /afs/cern.ch/user/b/biliu/FourJetsAnalysis/4b/run/FourBSignal_Feb13th/batchSignalProd
cd job_$1
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
lsetup asetup
asetup 20.7.5.1, AtlasProduction,here
cmd="python /afs/cern.ch/user/b/biliu/FourJetsAnalysis/4b/run/FourBSignal_Feb13th/batchSignalProd/lxbatchRunReco.py $1"
$cmd
