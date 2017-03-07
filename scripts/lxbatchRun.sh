#!/bin/sh 
#make a directory to save all your log files
cd /afs/cern.ch/user/b/biliu/FourJetsAnalysis/4b/run/FourBSignal_Feb13th/batchSignalProd
mkdir job_$1
#copy the DM models and the madgraph configs
cmd="cp -r /afs/cern.ch/user/b/biliu/FourJetsAnalysis/4b/run/FourBSignal_Feb13th/DMsimp_s_spin1 job_$1/"  
$cmd
cmd="cp /afs/cern.ch/user/b/biliu/FourJetsAnalysis/4b/run/FourBSignal_Feb13th/MC15.578287.MadGraphPythia8EvtGen_A14NNPDF23_y1bbbb.py job_$1/"  
$cmd
cmd="cp  /afs/cern.ch/user/b/biliu/FourJetsAnalysis/4b/run/FourBSignal_Feb13th/MadGraphControl_y1bbbb_LO.py job_$1/"  
$cmd
cd job_$1
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
lsetup asetup
asetup AtlasProduction,19.2.5.5,here
cmd="Generate_tf.py --ecmEnergy=13000. --runNumber=578287 --firstEvent=1 --maxEvents=20 --randomSeed=$1 --jobConfig=MC15.578287.MadGraphPythia8EvtGen_A14NNPDF23_y1bbbb.py --outputEVNTFile=/afs/cern.ch/work/b/biliu/private/FourBSignal/user.biliu.evnt.pool.root_$1"
$cmd
 
