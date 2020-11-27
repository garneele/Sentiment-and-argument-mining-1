1. Work on the [Twitter Climate Change](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/5QCCUU) corpus:
	1. figure out how to use the Twitter API to download tweets:
	2. after saving the tweets:
		- extract keywords?
		- train a binary classifier? -> for this step we will also need to download tweets that don't relate to climate change, so we can have a diversified dataset and create a binary climate/not-climate classifier
2. Topic modelling using Latent Dirchlet Allocation (LDA)
	- The idea is to extract a list of most important topics from each article (or maybe even on the corpus level?) with LDA and manually select the topics that seem to have to do with climate change. We could then turn these words into vectors(we can try both tf-idf or word embeddings) as well as turn the entire corpus into word vectors, and then by comparing the similarity of the sentences in the articles with the embeddings of the topics, we can select the sentences that contain words or phrases that are similar to the vectors of the topics we obtained by LDA 
