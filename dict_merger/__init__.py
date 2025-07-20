"""
Dict Merger - 一个用于合并字典的Python包
支持深度合并，当key相同时用目标值覆盖源值
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .merger import merge_dicts, deep_merge_dicts

__all__ = ["merge_dicts", "deep_merge_dicts"] 