# run this from an environment that has asetup AnalysisBase,blahblah
import ROOT
if(not ROOT.xAOD.Init().isSuccess()): print('Failed xAOD.Init()')

f = ROOT.TFile('/data/hnl/VSI_rerun/mc16_13TeV.311639.Pythia8EvtGen_A14NNPDF23LO_WmuHNL50_12p5G_lt10dd_SUSY15_comboLRTd0Test_VSILepMod/DAOD_SUSY15_1.output.pool.root')
t = ROOT.xAOD.MakeTransientTree(f, 'CollectionTree')

def find_truth_hnls():
    print(t.GetEntries())
    for i in range(10):
        t.GetEntry(i)
        # Get truth vertex container
        truth_vertices = t.TruthVertices
        # Loop over every vertex
        for j in range(len(truth_vertices)):
            # Get pdgId and check it's HNL
            pdgId = truth_vertices.at(j).incomingParticleLinks().at(0).pdgId()
            if abs(pdgId) in [50, 9900012]: # 50 is for Pythia, 9900012 is for MadGraph
                print('Found an HNL!')
                # Print some info
                print('(x, y) : ({}, {})'.format(truth_vertices.at(j).x(), truth_vertices.at(j).y()))
                print('(z, t) : ({}, {})'.format(truth_vertices.at(j).z(), truth_vertices.at(j).t()))
                print('(barcode, id) : ({}, {})'.format(truth_vertices.at(j).barcode(), truth_vertices.at(j).id()))
                print('(px, py) : ({}, {})'.format(truth_vertices.at(j).incomingParticleLinks().at(0).px(), truth_vertices.at(j).incomingParticleLinks().at(0).py()))
    
weights = []
def get_event_weights():
    print(t.GetEntries())
    for i in range(t.GetEntries()):
        t.GetEntry(i)
        # Get truth vertex container
        event_info = t.EventInfo
        weights.append(event_info.mcEventWeight())
        # print()
        # Loop over every vertex
        # for j in range(len(truth_vertices)):
        #     # Get pdgId and check it's HNL
        #     pdgId = truth_vertices.at(j).incomingParticleLinks().at(0).pdgId()
        #     if abs(pdgId) in [50, 9900012]: # 50 is for Pythia, 9900012 is for MadGraph
        #         print('Found an HNL!')
        #         # Print some info
        #         print('(x, y) : ({}, {})'.format(truth_vertices.at(j).x(), truth_vertices.at(j).y()))
        #         print('(z, t) : ({}, {})'.format(truth_vertices.at(j).z(), truth_vertices.at(j).t()))
        #         print('(barcode, id) : ({}, {})'.format(truth_vertices.at(j).barcode(), truth_vertices.at(j).id()))
        #         print('(px, py) : ({}, {})'.format(truth_vertices.at(j).incomingParticleLinks().at(0).px(), truth_vertices.at(j).incomingParticleLinks().at(0).py()))
    print(set(weights))


get_event_weights()