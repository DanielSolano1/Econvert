import reflex as rx
from calhacks1 import style
from calhacks1.state import State

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=style.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=style.answer_style,
        ),
        margin_y="1em",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.vstack(  # Change from rx.hstack to rx.vstack to stack elements vertically
        rx.text("Econ Converter", font_size="4.0em",color = "green"),  # Add the "Econvert" text
        rx.text("Convert from USD to any currency(Yen,Vbucks,Bitcoin)", font_size="1.3em", color = "#c8a47e"),  
        rx.hstack(
            rx.input(
                value=State.question,
                placeholder="Currency for Conversion",
                on_change=State.set_question,
                style=style.input_style,
            ),rx.input(
                value=State.currency,
                placeholder="USD$",
                on_change=State.set_currency,
                style=style.input_style,
            ),rx.button(
                rx.text("Convert", _hover={"color": "green"}),
                on_click=State.answer,
                style=style.button_style,
            ),
        ),
    )

def index() -> rx.Component:
    return rx.container(
        action_bar(),
        chat(),
    )

app = rx.App()
app.add_page(index)
app.compile()