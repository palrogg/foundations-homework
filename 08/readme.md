What was problematic or confusing:

1) In both data sets:

* I had to understand the documentation in german, then to translate the columns in english

2) Stations and frequency:

* To use regular expressions, I had to type: `df[df['Station'].str.match('^A')]`

* I had to learn how to use a condition when creating a new column: `df['automat_ktu'].apply(automat)`

* I had to figure out how to avoid the error “A value is trying to be set on a copy of a slice from a DataFrame.”

3) Equipment for disabled people:

* Changing the graphs layout with the `gcf()` function (get current figure) is a bit confusing.

