

input_text = input("Text: ")

text = input_text.split()

text_counter_dict = {}
for word in text:
    text_counter_dict[word] = text_counter_dict.get(word, 0) + 1

text = list(text_counter_dict.keys())
text.sort()
max_length = max(len(word) for word in text)

for word in text:
    print("{:{}} : {}".format(word, max_length, text_counter_dict[word]))
