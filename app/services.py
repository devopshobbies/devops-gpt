from .utils import save_to_mongo

def write_basic(request,output):

    data = {
        'question':request.question,
        'output':output
    }

    save_to_mongo(data, index='question', collection = 'qa')


def write_bugfix(request,output):

    data = {
        'bug_description':request.bug_description,
        'service':request.service,
        'output':output
    }

    save_to_mongo(data, index=['bug_description','service'], collection = 'bugfix')


def write_installation(request,output):

    data = {
        'os':request.os,
        'service':request.service,
        'output':output
    }

    save_to_mongo(data, index=['os','service'], collection = 'installation')

