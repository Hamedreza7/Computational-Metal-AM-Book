from pathlib import Path
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
ALPHA0=.35; TREF=300.; BETA=(.53-.35)/(1200.-TREF); AMIN=.20; AMAX=.70; DT_CONST=1.6

def alpha(T): return np.clip(ALPHA0+BETA*(np.asarray(T)-TREF),AMIN,AMAX)
out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True); T=1200.; a=float(alpha(T)); mult=a/ALPHA0; dt=mult*DT_CONST
pd.DataFrame({'quantity':['T_K','alpha0','alpha_corrected','source_multiplier','constant_step_rise_K','AEPB_step_rise_K'],'value':[T,ALPHA0,a,mult,DT_CONST,dt]}).to_csv(out/'aepb_summary.csv',index=False)
Tv=np.linspace(300,2000,300); fig,ax=plt.subplots(figsize=(7,4.5)); ax.plot(Tv,alpha(Tv)); ax.set_xlabel('temperature (K)'); ax.set_ylabel('effective absorptivity'); ax.grid(True,alpha=.25); fig.tight_layout(); fig.savefig(out/'absorptivity_vs_temperature.png',dpi=180); plt.close(fig)
print(f'alpha(1200 K)={a:.3f}; multiplier={mult:.3f}; corrected rise={dt:.2f} K')
