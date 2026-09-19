from tokenizers.simple_tokenizer import SimpleTokenizerV1

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
    
if __name__ == "__main__":
    main()