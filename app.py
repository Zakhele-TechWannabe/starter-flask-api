from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

# from getpass import getpass
# from langchain import HuggingFaceHub
# from langchain import PromptTemplate, LLMChain

# # HUGGINGFACEHUB_API_TOKEN = getpass()

# import os

# HUGGINGFACEHUB_API_TOKEN = "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"

# os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

# question = "Who won the FIFA World Cup in the year 1994? "

# template = """Question: {question}

# Answer: Let's think step by step."""

# prompt = PromptTemplate(template=template, input_variables=["question"])

# repo_id = "google/flan-t5-xxl"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options

# llm = HuggingFaceHub(
#     repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
# )
# llm_chain = LLMChain(prompt=prompt, llm=llm)

# print(llm_chain.run(question))
