#!/bin/sh 
cd /afs/cern.ch/user/b/biliu/FourJetsAnalysis/4b/run/FourBSignal_Feb13th/batchSignalProd
cd job_$1
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
lsetup asetup
asetup 20.7.5.1, AtlasProduction,here
cmd="Digi_tf.py --inputHITSFile=/afs/cern.ch/work/b/biliu/private/FourBSignal/sim/out.biliu.hits.root_$1 --outputRDOFile=/afs/cern.ch/work/b/biliu/private/FourBSignal/out.biliu.rdo.root_$1 --ignoreErrors True --maxEvents 10 --geometryVersion ATLAS-R2-2015-03-01-00 --digiSeedOffset1 $1 --conditionsTag OFLCOND-MC15c-SDR-09"
$cmd
 
