from agenta import post, TextParam, FloatParam
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os


default_prompt = """
    please write a short linkedin message (2 SENTENCES MAX) to an investor pitchin the following startup:
    startup name: {startup_name}
    startup idea: {startup_idea}"""


@post
def generate(startup_name: str, startup_idea: str, prompt_template: TextParam = default_prompt, temperature: FloatParam = 0.5) -> str:
    load_dotenv()
    llm = OpenAI(temperature=temperature)
    prompt = PromptTemplate(
        input_variables=["startup_name", "startup_idea"],
        template=prompt_template)

    chain = LLMChain(llm=llm, prompt=prompt)
    output = chain.run(startup_name=startup_name, startup_idea=startup_idea)
    return output
