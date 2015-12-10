import configtools
import mc12_ee

def config():
	cfg = mc12_ee.config()
	cfg["InputFiles"] = configtools.setInputFiles(
		ekppath="/storage/a/dhaitz/skims/2015-07-28_ee-backgrounds_Run2012/kappa_ZZ*.root",
		nafpath="/pnfs/desy.de/cms/tier2/store/user/dhaitz/2015-07-28_ee-backgrounds_Run2012/kappa_ZZ*.root",
	)
	cfg['CrossSection'] = 17.654 
	cfg['NumberGeneratedEvents'] = 9799908
	return cfg
