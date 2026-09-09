from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

RHO=7800.0; CP=500.0; L=5e-4; V=0.5; SIGMA=1e-4; Q0=1.25e13; X0=2e-4

def q(x,t):
    xl=X0+V*t
    return Q0*np.exp(-((x-xl)**2)/(2*SIGMA**2))

def main():
    out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True)
    x=np.linspace(0,L,501); times=np.array([0,1e-4,2e-4,3e-4])
    data={'x_m':x}
    fig,ax=plt.subplots(figsize=(7,4.5))
    for t in times:
        y=q(x,t); data[f'Q_t_{t:.0e}_W_m3']=y
        ax.plot(x*1e3,y/1e12,label=f't={t*1e3:.1f} ms')
    ax.set_xlabel('x (mm)'); ax.set_ylabel('Q (10^12 W/m^3)'); ax.legend(); ax.grid(True,alpha=.25)
    fig.tight_layout(); fig.savefig(out/'gaussian_heat_source.png',dpi=180); plt.close(fig)
    pd.DataFrame(data).to_csv(out/'source_profiles.csv',index=False)
    smax=1e-4*Q0/(RHO*CP)
    print(f'Maximum source-driven temperature increment per 1e-4 s step: {smax:.2f} K')
if __name__=='__main__': main()
