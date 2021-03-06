import textmining
import os


def termdocumentmatrix_example():
    # import some sample documents
    #doc1 = open('lovecraftshort.txt', 'r')
   # doc2 = open('lovecraftshort2.txt', 'r')
    #doc3 = open('lovecraftshort3', 'r')
    

    example_dir = os.path.dirname(__file__)
    sample_text_file = os.path.join(example_dir, 'hpwords.txt')
    doc1 = open(sample_text_file).read()
    

    # Initialize class to create term-document matrix
    tdm = textmining.TermDocumentMatrix()
    
    # Add the documents
    tdm.add_doc(doc1)
    
    # Write out the matrix to a csv file. Note that setting cutoff=1 means
    # that words which appear in 1 or more documents will be included in
    # the output (i.e. every word will appear in the output). The default
    # for cutoff is 2, since we usually aren't interested in words which
    # appear in a single document. For this example we want to see all
    # words however, hence cutoff=1.

    tdm.write_csv('hpbigmatrix.csv', cutoff=1)
    
    # Instead of writing out the matrix you can also access its rows directly.
    # Let's print them to the screen.
    
    for row in tdm.rows(cutoff=1):
        print row

termdocumentmatrix_example()
