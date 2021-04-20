import uproot

import atlasplots as aplt
import numpy as np
import pandas as pd
import ROOT as root

from array import array

from config import *
from tools import extract, error
from hists import setup_layout


def build_reader(model_id):
	reader = root.TMVA.Reader("reader")

	var_mJJ 				= array('f',[0])
	var_deltaYJJ 			= array('f',[0])
	var_metPt 				= array('f',[0])
	var_ptBalance 			= array('f',[0])
	var_subleadJetEta 		= array('f',[0])
	var_leadJetPt 			= array('f',[0])
	var_photonEta 			= array('f',[0])
	var_ptBalanceRed 		= array('f',[0])
	var_nJets 				= array('f',[0])
	var_sinDeltaPhiJJOver2 	= array('f',[0])
	var_deltaYJPh 			= array('f',[0])

	reader.AddVariable("mJJ",				var_mJJ)
	reader.AddVariable("deltaYJJ",			var_deltaYJJ)
	reader.AddVariable("metPt",				var_metPt)
	reader.AddVariable("ptBalance",			var_ptBalance)
	reader.AddVariable("subleadJetEta",		var_subleadJetEta)
	reader.AddVariable("leadJetPt",			var_leadJetPt)
	reader.AddVariable("photonEta",			var_photonEta)
	reader.AddVariable("ptBalanceRed",		var_ptBalanceRed)
	reader.AddVariable("nJets",				var_nJets)
	reader.AddVariable("sinDeltaPhiJJOver2",var_sinDeltaPhiJJOver2)
	reader.AddVariable("deltaYJPh",			var_deltaYJPh)

	reader.BookMVA("MLP", f"dataloader/weights/TMVAClassification_MLP{model_id}.weights.xml")

	SDataframe, BDataframe = extract()
	SDataframe["BDToutput"] = 0.0
	BDataframe["BDToutput"] = 0.0
	print("Веса до применения классификатора:")
	print(np.sum(SDataframe["weightModified"]))
	print(np.sum(BDataframe["weightModified"]))

	output = []
	for i, row in SDataframe.iterrows():
		var_mJJ[0]					= row["mJJ"]
		var_deltaYJJ[0]				= row["deltaYJJ"]
		var_metPt[0]				= row["metPt"]
		var_ptBalance[0]			= row["ptBalance"]
		var_subleadJetEta[0]		= row["subleadJetEta"]
		var_leadJetPt[0]			= row["leadJetPt"]
		var_photonEta[0]			= row["photonEta"]
		var_ptBalanceRed[0]			= row["ptBalanceRed"]
		var_nJets[0]				= row["nJets"]
		var_sinDeltaPhiJJOver2[0]	= row["sinDeltaPhiJJOver2"]
		var_deltaYJPh[0]			= row["deltaYJPh"]
		output.append(reader.EvaluateMVA("MLP"))
	SDataframe["BDToutput"] = output

	output = []
	for i, row in BDataframe.iterrows():
		var_mJJ[0]					= row["mJJ"]
		var_deltaYJJ[0]				= row["deltaYJJ"]
		var_metPt[0]				= row["metPt"]
		var_ptBalance[0]			= row["ptBalance"]
		var_subleadJetEta[0]		= row["subleadJetEta"]
		var_leadJetPt[0]			= row["leadJetPt"]
		var_photonEta[0]			= row["photonEta"]
		var_ptBalanceRed[0]			= row["ptBalanceRed"]
		var_nJets[0]				= row["nJets"]
		var_sinDeltaPhiJJOver2[0]	= row["sinDeltaPhiJJOver2"]
		var_deltaYJPh[0]			= row["deltaYJPh"]
		output.append(reader.EvaluateMVA("MLP"))
	BDataframe["BDToutput"] = output

	SHist = root.TH1F("", "", 50, 0, 1)
	BHist = root.TH1F("", "", 50, 0, 1)

	BHist.SetStats(False)
	SHist.SetStats(False)
	BHist.SetLineWidth(2)	
	BHist.SetLineColor(2)
	BHist.SetFillColor(2)
	BHist.SetFillStyle(3004)

	BHist.GetXaxis().CenterTitle()
	BHist.GetYaxis().SetTitle("Fraction of events")
	BHist.GetYaxis().CenterTitle()
	BHist.GetXaxis().SetTitleOffset(1.2)
	BHist.SetMinimum(0)

	SHist.SetLineWidth(2)
	SHist.SetLineColor(4)
	SHist.SetFillColorAlpha(4, 0.2)

	SHist.GetXaxis().CenterTitle()
	SHist.GetYaxis().SetTitle("Fraction of events")
	SHist.GetYaxis().CenterTitle()
	SHist.GetXaxis().SetTitleOffset(1.2)
	SHist.SetMinimum(0)


	for out, weight in zip(SDataframe["BDToutput"], SDataframe["weightModified"]):
		SHist.Fill(out, weight)
	for out, weight in zip(BDataframe["BDToutput"], BDataframe["weightModified"]):
		BHist.Fill(out, weight)

	aplt.set_atlas_style()
	fig, ax = aplt.subplots(1, 1, name="fig1", figsize=(800, 600))
	#####################################
	ax.plot(SHist, "E1")
	ax.plot(BHist, "E1")
	######################################
	ax.add_margins(top=0.16)
	# ax.add_margins(top=0.2)

	ax.set_xlabel(f"MLP{model_id} classifier response")
	ax.set_ylabel("Fraction of events")

	ax.text(0.2, 0.92, "#sqrt{s} = 13 TeV, 139 fb^{-1}", size=27, align=13)

	legend = root.TLegend(0.65, 0.8, 0.95, 0.92)
	legend.SetFillColorAlpha(0, 0)
	legend.AddEntry(SHist, "Signal", "F")
	legend.AddEntry(BHist, "Background", "F")
	legend.Draw()

	fig.savefig(f"MLP{model_id}output.pdf")

	# input()

	return make_selections(SDataframe, BDataframe)


def make_selections(SDataframe, BDataframe):
	Min = max(min(SDataframe["BDToutput"]), min(BDataframe["BDToutput"]))
	Max = min(max(SDataframe["BDToutput"]), max(BDataframe["BDToutput"]))

	ROC_SIG = []
	ROC_BG = []

	initS = sum(SDataframe["weightModified"])
	initB = sum(BDataframe["weightModified"])

	cursor = Min
	plot_data = [[],[]]
	while cursor <= Max:
		S = sum(SDataframe[SDataframe["BDToutput"] > cursor]["weightModified"])
		B = sum(BDataframe[BDataframe["BDToutput"] > cursor]["weightModified"])

		ROC_SIG.append(S)
		ROC_BG.append(B)

		plot_data[0].append(cursor)
		plot_data[1].append(S/(S+B)**0.5)
		cursor += BDTSTEP

	ROC(ROC_SIG, ROC_BG, initS, initB, model_id)

	peak = max(enumerate(plot_data[1]), key=lambda x: x[1])
	meta = {"initS": round(sum(SDataframe["weightModified"])),
			"initB": round(sum(BDataframe["weightModified"])),
			"peak": (peak[1], plot_data[0][peak[0]])}
	plot_data.append(meta)
	
	a = SDataframe[SDataframe["BDToutput"] > plot_data[0][peak[0]]]
	b = BDataframe[BDataframe["BDToutput"] > plot_data[0][peak[0]]]
	print("Significance error:")
	print(error(np.array(a["weightModified"]), np.array(b["weightModified"])))

	print("Веса после применения классификатора:")
	print(np.sum(np.array(a["weightModified"])))
	print(np.sum(np.array(b["weightModified"])))

	return plot_data


def plot(plot_data, model_id):
	xPlot, yPlot = array("d"), array("d")
	for x, y in zip(plot_data[0], plot_data[1]):
		xPlot.append(x)
		yPlot.append(y)

	curve = root.TGraph(len(xPlot), xPlot, yPlot)
	curve.SetLineColor(2)
	curve.SetLineWidth(2)
	curve.SetMarkerColor(2)
	curve.SetMarkerSize(0)
	curve.GetXaxis().SetRangeUser(-1, 1)
	curve.GetXaxis().SetTitle(f"Cut value applied on MLP{model_id} output")
	curve.GetYaxis().SetTitle('Significance')
	# print(dir(curve))
	fig, ax = aplt.subplots(1, 1, name="fig2", figsize=(800, 600))
	ax.plot(curve)

	ax.add_margins(top=0.16)
	ax.set_xlabel(f"Cut value applied on MLP{model_id} output")
	ax.set_ylabel("Significance")

	# aplt.atlas_label(text="Internal", loc="upper left")
	ax.text(0.2, 0.92, "#sqrt{s} = 13 TeV, 139 fb^{-1}", size=27, align=13)
	# ax.text(0.205, 0.865, "Z_{#gamma} inc. region", size=27, align=13)

	text1 = "For {} signal and {} background".format(round(plot_data[2]["initS"]),
													 round(plot_data[2]["initB"]))
	text2 = "events the maximum {} is".format("S/#sqrt{S+B}")
	text3 = "{} when cutting at {}".format(round(plot_data[2]["peak"][0], 3),
										   round(plot_data[2]["peak"][1], 3))

	ax.text(0.2, 0.3, text1, size=20, align=13)
	ax.text(0.2, 0.27, text2, size=20, align=13)
	ax.text(0.2, 0.22, text3, size=20, align=13)

	cut_pos = round(plot_data[2]["peak"][1], 3)

	line = root.TLine(cut_pos, 0, cut_pos, 4)
	line.SetLineStyle(10)
	line.SetLineColor(6)
	ax.plot(line)

	fig.canvas.SetGrid()
	fig.savefig(f"MLP{model_id}outputCut.pdf")

	# input()


def ROC(ROC_SIG, ROC_BG, initS, initB, model_id):
	xPlot, yPlot = array("d"), array("d")

	ROC_SIG = np.array(ROC_SIG)
	ROC_BG = np.array(ROC_BG)
	SIG_EFF = ROC_SIG/initS
	BG_REJ = 1 - ROC_BG/initB

	area = 0
	for index, x_val in enumerate(SIG_EFF[:-1]):
		delta = x_val - SIG_EFF[index+1]
		area += delta*BG_REJ[index]	

	for x, y in zip(SIG_EFF, BG_REJ):
		xPlot.append(x)
		yPlot.append(y)

	Area = 0
	for i, x in enumerate(xPlot[:-1]):
		deltaX = x - xPlot[i+1]
		SCol = deltaX*yPlot[i+1]
		Area += SCol

	print(Area)

	NDots = len(xPlot)

	fig, ax = aplt.subplots(1, 1, name="fig", figsize=(800, 800))

	curve = root.TGraph(NDots, xPlot, yPlot)
	curve.SetLineColor(4)
	curve.SetLineWidth(2)
	curve.GetXaxis().SetTitle(f"MLP{model_id} signal efficiency")
	curve.GetYaxis().SetTitle(f"MLP{model_id} background rejection")
	curve.SetMarkerSize(0)

	ax.plot(curve)

	ax.text(0.19, 0.92, "#sqrt{s} = 13 TeV, 139 fb^{-1}", size=27, align=13)
	ax.text(0.195, 0.8, f"Area under ROC-curve: {round(area, 3)}")
	fig.savefig(f"MLP{model_id}ROC_curve.pdf")

	# input()


if __name__ == "__main__":
	root.TMVA.Tools.Instance()
	model_id = input("ID: ")
	plot_data = build_reader(model_id)
	plot(plot_data, model_id)
