# Analizador de Informes Técnicos con IA

Aplicación en Python que utiliza un modelo de lenguaje de Google Gemini para analizar textos técnicos y generar informes estructurados mediante LangChain y Pydantic.

## Objetivo

Transformar descripciones de incidentes o problemas informáticos en informes técnicos estructurados que permitan identificar tecnologías involucradas, evaluar el nivel de criticidad y resumir la situación.

## Tecnologías utilizadas

- **Python 3.13**
- **Google Gemini** como modelo de lenguaje.
- **LangChain** para construir y ejecutar la cadena de procesamiento.
- **LCEL (LangChain Expression Language)** para conectar los componentes.
- **Pydantic** para validar la estructura y los datos de salida.
- **PydanticOutputParser** para convertir la respuesta del modelo en un objeto validado.
- **OutputFixingParser** para intentar reparar respuestas que no cumplen con el formato esperado.
- **Retry** para reintentar la ejecución cuando se producen errores recuperables.

## Arquitectura del proyecto

```text
coderhouse/
├── application/
│   ├── interfaces/
│   │   └── prompts/
│   │       └── technical_report_prompt.py
│   └── services/
│       └── technical_report_chain.py
├── domain/
│   └── schemas.py
├── .env
├── .gitignore
├── main.py
├── test_chain.py
├── test_prompt.py
├── test_schema.py
└── README.md
```

**Responsabilidades principales:**

- `domain/schemas.py`: define los modelos de datos y las reglas de validación mediante Pydantic.
- `application/interfaces/prompts/technical_report_prompt.py`: contiene las instrucciones para analizar el texto.
- `application/services/technical_report_chain.py`: configura Gemini, los parsers y la cadena LCEL.
- `test_schema.py`: permite probar los modelos de datos.
- `test_prompt.py`: permite verificar el prompt.
- `test_chain.py`: ejecuta la cadena completa y muestra el informe generado.
- `main.py`: punto de entrada de la aplicación principal.

## Requisitos previos

- Python 3.13 o compatible con las dependencias utilizadas.
- Una API key de Google AI Studio con acceso al modelo configurado.
- Un entorno virtual de Python.

## Instalación

### 1. Clonar o descargar el proyecto

Ubicate en la carpeta raíz del proyecto:

```bash
cd /Users/development/Desktop/coderhouse
```

### 2. Activar el entorno virtual

En macOS o Linux:

```bash
source .venv/bin/activate
```

### 3. Instalar las dependencias

Si todavía no tenés instaladas las dependencias:

```bash
python3 -m pip install -U langchain langchain-core langchain-classic langchain-google-genai pydantic python-dotenv
```

## Configuración de la API key

Definí la variable de entorno `GEMINI_API_KEY` con tu clave de Google AI Studio.

Podés guardarla en un archivo `.env` ubicado en la raíz del proyecto:

```dotenv
GEMINI_API_KEY=tu_api_key
```

Asegurate de que el código cargue esa variable de entorno. Si utilizás `python-dotenv`, podés inicializarlo con:

```python
from dotenv import load_dotenv

load_dotenv()
```

**Importante:** no publiques tu API key ni subas el archivo `.env` a Git. Agregá lo siguiente a `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
```

## Ejecución

Para ejecutar la prueba de la cadena completa:

```bash
python3 -u test_chain.py
```

Para probar el prompt de forma independiente:

```bash
python3 test_prompt.py
```

Para validar los modelos Pydantic:

```bash
python3 test_schema.py
```

## Flujo de procesamiento

1. El usuario proporciona un texto técnico.
2. El `PromptTemplate` incorpora el texto y las instrucciones de formato.
3. Gemini analiza la información y genera una respuesta.
4. `PydanticOutputParser` interpreta y valida la estructura de salida.
5. `OutputFixingParser` puede solicitar una corrección si la respuesta no cumple con el formato esperado.
6. La cadena devuelve un objeto `InformeTecnico` validado.

## Formato del informe

El modelo `InformeTecnico` contempla los siguientes campos:

| Campo | Descripción |
|---|---|
| `tecnologias` | Lista de tecnologías identificadas en el texto. |
| `nivel_de_criticidad` | Nivel de criticidad: `baja`, `media` o `alta`. |
| `resumen_tecnico` | Resumen claro y conciso del problema. |

Ejemplo ilustrativo de salida:

```json
{
  "tecnologias": [
    "Python",
    "PostgreSQL",
    "Docker"
  ],
  "nivel_de_criticidad": "alta",
  "resumen_tecnico": "El sistema experimenta fallos recurrentes en la base de datos que afectan la disponibilidad del servicio."
}
```

## Validación y resiliencia

La aplicación utiliza validación estructurada con Pydantic para reducir el riesgo de recibir datos incompletos o incompatibles con el esquema esperado.

También se configura `OutputFixingParser` para intentar corregir respuestas inválidas y `with_retry()` para reintentar la ejecución ante determinados errores.

Los reintentos no garantizan que todos los errores puedan resolverse. Su comportamiento depende del tipo de error, la configuración y la disponibilidad del servicio de Gemini.

## Consideraciones

- El nivel de criticidad generado por el modelo debe revisarse según las reglas del negocio.
- La calidad del resultado depende del texto de entrada y de la respuesta del modelo.
- Las llamadas a Gemini pueden estar sujetas a límites de uso y cuotas de la API.
- Las pruebas que invocan al modelo pueden consumir cuota; las pruebas de esquemas y prompts pueden ejecutarse por separado.

## Estado del proyecto

La cadena completa de análisis técnico se ejecutó correctamente con Gemini y generó un informe validado con el esquema Pydantic.

La reparación automática de respuestas inválidas debe probarse de forma específica para confirmar su comportamiento ante errores de formato.