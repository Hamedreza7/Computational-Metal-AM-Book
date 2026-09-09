from pathlib import Path
import pandas as pd
A2=1e-5; A1=.30; A0=-200.; TPEAK=1450.; GRAD=2.1e6; SA=180.; SM_SERVICE=60.; SE=450.; SUT=840.
sres=A0+A1*TPEAK+A2*GRAD; sme=SM_SERVICE+sres; eta=SA/SE+sme/SUT; margin=1-eta
out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True); pd.DataFrame({'quantity':['a0_MPa','a1_MPa_per_K','a2_MPa_per_K_per_m','Tpeak_K','grad_K_per_m','sigma_res_MPa','sigma_m_eff_MPa','Goodman_index','margin'],'value':[A0,A1,A2,TPEAK,GRAD,sres,sme,eta,margin]}).to_csv(out/'digital_twin_summary.csv',index=False)
print(f'Residual stress prediction: {sres:.1f} MPa'); print(f'Effective mean stress: {sme:.1f} MPa'); print(f'Goodman index={eta:.3f}; margin={margin:.3f}')
