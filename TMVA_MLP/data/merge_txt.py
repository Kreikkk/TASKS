# sig_max_file = open("results/sig_max.txt", "w")
# optimal_cut_file = open("results/optimal_cut.txt", "w")
# sig_err_file = open("results/sig_err.txt", "w")
# roc_area_file = open("results/roc_area.txt", "w")


# for i in range(1, 55):
# 	with open(f"out{i}.txt") as readfile:
# 		sig_max 			= readfile.readline().split(":")[1]
# 		optimal_cut 		= readfile.readline().split(":")[1]
# 		sig_err 			= readfile.readline().split(":")[1]
# 		roc_area 			= readfile.readline().split(":")[1]

# 		sig_max_file.write(sig_max)
# 		optimal_cut_file.write(optimal_cut)
# 		sig_err_file.write(sig_err)
# 		roc_area_file.write(roc_area)

# sig_max_file.close()
# optimal_cut_file.close()
# sig_err_file.close()
# roc_area_file.close()

# time = open("results/time.txt", "w")

# for i in range(1, 55):
# 	with open(f"out{i}zzz.txt") as readfile:
# 		tm = readfile.readline()
# 		time.write(tm+"\n")

# time.close()

SChi_file = open("results/SChi.txt", "w")
BChi_file = open("results/BChi.txt", "w")
SChi_over_ndof_file = open("results/SChi_over_ndof.txt", "w")
BChi_over_ndof_file = open("results/BChi_over_ndof.txt", "w")
SPval_file = open("results/SPval.txt", "w")
BPval_file = open("results/BPval.txt", "w")


for i in range(1, 55):
	with open(f"out{i}chi.txt") as readfile:
		SChi 			= readfile.readline().split(":")[1]
		BChi 			= readfile.readline().split(":")[1]
		SChi_over_ndof 	= readfile.readline().split(":")[1]
		BChi_over_ndof 	= readfile.readline().split(":")[1]
		SPval 			= readfile.readline().split(":")[1]
		BPval 			= readfile.readline().split(":")[1]

		SChi_file.write(SChi)
		BChi_file.write(BChi)
		SChi_over_ndof_file.write(SChi_over_ndof)
		BChi_over_ndof_file.write(BChi_over_ndof)
		SPval_file.write(SPval)
		BPval_file.write(BPval)

SChi_file.close()
BChi_file.close()
SChi_over_ndof_file.close()
BChi_over_ndof_file.close()
SPval_file.close()
BPval_file.close()