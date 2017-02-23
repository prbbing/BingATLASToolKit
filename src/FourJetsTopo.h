#ifndef analysis_FourJetsTopo_h
#define analysis_FourJetsTopo_h

#include "SampleAnalyzer/Process/Analyzer/AnalyzerBase.h"

namespace MA5
{
class FourJetsTopo : public AnalyzerBase
{
  INIT_ANALYSIS(FourJetsTopo,"FourJetsTopo")

 public:
  virtual bool Initialize(const MA5::Configuration& cfg, const std::map<std::string,std::string>& parameters);
  virtual void Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files);
  virtual bool Execute(SampleFormat& sample, const EventFormat& event);
  bool genMatch(const MCParticleFormat* prt); 
 private:
};
}

#endif
