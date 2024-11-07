#!/usr/bin/env python3
""" encrypt password """
import bcrypt


def encrypt_password(password: str) -> bytes:
    """Encrypts a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
