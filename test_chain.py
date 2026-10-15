import asyncio
from dotenv import load_dotenv
from application.services.technical_report_chain import crear_cadena


async def main():
    load_dotenv()

    cadena = crear_cadena()

    texto = """
    El sistema utiliza Python, PostgreSQL y Docker.
    Se detectaron fallos recurrentes en la base de datos
    que afectan la disponibilidad del servicio.
    """

    print("Generando informe técnico...\n")

    try:
        resultado = await cadena.ainvoke({"texto": texto})

        print("--- INFORME TÉCNICO ---")
        print(resultado.model_dump_json(indent=2))

    except Exception as error:
        print(f"Error al generar el informe: {error}")


if __name__ == "__main__":
    asyncio.run(main())
