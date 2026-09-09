from pathlib import Path
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
ALPHA=.1; t=.1; xs=np.array([.25,.5,.75])
coef=-1+ALPHA*(1-t)*np.pi**2; R=coef*np.sin(np.pi*xs); loss=np.mean(R**2)
trial=(1-t)*np.sin(np.pi*xs); exact=np.exp(-ALPHA*np.pi**2*t)*np.sin(np.pi*xs)
out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True); pd.DataFrame({'x':xs,'t':t,'residual_from_stated_PDE':R,'trial_T':trial,'exact_T':exact}).to_csv(out/'residuals.csv',index=False)
x=np.linspace(0,1,250); fig,ax=plt.subplots(figsize=(7,4.5)); ax.plot(x,(1-t)*np.sin(np.pi*x),label='trial'); ax.plot(x,np.exp(-ALPHA*np.pi**2*t)*np.sin(np.pi*x),'--',label='exact'); ax.set_xlabel('x'); ax.set_ylabel('T'); ax.legend(); ax.grid(True,alpha=.25); fig.tight_layout(); fig.savefig(out/'trial_vs_exact.png',dpi=180); plt.close(fig)
print('Residuals from stated PDE:',np.round(R,6)); print(f'Mean squared residual: {loss:.6f}'); print('Current manuscript table reports ~[6.98, 9.87, 6.98]; see docs/BOOK_VALIDATION_NOTES.md')
