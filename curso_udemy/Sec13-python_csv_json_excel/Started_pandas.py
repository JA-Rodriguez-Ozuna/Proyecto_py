'''
In [1]: import pandas

In [2]: df1 = pandas.DataFrame([[2,4,6], [10,20,30]])

In [3]: df1
Out[3]: 
    0   1   2
0   2   4   6
1  10  20  30

In [4]: df1 = pandas.DataFrame([[2,4,6], [10,20,30]],columns=["Price","Age","Value"])  
      ⋮ 

In [5]: df1
Out[5]: 
   Price  Age  Value
0      2    4      6
1     10   20     30

In [6]: df1 = pandas.DataFrame([[2,4,6], [10,20,30]],columns=["Price","Age","Value"],i 
      ⋮ ndex=["First","Second"])

In [7]: df1
Out[7]: 
        Price  Age  Value
First       2    4      6
Second     10   20     30

In [8]: df2 = pandas.DataFrame([{"Name":"John"},{"Name":"Jack"}])

In [9]: df2
Out[9]: 
   Name
0  John
1  Jack

In [10]: df2 = pandas.DataFrame([{"Name":"John","Surname":"Johns"},{"Name":"Jack"}])   

In [11]: df2
Out[11]:       
   Name Surname
0  John   Johns
1  Jack     NaN

In [12]: 

In [13]: df1.mean()
Out[13]: 
Price     6.0
Age      12.0
Value    18.0
dtype: float64

In [14]: df1.mean().mean()
Out[14]: np.float64(12.0)

In [15]: type(df1.mean())
Out[15]: pandas.core.series.Series

In [16]: df1
Out[16]: 
        Price  Age  Value
First       2    4      6
Second     10   20     30

In [17]: df1.Price
Out[17]: 
First      2
Second    10
Name: Price, dtype: int64

In [18]: type(df1.mean())
Out[18]: pandas.core.series.Series

In [19]: df1.Price.mean()
Out[19]: np.float64(6.0)

In [20]: df1.Price.max()
Out[20]: np.int64(10)
'''