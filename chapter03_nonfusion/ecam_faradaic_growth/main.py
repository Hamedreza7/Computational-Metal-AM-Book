from pathlib import Path
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
F=96485.33212; Z=2; D=7e-10; C_B=1000.0; DELTA=50e-6; ETA_F=0.95; M=0.063546; RHO_M=8960.0

def v_n(j): return ETA_F*M*j/(Z*F*RHO_M)
def main():
    out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True)
    jlim=Z*F*D*C_B/DELTA
    j=np.linspace(0,1.2*jlim,250); j_eff=np.minimum(j,jlim); v=v_n(j_eff)
    df=pd.DataFrame({'requested_current_A_m2':j,'transport_limited_current_A_m2':j_eff,'growth_velocity_m_s':v}); df.to_csv(out/'growth_table.csv',index=False)
    fig,ax=plt.subplots(figsize=(7,4.5)); ax.plot(j,j_eff,label='available deposition current'); ax.plot(j,j,label='requested current'); ax.set_xlabel('requested current density (A/m²)'); ax.set_ylabel('current density (A/m²)'); ax.legend(); ax.grid(True,alpha=.25); fig.tight_layout(); fig.savefig(out/'growth_vs_current.png',dpi=180); plt.close(fig)
    print(f'Diffusion-limited current density: {jlim:.1f} A/m²'); print(f'Growth velocity at j_lim: {v_n(jlim)*1e9:.3f} nm/s')
if __name__=='__main__': main()
