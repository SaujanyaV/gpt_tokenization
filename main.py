# text from https://www.reedbeta.com/blog/programmers-intro-to-unicode/
text = "Ｕｎｉｃｏｄｅ! 🅤🅝🅘🅒🅞🅓🅔‽ 🇺‌🇳‌🇮‌🇨‌🇴‌🇩‌🇪! 😄 The very name strikes fear and awe into the hearts of programmers worldwide. We all know we ought to “support Unicode” in our software (whatever that means—like using wchar_t for all the strings, right?). But Unicode can be abstruse, and diving into the thousand-page Unicode Standard plus its dozens of supplementary annexes, reports, and notes can be more than a little intimidating. I don’t blame programmers for still finding the whole thing mysterious, even 30 years after Unicode’s inception."
tokens = text.encode("utf-8") # raw bytes
tokens = list(map(int, tokens)) # convert to a list of integers in range 0..255 for convenience
print(f"The text being encoded: \n\n {text} \n\n Length of text: {len(text)}")
print('--------------------------------------')
print(f"The encoded tokens: \n\n {tokens} \n\n Length of tokens: {len(tokens)}")
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