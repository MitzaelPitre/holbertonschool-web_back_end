#!/usr/bin/env python3
""" List all documents"""


def list_all(mongo_collection):
    """ lists all documents  """
    documents = mongo_collection.find()
    
    # Convert the cursor to a list
    document_list = list(documents)
    
    # Return the list of documents, or an empty list if no documents are found
    return document_list