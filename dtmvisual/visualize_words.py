
import pandas as pd
import matplotlib.pyplot as plt

def DF(timespans, num_topics, model, num_words = 10):
    
    """
    :param timespans: number od timespans/periods
    :param num_topics: number of topics
    :param model: DTM trained model
    :param num_words: number of words to display for the topicid at the time period
    :return: Dataframe with corresponding weight for each top word in each topic of each period
    """
    topicId, period, weight, word = [], [], [], []
    for t in range(timespans):
        for s in range (num_topics):
            topics = model.show_topic(topicid=s, time=t, num_words=num_words)
            for i, (word_, w) in enumerate(topics):
                topicId.append(s)
                period.append(t)
                weight.append(w)
                word.append(word_)
    return pd.DataFrame(list(zip(topicId, period, weight, word)), columns = ['topicId', 'period', 'word', 'weight',])

def partitioning(df):
    
    """
    :param df: Dataframe with corresponding weight for each top word in each topic of each period
    :return: partition based on TopicID
    
    """
    
    d = {} # d[i] contains records for TopicID i
    for topic in list(df['topicId'].unique()): # for each topic
        d[topic] = df.loc[df['topicId'] == topic] # create dataframe with records
        print('Number of records for Topic %d = %d' %(topic, len(d[topic])))
    return d

def displayTopic(d, i):
    
    """
    function to display Word-Probability by period for topic i
    """
    s = d[i][['period', 'word', 'weight']]
    fig, ax = plt.subplots(figsize=(15,10))
    for key, grp in s.groupby(['word']):
        ax = grp.plot(ax=ax, kind='line', x='period', y='weight', fontsize=12, label=key, linewidth=3.0)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title = "Top keywords", fontsize='large', labelspacing=0.6, fancybox = False)
    plt.show()
        
def visualize_words(df, d):
    """
    function to visualize words evolution
    """
    
    for topic in list(df['topicId'].unique()):
        displayTopic(d, topic)
        print("\nResults for the topic: ", topic)


