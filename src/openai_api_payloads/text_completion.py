from typing import *

from pydantic import BaseModel, Field, Required


class TextCompletionInputs(BaseModel):
    model: str = Field(default=Required)
    prompt: Union[str, List] = Field(default="<|endoftext|>")
    suffix: Optional[str] = Field(default=None)
    max_tokens: int = Field(default=16)
    temperature: float = Field(default=1)
    top_p: float = Field(default=1)
    n: int = Field(default=1)
    stream: bool = Field(default=False)
    logprobs: Optional[int] = Field(default=None)
    echo: bool = Field(default=False)
    stop: Optional[Union[str, List[str]]] = Field(default=None)
    presence_penalty: float = Field(default=0)
    frequency_penalty: float = Field(default=0)
    best_of: int = Field(default=1)
    logit_bias: Optional[Dict[Union[str, int], float]] = Field(default=None)
    user: Optional[str] = Field(default=None)


class TextCompletionChoice(BaseModel):
    text: str = Field(default=Required)
    index: int = Field(default=Required)
    logprobs: Optional[int] = Field(default=None)
    finish_reason: str = Field(default="length")


class TextCompletionUsage(BaseModel):
    prompt_tokens: int = Field(default=Required)
    completion_tokens: int = Field(default=Required)
    total_tokens: int = Field(default=Required)


class TextCompletionOutputs(BaseModel):
    model: str
    choices: List[TextCompletionChoice] = Field(default=Required)
    usage: TextCompletionUsage = Field(default=Required)
    id: Optional[str] = Field(default=None)
    created: Optional[int] = Field(default=None)
    object: str = Field(default="text_completion")
