import os
from openai import OpenAI
from fastapi import HTTPException

def gpt_service(prompt):

    try:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [{"type": "text", "text": prompt}],
                }
            ],
            model="gpt-4o-mini",
        )
        generated_text = chat_completion.choices[0].message.content
        
        return generated_text

    except Exception as e:
        
        raise HTTPException(status_code=400, detail=str(e))