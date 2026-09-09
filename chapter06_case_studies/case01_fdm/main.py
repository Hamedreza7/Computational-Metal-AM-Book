from pathlib import Path
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
RHO=7800.; CP=500.; K=25.; L=5e-4; N=6; DX=L/(N-1); DT=1e-4; V=.5; SIGMA=1e-4; Q0=1.25e13; X0=2e-4; TAMB=300.; ALPHA=K/(RHO*CP); FO=ALPHA*DT/DX**2
x=np.arange(N)*DX

def source_increment(n):
    xl=X0+V*(n*DT); Q=Q0*np.exp(-((x-xl)**2)/(2*SIGMA**2)); return DT*Q/(RHO*CP)
def solve():
    hist=[np.full(N,TAMB)]
    for n in range(4):
        Told=hist[-1]; Tnew=Told.copy(); S=source_increment(n)
        for i in range(1,N-1): Tnew[i]=Told[i]+FO*(Told[i+1]-2*Told[i]+Told[i-1])+S[i]
        Tnew[0]=Tnew[-1]=TAMB; hist.append(Tnew)
    return np.array(hist)
def main():
    out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True); H=solve(); df=pd.DataFrame(H,columns=[f'T{i}_K' for i in range(N)]); df.insert(0,'step',range(len(H))); df.to_csv(out/'temperatures.csv',index=False)
    fig,ax=plt.subplots(figsize=(7,4.5));
    for n,row in enumerate(H): ax.plot(x*1e3,row,marker='o',label=f'step {n}')
    ax.set_xlabel('x (mm)'); ax.set_ylabel('temperature (K)'); ax.legend(ncol=2); ax.grid(True,alpha=.25); fig.tight_layout(); fig.savefig(out/'temperature_history.png',dpi=180); plt.close(fig)
    expected=np.array([300,656.66,1134.64,1336.70,946.38,300]); print('Step 4:',np.round(H[-1],2)); print('Max abs difference vs book rounded vector:',np.max(np.abs(H[-1]-expected)))
if __name__=='__main__': main()
