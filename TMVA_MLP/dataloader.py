import uproot

import numpy as np
import pandas as pd

from config import *


def build_dataframe(tree):
	dataframe = pd.DataFrame({"mJJ":			pd.Series(np.array(tree["mJJ"].array())),
							  "deltaYJJ":		pd.Series(np.array(tree["deltaYJJ"].array())),
							  "metPt":			pd.Series(np.array(tree["metPt"].array())),
							  "ptBalance":		pd.Series(np.array(tree["ptBalance"].array())),
							  "subleadJetEta":	pd.Series(np.array(tree["subleadJetEta"].array())),
							  "leadJetPt":		pd.Series(np.array(tree["leadJetPt"].array())),
							  "photonEta":		pd.Series(np.array(tree["photonEta"].array())),
							  "ptBalanceRed":	pd.Series(np.array(tree["ptBalanceRed"].array())),
							  "nJets":			pd.Series(np.array(tree["nJets"].array())),
							  "sinDeltaPhiJJOver2": pd.Series(np.array(tree["sinDeltaPhiJJOver2"].array())),
							  "deltaYJPh":		pd.Series(np.array(tree["deltaYJPh"].array())),
							  "phCentrality":	pd.Series(np.array(tree["phCentrality"].array())),
							  "nLeptons":		pd.Series(np.array(tree["nLeptons"].array())),
							  "weightModified":	pd.Series(np.array(tree["weightModified"].array())),
							 })

	return dataframe


def selection(dataframe, region="zgamma"):
	if region not in ("zgamma", "signal"):
		raise ValueError("Wrong region name")

	dataframe = dataframe[dataframe["nJets"] > 1]
	dataframe = dataframe[dataframe["nLeptons"] == 0]

	if region == "signal":
		dataframe = dataframe[dataframe["mJJ"] > 300]
		dataframe = dataframe[dataframe["phCentrality"] < 0.6]

	return dataframe


def extract(region="zgamma"):
	SFile = uproot.open("source/"+SFILENAME)
	STree = SFile[TREENAME]
	SDataframe = build_dataframe(STree)

	BDataframe = pd.DataFrame(columns=["mJJ", "deltaYJJ", "metPt", "ptBalance", "subleadJetEta",
									   "leadJetPt", "photonEta", "ptBalanceRed", "nJets",
									   "sinDeltaPhiJJOver2", "deltaYJPh", "phCentrality", 
									   "nLeptons", "weightModified"])
	for filename in BFILENAMES:
		print(f"Added background {filename}")
		BFile 	= uproot.open("source/"+filename)
		BTree 	= BFile[TREENAME]
		BDataframe = BDataframe.append(build_dataframe(BTree), ignore_index=True)

	SDataframe = selection(SDataframe, region)
	BDataframe = selection(BDataframe, region)

	return SDataframe, BDataframe


def build_output_dataframe(tree):
	dataframe = pd.DataFrame({"mJJ":			pd.Series(np.array(tree["mJJ"].array())),
							  "deltaYJJ":		pd.Series(np.array(tree["deltaYJJ"].array())),
							  "metPt":			pd.Series(np.array(tree["metPt"].array())),
							  "ptBalance":		pd.Series(np.array(tree["ptBalance"].array())),
							  "subleadJetEta":	pd.Series(np.array(tree["subleadJetEta"].array())),
							  "leadJetPt":		pd.Series(np.array(tree["leadJetPt"].array())),
							  "photonEta":		pd.Series(np.array(tree["photonEta"].array())),
							  "ptBalanceRed":	pd.Series(np.array(tree["ptBalanceRed"].array())),
							  "nJets":			pd.Series(np.array(tree["nJets"].array())),
							  "sinDeltaPhiJJOver2": pd.Series(np.array(tree["sinDeltaPhiJJOver2"].array())),
							  "deltaYJPh":		pd.Series(np.array(tree["deltaYJPh"].array())),
							  "weightModified":	pd.Series(np.array(tree["weightModified"].array())),
							  "classID":		pd.Series(np.array(tree["classID"].array())),
							 })
	return dataframe


def extract_from_output(output_type="test", uploadfile="output"):
	file 		= uproot.open("outputs/" + uploadfile + ".root")
	directory 	= file["dataloader"]
	if output_type == "test":
		Tree 		= directory["TestTree"]
		Dataframe 	= build_output_dataframe(Tree)
		SDataframe 	= Dataframe[Dataframe["classID"] == 0]
		BDataframe 	= Dataframe[Dataframe["classID"] == 1]

		return SDataframe, BDataframe

	elif output_type == "train":
		Tree 		= directory["TrainTree"]
		Dataframe 	= build_output_dataframe(Tree)
		SDataframe 	= Dataframe[Dataframe["classID"] == 0]
		BDataframe 	= Dataframe[Dataframe["classID"] == 1]

		return SDataframe, BDataframe

	else:
		raise Exception("Wrong output type")


if __name__ == "__main__":
	pass