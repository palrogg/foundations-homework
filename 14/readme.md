Very instructive exercise. I tried such a rough text analysis directly with NLTK two weeks ago: much more complicated, much worse result.

##Methods to remember:

`CountVectorizer()`: Convert a collection of text documents to a matrix of token counts

`TfidfVectorizer(use_idf=False)`: Convert a collection of raw documents to a matrix of TF-IDF features. Equivalent to CountVectorizer followed by TfidfTransformer.

`TfidfVectorizer(use_idf=True)` (default): Enable inverse-document-frequency reweighting.

`vectorizer.fit_transform()`: Learn the vocabulary dictionary and return term-document matrix.


###Find relevant text data:

```
X = vectorizer.fit_transform(speeches_df['content'])
TF_pd = pd.DataFrame(X.toarray(), columns=tfidf_vectorizer.get_feature_names())
china_trade = TF_pd.sort_values(by=['china', 'trade'], ascending=[0, 0])[['china', 'trade']].head(3)
```

###Cluster data:
```
X = vectorizer.fit_transform(speeches_df['content'])
number_of_clusters = 8
km = KMeans(n_clusters=number_of_clusters)
km.fit(X)

order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(number_of_clusters):
        top_five_words = [terms[ind] for ind in order_centroids[i, :10]]
        print("Cluster {}: {}".format(i, ' '.join(top_five_words)))
```
