#include "SampleAnalyzer/User/Analyzer/FourJetsTopo.h"
using namespace MA5;
using namespace std;

// -----------------------------------------------------------------------------
// Initialize
// function called one time at the beginning of the analysis
// -----------------------------------------------------------------------------
bool FourJetsTopo::Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters)
{
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  INFO << "        <>  Analysis: Four Jets Phenomenology         <>" << endmsg;
  INFO << "        <>  Contact: bingxuan.liu@cern.ch             <>" << endmsg;
  INFO << "        <>  Based on MadAnalysis 5 v2.5.2             <>" << endmsg;
  INFO << "        <>  DOI: xx.yyyy/zzz                          <>" << endmsg;
  INFO << "        <>  Please cite arXiv.YYMM.NNNN               <>" << endmsg;
  INFO << "        <><><><><><><><><><><><><><><><><><><><><><><><>" << endmsg;
  // initialize variables, histo
  Manager()->AddRegionSelection("4j25");
  Manager()->AddRegionSelection("4j25, 4bj");
  //Manager()->AddRegionSelection("4j25, >=1 bjet");
  //Manager()->AddRegionSelection("4j25, >=2 bjet");
  //Manager()->AddRegionSelection("4j25, >=3 bjet");
  //Manager()->AddRegionSelection("4j25, >=4 bjet");
  // add cuts 
  std::string SR4j25Cut[] = {"4j25", "4j25, 4bj"};
  //std::string SR4j25Cut[] = {"4j25, >=0 bjet", "4j25, >=1 bjet", "4j25, >=2 bjet", "4j25, >=3 bjet", "4j25, >=4 bjet"};
  Manager()->AddCut("4 jets with pT > 25", SR4j25Cut);
  //Manager()->AddCut(">=0 bjets with pT > 25",SR4j25Cut);
  //Manager()->AddCut(">=1 bjets with pT > 25, eta < 2.5",SR4j25Cut);
  //Manager()->AddCut(">=2 bjets with pT > 25, eta < 2.5",SR4j25Cut);
  //Manager()->AddCut(">=3 bjets with pT > 25, eta < 2.5",SR4j25Cut);
  //Manager()->AddCut(">=4 bjets with pT > 25, eta < 2.5",SR4j25Cut);
  // add histograms
  Manager()->AddHisto("Deta_12 in 4j25",100,0,10.0,"4j25"); 
  Manager()->AddHisto("Dphi_12 in 4j25",32,0,3.2,"4j25"); 
  Manager()->AddHisto("Angle_12 in 4j25",32,0,3.2,"4j25"); 
  Manager()->AddHisto("Mass_12 in 4j25",150,0,1500,"4j25"); 
  Manager()->AddHisto("Deta_34 in 4j25",100,0,10.0,"4j25"); 
  Manager()->AddHisto("Dphi_34 in 4j25",32,0,3.2,"4j25"); 
  Manager()->AddHisto("Angle_34 in 4j25",32,0,3.2,"4j25"); 
  Manager()->AddHisto("Mass_34 in 4j25",150,0,1500,"4j25"); 
  Manager()->AddHisto("Pt_1 in 4j25",100,0,1000,"4j25"); 
  Manager()->AddHisto("Pt_2 in 4j25",100,0,1000,"4j25"); 
  Manager()->AddHisto("Pt_3 in 4j25",100,0,1000,"4j25"); 
  Manager()->AddHisto("Pt_4 in 4j25",100,0,1000,"4j25"); 
  Manager()->AddHisto("Eta_1 in 4j25",100,-5,5,"4j25"); 
  Manager()->AddHisto("Eta_2 in 4j25",100,-5,5,"4j25"); 
  Manager()->AddHisto("Eta_3 in 4j25",100,-5,5,"4j25"); 
  Manager()->AddHisto("Eta_4 in 4j25",100,-5,5,"4j25"); 
  Manager()->AddHisto("Phi_1 in 4j25",64,-3.2,3.2,"4j25"); 
  Manager()->AddHisto("Phi_2 in 4j25",64,-3.2,3.2,"4j25"); 
  Manager()->AddHisto("Phi_3 in 4j25",64,-3.2,3.2,"4j25"); 
  Manager()->AddHisto("Phi_4 in 4j25",64,-3.2,3.2,"4j25"); 
  Manager()->AddHisto("pTRel in 4j25",100,0,1000,"4j25"); 
  Manager()->AddCut("4bj", SR4j25Cut);
  Manager()->AddHisto("Deta_12 in 4j25, 4bj",100,0,10.0,"4j25, 4bj"); 
  Manager()->AddHisto("Dphi_12 in 4j25, 4bj",32,0,3.2,"4j25, 4bj"); 
  Manager()->AddHisto("Angle_12 in 4j25, 4bj",32,0,3.2,"4j25, 4bj"); 
  Manager()->AddHisto("Mass_12 in 4j25, 4bj",150,0,1500,"4j25, 4bj"); 
  Manager()->AddHisto("Deta_34 in 4j25, 4bj",100,0,10.0,"4j25, 4bj"); 
  Manager()->AddHisto("Dphi_34 in 4j25, 4bj",32,0,3.2,"4j25, 4bj"); 
  Manager()->AddHisto("Angle_34 in 4j25, 4bj",32,0,3.2,"4j25, 4bj"); 
  Manager()->AddHisto("Mass_34 in 4j25, 4bj",150,0,1500,"4j25, 4bj"); 
  Manager()->AddHisto("Pt_1 in 4j25, 4bj",100,0,1000,"4j25, 4bj"); 
  Manager()->AddHisto("Pt_2 in 4j25, 4bj",100,0,1000,"4j25, 4bj"); 
  Manager()->AddHisto("Pt_3 in 4j25, 4bj",100,0,1000,"4j25, 4bj"); 
  Manager()->AddHisto("Pt_4 in 4j25, 4bj",100,0,1000,"4j25, 4bj"); 
  Manager()->AddHisto("Eta_1 in 4j25, 4bj",100,-5,5,"4j25, 4bj"); 
  Manager()->AddHisto("Eta_2 in 4j25, 4bj",100,-5,5,"4j25, 4bj"); 
  Manager()->AddHisto("Eta_3 in 4j25, 4bj",100,-5,5,"4j25, 4bj"); 
  Manager()->AddHisto("Eta_4 in 4j25, 4bj",100,-5,5,"4j25, 4bj"); 
  Manager()->AddHisto("Phi_1 in 4j25, 4bj",64,-3.2,3.2,"4j25, 4bj"); 
  Manager()->AddHisto("Phi_2 in 4j25, 4bj",64,-3.2,3.2,"4j25, 4bj"); 
  Manager()->AddHisto("Phi_3 in 4j25, 4bj",64,-3.2,3.2,"4j25, 4bj"); 
  Manager()->AddHisto("Phi_4 in 4j25, 4bj",64,-3.2,3.2,"4j25, 4bj"); 
  Manager()->AddHisto("pTRel in 4j25, 4bj",100,0,1000,"4j25, 4bj"); 
  return true;
}

// -----------------------------------------------------------------------------
// Finalize
// function called one time at the end of the analysis
// -----------------------------------------------------------------------------
void FourJetsTopo::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
  
}

// -----------------------------------------------------------------------------
// Execute
// function called each time one event is read
// -----------------------------------------------------------------------------
bool FourJetsTopo::Execute(SampleFormat& sample, const EventFormat& event)
{
  if (event.rec()!=0 && event.mc()!=0)
  {
    double myEventWeight;
    if(Configuration().IsNoEventWeight()) myEventWeight=1.;
    else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
    else
    {
      WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
      return false;
    }
    Manager()->InitializeForNewEvent(myEventWeight);
    std::vector<const RecJetFormat*> Jets, BJets, BFlavorJets;
    if (event.rec()->jets().size() < 4) return true;
    for (unsigned int i = 0; i < 4; i++) {
      const RecJetFormat& jet = event.rec()->jets()[i]; 
      if (jet.pt() >= 25 && fabs(jet.eta()) < 2.5) {
        Jets.push_back(&jet);
        if (jet.btag()) BJets.push_back(&jet);
      }
    }
    if (Jets.size() < 4) return true;
    std::vector<const MCParticleFormat*> BHadrons;
    for(unsigned int i=0; i<event.mc()->particles().size(); i++) {
      const MCParticleFormat* prt = &event.mc()->particles()[i];
      if(fabs(prt->pdgid()) >= 500 && fabs(prt->pdgid()) <= 600 && fabs(prt->eta()) < 2.5) {
        if (fabs(prt->statuscode()) != 91) BHadrons.push_back(prt);
      }
    }
    SORTER->sort(Jets, PTordering);
    SORTER->sort(BJets, PTordering);
    double pt_1 = Jets[0]->momentum().Pt();
    double pt_2 = Jets[1]->momentum().Pt();
    double pt_3 = Jets[2]->momentum().Pt();
    double pt_4 = Jets[3]->momentum().Pt();
    double eta_1 = Jets[0]->momentum().Eta();
    double eta_2 = Jets[1]->momentum().Eta();
    double eta_3 = Jets[2]->momentum().Eta();
    double eta_4 = Jets[3]->momentum().Eta();
    double phi_1 = Jets[0]->momentum().Phi();
    double phi_2 = Jets[1]->momentum().Phi();
    double phi_3 = Jets[2]->momentum().Phi();
    double phi_4 = Jets[3]->momentum().Phi();
    double dphi_12 = fabs(Jets[0]->momentum().Phi() - Jets[1]->momentum().Phi());
    if (dphi_12 > M_PI) dphi_12 = 2*M_PI - dphi_12;
    double dphi_34 = fabs(Jets[2]->momentum().Phi() - Jets[3]->momentum().Phi());
    if (dphi_34 > M_PI) dphi_34 = 2*M_PI - dphi_34;
    double mass_12 = (Jets[0]->momentum() + Jets[1]->momentum()).M();
    double mass_34 = (Jets[2]->momentum() + Jets[3]->momentum()).M();
    double deta_12 = fabs(Jets[0]->momentum().Eta() - Jets[1]->momentum().Eta());
    double deta_34 = fabs(Jets[2]->momentum().Eta() - Jets[3]->momentum().Eta());
    double angle_12 = Jets[0]->momentum().Angle(Jets[1]->momentum());
    double angle_34 = Jets[2]->momentum().Angle(Jets[3]->momentum());
    double Angle = fabs((Jets[0]->momentum() + Jets[1]->momentum()).Phi() - (Jets[2]->momentum() + Jets[3]->momentum()).Phi()); 
    if (Angle > M_PI) Angle = 2*M_PI - Angle;
    double pTRel = (Jets[0]->momentum() + Jets[1]->momentum()).Pt()*tan(Angle/2);
    //int nbj = BJets.size();
    Manager()->ApplyCut(Jets.size()>=4,"4 jets with pT > 25");
    //Manager()->ApplyCut(nbj>=0,">=0 bjets with pT > 25");
    //Manager()->ApplyCut(nbj>=1,">=1 bjets with pT > 25, eta < 2.5");
    //Manager()->ApplyCut(nbj>=2,">=2 bjets with pT > 25, eta < 2.5");
    //Manager()->ApplyCut(nbj>=3,">=3 bjets with pT > 25, eta < 2.5");
    //Manager()->ApplyCut(nbj>=4,">=4 bjets with pT > 25, eta < 2.5");
    Manager()->FillHisto("Deta_12 in 4j25",deta_12);
    Manager()->FillHisto("Dphi_12 in 4j25",dphi_12);
    Manager()->FillHisto("Angle_12 in 4j25",angle_12);
    Manager()->FillHisto("Mass_12 in 4j25",mass_12);
    Manager()->FillHisto("Deta_34 in 4j25",deta_34);
    Manager()->FillHisto("Dphi_34 in 4j25",dphi_34);
    Manager()->FillHisto("Angle_34 in 4j25",angle_34);
    Manager()->FillHisto("Mass_34 in 4j25",mass_34);
    Manager()->FillHisto("Pt_1 in 4j25",pt_1);
    Manager()->FillHisto("Pt_2 in 4j25",pt_2);
    Manager()->FillHisto("Pt_3 in 4j25",pt_3);
    Manager()->FillHisto("Pt_4 in 4j25",pt_4);
    Manager()->FillHisto("Eta_1 in 4j25",eta_1);
    Manager()->FillHisto("Eta_2 in 4j25",eta_2);
    Manager()->FillHisto("Eta_3 in 4j25",eta_3);
    Manager()->FillHisto("Eta_4 in 4j25",eta_4);
    Manager()->FillHisto("Phi_1 in 4j25",phi_1);
    Manager()->FillHisto("Phi_2 in 4j25",phi_2);
    Manager()->FillHisto("Phi_3 in 4j25",phi_3);
    Manager()->FillHisto("Phi_4 in 4j25",phi_4);
    Manager()->FillHisto("pTRel in 4j25",pTRel);
    Manager()->ApplyCut(BHadrons.size()>=4,"4bj");
    Manager()->FillHisto("Deta_12 in 4j25, 4bj",deta_12);
    Manager()->FillHisto("Dphi_12 in 4j25, 4bj",dphi_12);
    Manager()->FillHisto("Angle_12 in 4j25, 4bj",angle_12);
    Manager()->FillHisto("Mass_12 in 4j25, 4bj",mass_12);
    Manager()->FillHisto("Deta_34 in 4j25, 4bj",deta_34);
    Manager()->FillHisto("Dphi_34 in 4j25, 4bj",dphi_34);
    Manager()->FillHisto("Angle_34 in 4j25, 4bj",angle_34);
    Manager()->FillHisto("Mass_34 in 4j25, 4bj",mass_34);
    Manager()->FillHisto("Pt_1 in 4j25, 4bj",pt_1);
    Manager()->FillHisto("Pt_2 in 4j25, 4bj",pt_2);
    Manager()->FillHisto("Pt_3 in 4j25, 4bj",pt_3);
    Manager()->FillHisto("Pt_4 in 4j25, 4bj",pt_4);
    Manager()->FillHisto("Eta_1 in 4j25, 4bj",eta_1);
    Manager()->FillHisto("Eta_2 in 4j25, 4bj",eta_2);
    Manager()->FillHisto("Eta_3 in 4j25, 4bj",eta_3);
    Manager()->FillHisto("Eta_4 in 4j25, 4bj",eta_4);
    Manager()->FillHisto("Phi_1 in 4j25, 4bj",phi_1);
    Manager()->FillHisto("Phi_2 in 4j25, 4bj",phi_2);
    Manager()->FillHisto("Phi_3 in 4j25, 4bj",phi_3);
    Manager()->FillHisto("Phi_4 in 4j25, 4bj",phi_4);
    Manager()->FillHisto("pTRel in 4j25, 4bj",pTRel);
  }
  if (event.mc()!=0)
  {
    double myEventWeight;
    if(Configuration().IsNoEventWeight()) myEventWeight=1.;
    else if(event.mc()->weight()!=0.) myEventWeight=event.mc()->weight();
    else
    {
      WARNING << "Found one event with a zero weight. Skipping..." << endmsg;
      return false;
    }
    Manager()->InitializeForNewEvent(myEventWeight);
    std::vector<const MCParticleFormat*> BHadrons;
    for(unsigned int i=0; i<event.mc()->particles().size(); i++) {
      const MCParticleFormat* prt = &event.mc()->particles()[i];
      if(fabs(prt->pdgid()) >= 500 && fabs(prt->pdgid()) <= 600) {
        //if (genMatch(prt)) BHadrons.push_back(prt);
        if (fabs(prt->statuscode()) != 91) BHadrons.push_back(prt);
      }
    }
    SORTER->sort(BHadrons, PTordering);
    //if (BHadrons.size() >= 2)
    //  Beta = fabs(BHadrons[0]->momentum().Phi() - (BHadrons[0]->momentum() + BHadrons[1]->momentum()).Phi());
    //if (Beta > M_PI) Beta = 2*M_PI - Beta;
    //double Dphi = -999;
    //if (BHadrons.size() >= 2)
    //  Dphi = fabs(BHadrons[0]->momentum().Phi() - BHadrons[1]->momentum().Phi());
    //if (Dphi > M_PI) Dphi = 2*M_PI - Dphi;
    //double Angle = -999;
    //if (BHadrons.size() >= 4)
    //  Angle = (BHadrons[0]->momentum() + BHadrons[1]->momentum()).Angle(BHadrons[2]->momentum() + BHadrons[3]->momentum()); 
    //int nbj = 4;
    //Manager()->ApplyCut(nbj>=4,"4 jets with pT > 25, eta < 2.5");
    //Manager()->ApplyCut(nbj>=0,">=0 bjets with pT > 25, eta < 2.5");
    //Manager()->ApplyCut(nbj>=1,">=1 bjets with pT > 25, eta < 2.5");
    //Manager()->ApplyCut(nbj>=2,">=2 bjets with pT > 25, eta < 2.5");
    //Manager()->ApplyCut(nbj>=3,">=3 bjets with pT > 25, eta < 2.5");
    //Manager()->ApplyCut(nbj>=4,">=4 bjets with pT > 25, eta < 2.5");
    //Manager()->FillHisto("Beta in 4j25, >=0 bjet", Beta);
    //Manager()->FillHisto("Angle in 4j25, >=0 bjet", Angle);
    //Manager()->FillHisto("Dphi in 4j25, >=0 bjet", Dphi);
    //Manager()->FillHisto("Beta in 4j25, >=1 bjet", Beta);
    //Manager()->FillHisto("Beta in 4j25, >=2 bjet", Beta);
    //Manager()->FillHisto("Beta in 4j25, >=3 bjet", Beta);
    //Manager()->FillHisto("Beta in 4j25, >=4 bjet", Beta);
  }
  return true;
}

bool FourJetsTopo::genMatch(const MCParticleFormat* prt) {
  bool matched = false;
  if (prt->mother1()){
    if (fabs(prt->mother1()->pdgid()) == 5000001) matched = true;
    else {                                             
    const MCParticleFormat* mother = prt->mother1(); 
    matched = genMatch(mother);
    }
  }
  if (prt->mother2()){
    if (fabs(prt->mother2()->pdgid()) == 5000001) matched = true;
    else {                                             
    const MCParticleFormat* mother = prt->mother2(); 
    matched = genMatch(mother);
    }
  }
  return matched;
}
