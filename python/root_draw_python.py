# Start a jupyter notebook from an envoironment with asetup already run
# if jupyter is not installed, use:
# > pip install jupyter --user
# > ~/.local/bin/jupyter-notebook --port=8889 --NotebookApp.port_retries=0 --no-browser --NotebookApp.token='atlas'&


# import uproot
import numpy as np

import ROOT

import itertools
from array import array

ROOT.gROOT.SetStyle('ATLAS')
import time
import os
# from IPython.display import Image, display

def draw_note(x, y, text='Internal', size=30, font=63):
    l = ROOT.TLatex()
    l.SetNDC()
    l.SetTextColor(1)
    l.SetTextFont(font)
    l.SetTextSize(size);
    l.DrawLatex(x, y, text)

def atlas_label(x, y, text=None, color=1):
    draw_note(x, y, r"#bf{#it{ATLAS}} " + text)

FONT_SIZE = 30

if(not ROOT.xAOD.Init().isSuccess()): print("Failed xAOD.Init()")

f = ROOT.TFile(f'/data/newhouse/LRT/from_max.AOD.root')
t = ROOT.xAOD.MakeTransientTree( f, "CollectionTree")
t.GetEntries()

# InDetTrackParticles
# InDetLargeD0TrackParticles

h_InDetTrackParticles_d0 = ROOT.TH1F("h_InDetTrackParticles_d0","h_InDetTrackParticles_d0",100,-350,350); 
t.Draw("InDetTrackParticles.d0()>>h_InDetTrackParticles_d0","", "")
# h_InDetTrackParticles_d0 = ROOT.gDirectory.Get("h_InDetTrackParticles_d0");

# Get histogram by Draw method
h_InDetForwardTrackParticles_d0 = ROOT.TH1F("h_InDetLargeD0TrackParticles_d0","h_InDetLargeD0TrackParticles_d0",100,-350,350); 
t.Draw("InDetLargeD0TrackParticles.d0()>>h_InDetLargeD0TrackParticles_d0","", "")
# h_InDetLargeD0TrackParticles_d0 = ROOT.gDirectory.Get("h_InDetLargeD0TrackParticles_d0");
