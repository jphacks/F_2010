import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


adapter_path = 'sst-2'

model = AutoModelForSequenceClassification.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
tokenizer = AutoTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
model.load_adapter(adapter_path)


def predict(sentence):
    token_ids = tokenizer.convert_tokens_to_ids(tokenizer.tokenize(sentence))
    input_tensor = torch.tensor([token_ids])
    outputs = model(input_tensor, adapter_names=['sst-2'])
    result = torch.argmax(outputs[0]).item()

    return 'positive' if result == 1 else 'negative'


if __name__ == '__main__':
    result = predict('面白い')
    print(result)
