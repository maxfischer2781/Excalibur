import configtools


def modify_config(cfg):
	"""
	Use 2015D data only
	"""
	cfg['JsonFiles'].add_run_range(253888, 256629)
	if cfg['InputIsData']:
		cfg["InputFiles"] = configtools.setInputFiles(
			ekppath="/storage/a/mfischer/skims/zjet/2015-10-09/DoubleMu_Run2015C_Jul2015_13TeV/*.root",
			nafpath="/pnfs/desy.de/cms/tier2/store/user/mafische/skims/MF_AnyMu_2015_746/2015-10-09/DoubleMu_Run2015C_Jul2015_13TeV/*.root",
		)
		cfg['Lumi'] = configtools.get_lumi(json_source=cfg['JsonFiles'])
	else:
		cfg['PileupWeightFile'] = configtools.get_puweights(cfg['JsonFiles'], cfg['InputFiles'], min_bias_xsec=69.0, weight_limits=(0, 4))
	return cfg
