import numpy as np
import ROOT as root
from array import array

from chisq import chisq
from helpers import *


def clear_file(filename):
	with open(f"data/{filename}.txt", "w"):
		pass


def dump(filename, data):
	with open(f"data/{filename}chi.txt", "a") as file:
		file.write(data)


def significance_plot(SDataframe, BDataframe, ratio, ndots=1000, model_id="", ROC=True):
	Min = np.max((np.min(SDataframe["BDToutput"]), np.min(BDataframe["BDToutput"])))
	Max = np.min((np.max(SDataframe["BDToutput"]), np.max(BDataframe["BDToutput"])))
	SWSum = np.sum(SDataframe["weightModified"])
	BWSum = np.sum(BDataframe["weightModified"])

	XData = np.linspace(Min, Max, ndots)
	SData, BData = np.array([]), np.array([])
	for cursor in XData:
		S = np.sum(SDataframe[SDataframe["BDToutput"] >= cursor]["weightModified"])
		B = np.sum(BDataframe[BDataframe["BDToutput"] >= cursor]["weightModified"])
		SData = np.append(SData, S)
		BData = np.append(BData, B)

	YData = SData/np.sqrt(ratio*(SData+BData))
	SEff = SData/SWSum
	BRej = 1 - BData/BWSum

	XPlot, YPlot = array("d"), array("d")
	for x, y in zip(XData, YData):
		XPlot.append(x)
		YPlot.append(y)

	curve = root.TGraph(ndots, XPlot, YPlot)
	curve.SetLineColor(2)

	curve.SetLineWidth(2)
	curve.SetMarkerColor(2)
	curve.SetMarkerSize(0)
	curve.GetXaxis().SetRangeUser(0, 1)
	curve.GetXaxis().SetTitle(f"Cut value applied on TMVA_MLP-{model_id} output")
	curve.GetYaxis().SetTitle('Significance')

	fig, ax = aplt.subplots(1, 1, name="", figsize=(800, 600))
	ax.plot(curve)

	ax.add_margins(top=0.16)

	peak_index = YData.argmax()
	cut = XData[peak_index]
	sig_max = YData[peak_index]

	ax.text(0.2, 0.92, "#sqrt{s} = 13 TeV, 139 fb^{-1}", size=27, align=13)

	text1 = "For {} signal and {} background".\
		format(round(np.sum(SDataframe["weightModified"])),
			   round(np.sum(BDataframe["weightModified"])))

	text2 = "events the maximum {} is".format("S/#sqrt{S+B}")
	text3 = "{} when cutting at {}".format(round(sig_max, 3),
										   round(cut, 3))

	ax.text(0.2, 0.3, text1, size=20, align=13)
	ax.text(0.2, 0.27, text2, size=20, align=13)
	ax.text(0.2, 0.22, text3, size=20, align=13)

	line = root.TLine(cut, 0, cut, 4)
	line.SetLineStyle(10)
	line.SetLineColor(6)
	ax.plot(line)

	fig.savefig(f"pictures_sig/TMVA_MLP-{model_id}_outputCut.pdf")

	SWCut = np.array(SDataframe[SDataframe["BDToutput"] > cut]["weightModified"])
	BWCut = np.array(BDataframe[BDataframe["BDToutput"] > cut]["weightModified"])
	print("Significance error:")
	err = error(SWCut, BWCut)/np.sqrt(ratio)	### Нужно ли делить на sqrt(ratio)?

	print(err)

	dump(model_id, "sig_max:"+str(round(sig_max, 3))+"\n")
	dump(model_id, "optimal_cut:"+str(round(cut, 3))+"\n")
	dump(model_id, "sig_err:"+str(round(err, 3))+"\n")

	if ROC:
		ROC_plot(SEff, BRej, model_id=model_id)


def ROC_plot(SEff, BRej, model_id=""):
	area = 0
	for index, xval in enumerate(SEff[:-1]):
		delta = SEff[index+1] - xval
		area -= delta*BRej[index]

	XPlot, YPlot = array("d"), array("d")
	for x, y in zip(SEff, BRej):
		XPlot.append(x)
		YPlot.append(y)

	ndots = len(SEff)

	fig, ax = aplt.subplots(1, 1, name="fig", figsize=(800, 800))

	curve = root.TGraph(ndots, XPlot, YPlot)
	curve.SetLineColor(4)
	curve.SetLineWidth(2)
	curve.GetXaxis().SetTitle(f"TMVA_MLP-{model_id} signal efficiency")
	curve.GetYaxis().SetTitle(f"TMVA_MLP-{model_id} background rejection")
	curve.SetMarkerSize(0)

	ax.plot(curve)

	ax.text(0.19, 0.92, "#sqrt{s} = 13 TeV, 139 fb^{-1}", size=27, align=13)
	ax.text(0.195, 0.84, f"Area under ROC-curve: {round(area, 3)}")

	dump(model_id, "roc_area:"+str(round(area, 3))+"\n")
	fig.savefig(f"pictures_roc/TMVA_MLP-{model_id}_ROC_curve.pdf")


def BDT_output_hist_plot(STestDataframe, BTestDataframe,
						 STrainDataframe, BTrainDataframe, model_id=""):

	STestHist = root.TH1F("", "", 20, 0, 1)
	BTestHist = root.TH1F("", "", 20, 0, 1)
	STrainHist = root.TH1F("", "", 20, 0, 1)
	BTrainHist = root.TH1F ("", "", 20, 0, 1)

	STestHist.SetStats(False)
	BTestHist.SetStats(False)
	STestHist.SetMinimum(0)
	BTestHist.SetMinimum(0)
	STestHist.SetLineWidth(2)
	BTestHist.SetLineWidth(2)
	STestHist.SetLineColor(4)
	BTestHist.SetLineColor(2)
	STestHist.SetMarkerSize(0)
	BTestHist.SetMarkerSize(0)

	STestHist.SetFillColorAlpha(4, 0.2)
	BTestHist.SetFillColor(2)
	BTestHist.SetFillStyle(3004)

	STrainHist.SetStats(False)
	BTrainHist.SetStats(False)
	STrainHist.SetMinimum(0)
	BTrainHist.SetMinimum(0)
	STrainHist.SetLineWidth(2)
	BTrainHist.SetLineWidth(2)
	STrainHist.SetLineColor(4)
	BTrainHist.SetLineColor(2)
	STrainHist.SetMarkerSize(1)
	BTrainHist.SetMarkerSize(1)
	STrainHist.SetMarkerColor(4)
	BTrainHist.SetMarkerColor(2)


	for out, weight in zip(STestDataframe["BDToutput"], STestDataframe["weightModified"]):
		STestHist.Fill(out, weight)
	for out, weight in zip(BTestDataframe["BDToutput"], BTestDataframe["weightModified"]):
		BTestHist.Fill(out, weight)

	for out, weight in zip(STrainDataframe["BDToutput"], STrainDataframe["weightModified"]):
		STrainHist.Fill(out, weight)
	for out, weight in zip(BTrainDataframe["BDToutput"], BTrainDataframe["weightModified"]):
		BTrainHist.Fill(out, weight)

	SChi, SChi_over_ndof, SPval = chisq(STrainHist, STestHist, "signal")
	BChi, BChi_over_ndof, BPval = chisq(BTrainHist, BTestHist, "background")

	dump(model_id, f"SChi:{round(SChi, 3)}\n")
	dump(model_id, f"BChi:{round(BChi, 3)}\n")
	dump(model_id, f"SChi_over_ndof:{round(SChi_over_ndof, 3)}\n")
	dump(model_id, f"BChi_over_ndof:{round(BChi_over_ndof, 3)}\n")
	dump(model_id, f"SPval:{round(SPval, 3)}\n")
	dump(model_id, f"BPval:{round(BPval, 3)}\n")

	hists_max = np.max((get_hist_max(STestHist, 20),
						get_hist_max(BTestHist, 20),
						get_hist_max(STrainHist, 20),
						get_hist_max(BTrainHist, 20),))

	margins = [0, 1, 0, hists_max]

	fig, (ax1, ax2, ax3) = aplt.ratio_plot(name="", dbl=True, figsize=(800, 1000), hspace=0.05)

	ax1.plot(STestHist, margins, "NORM HIST")
	ax1.plot(BTestHist, margins, "NORM HIST")
	ax1.plot(STrainHist, margins, "E1 NORM")
	ax1.plot(BTrainHist, margins, "E1 NORM")

	ylow, yup = get_contour_ys(STestHist, 20)
	SYLowHist = root.TH1F("", "", 20, 0, 1)
	SYUpHist = root.TH1F("", "", 20, 0, 1)


	SYUpHist.SetLineWidth(0)
	SYUpHist.SetFillColorAlpha(4, 0.2)

	SYLowHist.SetLineWidth(0)
	SYLowHist.SetFillColor(10)


	for ind, (low, up) in enumerate(zip(ylow, yup)):
		SYLowHist.SetBinContent(ind+1, low)
		SYUpHist.SetBinContent(ind+1, up)

	ax2.plot(SYUpHist, margins=[0, 1, 0.25, 1.75], options="HIST")
	ax2.plot(SYLowHist, margins=[0, 1, 0.25, 1.75], options="HIST")

	SRatio = STrainHist.Clone()
	SRatio.GetYaxis().CenterTitle(True)
	SRatio.Divide(STestHist)
	ax2.plot(SRatio, margins=[0, 1, 0.25, 1.75], options="E1")

	ylow, yup = get_contour_ys(BTestHist, 20)
	BYLowHist = root.TH1F("", "", 20, 0, 1)
	BYUpHist = root.TH1F("", "", 20, 0, 1)

	BYUpHist.SetLineWidth(0)
	BYUpHist.SetFillColorAlpha(2, 0.2)

	BYLowHist.SetLineWidth(0)
	BYLowHist.SetFillColor(10)


	for ind, (low, up) in enumerate(zip(ylow, yup)):
		BYLowHist.SetBinContent(ind+1, low)
		BYUpHist.SetBinContent(ind+1, up)

	ax3.plot(BYUpHist, margins=[0, 1, 0.25, 1.75], options="HIST")
	ax3.plot(BYLowHist, margins=[0, 1, 0.25, 1.75], options="HIST")

	BRatio = BTrainHist.Clone()
	BRatio.GetYaxis().CenterTitle(True)
	BRatio.Divide(BTestHist)
	ax3.plot(BRatio, margins=[0, 1, 0.25, 1.75], options="E1")

	ax1.add_margins(top=0.25)

	ax3.set_xlabel(f"TMVA_MLP-{model_id} classifier response")
	ax1.set_ylabel("Fraction of events")
	ax1.text(0.16, 0.8, "#sqrt{s} = 13 TeV, 139 fb^{-1}", size=24, align=13)
	ax1.text(0.56, 0.79, "Signal #chi^{2}/N_{dof} = " +  str(round(SChi_over_ndof, 3)), size=20, align=13)
	ax1.text(0.56, 0.73, "Background #chi^{2}/N_{dof} = " + str(round(BChi_over_ndof, 3)), size=20, align=13)
	ax2.set_ylabel("Train/Test")
	ax3.set_ylabel("Train/Test")

	line = root.TLine(0, 1, 1, 1)

	ax2.plot(line)
	ax3.plot(line)

	ax1.cd()

	legend1 = root.TLegend(0.15, 0.82, 0.46, 0.97)
	legend2 = root.TLegend(0.55, 0.82, 0.86, 0.97)
	root.gStyle.SetLegendTextSize(24)

	legend1.SetFillColorAlpha(0, 0)
	legend2.SetFillColorAlpha(0, 0)

	legend1.AddEntry(STestHist, "Signal (test sample)", "F")
	legend1.AddEntry(BTestHist, "Background (test sample)", "F")
	legend2.AddEntry(STrainHist, "Signal (train sample)", "F")
	legend2.AddEntry(BTrainHist, "Background (train sample)", "F")
	legend1.Draw()
	legend2.Draw()

	fig.savefig(f"pictures/TMVA_MLP-{model_id}_output.pdf")