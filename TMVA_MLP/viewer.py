import ROOT as root


if __name__ == "__main__":
	t = input()
	root.TMVA.Tools.Instance()
	root.TMVA.TMVAGui(f"{t}.root")
	root.gApplication.Run()