#!/usr/bin/python

import os
from ROOT import *
import re

def getWeight(fileName):
  weight = 1.0
  tmpFile = TFile(fileName)
  eventInfoHist = tmpFile.Get("cutflow").Clone()
  weight = 36100*xs_eff[fileName.split(".")[0].split("_")[0]]/eventInfoHist.GetBinContent(1)
  return weight

xs_eff = {
    "Zprimebb1250" : 0.6336,
    "Zprimebb1500" : 0.2768,
    "Zprimebb1750" : 0.1317,
    "Zprimebb2000" : 0.06717,
    "Zprimebb2500" : 0.01994,
    "Zprimebb3000" : 0.006724,
    "Zprimebb4000" : 0.001028,
    "Zprimebb5000" : 0.0002325,
}

samples = [
  #"Zprimebb1250",
  "Zprimebb1500",
  "Zprimebb1750",
  "Zprimebb2000",
  "Zprimebb2500",
  "Zprimebb3000",
  "Zprimebb4000",
  "Zprimebb5000",
]


for sample in samples:

  os.system("mv " + sample + ".root " + sample + "_Tmp.root")
  inputFile  = TFile(sample + "_Tmp.root")
  outputFile = TFile(sample + ".root","RECREATE")

  for key in inputFile.GetListOfKeys():
    if not (re.match ('TH1', key.GetClassName()) or re.match ('TH2', key.GetClassName())):
      continue
    histObj = inputFile.Get(key.GetName()).Clone()
    histObj.Scale(0)
    histObj.Sumw2()
    tmpHist = inputFile.Get(key.GetName()).Clone()
    histObj.Add(tmpHist, getWeight(sample + "_Tmp.root"))
    outputFile.cd()
    histObj.SetDirectory(0)
    histObj.Write()

  inputFile.Close()
  outputFile.Close()
  os.system("rm " + sample + "_Tmp.root")
