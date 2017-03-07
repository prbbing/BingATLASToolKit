After creating your own analysis packcage in MadAnalysis expert mode, copy the files here to the following directory:
FourJetTopo/Build/SampleAnalyzer/User/Analyzer
got to FourJetTopo/Build/

source setup.sh
make clean
make

./MadAnalysis5job listosamples

it will create a directory in FourJetTopo/Output/listosamples

each run will have a new directory to store the outputs:

FourJetTopo/Output/listosamples/FourJetTopo_*

in FourJetTopo/Output/listosamples/FourJetTopo_*/Histograms you need the plotting tool to creat histograms
