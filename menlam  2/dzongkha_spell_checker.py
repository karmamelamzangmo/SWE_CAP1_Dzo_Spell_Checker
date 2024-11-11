import re

def spell_checker(text, dictionary):
    results = []
    lines = text.splitlines()  # Split text by lines
    for line_num, line in enumerate(lines, start=1):
        words = re.findall(r'\b\w+\b', line)  # Extract words from each line
        for word_pos, word in enumerate(words, start=1):
            if word not in dictionary:
                results.append({
                    "line": line_num,
                    "position": word_pos,
                    "incorrect_word": word
                })
    return results

# Sample input text in Tibetan (for demonstration)
text = """༉ རྒྱལ་ཡོངས་ རོ་ཁྱིའི ་གྱངས་ཁ་ ཚད་འཛིན ་གྱི་ ལས་ རིམ་ དང་ འབྲེལ་ ཏེ་ རྒྱལ་ཁབ་ ནང་ ...
འགོ་དཔོན་ུ་ གིས་ སླབ་ མི་ ནང་ ཞིབ་འཇུག་ དེ་ལས་ བརྟེན་ཏེ་ བདུན་ཕྲག་ ༢ ཀྱི་ རིང་ ལུ་ འགོ་ ...
ལས་རིམ་འདི་གི་ཆ་ཤས་ཅིག་སྦེ་ དུས་ཅི་ སྤྱི་ཟླ་༡༠པའི་ནང་ ཐིམ་ཕུག་ལུ་ ...
"""

# Sample dictionary of correct words (replace with a comprehensive Tibetan dictionary as needed)
dictionary = {"རྒྱལ་ཡོངས་", "རོ་ཁྱིའི", "གྱངས་ཁ་", "ལས་", "རིམ་", "དང་", "རྒྱལ་ཁབ་", "ནང་", ... }

# Run the spell checker
misspelled_words = spell_checker(text, dictionary)

# Display the results
for entry in misspelled_words:
    print(f"Line {entry['line']}, Position {entry['position']}: {entry['incorrect_word']}")
