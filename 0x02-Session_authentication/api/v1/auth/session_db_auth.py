#!/usr/bin/env python3
"""session_auth manager"""
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """SessionDBaUTH CLASS"""

    def create_session(self, user_id=None):
        """Creates  session"""
        session_id = super().create_session(user_id)
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Gets a user by the session_id"""
        user_id = super().user_id_for_session_id(session_id)
        return user_id

    def destroy_session(self, request=None):
        """Destroies a users session"""
        super().destroy_session(request)
