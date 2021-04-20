SFILENAME	= "ZgEWK.root"
BFILENAMES	= ["ZgQCD.root", "ttgamma.root", "SinglePhoton.root", "WenuDataDriven.root",
			   "Wgam.root", "WgamEWK.root", "Zllgam.root", "ZnunuFromQcd.root"]

TREENAME = "TMVA_input"


from ROOT import TString as string

METHODNAME = string("BDTgrad")
WEIGHTSPATH = string("dataloader/weights/TMVAClassification_BDTG.weights.xml")



BDTSTEP = 0.005


COMBINATIONS = ""
IGNORE_GRAPH_SHOW = True
GRAPHING = True

STG = 	{"mJJ":			{"step":5, "sign":"+", "max": 2000},
		 "deltaYJJ":	{"step":0.01, "sign":"+", "max": 4},
		 "phCentrality":{"step":0.001, "sign":"-", "max": 1},
		 "ptBalance":	{"step":0.002, "sign":"-", "max": 0.3}}


MARGINS = {"mJJ":				[0, 3500, 0, 0.36],
		   "deltaYJJ":			[0, 8, 0, 0.09],
		   "metPt":				[150, 900, 0, 0.17],
		   "ptBalance":			[0, 0.2, 0, 0.31],
		   "subleadJetEta":		[-4.5, 4.5, 0, 0.05],
		   "leadJetPt":			[50, 800, 0, 0.25],
		   "photonEta":			[-2.5, 2.5, 0, 0.035],
		   "ptBalanceRed":		[0.1, 1, 0, 0.045],
		   "nJets":				[2, 8, 0, 0.8],
		   "sinDeltaPhiJJOver2":[0, 1, 0, 0.24],
		   "deltaYJPh":			[0, 5, 0, 0.08],
		   "phCentrality":		[0, 1, 0, 1]} # Почему такое распределение?

TITLES = {"mJJ": "m_{jj}[TeV]",
		  "deltaYJJ": "#DeltaY(j_{1},j_{2})",
		  "metPt": "E^{miss}_{T}[GeV]",
		  "ptBalance": "p_{T}- balance",
		  "subleadJetEta": "#eta(j_{2})",
		  "leadJetPt": "p_{T}(j_{1})[GeV]",
		  "photonEta": "#eta(#gamma)",
		  "ptBalanceRed": "p_{T}- balance(reduced)",
		  "nJets": "N_{jets}",
		  "sinDeltaPhiJJOver2": "sin(|#Delta#varphi(j_{1},j_{2})|)",
		  "deltaYJPh":"#DeltaY(j_{1},#gamma)",
		  "phCentrality": "#gamma_{cent}"}


YLIMS = {"mJJ": (1.6 ,3.4),
		 "ptBalance": (0, 3.9),
		 "deltaYJJ": (2.6 ,3.35),
		 "phCentrality": (0 ,2.37)}


SHOWHIST = True
SAVEPNG = False
DEF_BINS = 50
FILTER = 1