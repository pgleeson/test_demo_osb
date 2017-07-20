'''
NETPYNE simulator compliant export for:

Components:
    null (Type: notes)
    CavL (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    CavN (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    HCN (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    HCNolm (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    HCNp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    HCNsomap (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KCaS (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Kdrfast (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Kdrfastngf (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Kdrp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Kdrslow (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvA (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvAdistp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvAngf (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvAolm (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvAproxp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvCaB (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    KvGroup (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Nav (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Navaxonp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Navbis (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Navcck (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Navngf (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Navp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    Navapicalp (Type: ionChannelHH:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    leak_chan (Type: ionChannelPassive:  conductance=1.0E-12 (SI conductance))
    null (Type: notes)
    Capool (Type: BezaireCaConcentrationModel:  restingConc=5.0E-5 (SI concentration) decayConstant=0.009000000000000001 (SI time) shellThickness=2.0E-7 (SI length) Faraday=96520.0 (SI charge_per_mole))
    Capoolngf (Type: BezaireCaConcentrationModel:  restingConc=5.0E-6 (SI concentration) decayConstant=0.01 (SI time) shellThickness=2.0E-7 (SI length) Faraday=96520.0 (SI charge_per_mole))
    axoaxoniccell (Type: cell)
    bistratifiedcell (Type: cell)
    cckcell (Type: cell)
    cutsuridiscell (Type: cell)
    ivycell (Type: cell)
    ngfcell (Type: cell)
    olmcell (Type: cell)
    poolosyncell (Type: cell)
    pvbasketcell (Type: cell)
    scacell (Type: cell)
    null (Type: notes)
    syn_bistratified_to_axoaxonic (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=6.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_axoaxonic (Type: expTwoSynapse:  tauRise=4.32E-4 (SI time) tauDecay=0.00449 (SI time) peakTime=0.0011190597986863605 (SI time) waveformFactor=1.4196299918241655 (dimensionless) gbase=7.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_axoaxonic (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=5.7000000000000003E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_axoaxonic (Type: expTwoSynapse:  tauRise=7.28E-4 (SI time) tauDecay=0.01 (SI time) peakTime=0.00205714908079322 (SI time) waveformFactor=1.3248521854125708 (dimensionless) gbase=1.2E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_axoaxonic (Type: expTwoSynapse:  tauRise=3.0E-4 (SI time) tauDecay=6.0E-4 (SI time) peakTime=4.158883083359671E-4 (SI time) waveformFactor=4.0 (dimensionless) gbase=4.0000000000000004E-11 (SI conductance) erev=0.0 (SI voltage))
    syn_pvbasket_to_axoaxonic (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=1.2E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_axoaxonic (Type: expTwoSynapse:  tauRise=4.19E-4 (SI time) tauDecay=0.0049900000000000005 (SI time) peakTime=0.0011331450429356179 (SI time) waveformFactor=1.3699675937330524 (dimensionless) gbase=6.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ca3_to_axoaxonic (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=1.2E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_ec_to_axoaxonic (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=1.2E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_bistratified_to_bistratified (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=5.1E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_bistratified (Type: expTwoSynapse:  tauRise=4.32E-4 (SI time) tauDecay=0.00449 (SI time) peakTime=0.0011190597986863605 (SI time) waveformFactor=1.4196299918241655 (dimensionless) gbase=7.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_bistratified (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=7.7E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_bistratified (Type: expTwoSynapse:  tauRise=6.0E-4 (SI time) tauDecay=0.015 (SI time) peakTime=0.002011797390542625 (SI time) waveformFactor=1.1911769125863754 (dimensionless) gbase=1.1000000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_bistratified (Type: expTwoSynapse:  tauRise=1.1E-4 (SI time) tauDecay=2.5E-4 (SI time) peakTime=1.6126403701371666E-4 (SI time) waveformFactor=3.4037393745369364 (dimensionless) gbase=1.9E-9 (SI conductance) erev=0.0 (SI voltage))
    syn_pvbasket_to_bistratified (Type: expTwoSynapse:  tauRise=1.7999999999999998E-4 (SI time) tauDecay=4.5000000000000004E-4 (SI time) peakTime=2.748872195622465E-4 (SI time) waveformFactor=3.0700262488669883 (dimensionless) gbase=2.9E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_bistratified (Type: expTwoSynapse:  tauRise=4.19E-4 (SI time) tauDecay=0.0049900000000000005 (SI time) peakTime=0.0011331450429356179 (SI time) waveformFactor=1.3699675937330524 (dimensionless) gbase=6.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ca3_to_bistratified (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=1.5E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_ec_to_bistratified (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=1.5E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_bistratified_to_cck (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=8.000000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_cck (Type: expTwoSynapse:  tauRise=4.32E-4 (SI time) tauDecay=0.00449 (SI time) peakTime=0.0011190597986863605 (SI time) waveformFactor=1.4196299918241655 (dimensionless) gbase=4.5000000000000005E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_cck (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=3.7E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_cck (Type: expTwoSynapse:  tauRise=7.28E-4 (SI time) tauDecay=0.0202 (SI time) peakTime=0.0025096919188377386 (SI time) waveformFactor=1.1746229968441386 (dimensionless) gbase=1.2E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_pvbasket_to_cck (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=1.2E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_cck (Type: expTwoSynapse:  tauRise=4.19E-4 (SI time) tauDecay=0.0049900000000000005 (SI time) peakTime=0.0011331450429356179 (SI time) waveformFactor=1.3699675937330524 (dimensionless) gbase=8.500000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ca3_to_cck (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=6.5E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_ec_to_cck (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=6.5E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_bistratified_to_ivy (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=5.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_ivy (Type: expTwoSynapse:  tauRise=4.32E-4 (SI time) tauDecay=0.00449 (SI time) peakTime=0.0011190597986863605 (SI time) waveformFactor=1.4196299918241655 (dimensionless) gbase=3.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_ivy (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=5.7000000000000003E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_ivy (Type: expTwoSynapse:  tauRise=3.0E-4 (SI time) tauDecay=6.0E-4 (SI time) peakTime=4.158883083359671E-4 (SI time) waveformFactor=4.0 (dimensionless) gbase=4.0500000000000005E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_pvbasket_to_ivy (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=1.6000000000000002E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_ivy (Type: expTwoSynapse:  tauRise=4.19E-4 (SI time) tauDecay=0.0049900000000000005 (SI time) peakTime=0.0011331450429356179 (SI time) waveformFactor=1.3699675937330524 (dimensionless) gbase=8.500000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ca3_to_ivy (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=3.0E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_ivy_to_ngf (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=5.7000000000000003E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_ngf (Type: expTwoSynapse:  tauRise=0.0013000000000000002 (SI time) tauDecay=0.010199999999999999 (SI time) peakTime=0.0030692034858662313 (SI time) waveformFactor=1.548425713511671 (dimensionless) gbase=9.800000000000001E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_ngf (Type: expTwoSynapse:  tauRise=4.19E-4 (SI time) tauDecay=0.0049900000000000005 (SI time) peakTime=0.0011331450429356179 (SI time) waveformFactor=1.3699675937330524 (dimensionless) gbase=8.500000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ec_to_ngf (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=3.5000000000000003E-9 (SI conductance) erev=0.0 (SI voltage))
    syn_bistratified_to_olm (Type: expTwoSynapse:  tauRise=0.001 (SI time) tauDecay=0.008 (SI time) peakTime=0.002376504619062669 (SI time) waveformFactor=1.5381716487226926 (dimensionless) gbase=2.0000000000000002E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_olm (Type: expTwoSynapse:  tauRise=0.001 (SI time) tauDecay=0.008 (SI time) peakTime=0.002376504619062669 (SI time) waveformFactor=1.5381716487226926 (dimensionless) gbase=7.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_olm (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=5.7000000000000003E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_olm (Type: expTwoSynapse:  tauRise=2.5E-4 (SI time) tauDecay=0.0075 (SI time) peakTime=8.796200124988334E-4 (SI time) waveformFactor=1.1632109250720026 (dimensionless) gbase=1.2E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_olm (Type: expTwoSynapse:  tauRise=3.0E-4 (SI time) tauDecay=6.0E-4 (SI time) peakTime=4.158883083359671E-4 (SI time) waveformFactor=4.0 (dimensionless) gbase=2.0000000000000003E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_sca_to_olm (Type: expTwoSynapse:  tauRise=0.001 (SI time) tauDecay=0.008 (SI time) peakTime=0.002376504619062669 (SI time) waveformFactor=1.5381716487226926 (dimensionless) gbase=8.500000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_axoaxonic_to_poolosyn (Type: expTwoSynapse:  tauRise=2.8000000000000003E-4 (SI time) tauDecay=0.008400000000000001 (SI time) peakTime=9.851744139986935E-4 (SI time) waveformFactor=1.1632109250720026 (dimensionless) gbase=1.15E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_bistratified_to_poolosyn (Type: expTwoSynapse:  tauRise=1.1E-4 (SI time) tauDecay=0.0097 (SI time) peakTime=4.983858865705835E-4 (SI time) waveformFactor=1.0647978670176388 (dimensionless) gbase=5.1E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_poolosyn (Type: expTwoSynapse:  tauRise=2.0E-4 (SI time) tauDecay=0.004200000000000001 (SI time) peakTime=6.393497119219188E-4 (SI time) waveformFactor=1.2226446837204854 (dimensionless) gbase=5.200000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_poolosyn (Type: expTwoSynapse:  tauRise=0.0011 (SI time) tauDecay=0.011 (SI time) peakTime=0.0028142706692149445 (SI time) waveformFactor=1.435055183349871 (dimensionless) gbase=4.100000000000001E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_poolosyn (Type: expTwoSynapse:  tauRise=1.3000000000000002E-4 (SI time) tauDecay=0.011 (SI time) peakTime=5.83855200082304E-4 (SI time) waveformFactor=1.0671230800079607 (dimensionless) gbase=3.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_poolosyn (Type: expTwoSynapse:  tauRise=1.0E-4 (SI time) tauDecay=0.0015 (SI time) peakTime=2.901482358323797E-4 (SI time) waveformFactor=1.3000789959133998 (dimensionless) gbase=7.0E-8 (SI conductance) erev=0.0 (SI voltage))
    syn_pvbasket_to_poolosyn (Type: expTwoSynapse:  tauRise=3.0E-4 (SI time) tauDecay=0.006200000000000001 (SI time) peakTime=9.547544236035908E-4 (SI time) waveformFactor=1.225794971825537 (dimensionless) gbase=2.0000000000000003E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_poolosyn (Type: expTwoSynapse:  tauRise=1.5E-4 (SI time) tauDecay=0.0039 (SI time) peakTime=5.082630599313511E-4 (SI time) waveformFactor=1.1847651563769113 (dimensionless) gbase=7.600000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ca3_to_poolosyn (Type: expTwoSynapse:  tauRise=5.0E-4 (SI time) tauDecay=0.003 (SI time) peakTime=0.0010750556815368332 (SI time) waveformFactor=1.7171628973263067 (dimensionless) gbase=2.0000000000000003E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_ec_to_poolosyn (Type: expTwoSynapse:  tauRise=5.0E-4 (SI time) tauDecay=0.003 (SI time) peakTime=0.0010750556815368332 (SI time) waveformFactor=1.7171628973263067 (dimensionless) gbase=2.0000000000000003E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_bistratified_to_pvbasket (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=9.000000000000001E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_pvbasket (Type: expTwoSynapse:  tauRise=4.32E-4 (SI time) tauDecay=0.00449 (SI time) peakTime=0.0011190597986863605 (SI time) waveformFactor=1.4196299918241655 (dimensionless) gbase=9.000000000000001E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_pvbasket (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=7.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_pvbasket (Type: expTwoSynapse:  tauRise=2.5E-4 (SI time) tauDecay=0.0075 (SI time) peakTime=8.796200124988334E-4 (SI time) waveformFactor=1.1632109250720026 (dimensionless) gbase=1.1000000000000001E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_pvbasket (Type: expTwoSynapse:  tauRise=7.000000000000001E-5 (SI time) tauDecay=2.0E-4 (SI time) peakTime=1.1305776725370377E-4 (SI time) waveformFactor=2.707624689928131 (dimensionless) gbase=7.0E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_pvbasket_to_pvbasket (Type: expTwoSynapse:  tauRise=8.0E-5 (SI time) tauDecay=0.0048 (SI time) peakTime=3.3309921862145905E-4 (SI time) waveformFactor=1.0900273513005547 (dimensionless) gbase=1.6000000000000003E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_pvbasket (Type: expTwoSynapse:  tauRise=4.19E-4 (SI time) tauDecay=0.0049900000000000005 (SI time) peakTime=0.0011331450429356179 (SI time) waveformFactor=1.3699675937330524 (dimensionless) gbase=1.3E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_ca3_to_pvbasket (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=2.2000000000000002E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_bistratified_to_sca (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=8.000000000000001E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_cck_to_sca (Type: expTwoSynapse:  tauRise=4.32E-4 (SI time) tauDecay=0.00449 (SI time) peakTime=0.0011190597986863605 (SI time) waveformFactor=1.4196299918241655 (dimensionless) gbase=7.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ivy_to_sca (Type: expTwoSynapse:  tauRise=0.0029 (SI time) tauDecay=0.0031000000000000003 (SI time) peakTime=0.0029977772837153148 (SI time) waveformFactor=40.766674825338406 (dimensionless) gbase=3.7E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_olm_to_sca (Type: expTwoSynapse:  tauRise=7.000000000000001E-5 (SI time) tauDecay=0.029 (SI time) peakTime=4.2287965467839903E-4 (SI time) waveformFactor=1.0171440692602471 (dimensionless) gbase=1.5E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_poolosyn_to_sca (Type: expTwoSynapse:  tauRise=3.0E-4 (SI time) tauDecay=6.0E-4 (SI time) peakTime=4.158883083359671E-4 (SI time) waveformFactor=4.0 (dimensionless) gbase=4.0500000000000005E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_pvbasket_to_sca (Type: expTwoSynapse:  tauRise=2.87E-4 (SI time) tauDecay=0.00267 (SI time) peakTime=7.172035578017181E-4 (SI time) waveformFactor=1.4657013117495854 (dimensionless) gbase=6.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_sca_to_sca (Type: expTwoSynapse:  tauRise=2.0E-4 (SI time) tauDecay=0.002 (SI time) peakTime=5.116855762208991E-4 (SI time) waveformFactor=1.435055183349871 (dimensionless) gbase=1.0E-9 (SI conductance) erev=-0.06 (SI voltage))
    syn_ca3_to_sca (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=3.0E-10 (SI conductance) erev=0.0 (SI voltage))
    syn_ec_to_sca (Type: expTwoSynapse:  tauRise=0.002 (SI time) tauDecay=0.0063 (SI time) peakTime=0.0033621560245937266 (SI time) waveformFactor=2.498299174531839 (dimensionless) gbase=4.5000000000000005E-10 (SI conductance) erev=0.0 (SI voltage))
    null (Type: notes)
    syn_ngf_to_axoaxonic_A (Type: expTwoSynapse:  tauRise=0.008 (SI time) tauDecay=0.039 (SI time) peakTime=0.015943402341559384 (SI time) waveformFactor=1.8934103667284334 (dimensionless) gbase=5.7000000000000003E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_ngf_to_axoaxonic_B (Type: expTwoSynapse:  tauRise=0.18 (SI time) tauDecay=0.2 (SI time) peakTime=0.18964892818408724 (SI time) waveformFactor=25.811747917131978 (dimensionless) gbase=1.69139E-11 (SI conductance) erev=-0.09 (SI voltage))
    syn_ngf_to_bistratified_A (Type: expTwoSynapse:  tauRise=0.008 (SI time) tauDecay=0.039 (SI time) peakTime=0.015943402341559384 (SI time) waveformFactor=1.8934103667284334 (dimensionless) gbase=5.7000000000000003E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_ngf_to_bistratified_B (Type: expTwoSynapse:  tauRise=0.18 (SI time) tauDecay=0.2 (SI time) peakTime=0.18964892818408724 (SI time) waveformFactor=25.811747917131978 (dimensionless) gbase=1.69139E-11 (SI conductance) erev=-0.09 (SI voltage))
    syn_ngf_to_cck_A (Type: expTwoSynapse:  tauRise=0.008 (SI time) tauDecay=0.039 (SI time) peakTime=0.015943402341559384 (SI time) waveformFactor=1.8934103667284334 (dimensionless) gbase=5.7000000000000003E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_ngf_to_cck_B (Type: expTwoSynapse:  tauRise=0.18 (SI time) tauDecay=0.2 (SI time) peakTime=0.18964892818408724 (SI time) waveformFactor=25.811747917131978 (dimensionless) gbase=1.69139E-11 (SI conductance) erev=-0.09 (SI voltage))
    syn_ngf_to_ivy_A (Type: expTwoSynapse:  tauRise=0.008 (SI time) tauDecay=0.039 (SI time) peakTime=0.015943402341559384 (SI time) waveformFactor=1.8934103667284334 (dimensionless) gbase=9.0E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_ngf_to_ivy_B (Type: expTwoSynapse:  tauRise=0.18 (SI time) tauDecay=0.2 (SI time) peakTime=0.18964892818408724 (SI time) waveformFactor=25.811747917131978 (dimensionless) gbase=2.67062E-11 (SI conductance) erev=-0.09 (SI voltage))
    syn_ngf_to_ngf_A (Type: expTwoSynapse:  tauRise=0.0031000000000000003 (SI time) tauDecay=0.042 (SI time) peakTime=0.008723291243813708 (SI time) waveformFactor=1.3289282339374142 (dimensionless) gbase=1.6000000000000002E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ngf_to_ngf_B (Type: expTwoSynapse:  tauRise=0.18 (SI time) tauDecay=0.2 (SI time) peakTime=0.18964892818408724 (SI time) waveformFactor=25.811747917131978 (dimensionless) gbase=4.74777E-11 (SI conductance) erev=-0.09 (SI voltage))
    syn_ngf_to_poolosyn_A (Type: expTwoSynapse:  tauRise=0.009000000000000001 (SI time) tauDecay=0.039 (SI time) peakTime=0.017156143704883095 (SI time) waveformFactor=2.018319804023249 (dimensionless) gbase=6.500000000000001E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_ngf_to_poolosyn_B (Type: expTwoSynapse:  tauRise=0.18 (SI time) tauDecay=0.2 (SI time) peakTime=0.18964892818408724 (SI time) waveformFactor=25.811747917131978 (dimensionless) gbase=1.9287800000000002E-11 (SI conductance) erev=-0.09 (SI voltage))
    syn_ngf_to_pvbasket_A (Type: expTwoSynapse:  tauRise=0.008 (SI time) tauDecay=0.039 (SI time) peakTime=0.015943402341559384 (SI time) waveformFactor=1.8934103667284334 (dimensionless) gbase=7.0E-10 (SI conductance) erev=-0.06 (SI voltage))
    syn_ngf_to_pvbasket_B (Type: expTwoSynapse:  tauRise=0.18 (SI time) tauDecay=0.2 (SI time) peakTime=0.18964892818408724 (SI time) waveformFactor=25.811747917131978 (dimensionless) gbase=2.0771500000000002E-10 (SI conductance) erev=-0.09 (SI voltage))
    syn_ngf_to_sca_A (Type: expTwoSynapse:  tauRise=0.008 (SI time) tauDecay=0.039 (SI time) peakTime=0.015943402341559384 (SI time) waveformFactor=1.8934103667284334 (dimensionless) gbase=5.7000000000000003E-11 (SI conductance) erev=-0.06 (SI voltage))
    syn_ngf_to_sca_B (Type: expTwoSynapse:  tauRise=0.18 (SI time) tauDecay=0.2 (SI time) peakTime=0.18964892818408724 (SI time) waveformFactor=25.811747917131978 (dimensionless) gbase=1.69139E-11 (SI conductance) erev=-0.09 (SI voltage))
    null (Type: notes)
    spikeGenPoisson (Type: spikeGeneratorPoisson:  averageRate=50.0 (SI per_time) averageIsi=0.02 (SI time))
    vc_ngf (Type: voltageClamp:  delay=0.0 (SI time) duration=0.001 (SI time) targetVoltage=-0.0599512 (SI voltage) simpleSeriesResistance=50000.0 (SI resistance))
    vc_bistratified (Type: voltageClamp:  delay=0.0 (SI time) duration=0.001 (SI time) targetVoltage=-0.0670184 (SI voltage) simpleSeriesResistance=50000.0 (SI resistance))
    vc_sca (Type: voltageClamp:  delay=0.0 (SI time) duration=0.001 (SI time) targetVoltage=-0.07056520000000001 (SI voltage) simpleSeriesResistance=50000.0 (SI resistance))
    vc_olm (Type: voltageClamp:  delay=0.0 (SI time) duration=0.001 (SI time) targetVoltage=-0.0711411 (SI voltage) simpleSeriesResistance=50000.0 (SI resistance))
    vc_ivy (Type: voltageClamp:  delay=0.0 (SI time) duration=0.001 (SI time) targetVoltage=-0.0599512 (SI voltage) simpleSeriesResistance=50000.0 (SI resistance))
    vc_pvbasket (Type: voltageClamp:  delay=0.0 (SI time) duration=0.001 (SI time) targetVoltage=-0.0650246 (SI voltage) simpleSeriesResistance=50000.0 (SI resistance))
    vc_cck (Type: voltageClamp:  delay=0.0 (SI time) duration=0.001 (SI time) targetVoltage=-0.0706306 (SI voltage) simpleSeriesResistance=50000.0 (SI resistance))
    vc_axoaxonic (Type: voltageClamp:  delay=0.0 (SI time) duration=0.001 (SI time) targetVoltage=-0.06501269999999999 (SI voltage) simpleSeriesResistance=50000.0 (SI resistance))
    vc_poolosyn (Type: voltageClamp:  delay=0.0 (SI time) duration=0.001 (SI time) targetVoltage=-0.0629601 (SI voltage) simpleSeriesResistance=50000.0 (SI resistance))
    MiniScale_HippocampalNet (Type: networkWithTemperature:  temperature=307.15 (SI temperature))
    Sim_MiniScale_HippocampalNet (Type: Simulation:  length=2.0 (SI time) step=1.0E-5 (SI time))


    This NETPYNE file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.5.2
         org.neuroml.model   v1.5.2
         jLEMS               v0.9.8.9

'''
# Main NetPyNE script for: MiniScale_HippocampalNet

# See https://github.com/Neurosim-lab/netpyne

from netpyne import specs  # import netpyne specs module
from netpyne import sim    # import netpyne sim module

from neuron import h

import sys


###############################################################################
# NETWORK PARAMETERS
###############################################################################

nml2_file_name = 'MiniScale_HippocampalNet.net.nml'

###############################################################################
# SIMULATION PARAMETERS
###############################################################################

simConfig = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

# Simulation parameters
simConfig.duration = simConfig.tstop = 2000.0 # Duration of the simulation, in ms
simConfig.dt = 0.01 # Internal integration timestep to use

# Seeds for randomizers (connectivity, input stimulation and cell locations)
# Note: locations and connections should be fully specified by the structure of the NeuroML,
# so seeds for conn & loc shouldn't affect networks structure/behaviour
simConfig.seeds = {'conn': 0, 'stim': 12345, 'loc': 0} 

simConfig.createNEURONObj = 1  # create HOC objects when instantiating network
simConfig.createPyStruct = 1  # create Python structure (simulator-independent) when instantiating network
simConfig.verbose = False  # show detailed messages 
simConfig.hParams['celsius'] = (307.15 - 273.15)

# Recording 
simConfig.recordCells = ['all']  
simConfig.recordTraces = {}

# For saving to file: ngf.v.dat (ref: of_ngf)
# Column: v_0: Pop: pop_ngf; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['of_ngf_pop_ngf_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_ngf','cellLabel':0}}
# For saving to file: bistratified.v.dat (ref: of_bistratified)
# Column: v_0: Pop: pop_bistratified; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['of_bistratified_pop_bistratified_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_bistratified','cellLabel':0}}
# For saving to file: sca.v.dat (ref: of_sca)
# Column: v_0: Pop: pop_sca; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['of_sca_pop_sca_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_sca','cellLabel':0}}
# For saving to file: olm.v.dat (ref: of_olm)
# Column: v_0: Pop: pop_olm; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['of_olm_pop_olm_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_olm','cellLabel':0}}
# For saving to file: ivy.v.dat (ref: of_ivy)
# Column: v_0: Pop: pop_ivy; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['of_ivy_pop_ivy_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_ivy','cellLabel':0}}
# For saving to file: pvbasket.v.dat (ref: of_pvbasket)
# Column: v_0: Pop: pop_pvbasket; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['of_pvbasket_pop_pvbasket_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_pvbasket','cellLabel':0}}
# For saving to file: cck.v.dat (ref: of_cck)
# Column: v_0: Pop: pop_cck; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['of_cck_pop_cck_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_cck','cellLabel':0}}
# For saving to file: axoaxonic.v.dat (ref: of_axoaxonic)
# Column: v_0: Pop: pop_axoaxonic; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['of_axoaxonic_pop_axoaxonic_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_axoaxonic','cellLabel':0}}
# For saving to file: poolosyn.v.dat (ref: of_poolosyn)
# Column: v_0: Pop: pop_poolosyn; cell: 0; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['of_poolosyn_pop_poolosyn_0_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_poolosyn','cellLabel':0}}
# Column: v_1: Pop: pop_poolosyn; cell: 1; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['of_poolosyn_pop_poolosyn_1_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_poolosyn','cellLabel':1}}
# Column: v_2: Pop: pop_poolosyn; cell: 2; segment id: 0; segment name: Seg0_soma_0; Neuron loc: soma_0(0.25); value: v (v)
simConfig.recordTraces['of_poolosyn_pop_poolosyn_2_Seg0_soma_0_v'] = {'sec':'soma_0','loc':0.25,'var':'v','conds':{'pop':'pop_poolosyn','cellLabel':2}}


simConfig.plotCells = ['all']


simConfig.recordStim = True  # record spikes of cell stims
simConfig.recordStep = simConfig.dt # Step size in ms to save data (eg. V traces, LFP, etc)



# Analysis and plotting 
simConfig.plotRaster = True # Whether or not to plot a raster
simConfig.plotLFPSpectrum = False # plot power spectral density
simConfig.maxspikestoplot = 3e8 # Maximum number of spikes to plot
simConfig.plotConn = False # whether to plot conn matrix
simConfig.plotWeightChanges = False # whether to plot weight changes (shown in conn matrix)
#simConfig.plot3dArch = True # plot 3d architecture

# Saving
simConfig.filename = 'MiniScale_HippocampalNet.txt'  # Set file output name
simConfig.saveFileStep = simConfig.dt # step size in ms to save data to disk
# simConfig.saveDat = True # save to dat file


###############################################################################
# IMPORT & RUN
###############################################################################

print("Running a NetPyNE based simulation for %sms (dt: %sms) at %s degC"%(simConfig.duration, simConfig.dt, h.celsius))

gids = sim.importNeuroML2SimulateAnalyze(nml2_file_name,simConfig)

print("Finished simulation")


###############################################################################
#   Saving data (this ensures the data gets saved in the format/files 
#   as specified in the LEMS <Simulation> element)
###############################################################################


if sim.rank==0: 
    print("Saving to file: ngf.v.dat (ref: of_ngf)")

 
    # Column: t
    col_of_ngf_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: v_0: Pop: pop_ngf; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_of_ngf_v_0 = sim.allSimData['of_ngf_pop_ngf_0_Seg0_soma_0_v']['cell_%s'%gids['pop_ngf'][0]]

    dat_file_of_ngf = open('ngf.v.dat', 'w')
    for i in range(len(col_of_ngf_t)):
        dat_file_of_ngf.write( '%s\t'%(col_of_ngf_t[i]/1000.0) +  '%s\t'%(col_of_ngf_v_0[i]/1000.0) +  '\n')
    dat_file_of_ngf.close()

    print("Saving to file: bistratified.v.dat (ref: of_bistratified)")

 
    # Column: t
    col_of_bistratified_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: v_0: Pop: pop_bistratified; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_of_bistratified_v_0 = sim.allSimData['of_bistratified_pop_bistratified_0_Seg0_soma_0_v']['cell_%s'%gids['pop_bistratified'][0]]

    dat_file_of_bistratified = open('bistratified.v.dat', 'w')
    for i in range(len(col_of_bistratified_t)):
        dat_file_of_bistratified.write( '%s\t'%(col_of_bistratified_t[i]/1000.0) +  '%s\t'%(col_of_bistratified_v_0[i]/1000.0) +  '\n')
    dat_file_of_bistratified.close()

    print("Saving to file: sca.v.dat (ref: of_sca)")

 
    # Column: t
    col_of_sca_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: v_0: Pop: pop_sca; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_of_sca_v_0 = sim.allSimData['of_sca_pop_sca_0_Seg0_soma_0_v']['cell_%s'%gids['pop_sca'][0]]

    dat_file_of_sca = open('sca.v.dat', 'w')
    for i in range(len(col_of_sca_t)):
        dat_file_of_sca.write( '%s\t'%(col_of_sca_t[i]/1000.0) +  '%s\t'%(col_of_sca_v_0[i]/1000.0) +  '\n')
    dat_file_of_sca.close()

    print("Saving to file: olm.v.dat (ref: of_olm)")

 
    # Column: t
    col_of_olm_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: v_0: Pop: pop_olm; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_of_olm_v_0 = sim.allSimData['of_olm_pop_olm_0_Seg0_soma_0_v']['cell_%s'%gids['pop_olm'][0]]

    dat_file_of_olm = open('olm.v.dat', 'w')
    for i in range(len(col_of_olm_t)):
        dat_file_of_olm.write( '%s\t'%(col_of_olm_t[i]/1000.0) +  '%s\t'%(col_of_olm_v_0[i]/1000.0) +  '\n')
    dat_file_of_olm.close()

    print("Saving to file: ivy.v.dat (ref: of_ivy)")

 
    # Column: t
    col_of_ivy_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: v_0: Pop: pop_ivy; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_of_ivy_v_0 = sim.allSimData['of_ivy_pop_ivy_0_Seg0_soma_0_v']['cell_%s'%gids['pop_ivy'][0]]

    dat_file_of_ivy = open('ivy.v.dat', 'w')
    for i in range(len(col_of_ivy_t)):
        dat_file_of_ivy.write( '%s\t'%(col_of_ivy_t[i]/1000.0) +  '%s\t'%(col_of_ivy_v_0[i]/1000.0) +  '\n')
    dat_file_of_ivy.close()

    print("Saving to file: pvbasket.v.dat (ref: of_pvbasket)")

 
    # Column: t
    col_of_pvbasket_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: v_0: Pop: pop_pvbasket; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_of_pvbasket_v_0 = sim.allSimData['of_pvbasket_pop_pvbasket_0_Seg0_soma_0_v']['cell_%s'%gids['pop_pvbasket'][0]]

    dat_file_of_pvbasket = open('pvbasket.v.dat', 'w')
    for i in range(len(col_of_pvbasket_t)):
        dat_file_of_pvbasket.write( '%s\t'%(col_of_pvbasket_t[i]/1000.0) +  '%s\t'%(col_of_pvbasket_v_0[i]/1000.0) +  '\n')
    dat_file_of_pvbasket.close()

    print("Saving to file: cck.v.dat (ref: of_cck)")

 
    # Column: t
    col_of_cck_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: v_0: Pop: pop_cck; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_of_cck_v_0 = sim.allSimData['of_cck_pop_cck_0_Seg0_soma_0_v']['cell_%s'%gids['pop_cck'][0]]

    dat_file_of_cck = open('cck.v.dat', 'w')
    for i in range(len(col_of_cck_t)):
        dat_file_of_cck.write( '%s\t'%(col_of_cck_t[i]/1000.0) +  '%s\t'%(col_of_cck_v_0[i]/1000.0) +  '\n')
    dat_file_of_cck.close()

    print("Saving to file: axoaxonic.v.dat (ref: of_axoaxonic)")

 
    # Column: t
    col_of_axoaxonic_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: v_0: Pop: pop_axoaxonic; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_of_axoaxonic_v_0 = sim.allSimData['of_axoaxonic_pop_axoaxonic_0_Seg0_soma_0_v']['cell_%s'%gids['pop_axoaxonic'][0]]

    dat_file_of_axoaxonic = open('axoaxonic.v.dat', 'w')
    for i in range(len(col_of_axoaxonic_t)):
        dat_file_of_axoaxonic.write( '%s\t'%(col_of_axoaxonic_t[i]/1000.0) +  '%s\t'%(col_of_axoaxonic_v_0[i]/1000.0) +  '\n')
    dat_file_of_axoaxonic.close()

    print("Saving to file: poolosyn.v.dat (ref: of_poolosyn)")

 
    # Column: t
    col_of_poolosyn_t = [i*simConfig.dt for i in range(int(simConfig.duration/simConfig.dt))]

    # Column: v_0: Pop: pop_poolosyn; cell: 0; segment id: 0; segment name: Seg0_soma_0; value: v
    col_of_poolosyn_v_0 = sim.allSimData['of_poolosyn_pop_poolosyn_0_Seg0_soma_0_v']['cell_%s'%gids['pop_poolosyn'][0]]

    # Column: v_1: Pop: pop_poolosyn; cell: 1; segment id: 0; segment name: Seg0_soma_0; value: v
    col_of_poolosyn_v_1 = sim.allSimData['of_poolosyn_pop_poolosyn_1_Seg0_soma_0_v']['cell_%s'%gids['pop_poolosyn'][1]]

    # Column: v_2: Pop: pop_poolosyn; cell: 2; segment id: 0; segment name: Seg0_soma_0; value: v
    col_of_poolosyn_v_2 = sim.allSimData['of_poolosyn_pop_poolosyn_2_Seg0_soma_0_v']['cell_%s'%gids['pop_poolosyn'][2]]

    dat_file_of_poolosyn = open('poolosyn.v.dat', 'w')
    for i in range(len(col_of_poolosyn_t)):
        dat_file_of_poolosyn.write( '%s\t'%(col_of_poolosyn_t[i]/1000.0) +  '%s\t'%(col_of_poolosyn_v_0[i]/1000.0) +  '%s\t'%(col_of_poolosyn_v_1[i]/1000.0) +  '%s\t'%(col_of_poolosyn_v_2[i]/1000.0) +  '\n')
    dat_file_of_poolosyn.close()


    print("Saved all data.")

if '-nogui' in sys.argv:
    quit()
