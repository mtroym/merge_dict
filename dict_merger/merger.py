"""
字典合并工具模块
提供浅层和深层字典合并功能
"""

from typing import Dict, Any, Union
import copy


def merge_dicts(source: Dict[Any, Any], target: Dict[Any, Any], inplace: bool = False) -> Dict[Any, Any]:
    """
    合并两个字典，target的值会覆盖source的值（浅层合并）
    
    Args:
        source: 源字典
        target: 目标字典，其值会覆盖source中相同key的值
        inplace: 是否在原地修改source字典，默认False
        
    Returns:
        合并后的字典
        
    Example:
        >>> source = {'a': 1, 'b': 2}
        >>> target = {'b': 3, 'c': 4}
        >>> merge_dicts(source, target)
        {'a': 1, 'b': 3, 'c': 4}
    """
    if inplace:
        result = source
    else:
        result = copy.copy(source)
    
    result.update(target)
    return result


def deep_merge_dicts(source: Dict[Any, Any], target: Dict[Any, Any], inplace: bool = False) -> Dict[Any, Any]:
    """
    深度合并两个字典，递归合并嵌套字典
    target的值会覆盖source的值
    
    Args:
        source: 源字典
        target: 目标字典，其值会覆盖source中相同key的值
        inplace: 是否在原地修改source字典，默认False
        
    Returns:
        深度合并后的字典
        
    Example:
        >>> source = {'a': {'x': 1, 'y': 2}, 'b': 3}
        >>> target = {'a': {'y': 4, 'z': 5}, 'c': 6}
        >>> deep_merge_dicts(source, target)
        {'a': {'x': 1, 'y': 4, 'z': 5}, 'b': 3, 'c': 6}
    """
    if inplace:
        result = source
    else:
        result = copy.deepcopy(source)
    
    for key, value in target.items():
        if (key in result and 
            isinstance(result[key], dict) and 
            isinstance(value, dict)):
            # 递归合并嵌套字典
            result[key] = deep_merge_dicts(result[key], value, inplace=True)
        else:
            # 直接覆盖或添加新key
            result[key] = copy.deepcopy(value) if not inplace else value
    
    return result


def merge_multiple_dicts(*dicts: Dict[Any, Any], deep: bool = False, inplace: bool = False) -> Dict[Any, Any]:
    """
    合并多个字典
    
    Args:
        *dicts: 要合并的字典列表
        deep: 是否进行深度合并，默认False
        inplace: 是否在原地修改第一个字典，默认False
        
    Returns:
        合并后的字典
        
    Example:
        >>> dict1 = {'a': 1}
        >>> dict2 = {'b': 2}
        >>> dict3 = {'c': 3}
        >>> merge_multiple_dicts(dict1, dict2, dict3)
        {'a': 1, 'b': 2, 'c': 3}
    """
    if not dicts:
        return {}
    
    if len(dicts) == 1:
        return copy.deepcopy(dicts[0]) if not inplace else dicts[0]
    
    result = dicts[0] if inplace else copy.deepcopy(dicts[0])
    merge_func = deep_merge_dicts if deep else merge_dicts
    
    for dict_to_merge in dicts[1:]:
        result = merge_func(result, dict_to_merge, inplace=True)
    
    return result 