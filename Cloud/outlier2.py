import re

class ArticleManager:
    def __init__(self, article_text, options=None):
        if options is None:
            options = {}
        
        self.article_text = article_text
        self.pages = []
        self.words = []
        self.options = {
            'words_per_line': options['words_per_line'] or 12 if 'words_per_line' in options else 12,
            'lines_per_page': options['lines_per_page'] or 20 if 'lines_per_page' in options else 20,
            # 'payment_structure': options.get('payment_structure', {
            #     1: 30,
            #     2: 30,
            #     3: 60,
            #     4: 60,
            #     'default': 100,
            # })
            'payment_structure': options.get('payment_structure', {
                1: 30,
                2: 30,
                3: 60,
                4: 60,
                'default': 100,
            })
        }

    def split_into_pages(self):
        words_per_line = self.options['words_per_line']
        lines_per_page = self.options['lines_per_page']

        # self.words = re.split(' ', self.article_text.strip())
        self.words = re.split(r'\s+', self.article_text.strip())
        # total_pages = -(-len(self.words) // (words_per_line * lines_per_page))  # equivalent to math.ceil

        # for i in range(total_pages + 1):
        #     page_words = self.words[i * words_per_line * lines_per_page:(i + 1) * words_per_line * lines_per_page]
        #     page_lines = []

        #     # Split the page into lines
        #     for j in range(0, len(page_words), words_per_line):
        #         page_lines.append(' '.join(page_words[j:j + words_per_line]))

        #     # Join the lines into a single string
        #     page = '\n'.join(page_lines)

        #     # Add the page to the list of pages
        #     self.pages.append(page)
        lines = []
        for i in range(0, len(lines), words_per_line):
            lines.append(' '.join(self.words[i:i + words_per_line]))

        self.pages = []
        for i in range(0, len(lines), lines_per_page):
            self.pages.append('\n'.join(lines[i:i + lines_per_page]))

    def calculate_payment(self):
        payment_structure = self.options['payment_structure']
        total_pages = len(self.pages)

        # Find the payment for the total number of pages
        payment = payment_structure.get(total_pages, payment_structure['default'])

        return payment

    def display_pages(self):
        payment = self.calculate_payment()

        print(f"Total Pages: {len(self.pages)}")
        print(f"Payment Due: ${payment}")

        for index, page in enumerate(self.pages):
            print(f"\nPage {index + 1}:\n{page}\n")

    def process_article(self):
        self.split_into_pages()
        self.display_pages()


  
# Example usage
article_text = '''What is GoLand IDE?
GoLand is a cross-platform IDE built by JetBrains for Go developers. It has support for different frontend technologies and databases, making it a perfect choice for full-stack web development. GoLand supports Docker, Kubernetes, and Terraform, so it’s equipped for DevOps tasks, too.
With GoLand, you get all the core functionality you need out of the box:
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
With GoLand, you get all the core functionality you need out of the box:
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
With GoLand, you get all the core functionality you need out of the box:
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
With GoLand, you get all the core functionality you need out of the box:
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
With GoLand, you get all the core functionality you need out of the box:
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
Go modules integration. Expanded Go modules support sadsa dasdasd
GoLand is a cross-platform IDE built by JetBrains for Go developers. It has support for different frontend technologies and databases, making it a perfect choice for full-stack web development. GoLand supports Docker, Kubernetes, and Terraform, so it’s equipped for DevOps tasks, too.
With GoLand, you get all the core functionality you need out of the box:
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
With GoLand, you get all the core functionality you need out of the box:
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
With GoLand, you get all the core functionality you need out of the box:
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
With GoLand, you get all the core functionality you need out of the box:
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
With GoLand, you get all the core functionality you need out of the box:
Go modules integration. Expanded Go modules support makes managing dependencies easy and straightforward.
Go modules integration. Expanded Go modules support sadsa dasdasd
'''
article_manager = ArticleManager(article_text)
article_manager.process_article()