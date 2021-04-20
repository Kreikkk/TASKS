sig_max_file = open("results/sig_max.txt", "w")
optimal_cut_file = open("results/optimal_cut.txt", "w")
sig_err_file = open("results/sig_err.txt", "w")
roc_area_file = open("results/roc_area.txt", "w")


for i in range(1, 55):
	with open(f"out{i}.txt") as readfile:
		sig_max 			= readfile.readline().split(":")[1]
		optimal_cut 		= readfile.readline().split(":")[1]
		sig_err 			= readfile.readline().split(":")[1]
		roc_area 			= readfile.readline().split(":")[1]

		sig_max_file.write(sig_max)
		optimal_cut_file.write(optimal_cut)
		sig_err_file.write(sig_err)
		roc_area_file.write(roc_area)

sig_max_file.close()
optimal_cut_file.close()
sig_err_file.close()
roc_area_file.close()