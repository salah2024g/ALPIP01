from app.security.utils.password import (
    hash_password,
    verify_password
)


class AuthService:

    def create_user_password(
        self,
        password: str
    ) -> str:

        return hash_password(password)


    def authenticate(
        self,
        password: str,
        stored_password: str
    ) -> bool:

        return verify_password(
            password,
            stored_password
        )
