```
feature_df = DataFrame(data.columns.delete(0))
feature_df.columns = ['Features']
feature_df["Feature Importance"] = pd.Series(model.feature_importances_)
```