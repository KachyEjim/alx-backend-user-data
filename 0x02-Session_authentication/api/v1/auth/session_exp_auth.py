#!/usr/bin/env python3
"""session_auth manager"""

from api.v1.auth.session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Class to manage session expiration"""

    def __init__(self):
        try:
            self.session_duration = int(os.getenv("SESSION_DURATION"))
        except (TypeError, ValueError):
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Creates a session"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dict = {"user_id": user_id, "created_at": datetime.now()}
        self.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Instance method"""
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        session_dict = self.user_id_by_session_id.get("session dictionary")
        if self.session_duration <= 0:
            user_id = session_dict.get("user_id")
            return user_id
        if session_dict.get("created_at") is None:
            return None

        expiration_time = session_dict.get("created_at") + timedelta(
            seconds=self.session_duration
        )

        if expiration_time < datetime.now():
            return None
        return session_dict["user_id"]
