from application.interfaces.prompts.technical_report_prompt import (
    technical_report_prompt,
)

prompt_generado = technical_report_prompt.format(
    texto="""
    El sistema utiliza Python y PostgreSQL.
    La aplicación presenta fallos frecuentes y afecta
    la disponibilidad del servicio.
    """,
    format_instructions=(
        "Respondé con un JSON que contenga las claves "
        "tecnologias, nivel_de_criticidad y resumen_tecnico."
    ),
)

print(prompt_generado)
