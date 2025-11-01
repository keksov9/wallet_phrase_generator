import unittest
import sys
import os

# Добавляем путь к src
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from generator import SeedPhraseGenerator

class TestSeedPhraseGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = SeedPhraseGenerator()
    
    def test_generate_16_words(self):
        phrase = self.generator.generate_16_words()
        words = phrase.split()
        self.assertEqual(len(words), 16)
    
    def test_word_in_list(self):
        phrase = self.generator.generate_16_words()
        words = phrase.split()
        
        for word in words:
            self.assertIn(word, self.generator.word_list)

if __name__ == "__main__":
    unittest.main()