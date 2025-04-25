import re

class ArticleManager:
    # Prices based on number of pages , which can be changed from here later
    one_two_page_price = 30
    three_four_page_price = 60
    more_four_pages_price = 100
    def __init__(self, article_text):
        self.article_text = article_text
        self.pages = []
        self.paid_pages = 0
        self.words = 0
    
    # Function to split input text into pages
    def split_into_pages(self):
        words_per_line = 12
        lines_per_page = 20

        try:
            self.words = re.split(r'\s+', self.article_text.strip())
            # print(len(self.words))
        except:
            print("Error in splitting words")

        lines = []
        for i in range(0, len(lines), words_per_line):
            try:
                lines.append(' '.join(self.words[i:i + words_per_line]))
            except:
                print("Error in joining words")

        self.pages = []
        for i in range(0, len(lines), lines_per_page):
            try:
                self.pages.append('\n'.join(lines[i:i + lines_per_page]))
            except:
                print("Error in joining lines")

  
    # Function to caluclate payment based on number of pages
    def calculate_payment(self,price1,price2,price3):
        try:
            self.paid_pages = len(self.words) // 240
        except:
            print("Error in length of the pages")
        if self.paid_pages < 1:
            return 0
        elif 1 <= self.paid_pages <= 2:
            return price1
        elif 3 <= self.paid_pages <= 4:
            return price2
        elif self.paid_pages > 4:
            return price3
        else:
            return 0
        
    # Function to display pages
    def display_pages(self):
        payment = self.calculate_payment(self.one_two_page_price,self.three_four_page_price,self.more_four_pages_price)
        # print(f"Total Pages: {self.pages}")
        print(f"Paid Pages: {self.paid_pages or 0}")
        print(f"Payment Due: ${payment}")
        
        for index, page in enumerate(self.pages):
            print(f"\nPage {index + 1}:\n{page}\n")

    def process_article(self):
        self.split_into_pages()
        self.display_pages()
  
# Example usage
article_text = '''Replace with actual article text'''  # Replace with actual article text
article_manager = ArticleManager(article_text)
article_manager.process_article()