import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def document_influence_dim(num_topics, model, time_seq = []):
    
    """
    function to compute the document influence on a topic: http://users.umiacs.umd.edu/~jbg/nips_tm_workshop/30.pdf 
    :param num_topics: number of topics
    
    """
    
    doc, topicId, period, distributions=[], [], [], []
    for topic in range(num_topics):
        for t in range(len(time_seq)):
            for document in range(time_seq[t]):
                distribution = round(model.influences_time[t][document][topic], 4)
                period.append(t)
                doc.append(document)
                topicId.append(topic)
                distributions.append(distribution)
    return pd.DataFrame(list(zip(doc, topicId, period, distributions)), columns=['document','topicId', 'period','distribution'])



def topic_distribution(num_topics, model, time_seq = []):
    
    """
    function to compute the topical distribution in a document
    :param num_topics: number of topics
    
    """
    doc, topicId, distributions=[], [], []
    df_dim = document_influence_dim(num_topics = num_topics, model = model, time_seq = time_seq)
    for document in range(0, sum(time_seq)):
        for topic in range(0, num_topics):
            distribution = round(model.gamma_[document][topic], 4)
            doc.append(document)
            topicId.append(topic)
            distributions.append(distribution)
    return pd.DataFrame(list(zip(doc, topicId, distributions, df_dim.period)), columns=['document','topicId', 'distribution', 'period'])



def visualize_topics(df):
    
    """
    function to vizualise mean topic distribution over defined periods
    :param num_topics: number of topics
    
    """
    fig, ax = plt.subplots(figsize=(30,10))
    df.groupby(['period', 'topicId'], sort=False).mean()['distribution'].unstack().plot(ax=ax,grid=True, linewidth =3.0, sharex=True)
    plt.ylabel("Topic Distribution", fontsize=16) 
    plt.xlabel("Period", fontsize=16) 
    plt.title("Topic evolution")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title = "Topics", fontsize='large', labelspacing=0.6, fancybox = True)

