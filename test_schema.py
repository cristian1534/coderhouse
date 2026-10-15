from domain.schemas import InformeTecnico

informe = InformeTecnico(
    tecnologias=["Python", "Gemini", "Pydantic"],
    nivel_de_criticidad="media",
    resumen_tecnico="Aplicación que utiliza un modelo de lenguaje para analizar información técnica."
)

print(informe.model_dump_json(indent=2))
