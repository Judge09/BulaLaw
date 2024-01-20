class LawDictionary:
    def __init__(self, file_path):
        self.legal_terms = self.load_legal_terms(file_path)

        def load_legal_terms(self, file_path):
            legal_terms = {}
            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        term, definition, location = line.strip().split('|')
                        legal_terms[term] = {"definition": definition, "location": location}
            except FileNotFoundError:
                print(f"File not found: {file_path}")
            return legal_terms

    def search(self, keyword):
        keyword = keyword.lower()
        results = []

        for term, data in self.legal_terms.items():
            term_lower = term.lower()
            definition_lower = data["definition"].lower()

            if keyword in term_lower or keyword in definition_lower:
                # Highlight the keyword in the term and definition
                highlighted_term = term_lower.replace(keyword, f"\033[1;31m{keyword}\033[0m")
                highlighted_definition = definition_lower.replace(keyword, f"\033[1;31m{keyword}\033[0m")

                results.append((highlighted_term, data["definition"], data["location"]))

        return results

if __name__ == "__main__":
    file_path = "legal_terms.txt"   # Replace with the actual path to your text file
    law_dict = LawDictionary(file_path)

    while True:
        search_query = input("Enter a keyword to search (type 'exit' to quit): ")

        if search_query.lower() == 'exit':
            break

        search_results = law_dict.search(search_query)

        if search_results:
            print("\nSearch results:")
            for result in search_results:
                print(f"\nTerm: {result[0]}\nDefinition: {result[1]}\nLocation: {result[2]}\n")
        else:
            print("\nNo matching terms found.")
