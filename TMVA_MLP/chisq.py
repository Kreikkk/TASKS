import numpy as np


def chisq(hist_true, hist_exp, tp):
	# array_true, array_exp = [], []
	# for ind in range(1, nbins+1):
	# 	array_true.append(hist_true.GetBinContent(ind))
	# 	array_exp.append(hist_exp.GetBinContent(ind))

	# array_true = np.array(array_true)
	# array_exp = np.array(array_exp)
	
	# array_true_norm = array_true/array_true.sum()
	# Nexp = array_exp.sum()
	
	# array_exp_norm = array_exp/Nexp
	# SUM = (((array_exp_norm-array_true_norm)**2)/array_true_norm).sum()

	# print(array_exp_norm)
	# print(array_true_norm)


	# return Nexp*SUM, Nexp*SUM/(nbins-ndepval)

	chisq = hist_true.Chi2Test(hist_exp, option="WW CHI2")
	p_val = hist_true.Chi2Test(hist_exp, option="WW")
	chisq_over_ndof = hist_true.Chi2Test(hist_exp, option="WW CHI2/NDF")

	return chisq, chisq_over_ndof, p_val