import os,sys
import optparse
import re

parser = optparse.OptionParser()
parser.add_option('--check2017',dest='check2017', help='Check 2017 data.',action="store_true", default=False)
parser.add_option('--check2018',dest='check2018', help='Check 2018 data.', action="store_true", default=False)
parser.add_option('--check2016',dest='check2016', help='Check 2016 data.', action="store_true", default=False)
parser.add_option('--containerString',dest='containerString', help='Container string to use.', default="")
parser.add_option('--runString',dest='runString', help='Run string to use.', default="")
(arguments, args) = parser.parse_args()

runDic = {}
sys.stderr = open('checklog.txt', 'w')

if arguments.check2017:
  sys.stderr.write("Checking year 2017: \n")
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
if arguments.check2018:
 sys.stderr.write("Checking year 2018: \n")
 runDic = {
    "B" : [348885, 349533],
    "C" : [349534, 350220],
    "D" : [350310, 352107],
    "E" : [352123, 352137],
    "F" : [352274, 352514],
    "G" : [354107, 354494],
    "H" : [354826, 355224],
    "I" : [355261, 355273],
    "J" : [355331, 355468],
    "K" : [355529, 356259],
    "L" : [357050, 359171],
    "M" : [359191, 360414],
    "N" : [361635, 361696],
    "O" : [361738, 363400],
 }

if arguments.check2016:
 sys.stderr.write("Checking year 2016: \n")
 runDic = {
    "A" : [296939, 300287],
    "B" : [300345, 300908],
    "C" : [301912, 302393],
    "D" : [302737, 303560],
    "E" : [303638, 303892],
    "F" : [303943, 304494],
    "G" : [305291, 306714],
    "I" : [307124, 308084],
    "K" : [309311, 309759],
    "L" : [310015, 311481],
 }

sys.stderr.write("Checking containers: " + str(arguments.containerString) + "\n")

command = 'rucio ls ' + str(arguments.runString)  +  '| grep \"deriv\" | awk \'{print $2}\''
runs = os.popen(command).readlines()

totalPeriodSize = 0
totalIndividualSize = 0

for period in runDic:
  command = 'rucio ls ' + str(arguments.containerString) + '| grep \"period' + period + '\" | awk \'{print $2}\''
  periodContainerName = os.popen(command).readlines()
  sys.stderr.write("Checking Period " + period + "\n")
  command = 'rucio list-files ' + periodContainerName[0].rstrip("\n") + ' | grep \"Total events\"'
  os.system(command)
  sizePeriod = 0
  sizePeriod = float(os.popen(command).readlines()[0].split(":")[1].strip(" ").split(" ")[0])
  totalPeriodSize = totalPeriodSize + sizePeriod
  totalSize  =  0
  for run in runs:
    size = 0
    runNumber = run.split(".")[1][2:8]
    if int(runNumber) >= runDic[period][0] and int(runNumber) <= runDic[period][1]:
      sys.stderr.write("  Checking Run " + runNumber + "\n")
      command = 'rucio list-files ' + run.rstrip("\n")  + ' | grep \"Total events\"'
      out = os.popen(command).readlines()
      size = float(out[0].split(":")[1].strip(" ").split(" ")[0])
      sys.stderr.write("    Size : " + str(size) + " Events\n")
    totalSize = totalSize + size
    totalIndividualSize = totalIndividualSize + size
  sys.stderr.write("Accumulated individual runs in Period" + period + ": " + str(totalSize) + " Events\n")
  sys.stderr.write("Data integrity: " + str(sizePeriod/totalSize) + "\n")
sys.stderr.write("Combined comtainiers size: " + str(totalPeriodSize) + " Events\n")
sys.stderr.write("Combined runs size: " + str(totalIndividualSize) + " Events\n")

sys.stderr.close()
sys.stderr = sys.__stderr__
