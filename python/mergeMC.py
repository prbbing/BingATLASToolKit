#!/usr/bin/python

import os
from ROOT import *
import re

def getWeight(fileName):
  weight = 1.0
  tmpFile = TFile(fileName)
  eventInfoHist = tmpFile.Get("cutflow").Clone()
  weight = 33000*xs_eff[fileName.split(".")[0]]/eventInfoHist.GetBinContent(1)
  return weight

xs_eff = {
    "JZ0W" : 7842.0E+07*0.98132+00,
    "JZ1W" : 7842.0E+07*6.7198E-04,
    "JZ2W" : 2433.4E+06*3.3264E-04,
    "JZ3W" : 2645.4E+04*3.1953E-04,
    "JZ4W" : 2546.4E+02*5.3009E-04,
    "JZ5W" : 4553.6E+00*9.2325E-04,
    "JZ6W" : 2575.2E-01*9.4016E-04,
    "JZ7W" : 1621.4E-02*3.9282E-04,
    "JZ8W" : 6250.5E-04*1.0162E-02,
    "JZ9W" : 1964.0E-05*1.2054E-02,
    "JZ10W" : 119.62E-05*5.897E-03,
    "JZ11W" : 4.226E-05*2.701E-03,
    "JZ12W" : 1.037E-06*0.425E-02,
}

unfilteredSamples = [
  #"JZ0W",
  "JZ1W",
  "JZ2W",
  "JZ3W",
  "JZ4W",
  "JZ5W",
  "JZ6W",
  "JZ7W",
  "JZ8W",
  "JZ9W",
  "JZ10W",
  "JZ11W",
  "JZ12W",
]

os.system("cp " + unfilteredSamples[0]+ ".root " + "unfilteredTmp.root" )

unfilteredMergedTmp = TFile("unfilteredTmp.root")
unfilteredMerged = TFile("merged.root","RECREATE")

for key in unfilteredMergedTmp.GetListOfKeys():
  if not (re.match ('TH1', key.GetClassName()) or re.match ('TH2', key.GetClassName())):
    continue
  histObj = unfilteredMergedTmp.Get(key.GetName()).Clone()
  histObj.Scale(0)
  histObj.Sumw2()
  for sample in unfilteredSamples:
    tmpFile = TFile(sample + ".root")
    tmpHist = tmpFile.Get(key.GetName()).Clone()
    histObj.Add(tmpHist, getWeight(sample + ".root"))
    tmpFile.Close()
  unfilteredMerged.cd()
  histObj.SetDirectory(0)
  histObj.Write()

unfilteredMergedTmp.Close()
os.system("rm unfilteredTmp.root")
unfilteredMerged.Close()
~                        
