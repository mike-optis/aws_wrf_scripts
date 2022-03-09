import os
import subprocess
import numpy as np

for n in np.arange(3):
    if n==0:
        cmd_out = ['sbatch', '/projects/oswwra/scripts/bash/test_slurm_dependency.sh']
    else:
        cmd_out = ['sbatch', '--dependency=afterok:%s' % job_id, '/projects/oswwra/scripts/bash/test_slurm_dependency.sh']
    print(cmd_out)
    out = subprocess.Popen(cmd_out,
                       stdout=subprocess.PIPE,
                       stderr = subprocess.STDOUT)

    stdout, stderr = out.communicate()
    job_id = stdout[-8:-1]
    print(stdout, 'x', job_id, 'x')
