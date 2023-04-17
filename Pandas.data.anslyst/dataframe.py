import pandas as pd
table3 = {'Name': ['Xyz','abc','drf','xdr'] , 'ID': [193002154,159785412,123665897,145895157]}
tab3=pd.DataFrame(table3)
print(tab3.info)


table4 = {'FName': ['Mahfujur','Fahad','Jubyer','Shoeb','Sanim'] , 'LName': ['Musfique','Islam','Rafsun','Sikder','Koy'] , 'ID': [193002154,193002039,193002070,193002041,193002037] , 'NoOfGF': [0,10,2,22,69]}
tab4=pd.DataFrame(table4)
print(tab4)

