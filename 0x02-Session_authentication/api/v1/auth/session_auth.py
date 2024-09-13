#!/usr/bin/env python3
"""session_auth manager"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """SessionAuth class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        uid = str(uuid4())
        self.user_id_by_session_id[uid] = user_id
        return uid

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a user id based on a session id"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a user instance"""

        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """Delects a users session"""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        instance = self.user_id_for_session_id(session_id)
        if instance is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
