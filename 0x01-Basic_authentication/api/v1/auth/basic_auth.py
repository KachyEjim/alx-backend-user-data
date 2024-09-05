#!/usr/bin/env python3
"""API auth manager"""

from api.v1.auth.auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract Base 64 Authorization Header"""

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        encoded = authorization_header.split(" ", 1)[1]

        return encoded

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Decodes the value of a base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            import base64

            encoded = base64_authorization_header.encode("utf-8")
            decoded64 = base64.b64decode(encoded)
            decoded = decoded64.decode("utf-8")
        except BaseException:
            return None

        return decoded

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """Returns a users email and password"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        user_data = decoded_base64_authorization_header.split(":", 1)
        return user_data[0], user_data[1]

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        """Gets a user with its email and pwd"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        from models.user import User

        user = User.search({"email": user_email})
        if not user:
            return None
        if not user[0].is_valid_password(user_pwd):
            return None
        return user[0]

    def current_user(self, request=None) -> TypeVar("User"):
        """Gets the current user"""
        header = self.authorization_header(request)
        encoded_header = self.extract_base64_authorization_header(header)
        dh = self.decode_base64_authorization_header(encoded_header)
        user_cred = self.extract_user_credentials(dh)
        user = self.user_object_from_credentials(user_cred[0], user_cred[1])
        return user
