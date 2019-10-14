# Script to read TRUTH3 DAODs and print simple kinematic plots
# Useful for validating MC requests
# This is a script shared by Alex Emerman

#from ROOT import gROOT
#gROOT.SetStyle("ATLAS")
from ROOT import RDataFrame, RDF, TCanvas, TH1
import argparse

parser = argparse.ArgumentParser(description='Make ratio plots.')
parser.add_argument('-i','--infile', help="Path to input")
parser.add_argument('-o','--output', help="Output directory")
parser.add_argument('--do', nargs='+', help="list of collections to make plots of")
args = parser.parse_args()

models = {
  'm'   : (';m_{{{0}}} [GeV]; Events',50,0,1000),
  'pt'  : (';p_{{T,{0}}} [GeV]; Events',50,0,1000),
  'eta' : (';#eta_{{{0}}}; Events',15,-3.,3.),
  'phi' : (';#phi_{{{0}}}; Events',20,-4.,4.)
}
outdir = 'plots'
if args.output:
  outdir = args.output

rdf = RDataFrame("CollectionTree",args.infile)
rdf = rdf.Define('wgt', 'EventInfoAuxDyn.mcEventWeights[0]')

canv = TCanvas('c','',800,600)

for coll in args.do:
  coll = coll.split(':')
  if len(coll) != 1 and len(coll) != 4:
    print('collection should either be "name" or "name:nbins:xmin:xmax"')
    continue

  varsuff = ''
  if 'fatjet' in coll[0]:
    cname = 'AntiKt10TruthTrimmedPtFrac5SmallR20JetsAux'
  elif 'jet' in coll[0]:
    cname = 'AntiKt4TruthDressedWZJetsAux'
  elif 'electron' in coll[0]:
    cname = 'TruthElectronsAuxDyn'
    varsuff = '_dressed'
  elif 'muon' in coll[0]:
    cname = 'TruthMuonsAuxDyn'
    varsuff = '_dressed'
  else:
    print('collection {} not handled, please add'.format(coll))
    continue
  varsuff += '[0]'

  model = RDF.TH1DModel(cname+'eta', models['eta'][0].format(coll[0]),
                        models['eta'][1], models['eta'][2], models['eta'][3])
  h = rdf.Define(cname+'_eta_0', cname+'.eta'+varsuff) \
         .Histo1D(model, cname+'_eta_0', 'wgt')
  h.Draw()
  canv.SaveAs(outdir+'/'+coll[0]+'_eta.pdf')
  canv.Clear('D')

  model = RDF.TH1DModel(cname+'phi', models['phi'][0].format(coll[0]),
                        models['phi'][1], models['phi'][2], models['phi'][3])
  h = rdf.Define(cname+'_phi_0', cname+'.phi'+varsuff) \
         .Histo1D(model, cname+'_phi_0', 'wgt')
  h.Draw()
  canv.SaveAs(outdir+'/'+coll[0]+'_phi.pdf')
  canv.Clear('D')

  canv.SetLogy()
  if len(coll) == 1:
    model = RDF.TH1DModel(cname+'pt', models['pt'][0].format(coll[0]),
                          models['pt'][1], models['pt'][2], models['pt'][3])
    h = rdf.Define(cname+'_pt_0', cname+'.pt'+varsuff+'/1e3') \
           .Histo1D(model, cname+'_pt_0', 'wgt')
    h.Draw()
  else:
    model = RDF.TH1DModel(cname+'pt', models['pt'][0].format(coll[0]),
                          int(coll[1]), float(coll[2]), float(coll[3]))
    h = rdf.Define(cname+'_pt_0', cname+'.pt'+varsuff+'/1e3') \
           .Histo1D(model, cname+'_pt_0', 'wgt')
    h.Draw()
  canv.SaveAs(outdir+'/'+coll[0]+'_pt.pdf')
  canv.Clear('D')
  canv.SetLogy(0)
