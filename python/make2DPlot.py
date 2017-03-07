#!/usr/bin/env python

from ROOT import *
import sys
import os
import re
import math

def getRatioError(num,numerror,den,denerror):
  error = math.pow(math.pow(numerror,2)/math.pow(den,2) + math.pow(denerror,2)*math.pow(num,2)/math.pow(den,4),0.5)
  return error


histTxt = open("PvsDeltaR.saf","r")
out = TFile("hist_2D.root","RECREATE")

histTxtLines = histTxt.readlines()
out.cd()

histTmp = TH2F("P vs #DeltaR", "P vs #DeltaR", 32,0,3.2,150,0,1500)
for i in range(0,len(histTxtLines)):
  if "p" not in histTxtLines[i]:
    if len(histTxtLines[i].split(":")) > 1:
      histTmp.Fill(float(histTxtLines[i].split(":")[0]),float(histTxtLines[i].split(":")[1]))
histTmp.Write()

out.Close()
  
