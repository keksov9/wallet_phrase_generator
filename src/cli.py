from generator import SeedPhraseGenerator

def main():
    generator = SeedPhraseGenerator()
    phrase = generator.generate_16_words()
    
    print("🚀 Сгенерирована мнемоническая фраза (16 слов):")
    print("-" * 40)
    
    words = phrase.split()
    for i, word in enumerate(words, 1):
        print(f"{i:2d}. {word}")
    
    print("-" * 40)
    print("⚠️  Сохраните в безопасном месте!")

if __name__ == "__main__":
    main()