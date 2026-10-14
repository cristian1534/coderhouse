
from abc import ABC, abstractmethod
from typing import AsyncGenerator

from domain.schemas import ChatMessage, ModelResponse


class BaseLLMClient(ABC):

    @abstractmethod
    async def generate(
        self,
        messages: list[ChatMessage],
    ) -> ModelResponse:
        raise NotImplementedError

    @abstractmethod
    async def generate_stream(
        self,
        messages: list[ChatMessage],
    ) -> AsyncGenerator[str, None]:
        raise NotImplementedError
        yield
