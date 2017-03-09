#!/usr/bin/env python

import os
import re
import sys
import math

#Define the Ntuple strings and the local locations here. Then run python NtupleCheck.py 

NtupleDics = {
    "data" : {
        "dataSetString" : "user.rcreager.data16_13TeV.*.DAOD_FTAG3.FTNtupCalib.PtRel_v16-11-07*tuple.root",
        "pathToLocalDataset" : "/cnfs/data1/users/bingxuan.liu/pTRelNtuples/data/",
    },
    "filtered" : {
        "dataSetString" : "user.rcreager.mc15_13TeV.4*.DAOD_FTAG3.FTNtupCalib.PtRel_v16-11-07*tuple.root",
        "pathToLocalDataset" : "/cnfs/data1/users/bingxuan.liu/pTRelNtuples/filtered/",
    },
    "unfiltered" : {
        "dataSetString" : "user.rcreager.mc15_13TeV.3*.DAOD_FTAG3.FTNtupCalib.PtRel_v16-11-07*tuple.root",
        "pathToLocalDataset" : "/cnfs/data1/users/bingxuan.liu/pTRelNtuples/unfiltered/",
    },
}

for category in NtupleDics:
    pathToLocalDataset = NtupleDics[category]["pathToLocalDataset"]
    print "Checkig " + category + " in " + pathToLocalDataset + ":"
    dataSetString = NtupleDics[category]["dataSetString"]
    ListOfContainers = os.popen("rucio ls " + dataSetString + " | grep .root").readlines()
    statement = category + " is complete."
    for container in ListOfContainers:
        fileInRemoteDataset = []
        fileListInRemoteDataset  = os.popen("rucio list-files " + container.split('|')[1] + " | grep .root").readlines()
        for File in fileListInRemoteDataset:
            FileName = File.split('|')[1].split(':')[1].rstrip('\n').strip(' ')
            fileInRemoteDataset.append(FileName)
        containerName = container.split('|')[1].split(':')[1]
        fileListInLocalDataset = os.popen("ls " + pathToLocalDataset + containerName + " | grep .root").readlines()
        fileInLocalDataset = []
        for File in fileListInLocalDataset:
            FileName = File.rstrip('\n')
            fileInLocalDataset.append(FileName)
        listOfMissingLocalFiles = set(fileInRemoteDataset).difference(set(fileInLocalDataset))
        if len(listOfMissingLocalFiles):
            print "Following files are missing in " + container.split('|')[1] + ":"
            statement = "WARNING!!!!!!!!: " + category + " is NOT complete."
            for missingFile in listOfMissingLocalFiles:
                print missingFile
    print statement
