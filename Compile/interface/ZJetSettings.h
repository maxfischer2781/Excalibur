#pragma once

#include "Artus/KappaAnalysis/interface/KappaSettings.h"

class ZJetSettings : public KappaSettings
{
  public:
    // ValidZllJetsProducer
    IMPL_SETTING(float, MinZllJetDeltaRVeto)
    IMPL_SETTING(std::string, PUJetID)
    IMPL_SETTING(float, MinPUJetID)
    IMPL_SETTING(bool, UseObjectJetYCut)

    // TypeIMETProducer
    IMPL_SETTING(float, TypeIJetPtMin)
    IMPL_SETTING_DEFAULT(bool, EnableMetPhiCorrection, false)
    IMPL_SETTING_DOUBLELIST(MetPhiCorrectionParameters)
    // Type-I MET modification (recommended jun. 2018 for 2017 JECs)
    IMPL_SETTING_DEFAULT(bool, EnableTypeIModification, false)
    IMPL_SETTING_DEFAULT(float, TypeIModExcludeJetPtMax, 0.0)
    IMPL_SETTING_DEFAULT(float, TypeIModExcludeJetAbsEtaMin, 0.0)
    IMPL_SETTING_DEFAULT(float, TypeIModExcludeJetAbsEtaMax, 0.0)

    // JetRecoilProducer
    IMPL_SETTING(float, JetRecoilMinPtThreshold)

    // ZJetCorrectionsProducer
    IMPL_SETTING_DEFAULT(std::string, CorrectionLevel, "None")
    IMPL_SETTING(std::string, Jec)
    IMPL_SETTING(std::string, L1Correction)
    IMPL_SETTING(bool, RC)
    IMPL_SETTING(bool, FlavourCorrections)
    IMPL_SETTING_DEFAULT(bool, ProvideL2ResidualCorrections, false)
    IMPL_SETTING_DEFAULT(bool, ProvideL2L3ResidualCorrections, false)
    IMPL_SETTING_DEFAULT(bool, ProvideJECUncertainties, false)

    // JERSmearer
    IMPL_SETTING(std::string, JER)
    IMPL_SETTING(std::string, JERMethod)
    IMPL_SETTING(int, JERSmearerSeed)

    // RecoJetGenJetMatchingProducer
    IMPL_SETTING_DEFAULT(double, DeltaRMatchingRecoJetGenJet, 0.25)

    // ZJetNumberGeneratedEventsWeightProducer (sample reweighting)
    IMPL_SETTING_DEFAULT(bool, SampleReweighting, false)
    IMPL_SETTING_DOUBLELIST(SampleReweightingCrossSections)
    IMPL_SETTING_INTLIST(SampleReweightingNEvents)

    // NPUProducer (insert npu from external file)
    IMPL_SETTING(std::string, NPUFile)  // pileup JSON reformatted as csv
    IMPL_SETTING_DEFAULT(bool, NPUSmearing, false) // NPUmean should be smeared
    IMPL_SETTING_DEFAULT(int,  NPUSmearingSeed, 1) // set smearing seed
    IMPL_SETTING(float, Minbxsec)       // MinBias Cross Section in mb

    // ZJetValidElectronsProducer
    IMPL_SETTING_DEFAULT(bool, ExcludeECALGap, false)
    IMPL_SETTING_DEFAULT(bool, ApplyElectronVID, false)  // whether to apply electron VID
    IMPL_SETTING_DEFAULT(std::string, ElectronVIDName, "")  // name of VID (e.g. "Summer16-80X-V1")
    IMPL_SETTING_DEFAULT(std::string, ElectronVIDType, "")  // type of VID (e.g. 'cutbased')
    IMPL_SETTING_DEFAULT(std::string, ElectronVIDWorkingPoint, "")  // e.g. 'tight'

    // ZJetCutsFilter
    IMPL_SETTING(unsigned, CutNLeptonsMin)
    IMPL_SETTING(unsigned, CutNLeptonsMax)
    IMPL_SETTING(float, CutLeadingLeptonPtMin)
    IMPL_SETTING(unsigned, CutNMuonsMin)
    IMPL_SETTING(unsigned, CutNMuonsMax)
    IMPL_SETTING(float, CutMuonPtMin)
    IMPL_SETTING(float, CutMuonEtaMax)
    IMPL_SETTING(float, CutElectronPtMin)
    IMPL_SETTING(float, CutElectronEtaMax)
    IMPL_SETTING(float, CutLeadingJetPtMin)
    IMPL_SETTING(float, CutLeadingJetEtaMax)
    IMPL_SETTING(float, CutLeadingJetYMax)
    IMPL_SETTING(float, CutZPtMin)
    IMPL_SETTING(float, CutPhistaretaMin)
    IMPL_SETTING(float, CutBackToBack)
    IMPL_SETTING(float, CutAlphaMax)
    IMPL_SETTING(float, CutEtaPhiCleaningPt)
    IMPL_SETTING(float, CutGenHTMax)
    IMPL_SETTING(float, GenZMassRange)
    IMPL_SETTING(std::string, CutEtaPhiCleaningFile)
    IMPL_SETTING(std::string, CutJetID)
    IMPL_SETTING(std::string, CutJetIDVersion)
    IMPL_SETTING(unsigned, CutJetIDFirstNJets)

    // LeptonSFProducer
    IMPL_SETTING(std::string, LeptonIDSFRootfile)
    IMPL_SETTING(std::string, LeptonIsoSFRootfile)
    IMPL_SETTING(std::string, LeptonTrackingSFRootfile)
    IMPL_SETTING(std::string, LeptonTriggerSFRootfile)
    IMPL_SETTING(std::string, LeptonIDSFHistogramName)
    IMPL_SETTING(std::string, LeptonIsoSFHistogramName)
    IMPL_SETTING(std::string, LeptonTrackingSFHistogramName)
    IMPL_SETTING(std::string, LeptonTriggerSFHistogramName)
    IMPL_SETTING_DEFAULT(bool, LeptonSFVariation, false)
    IMPL_SETTING_DEFAULT(std::string, Channel, "mm")
   
    // ZJetDressedMuonsProducer
    IMPL_SETTING(float, MaxZJetDressedMuonDeltaR)
    //GenZProducers
    //IMPL_SETTING_DEFAULT(float, GenZMassRange, 20.0)

    // JetEtaPhiCleaner
    IMPL_SETTING(std::string, JetEtaPhiCleanerFile)
    IMPL_SETTING_STRINGLIST(JetEtaPhiCleanerHistogramNames)
    IMPL_SETTING(double, JetEtaPhiCleanerHistogramValueMaxValid)
};
