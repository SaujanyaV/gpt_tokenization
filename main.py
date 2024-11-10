# text from https://www.reedbeta.com/blog/programmers-intro-to-unicode/
text = "Ｕｎｉｃｏｄｅ! 🅤🅝🅘🅒🅞🅓🅔‽ 🇺‌🇳‌🇮‌🇨‌🇴‌🇩‌🇪! 😄 The very name strikes fear and awe into the hearts of programmers worldwide. We all know we ought to “support Unicode” in our software (whatever that means—like using wchar_t for all the strings, right?). But Unicode can be abstruse, and diving into the thousand-page Unicode Standard plus its dozens of supplementary annexes, reports, and notes can be more than a little intimidating. I don’t blame programmers for still finding the whole thing mysterious, even 30 years after Unicode’s inception."
tokens = text.encode("utf-8") # raw bytes
tokens = list(map(int, tokens)) # convert to a list of integers in range 0..255 for convenience
print(f"The text being encoded: \n\n {text} \n\n Length of text: {len(text)}")
print('--------------------------------------')
print(f"The encoded tokens: \n\n {tokens[:10]}... \n\n Length of tokens: {len(tokens)}")
print('--------------------------------------')

"""
Now we need to count all the most frequently occuring pairs in the tokens list.
Use of zip -> we will use zip to create pairs of consequential numbers. Zip stops iterating when reaching end of smallest sized list
"""
def get_freq(ids: list):
    freq_map = {}

    for pair in zip(ids, ids[1:]):
        freq_map[pair] = freq_map.get(pair, 0) + 1
    return freq_map

frequencies = get_freq(tokens)
# print(sorted(((v,k) for k, v in frequencies.items()), reverse=True))
top_pair = max(frequencies, key=frequencies.get)
print(f"Pair with maximum occurences: {top_pair}")

"""
Now we need to replace all ocurrences of the top_pair with a new token id which goes out of utf-8 starting with 256
"""
def replace_occurences(ids, pair, token_id):
    new_ids = []

    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and ids[i]==pair[0] and ids[i+1]==pair[1]:
            new_ids.append(token_id)
            i+=2
        else:
            new_ids.append(ids[i])
            i+=1
    return new_ids

print(replace_occurences([1,1,2,3,1,2,2], (1,2), 99))