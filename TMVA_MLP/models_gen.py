import numpy as np
import ROOT as root
import time

from config import *

todos = [	"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N,N:TestRate=5:!UseRegulator:NeuronType=tanh",
			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N,N:TestRate=5:!UseRegulator:NeuronType=sigmoid",
			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N,N,N:TestRate=5:!UseRegulator:NeuronType=tanh",
			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N,N,N:TestRate=5:!UseRegulator:NeuronType=sigmoid",
			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N+5,N+5:TestRate=5:!UseRegulator:NeuronType=tanh",
			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N+5,N+5:TestRate=5:!UseRegulator:NeuronType=sigmoid",
			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N+5:TestRate=5:!UseRegulator:NeuronType=tanh",
			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N+5:TestRate=5:!UseRegulator:NeuronType=sigmoid",

			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N+5,N+5:TestRate=5:!UseRegulator:NeuronType=tanh:BPMode=batch:BatchSize=5",
			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N+5,N+5:TestRate=5:!UseRegulator:NeuronType=sigmoid:BPMode=batch:BatchSize=5",
			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N+10,N:TestRate=5:!UseRegulator:NeuronType=tanh:BPMode=batch:BatchSize=5",
			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N+10,N:TestRate=5:!UseRegulator:NeuronType=sigmoid:BPMode=batch:BatchSize=5",
			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N+10:TestRate=5:!UseRegulator:NeuronType=tanh:BPMode=batch:BatchSize=5",
			"H:!V:VarTransform=N:NCycles=500:HiddenLayers=N+10:TestRate=5:!UseRegulator:NeuronType=sigmoid:BPMode=batch:BatchSize=5",

			"H:!V:VarTransform=N:NCycles=1000:HiddenLayers=N-4,N-4:TestRate=5:UseRegulator:NeuronType=tanh:BPMode=batch:BatchSize=10",
			"H:!V:VarTransform=N:NCycles=1000:HiddenLayers=N-4,N-4:TestRate=5:UseRegulator:NeuronType=sigmoid:BPMode=batch:BatchSize=10",
			"H:!V:VarTransform=N:NCycles=1000:HiddenLayers=N-4:TestRate=5:UseRegulator:NeuronType=tanh:BPMode=batch:BatchSize=10",
			"H:!V:VarTransform=N:NCycles=1000:HiddenLayers=N-4:TestRate=5:UseRegulator:NeuronType=sigmoid:BPMode=batch:BatchSize=10",
			"H:!V:VarTransform=N:NCycles=1000:HiddenLayers=N:TestRate=5:UseRegulator:NeuronType=tanh:BPMode=batch:BatchSize=10",
			"H:!V:VarTransform=N:NCycles=1000:HiddenLayers=N:TestRate=5:UseRegulator:NeuronType=sigmoid:BPMode=batch:BatchSize=10",]

def main(todo_id):
	fout = root.TFile(f"{todo_id}.root", "RECREATE")
	factory = root.TMVA.Factory("TMVAClassification", fout,
                            ":".join([    "!V",
                                          "!Silent",
                                          "Color",
                                          "DrawProgressBar",
                                          "Transformations=I;D;P;G,D",
                                          "AnalysisType=Classification"]))

	dataloader = root.TMVA.DataLoader("dataloader")

	SFile = root.TFile("source/"+SFILENAME)
	STree = SFile.Get(TREENAME)
	dataloader.AddSignalTree(STree)

	BFile1 = root.TFile("source/"+"ZgQCD.root")
	BFile2 = root.TFile("source/"+"ttgamma.root")
	BFile3 = root.TFile("source/"+"SinglePhoton.root")
	BFile4 = root.TFile("source/"+"WenuDataDriven.root")
	BFile5 = root.TFile("source/"+"Wgam.root")
	BFile6 = root.TFile("source/"+"WgamEWK.root")
	BFile7 = root.TFile("source/"+"Zllgam.root")
	BFile8 = root.TFile("source/"+"ZnunuFromQcd.root")

	BTree1 = BFile1.Get(TREENAME)
	BTree2 = BFile2.Get(TREENAME)
	BTree3 = BFile3.Get(TREENAME)
	BTree4 = BFile4.Get(TREENAME)
	BTree5 = BFile5.Get(TREENAME)
	BTree6 = BFile6.Get(TREENAME)
	BTree7 = BFile7.Get(TREENAME)
	BTree8 = BFile8.Get(TREENAME)

	dataloader.AddBackgroundTree(BTree1)
	dataloader.AddBackgroundTree(BTree2)
	dataloader.AddBackgroundTree(BTree3)
	dataloader.AddBackgroundTree(BTree4)
	dataloader.AddBackgroundTree(BTree5)
	dataloader.AddBackgroundTree(BTree6)
	dataloader.AddBackgroundTree(BTree7)
	dataloader.AddBackgroundTree(BTree8)

	dataloader.AddVariable("mJJ","F")
	dataloader.AddVariable("deltaYJJ","F")
	dataloader.AddVariable("metPt","F")
	dataloader.AddVariable("ptBalance","F")
	dataloader.AddVariable("subleadJetEta","F")
	dataloader.AddVariable("leadJetPt","F")
	dataloader.AddVariable("photonEta","F")
	dataloader.AddVariable("ptBalanceRed","F")
	dataloader.AddVariable("nJets","F")
	dataloader.AddVariable("sinDeltaPhiJJOver2","F")
	dataloader.AddVariable("deltaYJPh","F")

	cut = root.TCut("(nJets > 1)&&(nLeptons == 0)")

	dataloader.PrepareTrainingAndTestTree(cut, ":".join(["nTrain_Signal=0",
														 "nTrain_Background=0",
														 "SplitMode=Random",
														 "NormMode=NumEvents",
														 "!V"]))




	method = factory.BookMethod(dataloader, root.TMVA.Types.kMLP, f"MLP{todo_id}", todos[int(todo_id)-1])

	factory.TrainAllMethods()
	factory.TestAllMethods()
	factory.EvaluateAllMethods()
	fout.Close()

	print()

	root.TMVA.TMVAGui(f"{todo_id}.root")
	root.gApplication.Run()


if __name__ == "__main__":
	todo_id = input("ID: ")
	root.TMVA.Tools.Instance()
	main(todo_id)


