// Class: ReadMLP
// Automatically generated by MethodBase::MakeClass
//

/* configuration options =====================================================

#GEN -*-*-*-*-*-*-*-*-*-*-*- general info -*-*-*-*-*-*-*-*-*-*-*-

Method         : MLP::MLP
TMVA Release   : 4.2.1         [262657]
ROOT Release   : 6.22/06       [398854]
Creator        : konstantin
Date           : Wed Mar 24 00:04:43 2021
Host           : Linux mach 5.8.0-43-generic #49~20.04.1-Ubuntu SMP Fri Feb 5 09:57:56 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
Dir            : /home/konstantin/Projects/CERN/TMVA_MLP
Training events: 170672
Analysis type  : [Classification]


#OPT -*-*-*-*-*-*-*-*-*-*-*-*- options -*-*-*-*-*-*-*-*-*-*-*-*-

# Set by User:
NCycles: "400" [Number of training cycles]
HiddenLayers: "N,N" [Specification of hidden layer architecture]
NeuronType: "sigmoid" [Neuron activation function type]
V: "False" [Verbose output (short form of "VerbosityLevel" below - overrides the latter one)]
VarTransform: "N" [List of variable transformations performed before training, e.g., "D_Background,P_Signal,G,N_AllClasses" for: "Decorrelation, PCA-transformation, Gaussianisation, Normalisation, each for the given class of events ('AllClasses' denotes all events of all classes, if no class indication is given, 'All' is assumed)"]
H: "True" [Print method-specific help message]
LearningRate: "2.000000e-02" [ANN learning rate parameter]
TestRate: "5" [Test for overtraining performed at each #th epochs]
BPMode: "batch" [Back-propagation learning mode: sequential or batch]
BatchSize: "3" [Batch size: number of events/batch, only set if in Batch Mode, -1 for BatchSize=number_of_events]
ConvergenceImprove: "2.500000e-03" [Minimum improvement which counts as improvement (<0 means automatic convergence check is turned off)]
ConvergenceTests: "5" [Number of steps (without improvement) required for convergence (<0 means automatic convergence check is turned off)]
UseRegulator: "False" [Use regulator to avoid over-training]
# Default:
RandomSeed: "1" [Random seed for initial synapse weights (0 means unique seed for each run; default value '1')]
EstimatorType: "CE" [MSE (Mean Square Estimator) for Gaussian Likelihood or CE(Cross-Entropy) for Bernoulli Likelihood]
NeuronInputType: "sum" [Neuron input function type]
VerbosityLevel: "Default" [Verbosity level]
CreateMVAPdfs: "False" [Create PDFs for classifier outputs (signal and background)]
IgnoreNegWeightsInTraining: "False" [Events with negative weights are ignored in the training (but are included for testing and performance evaluation)]
TrainingMethod: "BP" [Train with Back-Propagation (BP), BFGS Algorithm (BFGS), or Genetic Algorithm (GA - slower and worse)]
DecayRate: "1.000000e-02" [Decay rate for learning parameter]
EpochMonitoring: "False" [Provide epoch-wise monitoring plots according to TestRate (caution: causes big ROOT output file!)]
Sampling: "1.000000e+00" [Only 'Sampling' (randomly selected) events are trained each epoch]
SamplingEpoch: "1.000000e+00" [Sampling is used for the first 'SamplingEpoch' epochs, afterwards, all events are taken for training]
SamplingImportance: "1.000000e+00" [ The sampling weights of events in epochs which successful (worse estimator than before) are multiplied with SamplingImportance, else they are divided.]
SamplingTraining: "True" [The training sample is sampled]
SamplingTesting: "False" [The testing sample is sampled]
ResetStep: "50" [How often BFGS should reset history]
Tau: "3.000000e+00" [LineSearch "size step"]
UpdateLimit: "10000" [Maximum times of regulator update]
CalculateErrors: "False" [Calculates inverse Hessian matrix at the end of the training to be able to calculate the uncertainties of an MVA value]
WeightRange: "1.000000e+00" [Take the events for the estimator calculations from small deviations from the desired value to large deviations only over the weight range]
##


#VAR -*-*-*-*-*-*-*-*-*-*-*-* variables *-*-*-*-*-*-*-*-*-*-*-*-

NVar 11
mJJ                           mJJ                           mJJ                           mJJ                                                             'F'    [22.7864818573,7838.75537109]
deltaYJJ                      deltaYJJ                      deltaYJJ                      deltaYJJ                                                        'F'    [2.2119609639e-05,8.68471050262]
metPt                         metPt                         metPt                         metPt                                                           'F'    [125.825294495,2277.4987793]
ptBalance                     ptBalance                     ptBalance                     ptBalance                                                       'F'    [4.91857872476e-06,0.47649076581]
subleadJetEta                 subleadJetEta                 subleadJetEta                 subleadJetEta                                                   'F'    [-4.50663423538,4.51134681702]
leadJetPt                     leadJetPt                     leadJetPt                     leadJetPt                                                       'F'    [50.0584754944,2753.2824707]
photonEta                     photonEta                     photonEta                     photonEta                                                       'F'    [-2.4010925293,2.39041256905]
ptBalanceRed                  ptBalanceRed                  ptBalanceRed                  ptBalanceRed                                                    'F'    [0.0229892414063,0.999983787537]
nJets                         nJets                         nJets                         nJets                                                           'F'    [2,9]
sinDeltaPhiJJOver2            sinDeltaPhiJJOver2            sinDeltaPhiJJOver2            sinDeltaPhiJJOver2                                              'F'    [1.5914440155e-05,1]
deltaYJPh                     deltaYJPh                     deltaYJPh                     deltaYJPh                                                       'F'    [1.18112052405e-06,6.68952894211]
NSpec 1
weightModified                weightModified                weightModified                F                                                               'F'    [-0.191263645887,1.09073340893]


============================================================================ */

#include <array>
#include <vector>
#include <cmath>
#include <string>
#include <iostream>

#ifndef IClassifierReader__def
#define IClassifierReader__def

class IClassifierReader {

 public:

   // constructor
   IClassifierReader() : fStatusIsClean( true ) {}
   virtual ~IClassifierReader() {}

   // return classifier response
   virtual double GetMvaValue( const std::vector<double>& inputValues ) const = 0;

   // returns classifier status
   bool IsStatusClean() const { return fStatusIsClean; }

 protected:

   bool fStatusIsClean;
};

#endif

class ReadMLP : public IClassifierReader {

 public:

   // constructor
   ReadMLP( std::vector<std::string>& theInputVars )
      : IClassifierReader(),
        fClassName( "ReadMLP" ),
        fNvars( 11 )
   {
      // the training input variables
      const char* inputVars[] = { "mJJ", "deltaYJJ", "metPt", "ptBalance", "subleadJetEta", "leadJetPt", "photonEta", "ptBalanceRed", "nJets", "sinDeltaPhiJJOver2", "deltaYJPh" };

      // sanity checks
      if (theInputVars.size() <= 0) {
         std::cout << "Problem in class \"" << fClassName << "\": empty input vector" << std::endl;
         fStatusIsClean = false;
      }

      if (theInputVars.size() != fNvars) {
         std::cout << "Problem in class \"" << fClassName << "\": mismatch in number of input values: "
                   << theInputVars.size() << " != " << fNvars << std::endl;
         fStatusIsClean = false;
      }

      // validate input variables
      for (size_t ivar = 0; ivar < theInputVars.size(); ivar++) {
         if (theInputVars[ivar] != inputVars[ivar]) {
            std::cout << "Problem in class \"" << fClassName << "\": mismatch in input variable names" << std::endl
                      << " for variable [" << ivar << "]: " << theInputVars[ivar].c_str() << " != " << inputVars[ivar] << std::endl;
            fStatusIsClean = false;
         }
      }

      // initialize min and max vectors (for normalisation)
      fVmin[0] = -1;
      fVmax[0] = 0.99999988079071;
      fVmin[1] = -1;
      fVmax[1] = 1;
      fVmin[2] = -1;
      fVmax[2] = 1;
      fVmin[3] = -1;
      fVmax[3] = 0.99999988079071;
      fVmin[4] = -1;
      fVmax[4] = 1;
      fVmin[5] = -1;
      fVmax[5] = 1;
      fVmin[6] = -1;
      fVmax[6] = 1;
      fVmin[7] = -1;
      fVmax[7] = 1;
      fVmin[8] = -1;
      fVmax[8] = 1;
      fVmin[9] = -1;
      fVmax[9] = 1;
      fVmin[10] = -1;
      fVmax[10] = 1;

      // initialize input variable types
      fType[0] = 'F';
      fType[1] = 'F';
      fType[2] = 'F';
      fType[3] = 'F';
      fType[4] = 'F';
      fType[5] = 'F';
      fType[6] = 'F';
      fType[7] = 'F';
      fType[8] = 'F';
      fType[9] = 'F';
      fType[10] = 'F';

      // initialize constants
      Initialize();

      // initialize transformation
      InitTransform();
   }

   // destructor
   virtual ~ReadMLP() {
      Clear(); // method-specific
   }

   // the classifier response
   // "inputValues" is a vector of input values in the same order as the
   // variables given to the constructor
   double GetMvaValue( const std::vector<double>& inputValues ) const override;

 private:

   // method-specific destructor
   void Clear();

   // input variable transformation

   double fOff_1[3][11];
   double fScal_1[3][11];
   void InitTransform_1();
   void Transform_1( std::vector<double> & iv, int sigOrBgd ) const;
   void InitTransform();
   void Transform( std::vector<double> & iv, int sigOrBgd ) const;

   // common member variables
   const char* fClassName;

   const size_t fNvars;
   size_t GetNvar()           const { return fNvars; }
   char   GetType( int ivar ) const { return fType[ivar]; }

   // normalisation of input variables
   double fVmin[11];
   double fVmax[11];
   double NormVariable( double x, double xmin, double xmax ) const {
      // normalise to output range: [-1, 1]
      return 2*(x - xmin)/(xmax - xmin) - 1.0;
   }

   // type of input variable: 'F' or 'I'
   char   fType[11];

   // initialize internal variables
   void Initialize();
   double GetMvaValue__( const std::vector<double>& inputValues ) const;

   // private members (method specific)

   double ActivationFnc(double x) const;
   double OutputActivationFnc(double x) const;

   double fWeightMatrix0to1[12][12];   // weight matrix from layer 0 to 1
   double fWeightMatrix1to2[12][12];   // weight matrix from layer 1 to 2
   double fWeightMatrix2to3[1][12];   // weight matrix from layer 2 to 3

};

inline void ReadMLP::Initialize()
{
   // build network structure
   // weight matrix from layer 0 to 1
   fWeightMatrix0to1[0][0] = -0.606308735510521;
   fWeightMatrix0to1[1][0] = -0.0451538176806079;
   fWeightMatrix0to1[2][0] = 1.02797055720191;
   fWeightMatrix0to1[3][0] = 6.57660645640167;
   fWeightMatrix0to1[4][0] = -3.3082316731326;
   fWeightMatrix0to1[5][0] = -0.653415700417494;
   fWeightMatrix0to1[6][0] = -1.17936828371433;
   fWeightMatrix0to1[7][0] = 1.48576563548754;
   fWeightMatrix0to1[8][0] = 3.50026351048782;
   fWeightMatrix0to1[9][0] = -4.03452702256632;
   fWeightMatrix0to1[10][0] = -6.81820979317525;
   fWeightMatrix0to1[0][1] = -0.0591306393206655;
   fWeightMatrix0to1[1][1] = 0.293567388268884;
   fWeightMatrix0to1[2][1] = -0.172432156268119;
   fWeightMatrix0to1[3][1] = -0.525524990381421;
   fWeightMatrix0to1[4][1] = -1.00115464222305;
   fWeightMatrix0to1[5][1] = 2.44521081160575;
   fWeightMatrix0to1[6][1] = 2.55750614273362;
   fWeightMatrix0to1[7][1] = -0.732930053657277;
   fWeightMatrix0to1[8][1] = 4.15633098977037;
   fWeightMatrix0to1[9][1] = -4.70288518214628;
   fWeightMatrix0to1[10][1] = -1.8191191763715;
   fWeightMatrix0to1[0][2] = 4.98408687268213;
   fWeightMatrix0to1[1][2] = -0.4528563768091;
   fWeightMatrix0to1[2][2] = -1.29176019989128;
   fWeightMatrix0to1[3][2] = 0.747171036598778;
   fWeightMatrix0to1[4][2] = 0.714321606392072;
   fWeightMatrix0to1[5][2] = 0.17911308640811;
   fWeightMatrix0to1[6][2] = -1.80325203069625;
   fWeightMatrix0to1[7][2] = -1.47803329233194;
   fWeightMatrix0to1[8][2] = 0.164988307640318;
   fWeightMatrix0to1[9][2] = 1.34067424694551;
   fWeightMatrix0to1[10][2] = -0.761686898158342;
   fWeightMatrix0to1[0][3] = 0.259709805345359;
   fWeightMatrix0to1[1][3] = -0.919995121759219;
   fWeightMatrix0to1[2][3] = -0.484243468959367;
   fWeightMatrix0to1[3][3] = -6.54458508931099;
   fWeightMatrix0to1[4][3] = 0.15175542020008;
   fWeightMatrix0to1[5][3] = -0.121225636170794;
   fWeightMatrix0to1[6][3] = -1.4036862335489;
   fWeightMatrix0to1[7][3] = 0.441288673050375;
   fWeightMatrix0to1[8][3] = -0.423749278726796;
   fWeightMatrix0to1[9][3] = 0.487915913898602;
   fWeightMatrix0to1[10][3] = 0.263991609555469;
   fWeightMatrix0to1[0][4] = -0.735632402571907;
   fWeightMatrix0to1[1][4] = 0.105179649180159;
   fWeightMatrix0to1[2][4] = 0.623668653561261;
   fWeightMatrix0to1[3][4] = 0.239935028941487;
   fWeightMatrix0to1[4][4] = -0.106498162115692;
   fWeightMatrix0to1[5][4] = 5.42890161845541;
   fWeightMatrix0to1[6][4] = -0.483444380440524;
   fWeightMatrix0to1[7][4] = 0.109101647474737;
   fWeightMatrix0to1[8][4] = -5.78720029229621;
   fWeightMatrix0to1[9][4] = -1.36205088559841;
   fWeightMatrix0to1[10][4] = -1.73446006188725;
   fWeightMatrix0to1[0][5] = -2.33394282989965;
   fWeightMatrix0to1[1][5] = -1.2365974060878;
   fWeightMatrix0to1[2][5] = -1.80386456156318;
   fWeightMatrix0to1[3][5] = 3.68862649720786;
   fWeightMatrix0to1[4][5] = 1.654661139058;
   fWeightMatrix0to1[5][5] = -2.90050616313659;
   fWeightMatrix0to1[6][5] = 0.606977693329076;
   fWeightMatrix0to1[7][5] = 0.181813433149122;
   fWeightMatrix0to1[8][5] = -1.59423437502126;
   fWeightMatrix0to1[9][5] = 1.73982566752015;
   fWeightMatrix0to1[10][5] = -0.463968370494394;
   fWeightMatrix0to1[0][6] = 0.924411100003898;
   fWeightMatrix0to1[1][6] = 0.28735523083792;
   fWeightMatrix0to1[2][6] = 0.234545137782556;
   fWeightMatrix0to1[3][6] = -0.4075191254021;
   fWeightMatrix0to1[4][6] = -0.292532021784051;
   fWeightMatrix0to1[5][6] = -1.4968593957628;
   fWeightMatrix0to1[6][6] = 0.800636992976509;
   fWeightMatrix0to1[7][6] = 2.23887127933599;
   fWeightMatrix0to1[8][6] = 3.04420074899453;
   fWeightMatrix0to1[9][6] = 1.3348988870011;
   fWeightMatrix0to1[10][6] = 0.298909748105446;
   fWeightMatrix0to1[0][7] = -1.09233642329724;
   fWeightMatrix0to1[1][7] = 2.32558388452953;
   fWeightMatrix0to1[2][7] = 0.555085501798766;
   fWeightMatrix0to1[3][7] = -0.0278007667634452;
   fWeightMatrix0to1[4][7] = 0.397370757144918;
   fWeightMatrix0to1[5][7] = -0.226326135493649;
   fWeightMatrix0to1[6][7] = 0.0969046480085894;
   fWeightMatrix0to1[7][7] = 0.82990303404074;
   fWeightMatrix0to1[8][7] = 0.236767758827094;
   fWeightMatrix0to1[9][7] = -0.651811157840457;
   fWeightMatrix0to1[10][7] = -0.225265873907667;
   fWeightMatrix0to1[0][8] = -3.11981560315969;
   fWeightMatrix0to1[1][8] = -2.11270920436059;
   fWeightMatrix0to1[2][8] = -0.773947299503104;
   fWeightMatrix0to1[3][8] = -0.942397108882049;
   fWeightMatrix0to1[4][8] = 0.515152674924401;
   fWeightMatrix0to1[5][8] = -2.5412184562407;
   fWeightMatrix0to1[6][8] = -3.57634025253065;
   fWeightMatrix0to1[7][8] = 2.37768980004662;
   fWeightMatrix0to1[8][8] = 0.0338761296556979;
   fWeightMatrix0to1[9][8] = -0.6414876503756;
   fWeightMatrix0to1[10][8] = -0.53823657016742;
   fWeightMatrix0to1[0][9] = 0.402732278462805;
   fWeightMatrix0to1[1][9] = -1.42283660941241;
   fWeightMatrix0to1[2][9] = -1.87192479858157;
   fWeightMatrix0to1[3][9] = -0.0191903467071897;
   fWeightMatrix0to1[4][9] = 3.73658701102594;
   fWeightMatrix0to1[5][9] = 0.0372095551895408;
   fWeightMatrix0to1[6][9] = -0.0492138374723496;
   fWeightMatrix0to1[7][9] = -0.0914424733686479;
   fWeightMatrix0to1[8][9] = 0.0625539192049353;
   fWeightMatrix0to1[9][9] = 0.0099665030133203;
   fWeightMatrix0to1[10][9] = 0.0344096684647104;
   fWeightMatrix0to1[0][10] = -2.50292823209498;
   fWeightMatrix0to1[1][10] = 0.693437760227058;
   fWeightMatrix0to1[2][10] = 0.253962366658767;
   fWeightMatrix0to1[3][10] = 0.445607445825505;
   fWeightMatrix0to1[4][10] = 0.622519051388107;
   fWeightMatrix0to1[5][10] = 0.361920274534786;
   fWeightMatrix0to1[6][10] = 0.202474719910581;
   fWeightMatrix0to1[7][10] = -2.01650563735814;
   fWeightMatrix0to1[8][10] = -0.92756261965197;
   fWeightMatrix0to1[9][10] = 2.93574538498047;
   fWeightMatrix0to1[10][10] = -0.462031864417713;
   fWeightMatrix0to1[0][11] = -0.334645641167926;
   fWeightMatrix0to1[1][11] = -2.47450034954882;
   fWeightMatrix0to1[2][11] = 1.88669190540174;
   fWeightMatrix0to1[3][11] = 1.84322718491823;
   fWeightMatrix0to1[4][11] = -3.60896332789891;
   fWeightMatrix0to1[5][11] = -0.614722911496317;
   fWeightMatrix0to1[6][11] = -5.51189864526017;
   fWeightMatrix0to1[7][11] = -0.980565316026711;
   fWeightMatrix0to1[8][11] = 4.73949677332727;
   fWeightMatrix0to1[9][11] = -2.57890703682259;
   fWeightMatrix0to1[10][11] = -9.69422403819742;
   // weight matrix from layer 1 to 2
   fWeightMatrix1to2[0][0] = -0.856897509761652;
   fWeightMatrix1to2[1][0] = -2.55887538362319;
   fWeightMatrix1to2[2][0] = 0.8717488631264;
   fWeightMatrix1to2[3][0] = 0.0920590743021868;
   fWeightMatrix1to2[4][0] = 1.83422476113437;
   fWeightMatrix1to2[5][0] = -1.95008429023089;
   fWeightMatrix1to2[6][0] = -0.552619692375431;
   fWeightMatrix1to2[7][0] = 1.74371079925772;
   fWeightMatrix1to2[8][0] = 2.17716457428677;
   fWeightMatrix1to2[9][0] = -0.908667517288964;
   fWeightMatrix1to2[10][0] = -1.66405401194274;
   fWeightMatrix1to2[0][1] = 0.520065666497561;
   fWeightMatrix1to2[1][1] = -2.45648842614301;
   fWeightMatrix1to2[2][1] = 0.755619705925185;
   fWeightMatrix1to2[3][1] = 0.658799794055314;
   fWeightMatrix1to2[4][1] = -0.559279483713293;
   fWeightMatrix1to2[5][1] = -0.837486599292642;
   fWeightMatrix1to2[6][1] = -0.482217745504872;
   fWeightMatrix1to2[7][1] = -2.92368154886407;
   fWeightMatrix1to2[8][1] = 0.327041098989475;
   fWeightMatrix1to2[9][1] = 0.267542124197271;
   fWeightMatrix1to2[10][1] = 0.517011855860682;
   fWeightMatrix1to2[0][2] = -2.26152067593488;
   fWeightMatrix1to2[1][2] = 0.533513805787916;
   fWeightMatrix1to2[2][2] = 1.29629614102704;
   fWeightMatrix1to2[3][2] = -0.139434440490626;
   fWeightMatrix1to2[4][2] = -2.51220987837048;
   fWeightMatrix1to2[5][2] = -1.14747669490774;
   fWeightMatrix1to2[6][2] = 1.55336736564908;
   fWeightMatrix1to2[7][2] = -0.841501650743124;
   fWeightMatrix1to2[8][2] = 0.279064009013703;
   fWeightMatrix1to2[9][2] = 0.461371893077576;
   fWeightMatrix1to2[10][2] = -0.174527899420185;
   fWeightMatrix1to2[0][3] = -0.626736849528258;
   fWeightMatrix1to2[1][3] = 1.40568480090483;
   fWeightMatrix1to2[2][3] = -0.191002933530239;
   fWeightMatrix1to2[3][3] = -0.0881222829323234;
   fWeightMatrix1to2[4][3] = 1.38185940415413;
   fWeightMatrix1to2[5][3] = 2.16078509101968;
   fWeightMatrix1to2[6][3] = 2.60394135069859;
   fWeightMatrix1to2[7][3] = 1.79826973721465;
   fWeightMatrix1to2[8][3] = 1.74410961330178;
   fWeightMatrix1to2[9][3] = 0.806752460648546;
   fWeightMatrix1to2[10][3] = -5.9122542656019;
   fWeightMatrix1to2[0][4] = -0.656584408107214;
   fWeightMatrix1to2[1][4] = -0.675857534855717;
   fWeightMatrix1to2[2][4] = 1.05288365590048;
   fWeightMatrix1to2[3][4] = -2.75375192922014;
   fWeightMatrix1to2[4][4] = -0.374482993619787;
   fWeightMatrix1to2[5][4] = 1.64277087191014;
   fWeightMatrix1to2[6][4] = 0.949006316644503;
   fWeightMatrix1to2[7][4] = -0.570787893752105;
   fWeightMatrix1to2[8][4] = -0.194899125135683;
   fWeightMatrix1to2[9][4] = -1.42627810914268;
   fWeightMatrix1to2[10][4] = 1.13304236708851;
   fWeightMatrix1to2[0][5] = 1.77084377484183;
   fWeightMatrix1to2[1][5] = -0.552608400811731;
   fWeightMatrix1to2[2][5] = -2.36455399361741;
   fWeightMatrix1to2[3][5] = -2.34924052257782;
   fWeightMatrix1to2[4][5] = 2.54921840579041;
   fWeightMatrix1to2[5][5] = 2.11211693103193;
   fWeightMatrix1to2[6][5] = 1.86132427500826;
   fWeightMatrix1to2[7][5] = 1.29647423950916;
   fWeightMatrix1to2[8][5] = -0.0987449637249142;
   fWeightMatrix1to2[9][5] = -2.3640625731843;
   fWeightMatrix1to2[10][5] = -0.147568337524472;
   fWeightMatrix1to2[0][6] = 0.182796809205341;
   fWeightMatrix1to2[1][6] = -1.20196890067233;
   fWeightMatrix1to2[2][6] = 0.19294255878053;
   fWeightMatrix1to2[3][6] = -0.20988537180455;
   fWeightMatrix1to2[4][6] = 1.14745841876313;
   fWeightMatrix1to2[5][6] = -1.6761466377402;
   fWeightMatrix1to2[6][6] = 3.65053269701748;
   fWeightMatrix1to2[7][6] = 2.10359106719391;
   fWeightMatrix1to2[8][6] = -2.67456416415011;
   fWeightMatrix1to2[9][6] = -1.27656911943218;
   fWeightMatrix1to2[10][6] = 5.91703670898908;
   fWeightMatrix1to2[0][7] = 2.84637474940711;
   fWeightMatrix1to2[1][7] = 1.78696495682478;
   fWeightMatrix1to2[2][7] = 0.0656971261177162;
   fWeightMatrix1to2[3][7] = -2.42255493005028;
   fWeightMatrix1to2[4][7] = -0.715579360477962;
   fWeightMatrix1to2[5][7] = 1.32269980739271;
   fWeightMatrix1to2[6][7] = 1.18765334976566;
   fWeightMatrix1to2[7][7] = -1.25204122510753;
   fWeightMatrix1to2[8][7] = 0.129323992059271;
   fWeightMatrix1to2[9][7] = 2.46672999545674;
   fWeightMatrix1to2[10][7] = -1.13301755676472;
   fWeightMatrix1to2[0][8] = -2.94117068909259;
   fWeightMatrix1to2[1][8] = 0.633976177811967;
   fWeightMatrix1to2[2][8] = -4.48894054358352;
   fWeightMatrix1to2[3][8] = 0.553279424785192;
   fWeightMatrix1to2[4][8] = 3.96277821931018;
   fWeightMatrix1to2[5][8] = -0.625505189944229;
   fWeightMatrix1to2[6][8] = 0.131322582354926;
   fWeightMatrix1to2[7][8] = 3.33108582053488;
   fWeightMatrix1to2[8][8] = -1.60377425905917;
   fWeightMatrix1to2[9][8] = -1.06724788605449;
   fWeightMatrix1to2[10][8] = -1.94674029526125;
   fWeightMatrix1to2[0][9] = 1.75871830390308;
   fWeightMatrix1to2[1][9] = 0.873544280921396;
   fWeightMatrix1to2[2][9] = -3.57099375675127;
   fWeightMatrix1to2[3][9] = 2.58959332631609;
   fWeightMatrix1to2[4][9] = -5.01196795493408;
   fWeightMatrix1to2[5][9] = 1.02352395690092;
   fWeightMatrix1to2[6][9] = -1.49719480632761;
   fWeightMatrix1to2[7][9] = -3.07001789464549;
   fWeightMatrix1to2[8][9] = -1.92112243962698;
   fWeightMatrix1to2[9][9] = -3.31132580266631;
   fWeightMatrix1to2[10][9] = -0.825926127680471;
   fWeightMatrix1to2[0][10] = -4.49905371219485;
   fWeightMatrix1to2[1][10] = -1.35235801783387;
   fWeightMatrix1to2[2][10] = -0.0281717752460375;
   fWeightMatrix1to2[3][10] = 0.497599464114935;
   fWeightMatrix1to2[4][10] = -2.64875219365992;
   fWeightMatrix1to2[5][10] = -1.09350813468788;
   fWeightMatrix1to2[6][10] = 0.282802870301197;
   fWeightMatrix1to2[7][10] = -4.84203653207697;
   fWeightMatrix1to2[8][10] = -1.15164812240887;
   fWeightMatrix1to2[9][10] = -1.30619719312342;
   fWeightMatrix1to2[10][10] = 2.00207007733043;
   fWeightMatrix1to2[0][11] = 0.122766343842218;
   fWeightMatrix1to2[1][11] = 1.45647003366833;
   fWeightMatrix1to2[2][11] = -0.508625078480259;
   fWeightMatrix1to2[3][11] = -2.15309570055867;
   fWeightMatrix1to2[4][11] = -4.69105468152846;
   fWeightMatrix1to2[5][11] = -0.570785004029038;
   fWeightMatrix1to2[6][11] = -1.66871083701276;
   fWeightMatrix1to2[7][11] = -1.12882536257317;
   fWeightMatrix1to2[8][11] = 0.269250643052226;
   fWeightMatrix1to2[9][11] = 1.74830431405591;
   fWeightMatrix1to2[10][11] = -1.58617373147941;
   // weight matrix from layer 2 to 3
   fWeightMatrix2to3[0][0] = 3.42319006527498;
   fWeightMatrix2to3[0][1] = -1.48231096412508;
   fWeightMatrix2to3[0][2] = -3.63666587118051;
   fWeightMatrix2to3[0][3] = 2.57709502699837;
   fWeightMatrix2to3[0][4] = 3.38813510792993;
   fWeightMatrix2to3[0][5] = -1.07687603012997;
   fWeightMatrix2to3[0][6] = -2.45845228368898;
   fWeightMatrix2to3[0][7] = 2.44194681712832;
   fWeightMatrix2to3[0][8] = 1.10213122379955;
   fWeightMatrix2to3[0][9] = -1.45360907368396;
   fWeightMatrix2to3[0][10] = -3.72574679968919;
   fWeightMatrix2to3[0][11] = 0.0373906606836168;
}

inline double ReadMLP::GetMvaValue__( const std::vector<double>& inputValues ) const
{
   if (inputValues.size() != (unsigned int)11) {
      std::cout << "Input vector needs to be of size " << 11 << std::endl;
      return 0;
   }

   std::array<double, 12> fWeights1 {{}};
   std::array<double, 12> fWeights2 {{}};
   std::array<double, 1> fWeights3 {{}};
   fWeights1.back() = 1.;
   fWeights2.back() = 1.;

   // layer 0 to 1
   for (int o=0; o<11; o++) {
      std::array<double, 12> buffer; // no need to initialise
      for (int i = 0; i<12 - 1; i++) {
         buffer[i] = fWeightMatrix0to1[o][i] * inputValues[i];
      } // loop over i
      buffer.back() = fWeightMatrix0to1[o][11];
      for (int i=0; i<12; i++) {
         fWeights1[o] += buffer[i];
      } // loop over i
    } // loop over o
   for (int o=0; o<11; o++) {
      fWeights1[o] = ActivationFnc(fWeights1[o]);
   } // loop over o
   // layer 1 to 2
   for (int o=0; o<11; o++) {
      std::array<double, 12> buffer; // no need to initialise
      for (int i=0; i<12; i++) {
         buffer[i] = fWeightMatrix1to2[o][i] * fWeights1[i];
      } // loop over i
      for (int i=0; i<12; i++) {
         fWeights2[o] += buffer[i];
      } // loop over i
    } // loop over o
   for (int o=0; o<11; o++) {
      fWeights2[o] = ActivationFnc(fWeights2[o]);
   } // loop over o
   // layer 2 to 3
   for (int o=0; o<1; o++) {
      std::array<double, 12> buffer; // no need to initialise
      for (int i=0; i<12; i++) {
         buffer[i] = fWeightMatrix2to3[o][i] * fWeights2[i];
      } // loop over i
      for (int i=0; i<12; i++) {
         fWeights3[o] += buffer[i];
      } // loop over i
    } // loop over o
   for (int o=0; o<1; o++) {
      fWeights3[o] = OutputActivationFnc(fWeights3[o]);
   } // loop over o

   return fWeights3[0];
}

double ReadMLP::ActivationFnc(double x) const {
   // sigmoid
   return 1.0/(1.0+exp(-x));
}
double ReadMLP::OutputActivationFnc(double x) const {
   // sigmoid
   return 1.0/(1.0+exp(-x));
}

// Clean up
inline void ReadMLP::Clear()
{
}
inline double ReadMLP::GetMvaValue( const std::vector<double>& inputValues ) const
{
   // classifier response value
   double retval = 0;

   // classifier response, sanity check first
   if (!IsStatusClean()) {
      std::cout << "Problem in class \"" << fClassName << "\": cannot return classifier response"
                << " because status is dirty" << std::endl;
   }
   else {
         std::vector<double> iV(inputValues);
         Transform( iV, -1 );
         retval = GetMvaValue__( iV );
   }

   return retval;
}

//_______________________________________________________________________
inline void ReadMLP::InitTransform_1()
{
   double fMin_1[3][11];
   double fMax_1[3][11];
   // Normalization transformation, initialisation
   fMin_1[0][0] = 22.7864818573;
   fMax_1[0][0] = 7505.73046875;
   fScal_1[0][0] = 2.0/(fMax_1[0][0]-fMin_1[0][0]);
   fOff_1[0][0] = fMin_1[0][0]*fScal_1[0][0]+1.;
   fMin_1[1][0] = 23.5563087463;
   fMax_1[1][0] = 7838.75537109;
   fScal_1[1][0] = 2.0/(fMax_1[1][0]-fMin_1[1][0]);
   fOff_1[1][0] = fMin_1[1][0]*fScal_1[1][0]+1.;
   fMin_1[2][0] = 22.7864818573;
   fMax_1[2][0] = 7838.75537109;
   fScal_1[2][0] = 2.0/(fMax_1[2][0]-fMin_1[2][0]);
   fOff_1[2][0] = fMin_1[2][0]*fScal_1[2][0]+1.;
   fMin_1[0][1] = 0.000150358115206;
   fMax_1[0][1] = 8.68471050262;
   fScal_1[0][1] = 2.0/(fMax_1[0][1]-fMin_1[0][1]);
   fOff_1[0][1] = fMin_1[0][1]*fScal_1[0][1]+1.;
   fMin_1[1][1] = 2.2119609639e-05;
   fMax_1[1][1] = 8.68384933472;
   fScal_1[1][1] = 2.0/(fMax_1[1][1]-fMin_1[1][1]);
   fOff_1[1][1] = fMin_1[1][1]*fScal_1[1][1]+1.;
   fMin_1[2][1] = 2.2119609639e-05;
   fMax_1[2][1] = 8.68471050262;
   fScal_1[2][1] = 2.0/(fMax_1[2][1]-fMin_1[2][1]);
   fOff_1[2][1] = fMin_1[2][1]*fScal_1[2][1]+1.;
   fMin_1[0][2] = 126.97845459;
   fMax_1[0][2] = 2277.4987793;
   fScal_1[0][2] = 2.0/(fMax_1[0][2]-fMin_1[0][2]);
   fOff_1[0][2] = fMin_1[0][2]*fScal_1[0][2]+1.;
   fMin_1[1][2] = 125.825294495;
   fMax_1[1][2] = 1926.56140137;
   fScal_1[1][2] = 2.0/(fMax_1[1][2]-fMin_1[1][2]);
   fOff_1[1][2] = fMin_1[1][2]*fScal_1[1][2]+1.;
   fMin_1[2][2] = 125.825294495;
   fMax_1[2][2] = 2277.4987793;
   fScal_1[2][2] = 2.0/(fMax_1[2][2]-fMin_1[2][2]);
   fOff_1[2][2] = fMin_1[2][2]*fScal_1[2][2]+1.;
   fMin_1[0][3] = 4.91857872476e-06;
   fMax_1[0][3] = 0.405025333166;
   fScal_1[0][3] = 2.0/(fMax_1[0][3]-fMin_1[0][3]);
   fOff_1[0][3] = fMin_1[0][3]*fScal_1[0][3]+1.;
   fMin_1[1][3] = 5.9500340285e-05;
   fMax_1[1][3] = 0.47649076581;
   fScal_1[1][3] = 2.0/(fMax_1[1][3]-fMin_1[1][3]);
   fOff_1[1][3] = fMin_1[1][3]*fScal_1[1][3]+1.;
   fMin_1[2][3] = 4.91857872476e-06;
   fMax_1[2][3] = 0.47649076581;
   fScal_1[2][3] = 2.0/(fMax_1[2][3]-fMin_1[2][3]);
   fOff_1[2][3] = fMin_1[2][3]*fScal_1[2][3]+1.;
   fMin_1[0][4] = -4.50663423538;
   fMax_1[0][4] = 4.51134681702;
   fScal_1[0][4] = 2.0/(fMax_1[0][4]-fMin_1[0][4]);
   fOff_1[0][4] = fMin_1[0][4]*fScal_1[0][4]+1.;
   fMin_1[1][4] = -4.5036110878;
   fMax_1[1][4] = 4.50834369659;
   fScal_1[1][4] = 2.0/(fMax_1[1][4]-fMin_1[1][4]);
   fOff_1[1][4] = fMin_1[1][4]*fScal_1[1][4]+1.;
   fMin_1[2][4] = -4.50663423538;
   fMax_1[2][4] = 4.51134681702;
   fScal_1[2][4] = 2.0/(fMax_1[2][4]-fMin_1[2][4]);
   fOff_1[2][4] = fMin_1[2][4]*fScal_1[2][4]+1.;
   fMin_1[0][5] = 50.1059684753;
   fMax_1[0][5] = 1964.14489746;
   fScal_1[0][5] = 2.0/(fMax_1[0][5]-fMin_1[0][5]);
   fOff_1[0][5] = fMin_1[0][5]*fScal_1[0][5]+1.;
   fMin_1[1][5] = 50.0584754944;
   fMax_1[1][5] = 2753.2824707;
   fScal_1[1][5] = 2.0/(fMax_1[1][5]-fMin_1[1][5]);
   fOff_1[1][5] = fMin_1[1][5]*fScal_1[1][5]+1.;
   fMin_1[2][5] = 50.0584754944;
   fMax_1[2][5] = 2753.2824707;
   fScal_1[2][5] = 2.0/(fMax_1[2][5]-fMin_1[2][5]);
   fOff_1[2][5] = fMin_1[2][5]*fScal_1[2][5]+1.;
   fMin_1[0][6] = -2.4010925293;
   fMax_1[0][6] = 2.39041256905;
   fScal_1[0][6] = 2.0/(fMax_1[0][6]-fMin_1[0][6]);
   fOff_1[0][6] = fMin_1[0][6]*fScal_1[0][6]+1.;
   fMin_1[1][6] = -2.38632035255;
   fMax_1[1][6] = 2.38307738304;
   fScal_1[1][6] = 2.0/(fMax_1[1][6]-fMin_1[1][6]);
   fOff_1[1][6] = fMin_1[1][6]*fScal_1[1][6]+1.;
   fMin_1[2][6] = -2.4010925293;
   fMax_1[2][6] = 2.39041256905;
   fScal_1[2][6] = 2.0/(fMax_1[2][6]-fMin_1[2][6]);
   fOff_1[2][6] = fMin_1[2][6]*fScal_1[2][6]+1.;
   fMin_1[0][7] = 0.0488347522914;
   fMax_1[0][7] = 0.99988257885;
   fScal_1[0][7] = 2.0/(fMax_1[0][7]-fMin_1[0][7]);
   fOff_1[0][7] = fMin_1[0][7]*fScal_1[0][7]+1.;
   fMin_1[1][7] = 0.0229892414063;
   fMax_1[1][7] = 0.999983787537;
   fScal_1[1][7] = 2.0/(fMax_1[1][7]-fMin_1[1][7]);
   fOff_1[1][7] = fMin_1[1][7]*fScal_1[1][7]+1.;
   fMin_1[2][7] = 0.0229892414063;
   fMax_1[2][7] = 0.999983787537;
   fScal_1[2][7] = 2.0/(fMax_1[2][7]-fMin_1[2][7]);
   fOff_1[2][7] = fMin_1[2][7]*fScal_1[2][7]+1.;
   fMin_1[0][8] = 2;
   fMax_1[0][8] = 8;
   fScal_1[0][8] = 2.0/(fMax_1[0][8]-fMin_1[0][8]);
   fOff_1[0][8] = fMin_1[0][8]*fScal_1[0][8]+1.;
   fMin_1[1][8] = 2;
   fMax_1[1][8] = 9;
   fScal_1[1][8] = 2.0/(fMax_1[1][8]-fMin_1[1][8]);
   fOff_1[1][8] = fMin_1[1][8]*fScal_1[1][8]+1.;
   fMin_1[2][8] = 2;
   fMax_1[2][8] = 9;
   fScal_1[2][8] = 2.0/(fMax_1[2][8]-fMin_1[2][8]);
   fOff_1[2][8] = fMin_1[2][8]*fScal_1[2][8]+1.;
   fMin_1[0][9] = 1.5914440155e-05;
   fMax_1[0][9] = 1;
   fScal_1[0][9] = 2.0/(fMax_1[0][9]-fMin_1[0][9]);
   fOff_1[0][9] = fMin_1[0][9]*fScal_1[0][9]+1.;
   fMin_1[1][9] = 1.93119049072e-05;
   fMax_1[1][9] = 1;
   fScal_1[1][9] = 2.0/(fMax_1[1][9]-fMin_1[1][9]);
   fOff_1[1][9] = fMin_1[1][9]*fScal_1[1][9]+1.;
   fMin_1[2][9] = 1.5914440155e-05;
   fMax_1[2][9] = 1;
   fScal_1[2][9] = 2.0/(fMax_1[2][9]-fMin_1[2][9]);
   fOff_1[2][9] = fMin_1[2][9]*fScal_1[2][9]+1.;
   fMin_1[0][10] = 3.26525550918e-05;
   fMax_1[0][10] = 6.50682735443;
   fScal_1[0][10] = 2.0/(fMax_1[0][10]-fMin_1[0][10]);
   fOff_1[0][10] = fMin_1[0][10]*fScal_1[0][10]+1.;
   fMin_1[1][10] = 1.18112052405e-06;
   fMax_1[1][10] = 6.68952894211;
   fScal_1[1][10] = 2.0/(fMax_1[1][10]-fMin_1[1][10]);
   fOff_1[1][10] = fMin_1[1][10]*fScal_1[1][10]+1.;
   fMin_1[2][10] = 1.18112052405e-06;
   fMax_1[2][10] = 6.68952894211;
   fScal_1[2][10] = 2.0/(fMax_1[2][10]-fMin_1[2][10]);
   fOff_1[2][10] = fMin_1[2][10]*fScal_1[2][10]+1.;
}

//_______________________________________________________________________
inline void ReadMLP::Transform_1( std::vector<double>& iv, int cls) const
{
   // Normalization transformation
   if (cls < 0 || cls > 2) {
   if (2 > 1 ) cls = 2;
      else cls = 2;
   }
   const int nVar = 11;

   // get indices of used variables

   // define the indices of the variables which are transformed by this transformation
   static std::vector<int> indicesGet;
   static std::vector<int> indicesPut;

   if ( indicesGet.empty() ) {
      indicesGet.reserve(fNvars);
      indicesGet.push_back( 0);
      indicesGet.push_back( 1);
      indicesGet.push_back( 2);
      indicesGet.push_back( 3);
      indicesGet.push_back( 4);
      indicesGet.push_back( 5);
      indicesGet.push_back( 6);
      indicesGet.push_back( 7);
      indicesGet.push_back( 8);
      indicesGet.push_back( 9);
      indicesGet.push_back( 10);
   }
   if ( indicesPut.empty() ) {
      indicesPut.reserve(fNvars);
      indicesPut.push_back( 0);
      indicesPut.push_back( 1);
      indicesPut.push_back( 2);
      indicesPut.push_back( 3);
      indicesPut.push_back( 4);
      indicesPut.push_back( 5);
      indicesPut.push_back( 6);
      indicesPut.push_back( 7);
      indicesPut.push_back( 8);
      indicesPut.push_back( 9);
      indicesPut.push_back( 10);
   }

   static std::vector<double> dv;
   dv.resize(nVar);
   for (int ivar=0; ivar<nVar; ivar++) dv[ivar] = iv[indicesGet.at(ivar)];
   for (int ivar=0;ivar<11;ivar++) {
      double offset = fOff_1[cls][ivar];
      double scale  = fScal_1[cls][ivar];
      iv[indicesPut.at(ivar)] = scale*dv[ivar]-offset;
   }
}

//_______________________________________________________________________
inline void ReadMLP::InitTransform()
{
   InitTransform_1();
}

//_______________________________________________________________________
inline void ReadMLP::Transform( std::vector<double>& iv, int sigOrBgd ) const
{
   Transform_1( iv, sigOrBgd );
}
