# NLP_MorphologicalAnalysisAndWordGenerationFromFile
This script performs morphological analysis and generates word variations (like past tense, plural, etc.) based on text from a file.

This Python script reads a text from a file, tokenizes the words, lemmatizes them, and generates simple morphological variations (like past tense, present participle, plural, and noun forms). It is useful for basic morphological analysis and word generation in natural language processing tasks.

Steps:
1. Setup and Download: The script first ensures that the necessary NLTK data files (punkt for tokenization and wordnet for lemmatization) are downloaded.
2. Morphological Analysis and Word Generation Function:
    The function morphological_analysis_and_generation(text):
      Tokenizes the input text into individual words.
      Lemmatizes each word using NLTK's WordNetLemmatizer to find its base form (lemma).
      Generates morphological variations based on a few simple rules:
          Past Tense: Adds "ed" to the lemma (e.g., "jump" -> "jumped").
          Present Participle: Adds "ing" to the lemma (e.g., "run" -> "running").
          Plural: Adds "s" or "es" depending on whether the lemma ends with an "s" (e.g., "cat" -> "cats").
          Agent Noun: Adds "er" to the lemma to create an agent noun (e.g., "run" -> "runner").
3. User Input: The program prompts the user to input the file path from which the text will be read.
4. Processing the Text: The content of the file is read, and morphological analysis is performed on the words from the file.
Notes:
This script uses simple suffix-based rules for generating word variations, which may not cover all edge cases (e.g., irregular verbs like "go" -> "went").
The agent noun rule adds "er" to each lemma, but this may not always be correct (e.g., "sing" -> "singer" might be more accurate than "sing" -> "singer").
