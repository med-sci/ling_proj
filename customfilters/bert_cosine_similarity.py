import opusfilter
import torch

from typing import List, Dict, Iterable, Tuple
from sentence_transformers import SentenceTransformer, util


BERT_MODEL_NAME = 'bert-base-multilingual-cased'


class BERTCosineSimilarity(opusfilter.FilterABC):
    '''
    Retrieves 768-dim embeddings from pre-trained multilingual BERT model
    and filter by cosine similarity threshold.  
    '''

    def __init__(self, threshold: float=0.2, **kwargs):
        '''
        Args:
            threshold (float): a cosine similarity threshold  
        '''
        self.threshold = threshold
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model: SentenceTransformer = SentenceTransformer(BERT_MODEL_NAME)
        
        super().__init__(**kwargs)

    def get_representation(self, sentence: str) -> torch.Tensor:
        '''
        Args:
            sentence (str): a sentence from corpora 
        
        Returns: 
            torch.Tensor: 768-dim embeddings from pre-trained multilingual BERT model
        '''
        return self.model.encode(sentence, device=self.device)

    def get_score(self, sentences: List[str]) -> float:
        '''
        Compute cosine similarity between two vectors
        
        Args: 
            sentences (List): a sentences pair
        
        Returns:
            float: cosine similarity value
        '''
        representations = [self.get_representation(sentence) for sentence in sentences]
        return util.cos_sim(*representations).item()

    def score(self, pairs: Iterable[Tuple[str]]) -> float:
        '''
        Yields a score value for a corpora pair
        
        Args: 
            pairs (Iterable): an iterable of sentences pairs
        
        Returns:
            float: cosine similarity value
        '''
        for pair in pairs:
            yield self.get_score(pair)

    def accept(self, score) -> bool:
        '''
        Implements acceptance criteria
        
        Args:
            score (float): cosine similarity value
        
        Returns:
            bool: True if meet acceptance criteria

        '''
        return score > self.threshold 