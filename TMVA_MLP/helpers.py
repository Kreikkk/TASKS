import numpy as np
import ROOT as root
import atlasplots as aplt


def normalized_hist_to_array(hist, nbins, include_error=True):
	arr = []
	if include_error:
		for index in range(1, nbins+1):
			arr.append(hist.GetBinContent(index) + hist.GetBinErrorUp(index))
	else:
		for index in range(1, nbins+1):
			arr.append(hist.GetBinContent(index))

	sum_of_weights = hist.GetSumOfWeights()

	return np.array(arr)/sum_of_weights


def get_hist_max(hist, nbins, include_error=True):
	arr = normalized_hist_to_array(hist, nbins, include_error)
	return np.max(arr)


def error(signal_events, bg_events):
	S = np.sum(signal_events)
	B = np.sum(bg_events)

	SErr = np.sum(signal_events**2)**0.5
	BErr = np.sum(bg_events**2)**0.5

	SPart = (S + B)**(-0.5) - 0.5*S*((S + B)**(-1.5))
	BPart = -0.5*S*((S + B)**(-1.5))

	return ((SPart*SErr)**2 + (BPart*BErr)**2)**0.5


def reset_error(hist, nbins):
	for index in range(1, nbins+1):
		hist.SetBinError(index, np.sqrt(hist.GetBinContent(index)))


def reset_ratio_errors(hist1, hist2, ratio, nbins):
	for index in range(1, nbins+1):
		val1 = hist1.GetBinContent(index)
		err1 = hist1.GetBinError(index)

		val2 = hist2.GetBinContent(index)
		err2 = hist2.GetBinError(index)

		val = ratio.GetBinContent(index)
		err = val*np.sqrt((err1/val1)**2 + (err2/val2)**2)

		ratio.SetBinError(index, err)


def get_contour_ys(hist, nbins):
	ylow, yup = [], []
	for index in range(1, nbins+1):
		val = hist.GetBinContent(index)
		err = hist.GetBinError(index)
		try:
			# print(f"Bin: {index}, RelError: {err/val}, Low: {1 - err/val}, Up: {1 + err/val}")
			ylow.append(1 - err/val)
			yup.append(1 + err/val)
		except ZeroDivisionError:
			# print(f"Bin: {index}, RelError: {1}, Low: {1 - 1}, Up: {1 + 1}")
			ylow.append(1 - 1)
			yup.append(1 + 1)

	return ylow, yup


def setup(fontsize=27):
	root.TMVA.Tools.Instance()
	aplt.set_atlas_style(fontsize)
	root.gStyle.SetErrorX(0.5)
	root.gStyle.SetEndErrorSize(0.1)