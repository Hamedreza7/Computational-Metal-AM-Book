from pathlib import Path
import numpy as np, pandas as pd
import matplotlib.pyplot as plt

GAMMA=0.035; MU=0.010; DP=30e-6; POROSITY=0.42; C_R=0.20
R_EFF=C_R*POROSITY/(1-POROSITY)*DP

def penetration(t,theta_deg):
    c=np.cos(np.deg2rad(theta_deg))
    return np.sqrt(np.maximum(R_EFF*GAMMA*c*t/(2*MU),0.0))

def main():
    out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True)
    t=np.linspace(0,0.10,301); df=pd.DataFrame({'time_s':t})
    fig,ax=plt.subplots(figsize=(7,4.5))
    for th in (20,40,60):
        L=penetration(t,th); df[f'L_theta_{th}_m']=L; ax.plot(t,L*1e3,label=f'{th}°')
    ax.set_xlabel('time (s)'); ax.set_ylabel('penetration distance (mm)'); ax.legend(title='contact angle'); ax.grid(True,alpha=.25)
    fig.tight_layout(); fig.savefig(out/'penetration_vs_time.png',dpi=180); plt.close(fig); df.to_csv(out/'penetration.csv',index=False)
    pc=2*GAMMA*np.cos(np.deg2rad(40))/R_EFF
    print(f'Effective pore radius: {R_EFF*1e6:.3f} µm'); print(f'Capillary pressure at 40°: {pc/1e3:.2f} kPa')
if __name__=='__main__': main()
