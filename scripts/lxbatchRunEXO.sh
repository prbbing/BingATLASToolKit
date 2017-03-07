#!/bin/sh 
cd /afs/cern.ch/user/b/biliu/FourJetsAnalysis/4b/run/FourBSignal_Feb13th/batchSignalProd
mkdir job$1
cd job$1
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
lsetup asetup
asetup 20.7.7.4,AtlasDerivation,here
#cmd="Reco_tf.py --inputAODFile /afs/cern.ch/work/b/biliu/private/FourBSignal/reco/out.biliu.reco.root_$1  --outputDAODFile /afs/cern.ch/work/b/biliu/private/FourBSignal/out.biliu.EXO.root_$1 --reductionConf EXOT2"
cmd="Reco_tf.py --inputAODFile /afs/cern.ch/work/b/biliu/private/FourBSignal/reco/out.biliu.reco.root_$1  --outputDAODFile out.biliu.EXO.root_$1 --reductionConf EXOT2"
$cmd
 
