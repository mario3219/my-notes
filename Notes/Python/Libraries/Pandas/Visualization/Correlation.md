```
from pandas import Series,DataFrame
coeff_df = DataFrame(data.columns.delete(0))
coeff_df.columns = ['Features']
coeff_df["Coefficient"] = pd.Series(model.coef_[0])
```