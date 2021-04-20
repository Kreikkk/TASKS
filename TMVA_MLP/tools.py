import uproot

import numpy as np
import pandas as pd
import ROOT as root

from config import *


def build_dataframe(tree):
	dataframe = pd.DataFrame({"mJJ":			pd.Series(tree["mJJ"].array()),
							  "deltaYJJ":		pd.Series(tree["deltaYJJ"].array()),
							  "metPt":			pd.Series(tree["metPt"].array()),
							  "ptBalance":		pd.Series(tree["ptBalance"].array()),
							  "subleadJetEta":	pd.Series(tree["subleadJetEta"].array()),
							  "leadJetPt":		pd.Series(tree["leadJetPt"].array()),
							  "photonEta":		pd.Series(tree["photonEta"].array()),
							  "ptBalanceRed":	pd.Series(tree["ptBalanceRed"].array()),
							  "nJets":			pd.Series(tree["nJets"].array()),
							  "sinDeltaPhiJJOver2": pd.Series(tree["sinDeltaPhiJJOver2"].array()),
							  "deltaYJPh":		pd.Series(tree["deltaYJPh"].array()),
							  "phCentrality":	pd.Series(tree["phCentrality"].array()),
							  "weightModified":	pd.Series(tree["weightModified"].array()),
							  "nLeptons":		pd.Series(tree["nLeptons"].array()),
							 })

	return dataframe


def selection(dataframe):
	dataframe = dataframe[dataframe["nJets"] > 1]
	dataframe = dataframe[dataframe["nLeptons"] == 0]

	return dataframe


def extract():
	SFile = uproot.open("source/"+SFILENAME)
	STree = SFile[TREENAME]
	SDataframe = build_dataframe(STree)

	BDataframe = pd.DataFrame(columns=["mJJ", "deltaYJJ", "metPt", "ptBalance", "subleadJetEta",
									   "leadJetPt", "photonEta", "ptBalanceRed", "nJets",
									   "sinDeltaPhiJJOver2", "deltaYJPh", "phCentrality", 
									   "weightModified", "nLeptons"])
	for filename in BFILENAMES:
		BFile = uproot.open("source/"+filename)
		BTree = BFile[TREENAME]
		BDataframe = BDataframe.append(build_dataframe(BTree), ignore_index=True)

	SDataframe = selection(SDataframe)
	BDataframe = selection(BDataframe)

	return SDataframe, BDataframe


def error(signal_events, bg_events):
	S = np.sum(signal_events)
	B = np.sum(bg_events)

	SErr = np.sum(signal_events**2)**0.5
	BErr = np.sum(bg_events**2)**0.5

	SPart = (S + B)**(-0.5) - 0.5*S*((S + B)**(-1.5))
	BPart = -0.5*S*((S + B)**(-1.5))

	return ((SPart*SErr)**2 + (BPart*BErr)**2)**0.5
