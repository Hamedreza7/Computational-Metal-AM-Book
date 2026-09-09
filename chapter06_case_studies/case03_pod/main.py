from pathlib import Path
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
T0=np.full(6,300.)
Ts=np.array([[300,494.40,620.51,494.40,343.38,300],[300,594.08,887.20,775.65,454.33,300],[300,637.39,1055.66,1082.72,659.44,300],[300,656.66,1134.64,1336.70,946.38,300]],float).T
X=Ts-T0[:,None]; U,s,Vt=np.linalg.svd(X,full_matrices=False); energy=s*s/np.sum(s*s); cum=np.cumsum(energy)
out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True); pd.DataFrame({'mode':np.arange(1,len(s)+1),'singular_value':s,'energy_fraction':energy,'cumulative_energy':cum}).to_csv(out/'pod_energy.csv',index=False)
rows=[]
for r in (1,2):
    Xr=U[:,:r]@np.diag(s[:r])@Vt[:r,:]; Tr=T0[:,None]+Xr; rel=np.linalg.norm(Tr-Ts)/np.linalg.norm(Ts-T0[:,None]); rows.append((r,rel))
pd.DataFrame(rows,columns=['rank','relative_fluctuation_error']).to_csv(out/'reconstruction_errors.csv',index=False)
X2=U[:,:2]@np.diag(s[:2])@Vt[:2,:]; T2=T0[:,None]+X2; fig,ax=plt.subplots(figsize=(7,4.5)); ax.plot(range(6),Ts[:,-1],marker='o',label='FDM step 4'); ax.plot(range(6),T2[:,-1],marker='s',linestyle='--',label='rank-2 POD'); ax.set_xlabel('node'); ax.set_ylabel('temperature (K)'); ax.legend(); ax.grid(True,alpha=.25); fig.tight_layout(); fig.savefig(out/'rank2_reconstruction.png',dpi=180); plt.close(fig)
print(f'Rank-1 energy: {100*cum[0]:.2f}%'); print(f'Rank-2 energy: {100*cum[1]:.2f}%')
