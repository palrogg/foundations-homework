NB:

`mdata = df.groupby([lambda x: x.month]).size()`

or:

`mdata = df.groupby(by=df.index.month).size()`
