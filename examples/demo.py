import sys
import os

# Добавляем путь к src
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from generator import SeedPhraseGenerator

def demo():
    print("🎯 Демонстрация работы генератора")
    print()
    
    generator = SeedPhraseGenerator()
    
    # Генерация нескольких фраз
    for i in range(3):
        phrase = generator.generate_16_words()
        
        print(f"Фраза #{i+1}:")
        words = phrase.split()
        for j, word in enumerate(words, 1):
            print(f"  {j:2d}. {word}")
        print("-" * 50)

if __name__ == "__main__":
    demo()