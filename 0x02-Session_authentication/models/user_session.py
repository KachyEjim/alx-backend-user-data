#!/usr/bin/env python3
""" user_session model module
"""
from models.base import Base


class UserSession(Base):
    """Class for session db storage"""

    def __init__(self, *args: list, **kwargs: dict):
        """Initializes a new UserSession instance"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get("user_id")
        self.session_id = kwargs.get("session_id")
        
