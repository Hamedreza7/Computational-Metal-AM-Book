"""Optional full run. This is slower because every example is launched separately."""
from pathlib import Path
import subprocess, sys, os
ROOT=Path(__file__).resolve().parents[1]
SCRIPTS=[p for p in ROOT.rglob('main.py') if 'expected_output' not in p.parts]
env=os.environ.copy(); env.update({'OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1','MPLBACKEND':'Agg'})
for p in sorted(SCRIPTS):
    print(f'--- {p.relative_to(ROOT)} ---', flush=True)
    subprocess.run([sys.executable,str(p)],cwd=ROOT,check=True,env=env)
print(f'Completed {len(SCRIPTS)} examples.')
