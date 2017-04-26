import sqlite3

def iterate_db():
    mendeley_db_file = '/home/michi/.local/share/data/Mendeley Ltd./Mendeley Desktop/www.mendeley.com.sqlite'
    DOCUMENT_TABLE = 'Documents'
    with sqlite3.connect(mendeley_db_file) as conn:
        c = conn.cursor()
        s = "SELECT id, abstract, title, added, modified, doi, arxivId, citationKey, pmid, year from {}".format(DOCUMENT_TABLE)
        all_rows = c.execute(s)
        for id, abstract, title, added, modified, doi, arxivId, citationKey, pmid, year in all_rows:
            yield id, abstract, title, added, modified, doi, arxivId, citationKey, pmid, year




def bib_import():
    import bibtexparser
    with open('ICB.bib', encoding="ISO-8859-1") as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)

    for e in bib_database.entries:
        abstract = e['abstract'] if 'abstract' in e else None
        yield e['ID'],abstract, e['title'], None, None, None, None, None,None, e['year']