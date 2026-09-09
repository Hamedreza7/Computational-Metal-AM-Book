from pathlib import Path
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
HERE=Path(__file__).parent

def pareto(vals):
    n=len(vals); keep=np.ones(n,dtype=bool)
    for i in range(n):
        for j in range(n):
            if i!=j and np.all(vals[j]<=vals[i]) and np.any(vals[j]<vals[i]): keep[i]=False; break
    return keep

def main():
    out=HERE/'expected_output'; out.mkdir(exist_ok=True); df=pd.read_csv(HERE/'designs.csv'); cols=['mass_kg','distortion_mm','support_cm3']; vals=df[cols].to_numpy(float); mask=pareto(vals); df['pareto']=mask
    mn=vals.min(0); mx=vals.max(0); norm=(vals-mn)/(mx-mn); weights=np.array([0.30,0.45,0.25]); df['weighted_score']=norm@weights; df.loc[~mask,'weighted_score']=np.nan
    df.to_csv(out/'pareto_designs.csv',index=False); best=df.loc[df['weighted_score'].idxmin(),'design']
    fig,ax=plt.subplots(figsize=(6,4.5)); ax.scatter(df.mass_kg,df.distortion_mm,label='feasible'); pf=df[mask].sort_values('mass_kg'); ax.plot(pf.mass_kg,pf.distortion_mm,'o-',label='Pareto'); ax.set_xlabel('mass (kg)'); ax.set_ylabel('distortion (mm)'); ax.legend(); ax.grid(True,alpha=.25); fig.tight_layout(); fig.savefig(out/'pareto_mass_distortion.png',dpi=180); plt.close(fig)
    print(f'Weighted Pareto selection: Design {best}')
if __name__=='__main__': main()
