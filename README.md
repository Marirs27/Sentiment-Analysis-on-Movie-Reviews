
## Dataset
**Large Movie Review Dataset:**
This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. We provide a set of 25,000 highly polar movie reviews for training, and 25,000 for testing. There is additional unlabeled data for use as well. Raw text and already processed bag of words formats are provided. <br>
<a href = 'https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz'> Click to download the dataset </a> <br>

## Tools and Libraries

<ul>
  <li>NLTK (Words tokenizer, stopwords and WordNetLemmatizer)</li>
  <li>Seaborn and Matplotlib</li>
  <li>Gensim libraries</li>
  <li>Sentence Transformer and sklearn</li>
  <li>Numpy and Pandas</li>
</ul>

## Steps involved in the project
### 1. Pre-processing
<ul>
  <li>Remove stop-words with NLTK</li>
  <li>Remove number from text with regular expression function</li>
  <li>Lower the text and remove words lower than 3 letters</li>
  <li>Bring the text back to it's base word via lemmatization</li>
</ul>

### 2. EDA
<ul>
  <li>Did some visualization to understand the common words in the review</li>
  <li>Meta Analysis of the data</li>
</ul>

### 3. Survey of various ML models for sentiment analysis
Model  			  | Accuracy (%)
--------------------------| --------
Logistic Regression       | 85
KNN		          | 66 (K=11)
SVM		          | 76
Naive Bayes	          | 83


Logistic regression is a powerful machine learning algorithm that utilizes a sigmoid function and works best on binary classification problems.
It is a very powerful algorithm, even for very complex problems it may do a good job.



