#!/usr/bin/env python3
""" encrypt password """
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypts a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if a password is valid"""
    return bcrypt.checkpw(password.encode(), hashed_password)
