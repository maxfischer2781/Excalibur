#  -*- coding: utf-8 -*-

"""
	Derived from base in HarryPlotter
"""

import Artus.HarryPlotter.utility.labels as labels

class LabelsDictZJet(labels.LabelsDict):
	def __init__(self, additional_labels=None):
		super(LabelsDictZJet, self).__init__(additional_labels)
		
		self.labels_dict.update({
			#more general stuff. maybe move to Artus?
			'abs(jet1eta)': '|$\mathit{\eta}_{Leading \ Jet}$|',
			'abs(genzy)': '|$\mathit{y}_{Z, Gen}$|',
			'abs(geneminuseta)': '|$\mathit{\eta}_{e^{-}, Gen}$|',
			'abs(zy)': '|$\mathit{y}_Z$|',
			'algoflavour': 'Flavour (Algorithmic Definition)',
			'au': 'arb. units',
			'constituents': 'Number of Jet Constituents',
			'deltaphizeminus': '$\Delta\phi(\mathrm{Z},\mathrm{e^{-}})$',
			'deltaphizeplus': '$\Delta\phi(\mathrm{Z},\mathrm{e^{+}})$',
			'deltaphieminuseplus': '$\Delta\phi(\mathrm{e^{-}},\mathrm{e^{+}})$',
			'deltaphizmuminus': '$\Delta\phi(\mathrm{Z},\mathrm{\mu^{-}})$',
			'deltaphizmuplus': '$\Delta\phi(\mathrm{Z},\mathrm{\mu^{+}})$',
			'e1pt': '$\mathit{p}_{T}^{Leading\ Electron}$ / GeV',
			'e1abseta': '|$\mathit{\eta}_{Leading\ Electron}$|',
			'eabseta': '|$\mathit{\eta}_{Electron}$|',
			'eminuseta': '$\mathit{\eta}_{e^{-}}$',
			'eminuspt': '$\mathit{p}_{T}^{e^{-}}$ / GeV',
			'epluspt': '$\mathit{p}_{T}^{e^{+}}$ / GeV',
			'ept': '$\mathit{p}_{T}^{Electron}$ / GeV',
			'erecogen': 'Electron $\mathit{p}_T^{Reco}/\mathit{p}_T^{Gen}$',
			'eventsperbin': 'Events per Bin',
			'genabs(zy)': '$\mathit{|y|}_{Z, Gen}$',
			'geneminuseta': '$\mathit{\eta}_{e^{-}, Gen}$',
			'geneminuspt': '$\mathit{p}_{T}^{e^{-}, Gen}$ / GeV',
			'geneminusphi': r'$\mathit{\phi}_{e^{-}, Gen}$',
			'geneminusmass': '$\mathit{m}_{e^{-}, Gen}$ / GeV',
			'genjet1pt': '$\mathit{p}_{T}^{Leading Jet, Gen}$ / GeV',
			'genjet2pt': '$\mathit{p}_{T}^{Jet2, Gen}$ / GeV',
			'genzmass': '$\mathit{m}_{Z, Gen}$ / GeV',
			'genzpt': '$\mathit{p}_{T}^{Z, Gen}$ / GeV',
			'genzy': '$\mathit{y}_{Z, Gen}$',
			'genzphi': r'$\mathit{\phi}_{Z, Gen}$',
			'jet1abseta': '|$\mathit{\eta}_{Leading \ Jet}$|',
			'jet1area': 'Leading Jet Area',
			'jet1eta': '$\mathit{\eta}_{Leading \ Jet}$',
			'jet1phi': r'$\mathit{\phi}_{Leading \ Jet}$',
			'jet1pt': '$\mathit{p}_{T}^{Leading Jet}$ / GeV',
			'jet1btag': 'CSV b-Tag',
			'jet1qgtag': 'QG Likelihood',
			'jeteta': '$\mathit{\eta}_{Jet}$',
			'jetpt': '$\mathit{p}_{T}^{Jet}$ / GeV',
			'(jet1nhf*jet1pt)': 'Jet Neutral Hadron Energy / GeV',
			'(jet1chf*jet1pt)': 'Jet Charged Hadron Energy / GeV',
			'(jet1mf*jet1pt)': 'Jet Muon Energy / GeV',
			'(jet1pf*jet1pt)': 'Jet Photon Energy / GeV',
			'jet2eta': '$\mathit{\eta}^{Jet2}$',
			'jet2pt': '$\mathit{p}_{T}^{Jet2}$ / GeV',
			'jet2phi': r'$\mathit{\phi}^{Second \ Jet}$',
			'jetsvalid': 'Number of Valid Jets $n$',
			'matchedgenjet1pt': '$\mathit{p}_T^{Matched Gen Jet}$',
			'meteta': '$\mathit{\eta}^{MET}$',
			'metphi': r'$\mathit{\phi}^{MET}$',
			'met': '$\mathit{E}_{T}^{Miss}$ / GeV',
			'muphi': '$\mathit{\phi}^{\mu}$',
			'mueta': '$\mathit{\eta}^{\mu}$',
			'mu1pt': '$\mathit{p}_{T}^{\mu1}$ / GeV',
			'mu1eta': '$\mathit{\eta}^{\mu1}$',
			'mu1phi': '$\mathit{\phi}^{\mu1}$',
			'mu2pt': '$\mathit{p}_{T}^{\mu2}$ / GeV',
			'mu2eta': '$\mathit{\eta}^{\mu2}$',
			'mu2phi': '$\mathit{\phi}^{\mu2}$',
			'muminuseta': '$\mathit{\eta}^{\mu-}$',
			'muminusphi': '$\mathit{\phi}^{\mu-}$',
			'muminuspt': '$\mathit{p}_{T}^{\mu-}$ / GeV',
			'mupluseta': '$\mathit{\eta}^{\mu+}$',
			'muplusphi': '$\mathit{\phi}^{\mu+}$',
			'mupluspt': '$\mathit{p}_{T}^{\mu+}$ / GeV',
			'njets': 'Number of Valid Jets per Event',
			'njets30': '$\mathit{n}_{Jets, \mathit{p}_T>30 GeV}$',
			'npu': '$\mathit{n}_{PU}$',
			'npumean': r'$\langle\mathit{n}_{PU}\rangle$',
			'npv': '$\mathit{n}_{PV}$',
			'pdf': "$\mathit{x}f(\mathit{x}, \mathit{Q})$",
			'physflavour': 'Flavour (Physics Definition)',
			'rawmetphi': r'raw $\mathit{\phi}^{MET}$',
			'rawmet': '$raw \mathit{E}_{T}^{Miss}$ / GeV',
			'rho': r'$\mathit{\rho}$',
			'recoabs(zy)': '$\mathit{|y|}_{Z, Reco}$',
			'recozmass': '$\mathit{m}_{Z, Reco}$ / GeV',
			'recozpt': '$\mathit{p}_{T}^{Z, Reco}$ / GeV',
			'recozy': '$\mathit{y}_{Z, Reco}$',
			'recozphi': r'$\mathit{\phi}_{Z, Reco}$',
			'run': 'Run',
			'runtime': r'Processor Runtime / $\mu s$',
			'sumet': '$\sum E_{T}$',
			'xsec': '$\mathit{\sigma}$ / pb',
			'xsecabsy': 'd$\mathit{\sigma}$/d|$\mathit{y}$| / pb',
			'xseceta': 'd$\mathit{\sigma}$/d$\mathit{\eta}$ / pb',
			'xsecm': 'd$\mathit{\sigma}$/d$\mathit{m}$ / pb $GeV^{-1}$',
			'xsecphi': 'd$\mathit{\sigma}$/d$\mathit{\phi}$ / pb',
			'xsecpt': 'd$\mathit{\sigma}$/d$\mathit{p_\mathrm{T}}$ / pb $GeV^{-1}$',
			'zmass': '$\mathit{m}_{Z}$ / GeV',
			'zphi': r'$\mathit{\phi}^{Z}$',
			'zpt': '$\mathit{p}_{T}^{Z}$ / GeV',
			'zpt/genzpt': '$\mathit{p}_{T}^{Z, Reco}$ / $\mathit{p}_{T}^{Z, Gen}$',
			'zy': '$\mathit{y}_Z$',

			# ZJet specific
			'alpha': '$\mathit{p}_{T}^{Jet 2}/\mathit{p}_{T}^{Z}$',
			'extrapol': 'Response',
			'genalpha': '$\mathit{p}_{T}^{GenJet 2}/\mathit{p}_{T}^{Z, Gen}$',
			'genmpf': '$MPF$ Response (Gen level)',
			'(jet1pt/zpt)': r'$\mathit{p}_T$ balance',
			'mpf': '$MPF$ Response',
			'ptbalance': r'$\mathit{p}_T$ Balance',
			'trueresponse': r'$p_T^\mathrm{reco}$/$p_T^\mathrm{ptcl}$',
			'recogen': 'Jet Response $\mathit{p}_T^{RecoJet}/\mathit{p}_T^{GenJet}$',
			'sys': 'Relative Uncertainty [$\%$]',
			'sortedflavour': 'Leading Jet Flavour',
			'sortedabsflavour': 'Leading Jet Flavour',
			'tagflavour': 'Flavour (from Tagging)',
			'unc': 'Leading Jet Uncertainty',
			'deltaetajet1jet2': '$\Delta\eta(\mathrm{Jet1},\mathrm{Jet2})$',
			'deltaphijet1jet2': '$\Delta\phi(\mathrm{Jet1},\mathrm{Jet2})$',
			'deltarjet1jet2': '$\Delta R(\mathrm{Jet1},\mathrm{Jet2})$',
		})
		if additional_labels != None:
			self.labels_dict.update(additional_labels)
