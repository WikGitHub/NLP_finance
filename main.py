import spacy
import pandas as pd


def create_patterns(symbols, companies, stops):
    nlp = spacy.blank("en")
    ruler = nlp.add_pipe("entity_ruler")
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pattern = []
    for symbol in symbols:
        pattern.append({"label": "STOCK", "pattern": symbol})
        for letter in letters:
            pattern.append({"label": "STOCK", "pattern": symbol + f".{letter}"})
    for company in companies:
        if company not in stops:
            pattern.append({"label": "COMPANY", "pattern": company})
    ruler.add_patterns(pattern)

    return nlp


def main():
    stops = ["two"]
    stocks_df = pd.read_csv('stocks.tsv', sep='\t')
    symbols = stocks_df.Symbol.tolist()
    companies = stocks_df.CompanyName.tolist()
    nlp = create_patterns(symbols, companies, stops)
    doc = nlp('/Users/wiktoria/Desktop/pythonProject/fin_ner/sample')
    for ent in doc.ents:
        print(ent.text, ent.label_)


if __name__ == '__main__':
    main()
