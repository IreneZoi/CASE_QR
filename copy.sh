#!bin/bash
xsec=100
signal=WpToBpT_Wp3000_Bp400_Top170_ZbtReco #QstarToQW_M_2000_mW_400Reco #QstarToQW_M_2000_mW_170Reco #QstarToQW_M_2000_mW_400Reco
scp /eos/uscms/store/user/izoi/CASE/QR/QR_results/events/run_50005/sig_${signal}/xsec_${xsec}/loss_rk5_05/* izoi@lxplus.cern.ch:/eos/user/i/izoi/SWAN_projects/CASE/QR/run_50005/xsec_${xsec}/sig_${signal}/
scp /eos/uscms/store/user/izoi/CASE/QR/QR_results/analysis/run_50005/sig_${signal}/xsec_${xsec}/loss_rk5_05/qr_cuts//envelope/* izoi@lxplus.cern.ch:/eos/user/i/izoi/SWAN_projects/CASE/QR/run_50005//xsec_${xsec}/sig_${signal}/