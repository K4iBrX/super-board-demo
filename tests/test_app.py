from streamlit.testing.v1 import AppTest

import auth


def texts(at):
    return [e.value for e in at.markdown] + [e.value for e in at.title] + [e.value for e in at.header]


def test_unauthenticated_shows_sign_in_and_no_home():
    at = AppTest.from_file("../app.py").run()
    assert not at.exception
    shown = " ".join(texts(at))
    assert "Sign in" in shown
    assert "Home" not in shown
    assert not [b for b in at.button if b.label == "Sign out"]


def test_signed_in_shows_home_with_name_and_sign_out():
    at = AppTest.from_file("../app.py")
    at.session_state[auth.SESSION_KEY] = auth.User("Ada", "github")
    at.run()
    shown = " ".join(texts(at))
    assert "Home" in shown and "Ada" in shown
    assert "Sign in" not in shown


def test_sign_out_button_returns_to_gate():
    at = AppTest.from_file("../app.py")
    at.session_state[auth.SESSION_KEY] = auth.User("Ada", "github")
    at.run()
    at.button[0].click().run()
    assert "Sign in" in " ".join(texts(at))
    assert "Home" not in " ".join(texts(at))
