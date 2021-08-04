import pickle

from trp import Document

PROBLEMATIC_FILE = 'problematic_resp.pickle'


def test_document_parse_fail():
    with open(PROBLEMATIC_FILE, 'rb') as f:
        analysis_response_list = pickle.load(f)
    for analysis_response in analysis_response_list:
        Document(analysis_response)


if __name__ == '__main__':
    test_document_parse_fail()
