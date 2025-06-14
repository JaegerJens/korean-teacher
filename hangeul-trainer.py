import random


def hangeul_quiz():
    """
    A program to quiz the user on basic Hangeul consonants and vowels and their sounds.
    """
    # Define basic Hangeul characters (consonants and vowels) and their common sounds
    # Note: This uses a common romanization system (like Revised Romanization)
    # Sounds can be slightly different depending on context, but these are basic initial/alone sounds.
    # 'ㅇ' is silent at the beginning of a syllable.
    hangeul_chars = {
        # Basic Consonants
        'ㄱ': 'g',  # Can be 'k' at the end
        'ㄴ': 'n',
        'ㄷ': 'd',  # Can be 't' at the end
        'ㄹ': 'r',  # Often 'r' initially, 'l' at the end or before certain letters
        'ㅁ': 'm',
        'ㅂ': 'b',  # Can be 'p' at the end
        'ㅅ': 's',  # Can be 'sh' before 'i' or 'y' vowels, 't' at the end
        'ㅇ': 'silent',  # Silent at the beginning of a syllable, 'ng' at the end
        'ㅈ': 'j',  # Can be 't' at the end
        'ㅊ': 'ch',  # Can be 't' at the end
        'ㅋ': 'k',
        'ㅌ': 't',
        'ㅍ': 'p',
        'ㅎ': 'h',  # Can be 't' at the end or silent depending on context

        # Basic Vowels
        'ㅏ': 'a',
        'ㅑ': 'ya',
        'ㅓ': 'eo',  # The 'o' sound in 'song' or 'bought'
        'ㅕ': 'yeo',
        'ㅗ': 'o',  # The 'o' sound in 'go'
        'ㅛ': 'yo',
        'ㅜ': 'u',  # The 'oo' sound in 'moon'
        'ㅠ': 'yu',
        # A short, unrounded vowel sound (like the 'i' in 'kin' in some dialects, or imagine saying 'uh' but with lips unrounded and tongue flat)
        'ㅡ': 'eu',
        'ㅣ': 'i',  # The 'ee' sound in 'see'

        # Compound Vowels (Diphthongs)
        'ㅐ': 'ae',  # Sound like the 'e' in 'bed'
        'ㅒ': 'yae',
        # Sound like the 'e' in 'bed' (historically distinct, but often pronounced the same as ㅐ now)
        'ㅔ': 'e',
        'ㅖ': 'ye',
        'ㅘ': 'wa',  # 'o' + 'a'
        'ㅙ': 'wae',  # 'o' + 'ae' (often pronounced like 'we')
        # 'o' + 'i' (often pronounced like 'we' or 'oe' in French 'deux')
        'ㅚ': 'oe',
        'ㅝ': 'wo',  # 'u' + 'eo'
        'ㅞ': 'we',  # 'u' + 'e' (often pronounced like 'we')
        'ㅟ': 'wi',  # 'u' + 'i' (often pronounced like 'wi' or French 'ui')
        # 'eu' + 'i' (can vary in pronunciation depending on position, often 'i' or 'e' in certain contexts)
        'ㅢ': 'ui'

        # Optional: Add Tense Consonants if you want more challenge later
        # 'ㄲ': 'kk',
        # 'ㄸ': 'tt',
        # 'ㅃ': 'pp',
        # 'ㅆ': 'ss', # Can be 't' at the end
        # 'ㅉ': 'jj'
    }

    print("Welcome to the Hangeul Character Quiz!")
    print("I will show you a Hangeul consonant or vowel. Tell me its basic sound.")
    print("For 'ㅇ' at the beginning of a syllable, the sound is 'silent'.")
    print("Note: Some sounds have specific pronunciations (like 'eo' and 'eu').")
    print("-" * 30)

    # Get the characters (keys) and shuffle them
    chars_to_quiz = list(hangeul_chars.keys())
    random.shuffle(chars_to_quiz)

    score = 0
    total_chars = len(chars_to_quiz)

    for char in chars_to_quiz:
        correct_sound = hangeul_chars[char]

        # Display the character and ask for the sound
        print(f"\nWhat is the basic sound of this Hangeul character?")
        print(f"Character: {char}")

        # Get input, remove whitespace, make lowercase
        user_input = input("Your answer: ").strip().lower()

        # Check if the input is correct
        if user_input == correct_sound:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct sound is: {correct_sound}")

    print("-" * 30)
    print("Quiz finished!")
    print(f"Your final score: {score} out of {total_chars}")


# Run the quiz
if __name__ == "__main__":
    hangeul_quiz()
