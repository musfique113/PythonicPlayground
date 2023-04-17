import imp
from math import fabs
from msilib.schema import tables
import pandas as pd
import numpy as np


table1 = {
    'Name': ['Xavier','Don','Rfi','Asd','Cixna'], 'Id':[14,15,48,98,2], 'Username':['xd22','dg23','rf1','as33','cizzzx5']
}
lab = ['a','b','c','d','e']
tab1=pd.DataFrame(table1, index=lab)

print(tab1.info)
exit()