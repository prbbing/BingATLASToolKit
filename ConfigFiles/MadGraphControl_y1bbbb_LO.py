from MadGraphControl.MadGraphUtils import *

# General settings
minevents=50
nevents=50
mode=0

DSID_4b =[578287]


if runArgs.runNumber in DSID_4b:
    mgproc="""generate p p > y1 b b~, y1 > b b~"""
    name="4b"
    keyword=['exotic']

else: 
    raise RuntimeError("runNumber %i not recognised in these jobOptions."%runArgs.runNumber)

stringy = 'madgraph.'+str(runArgs.runNumber)+'.MadGraph_'+str(name)

fcard = open('proc_card_mg5.dat','w')
fcard.write("""
import ./DMsimp_s_spin1
"""+mgproc+"""
output -f
""")
fcard.close()


beamEnergy=-999
if hasattr(runArgs,'ecmEnergy'):
    beamEnergy = runArgs.ecmEnergy / 2.
else: 
    raise RuntimeError("No center of mass energy found.")


pdflabel="nn23lo1"


#Fetch default LO run_card.dat and set parameters
lhaid= 247000
extras = { 'lhe_version'  : '2.0',
           'pdlabel'      : "'lhapdf'",
           'lhaid'      : lhaid } 

process_dir = new_process()
build_run_card(run_card_old=get_default_runcard(process_dir),run_card_new='run_card.dat', 
               nevts=nevents,rand_seed=runArgs.randomSeed,beamEnergy=beamEnergy,
               extras=extras)

print_cards()
generate(run_card_loc='run_card.dat',param_card_loc=None,mode=mode,proc_dir=process_dir)
arrange_output(proc_dir=process_dir,outputDS=stringy+'._00001.events.tar.gz')


#### Shower 
evgenConfig.generators += ["MadGraph", "Pythia8"]
evgenConfig.description = 'MadGraph_'+str(name)
evgenConfig.keywords+=keyword 
evgenConfig.inputfilecheck = stringy
evgenConfig.minevents = minevents
runArgs.inputGeneratorFile=stringy+'._00001.events.tar.gz'

include("MC15JobOptions/Pythia8_A14_NNPDF23LO_EvtGen_Common.py")
include("MC15JobOptions/Pythia8_MadGraph.py")
