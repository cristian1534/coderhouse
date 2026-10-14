# Proyecto LLM - Gemini

Proyecto en Python que implementa un cliente para interactuar con la API de Google Gemini, con soporte para generación de respuestas normales y streaming asíncrono.

## Requisitos

- Python 3.13 o compatible.
- Una API key de Google Gemini.
- Un entorno virtual de Python.
- Las dependencias del proyecto instaladas.

## 1. Configurar el entorno virtual

Desde la raíz del proyecto, ejecutá:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Instalar las dependencias

Si el proyecto tiene un archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Asegurate de que incluya las dependencias utilizadas, como `google-genai` y `python-dotenv`.

Si todavía no tenés ese archivo, podés instalar ambas directamente:

```bash
pip install google-genai python-dotenv
```

## 3. Configurar las variables de entorno

Creá un archivo `.env` en la raíz del proyecto:

```env
GEMINI_API_KEY=tu_api_key_de_gemini
```

Reemplazá `tu_api_key_de_gemini` por tu clave real.

**Importante:** no compartas tu API key ni la subas al repositorio. Agregá `.env` a tu archivo `.gitignore`.

## 4. Ejecutar el script de prueba

Con el entorno virtual activado, ejecutá:

```bash
python3 main.py
```

El script realiza dos pruebas con el modelo `gemini-3.8-flash`:

- **Modo normal:** obtiene y muestra la respuesta completa.
- **Modo streaming:** recibe los fragmentos de texto progresivamente mediante un generador asíncrono.

La pregunta de prueba es: «¿Qué es la entropía?».

## 5. Estructura del proyecto

```text
coderhouse/
├── application/
│   └── interfaces/
│       └── llm_client.py
├── domain/
│   └── schemas.py
├── infrastructure/
│   └── llm/
│       └── gemini_client.py
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 6. Solución de problemas

- **Falta `GEMINI_API_KEY`:** verificá que el archivo `.env` exista en la raíz del proyecto y que contenga la clave.
- **`ModuleNotFoundError`:** activá el entorno virtual e instalá las dependencias.
- **`503 UNAVAILABLE`:** Gemini puede estar experimentando una sobrecarga temporal. Esperá unos minutos y volvé a ejecutar el script.
- **El streaming no muestra texto progresivamente:** verificá que `generate_stream()` recorra el stream del SDK con `async for` y entregue cada fragmento con `yield`.

## Objetivo

Validar el funcionamiento del cliente Gemini, su interfaz común y la generación de respuestas tanto en modo normal como en streaming asíncrono.