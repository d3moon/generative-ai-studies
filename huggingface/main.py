from transformers import pipeline

generator = pipeline("text-generation", model="pierreguillou/gpt2-small-portuguese")  
# detalhe: é "pierreguillou" com DOIS "l"
text = "Um transformers é um grande modelo de linguagem natural"
result = generator(text, max_length=100, do_sample=True)

print(result[0]["generated_text"])
