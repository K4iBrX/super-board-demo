from streamlit.testing.v1 import AppTest

import auth


def test_current_user_is_none_without_sign_in():
    at = AppTest.from_string(
        "import auth, streamlit as st\nst.write(repr(auth.current_user()))"
    ).run()
    assert at.markdown[0].value == "None"


def test_sign_in_then_current_user_returns_user():
    at = AppTest.from_string(
        "import auth, streamlit as st\n"
        "auth.sign_in(auth.User('Ada', 'github'))\n"
        "u = auth.current_user()\n"
        "st.write(f'{u.name}|{u.provider}')"
    ).run()
    assert at.markdown[0].value == "Ada|github"


def test_sign_out_clears_user():
    at = AppTest.from_string(
        "import auth, streamlit as st\n"
        "auth.sign_in(auth.User('Ada', 'github'))\n"
        "auth.sign_out()\n"
        "st.write(repr(auth.current_user()))"
    ).run()
    assert at.markdown[0].value == "None"
