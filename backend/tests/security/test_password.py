from app.security.utils.password import (
    hash_password,
    verify_password
)


def test_password_hash():

    password = "secret"

    hashed = hash_password(
        password
    )

    assert verify_password(
        password,
        hashed
    )
