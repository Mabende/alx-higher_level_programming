#!/usr/bin/python3
"""
   define Lookup
"""


def lookup(obj):
	"""
	It returns the list of available attributes and methods.
	Args:
	obj (object): object.
	"""
	return (dir(obj))
