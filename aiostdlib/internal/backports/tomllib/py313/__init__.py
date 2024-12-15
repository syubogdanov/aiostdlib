# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2021 Taneli Hukkinen
# Licensed to PSF under a Contributor Agreement.

__all__ = ("loads", "TOMLDecodeError")

from aiostdlib.internal.backports.tomllib.py313.parser import TOMLDecodeError, loads
