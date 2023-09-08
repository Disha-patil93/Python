import pandas as pd
d1=[[1,2,3,4],[4,5,67,7]]
d2=[[34,45,56,43],[34,67,78.6,78,89]]
d3=[["satara","sangli"],["pune","thane","barshi"]]
data={'first':d1,'second':d2,'city':d3}
data2={'fram1':d1,'frame':d3}
d=pd.DataFrame(data)
print(d)
d2=pd.DataFrame(data2)
print(d2)