import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

# Download the NLTK data files (only the first time you run this program)
nltk.download('punkt')
nltk.download('wordnet')

def morphological_analysis_and_generation(text):
    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Tokenize words from the input text
    word_tokens = word_tokenize(text)
    
    # Analyze each word and perform morphological analysis
    lemmatized_words = {}
    for word in word_tokens:
        lemma = lemmatizer.lemmatize(word)
        lemmatized_words[word] = lemma
    
    # Generate word variations based on morphological rules
    generated_words = {}
    for word, lemma in lemmatized_words.items():
        # Example variations: adding common suffixes or prefixes
        variations = {
            'past_tense': lemma + 'ed',  # Simple past form
            'present_participle': lemma + 'ing',  # Present participle
            'plural': lemma + 's' if lemma[-1] != 's' else lemma + 'es',  # Plural form
            'noun': lemma + 'er',  # Agent noun form (e.g., run -> runner)
        }
        generated_words[word] = variations
    
    return lemmatized_words, generated_words

if __name__ == "__main__":
    # Prompt the user to enter the path to the file
    file_path = input("Enter the path to the text file: ")
    
    # Read text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text_input = file.read()

    # Perform morphological analysis and word generation
    lemmatized_words, generated_words = morphological_analysis_and_generation(text_input)
    
    # Output the results
    print("\nLemmatized Words:")
    for word, lemma in lemmatized_words.items():
        print(f"{word} -> {lemma}")

    print("\nGenerated Word Variations:")
    for word, variations in generated_words.items():
        print(f"{word} -> {variations}")

# OUTPUT
# Enter the path to the text file: Textfile.txt

# Lemmatized Words:
# The -> The
# cat -> cat
# quickly -> quickly
# jumped -> jumped
# over -> over
# the -> the
# fence -> fence

# Generated Word Variations:
# The -> {'past_tense': 'Theed', 'present_participle': 'Theing', 'plural': 'Thes', 'noun': 'Theer'}
# cat -> {'past_tense': 'cated', 'present_participle': 'cating', 'plural': 'cats', 'noun': 'cater'}
# quickly -> {'past_tense': 'quicklyed', 'present_participle': 'quicklying', 'plural': 'quicklys', 'noun': 'quicklyer'}
# jumped -> {'past_tense': 'jumpeded', 'present_participle': 'jumpeding', 'plural': 'jumpeds', 'noun': 'jumpeder'}
# over -> {'past_tense': 'overed', 'present_participle': 'overing', 'plural': 'overs', 'noun': 'overer'}
# the -> {'past_tense': 'theed', 'present_participle': 'theing', 'plural': 'thes', 'noun': 'theer'}
# fence -> {'past_tense': 'fenceed', 'present_participle': 'fenceing', 'plural': 'fences', 'noun': 'fenceer'}
