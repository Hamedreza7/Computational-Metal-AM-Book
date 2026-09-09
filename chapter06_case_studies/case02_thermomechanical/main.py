from pathlib import Path
import numpy as np, pandas as pd
T=np.array([300.,656.66,1134.64,1336.70,946.38,300.]); E=200e9; A=12e-6; T0=300.; TSF=700.; ETA=.31
weights=np.array([.5,1,1,1,1,.5]); Tbar=(weights@T)/5.0
sigma_el=-E*A*(Tbar-T0)/1e6; sigma_res_full=E*A*(TSF-T0)/1e6; sigma_res=ETA*sigma_res_full
out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True); pd.DataFrame({'quantity':['Tbar_K','sigma_elastic_MPa','sigma_res_full_MPa','sigma_res_partial_MPa'],'value':[Tbar,sigma_el,sigma_res_full,sigma_res]}).to_csv(out/'stress_summary.csv',index=False)
print(f'Tbar={Tbar:.2f} K'); print(f'Fully constrained elastic stress={sigma_el:.1f} MPa'); print(f'Partial-constraint residual stress={sigma_res:.1f} MPa')
