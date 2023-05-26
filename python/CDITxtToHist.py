from ROOT import *
import os,sys,re
import ctypes
import array

ops = ["60","70","77","85"]
ouf = TFile("DL1r_b.root","RECREATE")

for op in ops:

  path = "MCcalibCDI_DL1r_extrap_FixedCutBEff_" + op + "_AntiKt4EMPFlowJets_BTagging201903_retagging.txt"

  inf = open(path, "r")

  command = "grep 'bin' " +  path

  bins = os.popen(command).readlines()

  command = "grep 'sys' " + path

  sys = os.popen(command).readlines()

  entries = []

  for line in sys:
    entry = line.split(',')[0].split('sys(')[1]
    entries.append(entry)

  entries = list(dict.fromkeys(entries))

  print("list of systematics: ")
  print(entries)

  edges = array.array('d',[])

  binDict = {}

  for line in bins:
    binEdges = line.split(',')[0].split('bin(')[1].split('<pt<')
    edges.append(ctypes.c_double(float(binEdges[0])).value)

  binEdges = bins[-1].split(',')[0].split('bin(')[1].split('<pt<')
  edges.append(ctypes.c_double(float(binEdges[1])).value)

  print("list of bins: ")
  print(edges)

  ouf.mkdir(op)

  for entry in entries:
    histTmp = TH1D(str(entry), str(entry), len(edges) - 1, edges)
    for i in range(1, len(edges)):
      command = "grep '" + entry + "' " + path + " | head -" + str(i)
      number = float(os.popen(command).readlines()[-1].split(',')[1].split("%")[0])/100.0
      histTmp.SetBinContent(i, number)
    ouf.cd(op)
    histTmp.Write()

  ouf.cd()

ouf.Close()
