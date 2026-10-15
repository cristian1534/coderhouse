import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.output_parsers import OutputFixingParser

from domain.schemas import InformeTecnico
from application.interfaces.prompts.technical_report_prompt import (
    technical_report_prompt,
)


def crear_cadena():
    parser = PydanticOutputParser(
        pydantic_object=InformeTecnico
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0.2,
        max_retries=2,
    )

    parser_con_reparacion = OutputFixingParser.from_llm(
        parser=parser,
        llm=llm,
        max_retries=2,
    )

    prompt = technical_report_prompt.partial(
        format_instructions=parser.get_format_instructions()
    )

    cadena = prompt | llm | parser_con_reparacion

    return cadena.with_retry(
        stop_after_attempt=2,
        wait_exponential_jitter=False,
    )