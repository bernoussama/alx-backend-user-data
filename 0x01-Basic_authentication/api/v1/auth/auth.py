#!/usr/bin/env python3
""" Auth module
"""
from typing import List, TypeVar
from flask import request
import re


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication"""
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                if exclusion_path.endswith("*"):
                    pattern = re.escape(exclusion_path[:-1]) + ".*"
                else:
                    pattern = re.escape(exclusion_path.rstrip("/")) + "/?"
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        if request is not None:
            if request.headers.get("Authorization") is not None:
                return request.headers.get("Authorization")
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """Current user"""
        return None
