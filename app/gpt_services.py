import os
from openai import OpenAI

class Client:

    _instance = None

    def connection(self ):

        client = OpenAI(
   
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
        return client

    def get_instance(cls):
        if cls._instance == None:
            cls._instance = cls.connection()
            return cls._instance
        return cls._instance



def gpt_service_IaC(input:str, service:str,max_tokens:int, min_tokens:int):

    client = Client()

    prompt = f"""
        Write a robust answer about {service},
        focusing on the latest update of {service} and based on this question:{input},
        minimun length of answer is {min_tokens} and maximum length is {max_tokens}

    """
    chat_completion = client.get_instance().chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion