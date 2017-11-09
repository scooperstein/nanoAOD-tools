#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.analysis.higgs.vhbb.VHbbProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import *

#files=["root://cms-xrd-global.cern.ch//store/user/arizzi/NanoTestProd006/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer17MiniAOD-92X-NanoCrabProd006/171006_144159/0000/nanolzma_1.root"]
#files=["lzma_1.root"]
#files=["root://cms-xrd-global.cern.ch://store/user/arizzi/NanoTestProd004/WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/NanoCrabProd004/171002_120520/0000/lzma_1.root"]
#files=["root://cms-xrd-global.cern.ch://store/user/arizzi/NanoTestProd004/WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/NanoCrabProd004/171002_120552/0000/lzma_1.root"]
#files=["root://cms-xrd-global.cern.ch://store/user/arizzi/NanoTestProd004/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/NanoCrabProd004/171002_120644/0000/lzma_1.root"]
#files=["root://cms-xrd-global.cern.ch://store/user/arizzi/NanoTestProd004/ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/NanoCrabProd004/171002_122256/0000/lzma_1.root"]
files=["root://cms-xrd-global.cern.ch://store/user/arizzi/NanoTestProd004/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/NanoCrabProd004/171002_122221/0000/lzma_1.root"]
filesTTbar= [
'root://cms-xrd-global.cern.ch//store/group/cmst3/group/nanoAOD/NanoTestProd006/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer17MiniAOD-92X-NanoCrabProd006/171006_155430/0000/nanolzma_1.root',
]

selection='''(Sum$(Electron_pt > 20 && Electron_mvaSpring16GP_WP90) >= 2  ||
 Sum$(Muon_pt > 20) >= 2 ||
 Sum$(Electron_pt > 20 && Electron_mvaSpring16GP_WP80) >= 1   ||
 Sum$(Muon_pt > 20 && Muon_tightId) >= 1 ||
 (Sum$(Muon_pt > 20) == 0 && Sum$(Electron_pt > 20 && Electron_mvaSpring16GP_WP90) == 0 && MET_pt > 80 ) ) 
 &&  Sum$((abs(Jet_eta)<2.5 && Jet_pt > 20 && Jet_jetId)) >= 2 && Entry$ < 10000
'''

selectionALL='''Sum$(Electron_pt > 20 && Electron_mvaSpring16GP_WP90) >= 2  ||
 Sum$(Electron_pt > 20 && Electron_mvaSpring16GP_WP80) >= 1   ||
 Sum$(Jet_pt > 40 && Jet_jetId) >= 4   || 
Sum$(Jet_pt *(abs(Jet_eta)<2.5 && Jet_pt > 20 && Jet_jetId)) > 160  || 
MET_pt > 100  || Sum$(Muon_pt > 20 && Muon_tightId) >= 1
'''
p=PostProcessor(".",files,selection.replace('\n',' '),"keep_and_drop.txt",[btagSF(),jecUncertAll_cppOut(),vhbb()],provenance=True)
p.run()
