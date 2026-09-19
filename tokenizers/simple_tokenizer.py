import re

class SimpleTokenizerV1:
    def __init__(self,vocab):   
        self.str_to_int = vocab
        self.int_to_str = {v: k for k, v in vocab.items()}

    def encode(self, text):
        # Simple whitespace tokenizer
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed =[
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int.get(token, self.str_to_int.get('<unk>')) for token in preprocessed]
        return ids
    
    def decode(self, tokens):
        # Join tokens with a space
        text = ' '.join([self.int_to_str.get(token, '<unk>') for token in tokens])
        text = re.sub(r'\s([,.?_!"()\'])', r'\1', text)  # Remove space before punctuation
        return text