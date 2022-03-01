# %%

import pandas as pd
import numpy as np
from pathlib import Path

# fancy way to retrieve the csv file
main_path = Path(__file__).parent
csv_file = [str(x) for x in Path(main_path).glob("*.csv")][0]

# %% 

df = pd.read_csv(csv_file, delimiter=';', lineterminator='\n')

# %%
