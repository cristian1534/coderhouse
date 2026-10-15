from langchain_core.prompts import PromptTemplate

technical_report_prompt = PromptTemplate(
    input_variables=["texto", "format_instructions"],
    template="""
Sos un analista técnico especializado en sistemas informáticos.

Analizá el siguiente texto y generá un informe técnico.

TEXTO A ANALIZAR:
{texto}

INSTRUCCIONES DE FORMATO:
{format_instructions}

Reglas:
- Identificá las tecnologías mencionadas explícitamente en el texto.
- Asigná un nivel de criticidad: baja, media o alta.
- Redactá un resumen técnico claro y conciso.
- No inventes tecnologías ni información que no aparezca en el texto.
- Devolvé únicamente el resultado solicitado, respetando las instrucciones de formato.
"""
)
