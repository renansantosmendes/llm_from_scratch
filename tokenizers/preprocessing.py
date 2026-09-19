import re

class TextPreprocessor:
    def __init__(self, text):
        self.text = text
        self.tokens = self.preprocess()
        self.vocab = self.build_vocab(self.tokens)

    def preprocess(self):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', self.text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        return preprocessed

    def build_vocab(self, tokens):
        vocab = {}
        all_tokens = sorted(list(set(tokens)))  # Sort tokens to ensure consistent ordering
        all_tokens.extend(['<|endoftext|>','<|unk|>'])
        vocab = {token: idx for idx, token in enumerate(all_tokens)}
        return vocab