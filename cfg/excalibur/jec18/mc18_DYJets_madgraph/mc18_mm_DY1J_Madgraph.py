import configtools
import os
import sys

# -- import common information
sys.path.append(os.path.dirname(__file__))
from common import JEC_BASE, JEC_VERSION, JER, SE_PATH_PREFIXES

CH='mm'
JEC='{}_{}'.format(JEC_BASE, JEC_VERSION)


def config():
    cfg = configtools.getConfig('mc', 2018, CH, JEC=JEC, JER=JER)
    cfg["InputFiles"].set_input(
        path1="{}/dsavoiu/Skimming/ZJet_DY1JetsToLL_Autumn18-madgraphMLM_realistic_v15-v2/*.root".format(SE_PATH_PREFIXES['xrootd_gridka_nrg']),
    )

    cfg = configtools.expand(cfg, ['basiccuts', 'finalcuts'], ['None', 'L1', 'L1L2L3'])

    cfg['PileupWeightFile'] = os.path.join(configtools.getPath() , 'data/pileup/mc_weights/mc18_DYJets_madgraph/PUWeights_ABCD_17Sep2018_DY1JetsToLL_Autumn18-madgraphMLM_realistic_v15-v2.root')

    cfg['NumberGeneratedEvents'] = 68898175
    cfg['GeneratorWeight'] = 1.0
    cfg['CrossSection'] = 877.8  # from XSDB

    cfg['VertexSummary'] = 'goodOfflinePrimaryVerticesSummary'

    # for testing JetID differences
    cfg['JetIDVersion'] = 2017  # for object-based JetID
    cfg['CutJetIDVersion'] = 2017  # for event-based JetID

    return cfg
