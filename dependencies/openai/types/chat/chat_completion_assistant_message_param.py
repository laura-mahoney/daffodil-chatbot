# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .chat_completion_message_tool_call_param import ChatCompletionMessageToolCallParam

__all__ = ["ChatCompletionAssistantMessageParam", "FunctionCall"]


class FunctionCall(TypedDict, total=False):
    arguments: Required[str]
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Required[str]
    """The name of the function to call."""


class ChatCompletionAssistantMessageParam(TypedDict, total=False):
    role: Required[Literal["assistant"]]
    """The role of the messages author, in this case `assistant`."""

    content: Optional[str]
    """The contents of the assistant message.

    Required unless `tool_calls` or `function_call` is specified.
    """

    function_call: FunctionCall
    """Deprecated and replaced by `tool_calls`.

    The name and arguments of a function that should be called, as generated by the
    model.
    """

    name: str
    """An optional name for the participant.

    Provides the model information to differentiate between participants of the same
    role.
    """

    tool_calls: Iterable[ChatCompletionMessageToolCallParam]
    """The tool calls generated by the model, such as function calls."""