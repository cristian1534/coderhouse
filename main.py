
import asyncio
import os
from dotenv import load_dotenv

from infrastructure.llm.gemini_client import GeminiClient
from domain.schemas import ChatMessage

load_dotenv()


async def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Falta GEMINI_API_KEY en el archivo .env")

    gemini_client = GeminiClient(
        api_key=api_key,
        model="gemini-3.8-flash",
        temperature=0.7,
        max_tokens=1024,
    )

    pregunta = [
        ChatMessage(
            role="user",
            content="¿Qué es la entropía? Respondé brevemente.",
        )
    ]

    try:
        print("\n🔵 RESPUESTA NORMAL\n")

        respuesta = await gemini_client.generate(pregunta)

        if respuesta.error:
            print(f"Error: {respuesta.error}")
        else:
            print(respuesta.content)

        print("\n🟣 RESPUESTA EN STREAMING\n")

        async for chunk in gemini_client.generate_stream(pregunta):
            print(chunk, end="", flush=True)

        print("\n")

    finally:
        gemini_client._client.close()


if __name__ == "__main__":
    asyncio.run(main())
