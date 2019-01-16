import os,sys

runDic = {
    "B" : [325713, 328393],
    "C" : [329385, 330470],
    "D" : [330857, 332304],
    "E" : [332720, 334779],
    "F" : [334842, 335290],
    "H" : [336497, 336782],
    "I" : [336832, 337833],
    "K" : [338183, 340453],
}

command = 'rucio ls data17_13TeV:*FTAG2*p3704 | grep \"deriv\" | awk \'{print $2}\''
runs = os.popen(command).readlines()

totalPeriodSize = 0
totalIndividualSize = 0

for period in runDic:
  command = 'rucio ls data17_13TeV:*FTAG2*p3704 | grep \"period' + period + '\" | awk \'{print $2}\''
  periodContainerName = os.popen(command).readlines()
  print "Checking Period " + period
  command = 'rucio list-files ' + periodContainerName[0].rstrip("\n") + ' | grep \"Total size\"'
  os.system(command)
  sizeInGBPeriod = 0
  size = os.popen(command).readlines()[0].split(":")[1].strip(" ")
  if "TB" in size:
    sizeInGBPeriod = round(float(size.split(" ")[0])*1000,3)
  elif "MB" in size:
    sizeInGBPeriod = round(float(size.split(" ")[0])/1000,3)
  else:
    sizeInGBPeriod = float(size.split(" ")[0])
  totalPeriodSize = totalPeriodSize + sizeInGBPeriod
  totalSize  =  0
  for run in runs:
    sizeInGB = 0
    runNumber = run.split(".")[1][2:8]
    if int(runNumber) >= runDic[period][0] and int(runNumber) <= runDic[period][1]:
      print "  Checking Run " + runNumber
      command = 'rucio list-files ' + run.rstrip("\n")  + ' | grep \"Total size\"'
      out = os.popen(command).readlines()
      size =  out[0].split(":")[1].strip(" ")
      if "MB" in size:
        sizeInGB = round(float(size.split(" ")[0])/1000,3)
      else:
        sizeInGB = float(size.split(" ")[0])
      print "    Size : " + str(sizeInGB) + " GB"
    totalSize = totalSize + sizeInGB
    totalIndividualSize = totalIndividualSize + sizeInGB
  print "Accumulated individual runs in Period" + period + ": " + str(totalSize) + " GB"
  print "Data integrity: " + str(sizeInGBPeriod/totalSize) + "% !"
print "Combined comtainiers size: " + str(totalPeriodSize) + " GB"
print "Combined runs size: " + str(totalIndividualSize) + " GB"
