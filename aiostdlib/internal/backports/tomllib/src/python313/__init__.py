# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2021 Taneli Hukkinen
# Licensed to PSF under a Contributor Agreement.

__all__ = ("TOMLDecodeError", "loads")

from aiostdlib.internal.backports.tomllib.src.python313.parser import TOMLDecodeError, loads
