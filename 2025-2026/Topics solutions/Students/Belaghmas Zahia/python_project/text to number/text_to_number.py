class TextAnalyzer:
    """Advanced text analysis class"""
   
    def __init__(self):
        self.stats = {
            'letters': 0,
            'digits': 0,
            'spaces': 0,
            'symbols': 0,
            'total_length': 0,
            'words': 0,
            'unique_chars': 0
        }
   
    def analyze(self, text):
        """Analyze text and extract statistics"""
        self.stats = {
            'letters': 0,
            'digits': 0,
            'spaces': 0,
            'symbols': 0,
            'total_length': len(text)
        }
       
        for char in text:
            if char.isalpha():
                self.stats['letters'] += 1
            elif char.isdigit():
                self.stats['digits'] += 1
            elif char.isspace():
                self.stats['spaces'] += 1
            else:
                self.stats['symbols'] += 1
       
        # Advanced stats
        self.stats['words'] = len(text.split())
        self.stats['unique_chars'] = len(set(text))
       
        return self.stats
   
    def print_report(self, stats):
        """Display formatted analysis report"""
        print("" + "="*60)
        print("📊     TEXT ANALYSIS REPORT     📊")
        print("="*60)
        print(f"📏 Total Length:           {stats['total_length']}")
        print(f"🔤 Letters:                {stats['letters']}")
        print(f"🔢 Digits:                 {stats['digits']}")
        print(f"␣  Spaces:                 {stats['spaces']}")
        print(f"💎 Symbols:                {stats['symbols']}")
        print("-"*60)
        print(f"📖 Words:                  {stats['words']}")
        print(f"🎭 Unique Characters:      {stats['unique_chars']}")
        print("="*60)
       
        # Percentages
        total = stats['total_length']
        if total > 0:
            print("📈 PERCENTAGE BREAKDOWN:")
            print(f"   Letters:     {stats['letters']/total*100:.1f}%")
            print(f"   Digits:      {stats['digits']/total*100:.1f}%")
            print(f"   Spaces:      {stats['spaces']/total*100:.1f}%")
            print(f"   Symbols:     {stats['symbols']/total*100:.1f}%")
        print("="*60)
   
    def advanced_stats(self, text):
        """Display advanced analysis"""
        stats = self.analyze(text)
        self.print_report(stats)
       
        # Additional insights
        avg_word_length = sum(len(word) for word in text.split()) / stats['words'] if stats['words'] > 0 else 0
        print(f"INSIGHTS:")
        print(f"   Average word length: {avg_word_length:.1f} chars")
        print(f"   Character density:   {stats['unique_chars']}/{stats['total_length']}")

def main():
    """Main program loop"""
    print("🔍 Welcome to Text Analyzer - Advanced CLI Tool")
    print("=" * 65)
   
    analyzer = TextAnalyzer()
   
    while True:
        print("Enter text to analyze (or 'quit' to exit):")
        user_input = input(">>> ").strip()
       
        if user_input.lower() in ['quit', 'q', 'exit']:
            print("Thank you for using Text Analyzer!")
            print("   Developed for learning Python projects")
            break
       
        if not user_input:
            print("⚠️  Please enter valid text!")
            continue
       
        # Process the text
        analyzer.advanced_stats(user_input)
        print( "" + "-"*65)
if __name__ == "__main__":
    main()