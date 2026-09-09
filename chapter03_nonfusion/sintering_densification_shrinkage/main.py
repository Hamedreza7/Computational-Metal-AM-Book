from pathlib import Path
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
R=8.314; T=1450.0; AS=2.0e5; QS=1.7e5; RHO0=0.60

def rhs(t,y):
    rho=float(y[0]); return [AS*(1-rho)*np.exp(-QS/(R*T))]

def main():
    out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True)
    t=np.linspace(0,7200,400); sol=solve_ivp(rhs,[t[0],t[-1]],[RHO0],t_eval=t,rtol=1e-9,atol=1e-11)
    rho=sol.y[0]; stretch=(RHO0/rho)**(1/3); shrink=1-stretch
    pd.DataFrame({'time_s':t,'relative_density':rho,'linear_shrinkage':shrink}).to_csv(out/'history.csv',index=False)
    fig,ax=plt.subplots(figsize=(7,4.5)); ax.plot(t/60,rho,label='relative density'); ax.plot(t/60,shrink,label='linear shrinkage'); ax.set_xlabel('time (min)'); ax.set_ylabel('dimensionless'); ax.legend(); ax.grid(True,alpha=.25); fig.tight_layout(); fig.savefig(out/'densification_shrinkage.png',dpi=180); plt.close(fig)
    print(f'Final relative density: {rho[-1]:.4f}'); print(f'Final isotropic linear shrinkage: {100*shrink[-1]:.2f}%')
if __name__=='__main__': main()
