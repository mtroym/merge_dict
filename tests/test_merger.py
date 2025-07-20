"""
Dict Merger包的测试用例
"""

import pytest
import copy
from dict_merger import merge_dicts, deep_merge_dicts
from dict_merger.merger import merge_multiple_dicts


class TestMergeDicts:
    """测试浅层字典合并功能"""
    
    def test_basic_merge(self):
        """测试基本合并功能"""
        source = {'a': 1, 'b': 2}
        target = {'b': 3, 'c': 4}
        
        result = merge_dicts(source, target)
        expected = {'a': 1, 'b': 3, 'c': 4}
        
        assert result == expected
        
    def test_merge_inplace(self):
        """测试原地合并"""
        source = {'a': 1, 'b': 2}
        target = {'b': 3, 'c': 4}
        original_source = copy.copy(source)
        
        result = merge_dicts(source, target, inplace=True)
        
        # 原字典应该被修改
        assert source == {'a': 1, 'b': 3, 'c': 4}
        assert result is source
        
    def test_merge_not_inplace(self):
        """测试非原地合并"""
        source = {'a': 1, 'b': 2}
        target = {'b': 3, 'c': 4}
        original_source = copy.copy(source)
        
        result = merge_dicts(source, target, inplace=False)
        
        # 原字典不应该被修改
        assert source == original_source
        assert result is not source
        
    def test_empty_dicts(self):
        """测试空字典"""
        assert merge_dicts({}, {}) == {}
        assert merge_dicts({'a': 1}, {}) == {'a': 1}
        assert merge_dicts({}, {'a': 1}) == {'a': 1}
        
    def test_same_keys_overwrite(self):
        """测试相同key时目标值覆盖源值"""
        source = {'x': 'old', 'y': 'keep'}
        target = {'x': 'new'}
        
        result = merge_dicts(source, target)
        assert result == {'x': 'new', 'y': 'keep'}


class TestDeepMergeDicts:
    """测试深度字典合并功能"""
    
    def test_deep_merge_nested(self):
        """测试嵌套字典的深度合并"""
        source = {
            'a': {'x': 1, 'y': 2},
            'b': 3
        }
        target = {
            'a': {'y': 4, 'z': 5},
            'c': 6
        }
        
        result = deep_merge_dicts(source, target)
        expected = {
            'a': {'x': 1, 'y': 4, 'z': 5},
            'b': 3,
            'c': 6
        }
        
        assert result == expected
        
    def test_deep_merge_different_types(self):
        """测试不同类型值的处理"""
        source = {'a': {'nested': True}}
        target = {'a': 'not_dict'}
        
        result = deep_merge_dicts(source, target)
        # target值应该完全覆盖source值
        assert result == {'a': 'not_dict'}
        
    def test_deep_merge_inplace(self):
        """测试深度合并的原地操作"""
        source = {'a': {'x': 1}, 'b': 2}
        target = {'a': {'y': 3}, 'c': 4}
        
        result = deep_merge_dicts(source, target, inplace=True)
        
        assert source == {'a': {'x': 1, 'y': 3}, 'b': 2, 'c': 4}
        assert result is source
        
    def test_deep_merge_multiple_levels(self):
        """测试多层嵌套的深度合并"""
        source = {
            'level1': {
                'level2': {
                    'level3': {'a': 1, 'b': 2}
                }
            }
        }
        target = {
            'level1': {
                'level2': {
                    'level3': {'b': 3, 'c': 4}
                }
            }
        }
        
        result = deep_merge_dicts(source, target)
        expected = {
            'level1': {
                'level2': {
                    'level3': {'a': 1, 'b': 3, 'c': 4}
                }
            }
        }
        
        assert result == expected


class TestMergeMultipleDicts:
    """测试多字典合并功能"""
    
    def test_merge_multiple_basic(self):
        """测试基本的多字典合并"""
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        dict3 = {'c': 3}
        
        result = merge_multiple_dicts(dict1, dict2, dict3)
        expected = {'a': 1, 'b': 2, 'c': 3}
        
        assert result == expected
        
    def test_merge_multiple_with_conflicts(self):
        """测试有冲突key的多字典合并"""
        dict1 = {'a': 1, 'b': 1}
        dict2 = {'b': 2, 'c': 2}
        dict3 = {'c': 3, 'd': 3}
        
        result = merge_multiple_dicts(dict1, dict2, dict3)
        # 后面的字典应该覆盖前面的
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
        
        assert result == expected
        
    def test_merge_multiple_deep(self):
        """测试多字典的深度合并"""
        dict1 = {'a': {'x': 1}}
        dict2 = {'a': {'y': 2}}
        dict3 = {'a': {'z': 3}}
        
        result = merge_multiple_dicts(dict1, dict2, dict3, deep=True)
        expected = {'a': {'x': 1, 'y': 2, 'z': 3}}
        
        assert result == expected
        
    def test_merge_multiple_empty_list(self):
        """测试空列表的处理"""
        result = merge_multiple_dicts()
        assert result == {}
        
    def test_merge_multiple_single_dict(self):
        """测试单个字典的处理"""
        single_dict = {'a': 1, 'b': 2}
        result = merge_multiple_dicts(single_dict)
        
        assert result == single_dict
        assert result is not single_dict  # 应该是副本
        
    def test_merge_multiple_inplace(self):
        """测试多字典原地合并"""
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        dict3 = {'c': 3}
        original_dict1 = copy.copy(dict1)
        
        result = merge_multiple_dicts(dict1, dict2, dict3, inplace=True)
        
        # 第一个字典应该被修改
        assert dict1 == {'a': 1, 'b': 2, 'c': 3}
        assert result is dict1


if __name__ == "__main__":
    pytest.main([__file__]) 