from TriggerJobOpts.TriggerFlags import TriggerFlags

TriggerFlags.triggerMenuSetup='MC_pp_v6'
TriggerFlags.L1PrescaleSet='None'
TriggerFlags.HLTPrescaleSet='None'

def modifySignatures():
   TriggerFlags.JetSlice.signatures = TriggerFlags.JetSlice.signatures() + [['2j250_j150','L1_J100', [], ["Main"], ['RATE:MultiJet', 'BW:Jet'], -1]]

from TriggerMenu.menu.GenerateMenu import GenerateMenu
GenerateMenu.overwriteSignaturesWith(modifySignatures)
