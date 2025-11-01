import secrets

class SeedPhraseGenerator:
    def __init__(self):
        # Упрощенный список слов BIP-39 (первые 50 для демо)
        self.word_list = [
            "abandon", "ability", "able", "about", "above", "absent", "absorb", 
            "abstract", "absurd", "abuse", "access", "accident", "account", 
            "accuse", "achieve", "acid", "acoustic", "acquire", "across", "act", 
            "action", "actor", "actress", "actual", "adapt", "add", "addict", 
            "address", "adjust", "admit", "adult", "advance", "advice", "aerobic", 
            "affair", "afford", "afraid", "again", "age", "agent", "agree", 
            "ahead", "aim", "air", "airport", "aisle", "alarm", "album", "alcohol"
        ]
    
    def generate_16_words(self):
        """Генерирует фразу из 16 случайных слов"""
        phrase_words = [
            secrets.choice(self.word_list) 
            for _ in range(16)
        ]
        return " ".join(phrase_words)