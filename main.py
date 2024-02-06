def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Calculates the Levenshtein distance between two strings.

    :param s1: The first input string.
    :param s2: The second input string.

    :return: The Levenshtein distance between the two strings.

    Example:
    >>> levenshtein_distance("kitten", "sitting")
    3

    Explanation:
    The function calculates the Levenshtein distance between the strings
    "kitten" and "sitting". The dynamic programming matrix for the given
    example looks like the following:

            s  i  t  t  i  n  g     (s2)
         ---------------------
        | 0  1  2  3  4  5  6
      k | 1  1  2  3  4  5  6
      i | 2  1  1  2  3  4  5
      t | 3  2  1  1  2  3  4
      t | 4  3  2  1  1  2  3
      e | 5  4  3  2  2  2  3
      n | 6  5  4  3  3  3  2
      (s1)

    The bottom-right cell value is 2, indicating that the Levenshtein distance
    is 2, and the necessary edits include adding the letter 'e' and deleting
    the letters 'g', 'n', and 'g'.
    """
    # Ensure s1 is the shorter string
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    # Initialize distances for the first row
    distances = range(len(s1) + 1)

    # Loop through each character in s2
    for index2, char2 in enumerate(s2):
        # Initialize the new distances with the current index2 value
        new_distances = [index2 + 1]

        # Loop through each character in s1
        for index1, char1 in enumerate(s1):
            # If characters are the same, no edit needed, take the diagonal
            # value
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                # If characters are different, find the minimum of three
                # possible edits
                new_distances.append(
                    1 + min(
                        (distances[index1],
                         distances[index1 + 1],
                         new_distances[-1])
                    )
                )

        # Update distances for the next row
        distances = new_distances

    # The final value in distances array is the Levenshtein distance
    return distances[-1]


def correct_typo(word_with_typo, word_list):
    """
    This method finds the closest word in the word_list to the word_with_typo
    using Levenshtein distance.
    :param word_with_typo: The word with typo.
    :param word_list: A list of words to compare with the word_with_typo.
    :return: The closest word
    """

    return sorted(
        word_list,
        key=lambda w: levenshtein_distance(word_with_typo, w)
    )[:10]


# read "words_bank.txt" and get the words in it
with open("words_bank.txt", "r", encoding='utf-8') as f:
    words = f.read().splitlines()

input_word = "appple"  # Intentional typo
corrected_word = correct_typo(input_word, words)
print(f"Original Word:\t{input_word},\n"
      f"Possible Words:\t{corrected_word}")
pass
