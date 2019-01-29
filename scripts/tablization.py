import os,sys,re,math

def writeALine(name, values):
  text = name.replace("_","\_")
  for value in values:
    text = text + " & " + value
  text = text + "\\\\"
  return text

def quadro(values):
  error = 0
  for value in values:
    error = error + math.pow(float(value),2)
  return str(round(math.sqrt(error),3))

sysDic = {
 "Detector and Calibration Uncertainties" : [
  "PileupOffsetMu",
  "PileupOffsetNPV" , 
  "PileupPtTerm",
  "PileupRhoTopology",
  "BJESResponse",
  "FlavourComposition",
  "FlavourResponse",
  "EtaIntercalibrationModeling",
  "EtaIntercalibrationTotalStat",
  "EffectiveNP1",
  "EffectiveNP2",
  "EffectiveNP3",
  "EffectiveNP4",
  "EffectiveNP5",
  "EffectiveNP6",
  "EffectiveNP7",
  "EffectiveNP8restTerm",
  "JER_DataVsMC",
  'JER_EffectiveNP_1',
  'JER_EffectiveNP_2',
  'JER_EffectiveNP_3',
  'JER_EffectiveNP_4',
  'JER_EffectiveNP_5',
  'JER_EffectiveNP_6',
  'JER_EffectiveNP_7restTerm',
  'PunchThrough_MC16',
  'MUON_SAGITTA_RESBIAS',
  'MUON_SAGITTA_RHO',
  "MuonID",
  "MuonMS",
  "MuonScale",
 ],
 "Modeling Uncertainties" : [
  "AxisSmearing",
  "BDecayFractions",
  "FakeMuons",
  "Extrapolation",
 ],
 "MC Statistical Uncertainties" : [
  "SimulationStats",
  "TemplateStats",
 ],
 "Template Selection Uncertainties" : [
  "LightContamination",
  "JVTEfficiency",
 ],
}

lines  = []
WP60EffLines = []
WP70EffLines = []
WP77EffLines = []
WP85EffLines = []
WP60SFLines = []
WP70SFLines = []
WP77SFLines = []
WP85SFLines = []

inputFile = open("syst.txt","r")

for line in inputFile:
  lines.append(line.rstrip("//\n")) 
inputFile.close()

for entryNum in range(0,len(lines)):
  if entryNum >= 1 and entryNum <= 10:
    WP60EffLines.append(lines[entryNum])   
  if entryNum >= 12 and entryNum <= 21:
    WP70EffLines.append(lines[entryNum])   
  if entryNum >= 23 and entryNum <= 32:
    WP77EffLines.append(lines[entryNum])   
  if entryNum >= 34 and entryNum <= 43:
    WP85EffLines.append(lines[entryNum])   
  if entryNum >= 45 and entryNum <= 54:
    WP60SFLines.append(lines[entryNum])   
  if entryNum >= 56 and entryNum <= 65:
    WP70SFLines.append(lines[entryNum])   
  if entryNum >= 67 and entryNum <= 76:
    WP77SFLines.append(lines[entryNum])   
  if entryNum >= 78 and entryNum <= 87:
    WP85SFLines.append(lines[entryNum])   

lineDic = {
  "WP60Eff": WP60EffLines, 
  "WP70Eff": WP70EffLines,
  "WP77Eff": WP77EffLines,
  "WP85Eff": WP85EffLines,
  "WP60SF":  WP60SFLines,
  "WP70SF":  WP70SFLines,
  "WP77SF":  WP77SFLines,
  "WP85SF":  WP85SFLines,
}

for table in lineDic:
  sysValues = []
  for num in range(1,9):
    sysValues.append(lineDic[table][num].split(" & "))
  sysNames = lineDic[table][0].split(" & ")
  sysMap = {}
  for sysNum in range(0,len(sysNames)):
    sysMap[sysNames[sysNum]] = []
    for sysValue in sysValues:
      sysMap[sysNames[sysNum]].append(sysValue[sysNum])
  os.system("touch " + table + ".tex")
  os.system("echo '\scalebox{0.7}{' >> " +  table + ".tex")  
  os.system("echo '\\renewcommand{\\arraystretch}{1.2}' >> " +  table + ".tex")  
  os.system("echo '\\begin{tabular}{|l|ccccccccc|}' >> " +  table + ".tex")  
  os.system("echo '\hline' >> " +  table + ".tex")  
  os.system("echo '\multirow{2}*{Systematic Uncertainty Source} & \multicolumn{9}{c|}{Systematic Uncertainty in $\ptjet\lbrack\,GeV\\rbrack$ Bins}\\' >> " +  table + ".tex")  
  os.system("echo '      & $\lbrack20,30\\rbrack$ & $\lbrack30,40\\rbrack$ & $\lbrack40,50\\rbrack$ & $\lbrack50,70\\rbrack$ & $\lbrack70,90\\rbrack$ & $\lbrack90,110\\rbrack$ & $\lbrack110,140\\rbrack$ & $\lbrack140,170\\rbrack$ & $\lbrack170,200\\rbrack$ \\\\' >> " +  table + ".tex")  
  os.system("echo '\hline' >> " +  table + ".tex")  
  os.system("echo '& \multicolumn{9}{c|}{Detector and Calibration Uncertainties}\\\\' >> " +  table + ".tex")
  for systematic in sysDic["Detector and Calibration Uncertainties"]: 
    textToWrite = writeALine(systematic, sysMap[systematic])
    os.system("echo '" + textToWrite + " ' >> " + table + ".tex")   
  os.system("echo '& \multicolumn{9}{c|}{Modeling Uncertainties}\\\\' >> " +  table + ".tex")
  for systematic in sysDic["Modeling Uncertainties"]: 
    textToWrite = writeALine(systematic, sysMap[systematic])
    os.system("echo '" + textToWrite + " ' >> " + table + ".tex")   
  os.system("echo '& \multicolumn{9}{c|}{MC Statistical Uncertainties}\\\\' >> " +  table + ".tex")
  for systematic in sysDic["MC Statistical Uncertainties"]: 
    textToWrite = writeALine(systematic, sysMap[systematic])
    os.system("echo '" + textToWrite + " ' >> " + table + ".tex")   
  os.system("echo '& \multicolumn{9}{c|}{Template Selection Uncertainties}\\\\' >> " +  table + ".tex")
  for systematic in sysDic["Template Selection Uncertainties"]: 
    textToWrite = writeALine(systematic, sysMap[systematic])
    os.system("echo '" + textToWrite + " ' >> " + table + ".tex")  
  os.system("echo '\hline' >> " +  table + ".tex")  
  textToWrite = writeALine("DataStats", sysMap["DataStats"])
  os.system("echo '" + textToWrite + " ' >> " + table + ".tex") 
  textToWrite = writeALine("TotalSystematicErr", sysMap["TotalSystematicErr"])
  os.system("echo '" + textToWrite + " ' >> " + table + ".tex") 
  os.system("echo '\hline' >> " +  table + ".tex")  
  os.system("echo '\end{tabular}' >> " +  table + ".tex")  
  os.system("echo '}' >> " +  table + ".tex")  
 
  os.system("touch " + table + "_Condensed.tex")
  os.system("echo '\scalebox{0.7}{' >> " +  table + "_Condensed.tex")  
  os.system("echo '\\renewcommand{\\arraystretch}{1.2}' >> " +  table + "_Condensed.tex")  
  os.system("echo '\\begin{tabular}{|l|ccccccccc|}' >> " +  table + "_Condensed.tex")  
  os.system("echo '\hline' >> " +  table + "_Condensed.tex")  
  os.system("echo '\multirow{2}*{Systematic Uncertainty Source} & \multicolumn{9}{c|}{Systematic Uncertainty in $\ptjet\lbrack\,GeV\\rbrack$ Bins}\\' >> " +  table + "_Condensed.tex")  
  os.system("echo '      & $\lbrack20,30\\rbrack$ & $\lbrack30,40\\rbrack$ & $\lbrack40,50\\rbrack$ & $\lbrack50,70\\rbrack$ & $\lbrack70,90\\rbrack$ & $\lbrack90,110\\rbrack$ & $\lbrack110,140\\rbrack$ & $\lbrack140,170\\rbrack$ & $\lbrack170,200\\rbrack$ \\\\' >> " +  table + "_Condensed.tex")  
  os.system("echo '\hline' >> " +  table + "_Condensed.tex")
  currentValues = []
  finalValues = []
  for number in range(0,8):
    for systematic in sysMap:
      if systematic in sysDic["Detector and Calibration Uncertainties"]:
        currentValues.append(sysMap[systematic][number])
    finalValues.append(quadro(currentValues))
    currentValues = []
  textToWrite = writeALine("Detector and Calibration Uncertainties", finalValues)   
  os.system("echo '" + textToWrite + " ' >> " + table + "_Condensed.tex") 
  currentValues = []
  finalValues = []
  for number in range(0,8):
    for systematic in sysMap:
      if systematic in sysDic["Modeling Uncertainties"]:
        currentValues.append(sysMap[systematic][number])
    finalValues.append(quadro(currentValues))
    currentValues = []
  textToWrite = writeALine("Modeling Uncertainties", finalValues)   
  os.system("echo '" + textToWrite + " ' >> " + table + "_Condensed.tex") 
  currentValues = []
  finalValues = []
  for number in range(0,8):
    for systematic in sysMap:
      if systematic in sysDic["MC Statistical Uncertainties"]:
        currentValues.append(sysMap[systematic][number])
    finalValues.append(quadro(currentValues))
    currentValues = []
  textToWrite = writeALine("MC Statistical Uncertainties", finalValues)   
  os.system("echo '" + textToWrite + " ' >> " + table + "_Condensed.tex") 
  currentValues = []
  finalValues = []
  for number in range(0,8):
    for systematic in sysMap:
      if systematic in sysDic["Template Selection Uncertainties"]:
        currentValues.append(sysMap[systematic][number])
    finalValues.append(quadro(currentValues))
    currentValues = []
  textToWrite = writeALine("Template Selection Uncertainties", finalValues)   
  os.system("echo '" + textToWrite + " ' >> " + table + "_Condensed.tex") 
  os.system("echo '\hline' >> " +  table + "_Condensed.tex")  
  textToWrite = writeALine("DataStats", sysMap["DataStats"])
  os.system("echo '" + textToWrite + " ' >> " + table + "_Condensed.tex") 
  textToWrite = writeALine("TotalSystematicErr", sysMap["TotalSystematicErr"])
  os.system("echo '" + textToWrite + " ' >> " + table + "_Condensed.tex") 
  os.system("echo '\hline' >> " +  table + "_Condensed.tex")  
  os.system("echo '\end{tabular}' >> " +  table + "_Condensed.tex")  
  os.system("echo '}' >> " +  table + "_Condensed.tex")  
     
 
