#!/usr/bin/env python

from ROOT import *
import sys
import os
import re

regions = ["4j25","4j25, 3rdbtag"]

histTxt = open("histos.saf","r")
out = TFile("hist_all.root","RECREATE")

histTxtLines = histTxt.readlines()
histNames = []
histBins = []
values = []

for region in regions:  
  for i in range(0, len(histTxtLines)):
    line = histTxtLines[i]
    if "in " + str(region) + "\""  in line:
      histName = line.split("\"")[1].split(" ")[0]
      histNames.append(histName + "_" + region)
      for j in range(i + 1, len(histTxtLines)): 
        newLine = histTxtLines[j]
        if "nbins" in newLine:
          nBins = histTxtLines[j+1].split()[0]
          xMin = histTxtLines[j+1].split()[1]
          xMax = histTxtLines[j+1].split()[2]
          histBins.append([float(nBins),float(xMin),float(xMax)])
          break
      for k in range(i + 1, len(histTxtLines)):
        newnewLine = histTxtLines[k]
        if "underflow" in newnewLine:
          valuesTmp = []  
          for l in range(k + 1, len(histTxtLines)):
            newnewnewLine = histTxtLines[l]
            if "overflow" in newnewnewLine:
              break
            else:
              valuesTmp.append(newnewnewLine.split()[0])
          values.append(valuesTmp)

out.cd()

for i in range(0,len(histNames)):
  histTmp = TH1F(histNames[i],histNames[i],int(histBins[i][0]),histBins[i][1],histBins[i][2])
  for j in range(0,len(values[i])):
    histTmp.SetBinContent(int(j+1),Double(values[i][j]))
  histTmp.Write()

out.Close()
  
