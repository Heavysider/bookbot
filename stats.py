def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_each_character(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
          char = char.lower()
          if char in char_count:
              char_count[char] += 1
          else:
              char_count[char] = 1
    return char_count

def sorted_characters_counts(char_counts):
    sorted_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts
