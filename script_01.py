from tokenizers.simple_tokenizer import SimpleTokenizerV1
from tokenizers.preprocessing import TextPreprocessor
from data.fetch_data import fetch_data


def main():
    vocab = {
        'Hello': 1,
        'world': 2,
        ',': 3,
        '!': 4,
        '<unk>': 0
    }
    
    tokenizer = SimpleTokenizerV1(vocab)
    
    text = "Hello, world!"
    encoded = tokenizer.encode(text)
    print(f"Encoded: {encoded}")
    
    decoded = tokenizer.decode(encoded)
    print(f"Decoded: {decoded}")
    
def process_text(text):
    preprocessor = TextPreprocessor(text)
    return preprocessor.tokens

if __name__ == "__main__":
    text = fetch_data()
    preprocessor = TextPreprocessor(text)
    print("*"*200)
    print(preprocessor.tokens[:50])
    
    tokenizer = SimpleTokenizerV1(preprocessor.vocab)
    
    text = "Hello, world! This is a test."
    encoded = tokenizer.encode(text)
    print(f"Encoded: {encoded}")
    
    decoded = tokenizer.decode(encoded)
    print(f"Decoded: {decoded}")
    
    print(list(preprocessor.vocab.items())[-5:])
    
    