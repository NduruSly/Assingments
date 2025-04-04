"""
Catholic University of Zimbabwe AI Chatbot
Author: AI Tutor
Date: [Date]
Description: NLP-powered chatbot for student inquiries using TF-IDF and cosine similarity
"""

# Import required libraries
import random
import string
import nltk
import ssl
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ========================
# SSL CONTEXT CONFIGURATION
# ========================
# Fix SSL certificate issues for NLTK downloads
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# =====================
# NLTK RESOURCE SETUP
# =====================
# Download required NLTK datasets quietly
nltk.download('punkt', quiet=True)  # For tokenization
nltk.download('stopwords', quiet=True)  # For stopword list


# ======================
# CHATBOT CLASS DEFINITION
# ======================
class CUZChatbot:
    def __init__(self):
        """
        Initialize chatbot with:
        - Knowledge base of questions/answers
        - NLP processing components
        - Trained similarity model
        """

        # ====================
        # KNOWLEDGE BASE SETUP
        # ====================
        self.knowledge_base = [
            # Greeting intent
            {
                "tag": "greeting",
                "patterns": ["hello", "hi", "hey", "good day"],
                "responses": ["Hello! Welcome to Catholic University of Zimbabwe. How can I assist you today?"]
            },

            # Short courses intent
            {
                "tag": "short_courses",
                "patterns": ["short courses", "certificate programs", "professional development courses"],
                "responses": [
                    "We offer short courses in:\n"
                    "- Computer Skills\n- Project Management\n- Accounting Basics\n- Theology Foundations\n"
                    "Duration: 1-3 months\nFees: $50-$300"
                ]
            },

            # Diploma programs intent
            {
                "tag": "diploma",
                "patterns": ["diploma programs", "diploma courses", "undergraduate diplomas"],
                "responses": [
                    "Diploma programs (2 years):\n"
                    "- Diploma in Theology\n- Diploma in Education\n"
                    "- Diploma in Business Management\n- Diploma in Information Technology"
                ]
            },

            # Add other intents here...
        ]

        # =====================
        # NLP INITIALIZATION
        # =====================
        self.ps = PorterStemmer()  # For word stemming
        self.stop_words = set(stopwords.words('english'))  # English stopwords
        self.vectorizer = TfidfVectorizer()  # TF-IDF vectorizer
        self._train_model()  # Train similarity model

    def _train_model(self):
        """
        Train the TF-IDF model by:
        1. Processing all patterns from knowledge base
        2. Creating TF-IDF vectors
        3. Storing tags for response matching
        """
        documents = []  # Store processed patterns
        self.tags = []  # Store corresponding tags

        # Process each intent in knowledge base
        for intent in self.knowledge_base:
            for pattern in intent['patterns']:
                # Clean and preprocess text
                processed_text = self._preprocess(pattern)
                documents.append(processed_text)
                self.tags.append(intent['tag'])

        # Create TF-IDF matrix from all patterns
        self.tfidf_matrix = self.vectorizer.fit_transform(documents)

    def _preprocess(self, text):
        """
        Clean and preprocess text through:
        1. Lowercasing
        2. Punctuation removal
        3. Tokenization
        4. Stopword removal
        5. Stemming
        """
        # Convert to lowercase and remove punctuation
        text = text.lower().translate(str.maketrans('', '', string.punctuation))

        # Split into individual words
        tokens = word_tokenize(text)

        # Remove stopwords and stem remaining words
        processed_tokens = [
            self.ps.stem(word)
            for word in tokens
            if word not in self.stop_words
        ]

        return ' '.join(processed_tokens)

    def get_response(self, user_input):
        """
        Process user input and return appropriate response:
        1. Preprocess input
        2. Convert to TF-IDF vector
        3. Calculate similarity with known patterns
        4. Find best matching intent
        5. Return random response from matched intent
        """
        try:
            # Clean user input
            processed_input = self._preprocess(user_input)

            # Convert to TF-IDF vector
            input_vector = self.vectorizer.transform([processed_input])

            # Calculate similarity scores
            similarity_scores = cosine_similarity(input_vector, self.tfidf_matrix)

            # Find best match index
            best_match_index = similarity_scores.argmax()
            highest_score = similarity_scores[0, best_match_index]

            # Check confidence threshold
            if highest_score > 0.3:
                # Find corresponding intent
                matched_tag = self.tags[best_match_index]

                # Return random response from matched intent
                for intent in self.knowledge_base:
                    if intent['tag'] == matched_tag:
                        return random.choice(intent['responses'])

            # Default response for low confidence
            return "For more details, visit our website: https://www.cuz.ac.zw"

        except Exception as e:
            return f"Error processing request: {str(e)}"


# ================
# MAIN APPLICATION
# ================
def main():
    # Initialize chatbot
    bot = CUZChatbot()

    # Display welcome message
    print("\nCatholic University of Zimbabwe Virtual Assistant")
    print("Type 'quit' to exit\n")

    # Conversation loop
    while True:
        try:
            # Get user input
            user_input = input("You: ")

            # Exit condition
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Bot:", random.choice(bot.knowledge_base[-1]['responses']))
                break

            # Get and display response
            response = bot.get_response(user_input)
            print("Bot:", response)

        except KeyboardInterrupt:
            print("\nSession ended")
            break


if __name__ == "__main__":
    # Start chatbot application
    main()
