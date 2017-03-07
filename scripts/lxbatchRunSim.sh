#!/bin/sh 
cd /afs/cern.ch/user/b/biliu/FourJetsAnalysis/4b/run/FourBSignal_Feb13th/batchSignalProd
cd job_$1
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
lsetup asetup
asetup 20.7.5.1, AtlasProduction,here
cmd="Sim_tf.py --outputHITSFile=/afs/cern.ch/work/b/biliu/private/FourBSignal/out.biliu.hits.root_$1 --inputEVNTFile=/afs/cern.ch/work/b/biliu/private/FourBSignal/evnt/user.biliu.evnt.pool.root_$1 --maxEvents 10 --randomSeed=$1 --geometryVersion ATLAS-R2-2015-03-01-00"
$cmd
 
