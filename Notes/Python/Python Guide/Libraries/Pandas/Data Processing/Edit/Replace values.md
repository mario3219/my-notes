```
#Replaces 0s with NA
X[c]=X[c].replace(0,pd.NA)

% Using dictionaries
label_dict = {'nv': 0,'mel': 1,'bkl': 2, 'bcc': 3, 'akiec': 4,'vasc': 5,'df': 6 }

# Recode labels in dataframe to be numbers
skin_df['labels'] = skin_df['dx'].map(label_dict)       % dx is a column
```