from importlib.metadata import version
import tiktoken

print(version("tiktoken"))


tokenizer = tiktoken.get_encoding("gpt2")
text = "Hello, world! <|endoftext|> This is a test with someunknownPlace."
integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(f"Encoded integers: {integers}")
strings = tokenizer.decode(integers)
print(f"Decoded string: {strings}")