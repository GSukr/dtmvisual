from gensim.corpora.textcorpus import TextCorpus


class DTMcorpus(TextCorpus):

    def get_texts(self):
        return self.input

    def __len__(self):
        return len(self.input)


def docs_to_list(documents):
    
    """converting documents to list"""
    
    texts = [] 
    for doc in documents:
        texts.append(doc.split())
    print (("The collection of documents contains {} documents").format(len(texts)))
    return texts

def corpus_dtm(texts):
    
    """converting corpora in BoW format"""
    
    try:
        corpora = DTMcorpus(texts)
        print ("DTMcorpus constructed")
    
    except Exception as e:
        print ('Input data must be a list of tokens. Use gensim_corpus.docs_to_list(documents)', e)
    
    return corpora

