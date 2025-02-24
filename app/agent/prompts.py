from typing import Optional

from llama_index.core import BasePromptTemplate, ChatPromptTemplate, PromptTemplate

SUMMARIZE_PROMPT = """Prepare a summary note for the following transcript.

If a target language is provided, write the summary note in that language. \
If no target language is specified, write the summary note in the same language \
as the transcript. Use strictly and exclusively the information provided in the \
transcript. Do not add, assume, infer, or expand on any details that are not \
explicitly stated in the transcript.

If a structured output is expected, return an empty string (`""`) for fields where \
no information is available. Avoid using placeholders, inferred content, or any \
indications of missing data. Ensure the summary note is concise, professional, \
and accurate, focusing only on the explicitly stated key details

---
Target Language: {target_language}
---

Transcript:
{transcript}
"""


class PromptManager:
    def __init__(self):
        self.prompts: dict[str, BasePromptTemplate] = {}

    def add_chat_prompt_template(
        self, name: str, messages: list[tuple[str, str]]
    ) -> None:
        self.prompts[name] = ChatPromptTemplate.from_messages(messages)

    def add_prompt_template(self, name: str, prompt: str) -> None:
        self.prompts[name] = PromptTemplate(prompt)

    def get_prompt(self, name: str) -> Optional[BasePromptTemplate]:
        return self.prompts.get(name)


prompt_manager = PromptManager()
prompt_manager.add_prompt_template("summarize", SUMMARIZE_PROMPT)
