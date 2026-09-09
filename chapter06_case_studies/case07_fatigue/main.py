from pathlib import Path
import pandas as pd
SA=220.; SME=240.; SE=450.; SUT=1100.; SE_EFF=350.
def screen(se):
    ig=SA/se+SME/SUT; return ig,1-ig
b=screen(SE); c=screen(SE_EFF); out=Path(__file__).parent/'expected_output'; out.mkdir(exist_ok=True); pd.DataFrame({'model':['baseline','AM-corrected'],'Se_MPa':[SE,SE_EFF],'Goodman_index':[b[0],c[0]],'margin':[b[1],c[1]],'pass':[b[1]>0,c[1]>0]}).to_csv(out/'fatigue_screening.csv',index=False)
print(f'Baseline: I_G={b[0]:.3f}, M={b[1]:.3f}'); print(f'AM-corrected: I_G={c[0]:.3f}, M={c[1]:.3f}')
