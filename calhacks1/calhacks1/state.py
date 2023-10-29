import reflex as rx
import os
import together
together.api_key = "2b084736a3bc9b659361dead521119d5bc00d5f8f3ad5c71e40f9ca5c14d25fd"
class State(rx.State):
#     # The current question being asked.
    question: str
    currency: str

#     # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
    #     # Our chatbot has some brains now!
        output = together.Complete.create(
            prompt = f"[INST]Convert {self.currency} dollars to {self.question}. Only give me the value[/INST]", 
            model = "togethercomputer/llama-2-70b-chat", 
            max_tokens = 256,
            temperature = 0.8,
            top_k = 60,
            top_p = 0.6,
            repetition_penalty = 1.1,
            stop = ['[INST]', '</s>']
        )
        #print(output['prompt'][0]+output['output']['choices'][0]['text'])

# print generated text
        # # Add to the answer as the chatbot responds.
        answer = output['output']['choices'][0]['text']
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        self.currency = ""
        # Yield here to clear the frontend input before continuing.
        yield

