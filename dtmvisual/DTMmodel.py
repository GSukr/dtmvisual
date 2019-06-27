
from gensim.models.wrappers.dtmmodel import DtmModel
import pickle
import pprint


def dtm_model(dtm_path, corpus=None, time_seq = None, num_topics=10,
                 id2word = None, alpha=0.01, rng_seed=0, model='fixed'):
    
    """
    :param dtm_path: path to dtm wrapper, see: https://github.com/blei-lab/dtm
    :param corpus: documents in bag-of-words format
    :param time_seq: pre-defined timestamps
    :param num_topics: number of topics
    :param id2word: mapping between tokens ids and words from corpus
    :param alpha: hyperparameter of the Dirichlet distribution that affects the document-topics sparsity
    :param id2word: mapping between tokens ids and words from corpus
    :param rng_seed: random seed
    :param model: "fixed" if document influence needed, 'dtm' otherwise
    :return: dtm model trained with the available corpus
    """

    print ("initializing the model...")
    model = DtmModel(dtm_path=dtm_path, corpus=corpus, time_slices = time_seq, num_topics=num_topics,
                 id2word = id2word, alpha=alpha, rng_seed=rng_seed, model='fixed')
    print('DTM model loaded')
    return model



def topics(model, topicid=0, time=0, num_words=10):
    
    """
    :param model: dtm_model
    :param topicid: number of topic
    :param time: number of time period
    :param num_topics: number of words to display for the topicid at the time period
    :param formatted: return the topics as a list of strings if True, otherwise as lists of (weight, word) pairs
    :return: top num_words for the certain topicid at the time period
    """
    topic = model.show_topic(topicid=topicid, time=time, num_words=num_words)
    return topic


def print_all_topics(model, topicid = None, time = None, num_words=10):
    
    """ function to output top words with pprint 
    :param model: dtm_model
    :param topicid: number of topic
    :param time: number of time period
    :param num_topics: number of words to display for the topicid at the time period
    """
    
    pp = pprint.PrettyPrinter(indent=4)
    for topic in range(topicid):
        for time in range(time):
            pp.pprint(model.show_topic(topicid, time, num_words))


def save_model(model, path, output_name):
    
    """
    function to save model in pickle format
    :param model: dtm_model
    :param path: str, path with output folder
    :param output_name: output file name
    """
    
    pickle.dump(model, open(path+"{}.pickle".format(output_name), 'wb'))

    print ("Model saved as '{}.pickle'".format(output_name))


def load_saved_model(path, output_name):
    
    """
    :param path: str, path with output folder
    :param output_name: model file name 
    :return: saved dtm model
    """
    
    with (open(path+"{}.pickle".format(output_name), "rb")) as f:
        model = pickle.load(f)
    return model



