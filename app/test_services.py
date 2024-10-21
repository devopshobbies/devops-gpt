from .utils import save_QA_to_mongo

def test_mongo_save():
    save_QA_to_mongo('q','a')
    

