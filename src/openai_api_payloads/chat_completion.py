from typing import *

from pydantic import BaseModel, Field, Required


class ChatCompletionMessage(BaseModel):
    role: str = Field(default=Required, regex=r"(system|user|assistant)")
    content: str = Field(default=Required)
    name: Optional[str] = Field(default=None)


class ChatCompletionInputs(BaseModel):
    model: str = Field(default=Required)
    messages: List[ChatCompletionMessage] = Field(default=Required)
    temperature: float = Field(default=1)
    top_p: float = Field(default=1)
    n: int = Field(default=1)
    stream: bool = Field(default=False)
    stop: Optional[Union[str, List[str]]] = Field(default=False)
    max_tokens: int = Field(default=16)
    presence_penalty: float = Field(default=0)
    frequency_penalty: float = Field(default=0)
    logit_bias: Optional[Dict[Union[str, int], float]] = Field(default=None)
    user: Optional[str] = Field(default=None)


class ChatCompletionChoice(BaseModel):
    index: int = Field(default=Required)
    message: ChatCompletionMessage = Field(default=Required)
    finish_reason: str = Field(default="stop")


class ChatCompletionUsage(BaseModel):
    prompt_tokens: int = Field(default=Required)
    completion_tokens: int = Field(default=Required)
    total_tokens: int = Field(default=Required)


class ChatCompletionOutputs(BaseModel):
    model: Optional[str] = Field(default=Required)
    choices: List[ChatCompletionChoice] = Field(default=Required)
    usage: ChatCompletionUsage = Field(default=Required)
    id: Optional[str] = Field(default=None)
    created: Optional[int] = Field(default=None)
    object: str = Field(default="chat_completion")
