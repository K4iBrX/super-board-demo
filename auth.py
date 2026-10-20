from dataclasses import dataclass

import streamlit as st

SESSION_KEY = "user"


@dataclass(frozen=True)
class User:
    name: str
    provider: str


def current_user() -> User | None:
    return st.session_state.get(SESSION_KEY)


def sign_in(user: User) -> None:
    st.session_state[SESSION_KEY] = user


def sign_out() -> None:
    st.session_state.pop(SESSION_KEY, None)
