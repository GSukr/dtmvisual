### dtmvisual
Package for Dynamic Topic Modeling training and visualization 

### Requirements
Currently, this package requires Python 3.4+ and the following dependencies:

* 'gensim==3.4.0',
* 'seaborn==0.8.1', 
* 'matplotlib==2.0.2'

We highly recommend you to clean and preprocess the collection before using it. We run the Dynamic topic modelling on the collection of abstracts from the [SIOE conference](https://www.sioe.org/conference/2019) from 1998 to 2018. We have 3225 documents. We use the following code for preprocessing [code](https://github.com/chaves/sioeTopics/blob/master/GetCleanCorpus.ipynb). 

### The following steps help install and use dtmvisual:

1. Download dtmvisual repository
2. Run in the terminal
```
$ cd Downloads
$ cd dtmvisual-master
$ python setup.py install
```
3. Import dtmvisual package into a Python environment:

```
import dtmvisual
```
You can use the package for the following purposes:
* Training the model:
1. Please download the [dtm](https://github.com/magsilva/dtm/tree/master/bin) binaries for your OS version and use it in the code as:

```
dtm_path = "/path/to/dtm/binary"
```
2. Divide your collection of texts on time slices with desired granularity. For instance, the distribution of 3225 documents per 21 years (1998-2018) in our dataset equals the following list:
```
time_seq = [50, 87, 90, 106, 93, 71, 176, 157, 175, 176, 111, 217, 114, 175, 152, 238, 158, 195, 254, 240, 191]
```
3. Transform your collection of documents to list of tokens. Then convert the list to the bag-of-words format:
```
sentences = docs_to_list(self.sentences)
corpus = corpus_dtm(sentences)
```
4. Train the model:
```
model = dtm_model(dtm_path, corpus, time_seq, num_topics=8,
                 id2word=corpus.dictionary, alpha=0.01) 
```
### Words evolution

5. Create a dataframe with the columns ['topicId', 'period', 'word', 'weight']:
```
df = visualize_words.DF(number_of_timespans, number_of_topics, model)
```
6. Ensure the words partition based on TopicID:
```
d = visualize_words.partitioning(df)
```
7. Visualize the words evolution:
```
visualize_words.visualize_words(df, d)
```
With our dataset we got the following words evolution:

<img src=https://github.com/GSukr/dtmvisual/blob/master/results/topics/topic0.png width=450>

See more in: [the folder](https://github.com/GSukr/dtmvisual/tree/master/results/topics)

### Topics evolution

8. Create the dataframe with the topical distribution in a document:
```
df = VisualizeTopics.topic_distribution(number_of_topics, model, time_seq)
```
9. Visualize the topics evolution:
```
VisualizeTopics.visualize_topics(df)
```
With our dataset we got the following words evolution:
![topics](https://github.com/GSukr/dtmvisual/blob/master/results/topic_distribution.png)

Please note that we smoothed the lines with moving average for topic distribution and added the topic titles based on the expert knowledge after analysis of the top words for each topic. If you run the code your topics titles will correspond to the topic ID (e.g. Topic 1). You can adjust your Dataframe before running 'VisualizeTopics.visualize_topics(Dataframe)' to change the topic names and apply moving averdage. 

Moreover, you save and then download your DTM model using:
```
save_model(model, output_path, output_name)
model = load_saved_model(output_path, output_name)
```
To print the words for a timeslice for a topic use:
```
print_all_topics(model, topicid = None, time = None, num_words=10)
```
The results with the SIOE data has been presented at the SIOE 2019 conference: [abstract](https://papers.sioe.org/paper/2466.html)
