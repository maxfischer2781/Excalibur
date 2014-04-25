#pragma once

#include "Artus/Core/interface/Cpp11Support.h"

#include "../ZJetTypes.h"

class ValidGenZFilter: public ZJetFilterBase {
public:

	virtual std::string GetFilterId() const ARTUS_CPP11_OVERRIDE {
		return "validgenz";
	}

	virtual bool DoesEventPassLocal(ZJetEvent const& event,
	ZJetProduct const& product,
	ZJetPipelineSettings const& settings) const ARTUS_CPP11_OVERRIDE
	{
		return DoesEventPass(event, product);
	}

	bool DoesEventPassGlobal(ZJetEvent const& event,
			ZJetProduct const& product, ZJetGlobalSettings const& global_settings) const
	{
		return DoesEventPass(event, product);
	}

private:

	virtual bool DoesEventPass(ZJetEvent const& event,
		ZJetProduct const& product) const
	{
		if (product.has_valid_genz)
			return true;
		else
			return false;
	}
};

