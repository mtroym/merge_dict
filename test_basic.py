#!/usr/bin/env python3
"""
基本功能测试脚本 - 不依赖pytest
验证dict_merger包的核心功能
"""

import sys
from dict_merger import merge_dicts, deep_merge_dicts
from dict_merger.merger import merge_multiple_dicts


def test_basic_merge():
    """测试基本合并功能"""
    print("测试基本合并功能...")
    source = {'a': 1, 'b': 2}
    target = {'b': 3, 'c': 4}
    result = merge_dicts(source, target)
    expected = {'a': 1, 'b': 3, 'c': 4}
    
    assert result == expected, f"期望 {expected}, 得到 {result}"
    print("✓ 基本合并测试通过")


def test_deep_merge():
    """测试深度合并功能"""
    print("测试深度合并功能...")
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
    
    assert result == expected, f"期望 {expected}, 得到 {result}"
    print("✓ 深度合并测试通过")


def test_inplace_merge():
    """测试原地合并功能"""
    print("测试原地合并功能...")
    source = {'a': 1, 'b': 2}
    target = {'b': 3, 'c': 4}
    original_id = id(source)
    
    result = merge_dicts(source, target, inplace=True)
    
    assert source == {'a': 1, 'b': 3, 'c': 4}, f"源字典应该被修改，得到 {source}"
    assert result is source, "返回的结果应该是源字典本身"
    assert id(result) == original_id, "应该是同一个对象"
    print("✓ 原地合并测试通过")


def test_no_inplace_merge():
    """测试非原地合并功能"""
    print("测试非原地合并功能...")
    source = {'a': 1, 'b': 2}
    target = {'b': 3, 'c': 4}
    original_source = source.copy()
    
    result = merge_dicts(source, target, inplace=False)
    
    assert source == original_source, f"源字典不应该被修改，期望 {original_source}, 得到 {source}"
    assert result is not source, "返回的结果应该是新对象"
    assert result == {'a': 1, 'b': 3, 'c': 4}, f"合并结果错误，得到 {result}"
    print("✓ 非原地合并测试通过")


def test_multiple_dicts():
    """测试多字典合并功能"""
    print("测试多字典合并功能...")
    dict1 = {'a': 1}
    dict2 = {'b': 2}
    dict3 = {'c': 3}
    
    result = merge_multiple_dicts(dict1, dict2, dict3)
    expected = {'a': 1, 'b': 2, 'c': 3}
    
    assert result == expected, f"期望 {expected}, 得到 {result}"
    print("✓ 多字典合并测试通过")


def test_multiple_dicts_deep():
    """测试多字典深度合并功能"""
    print("测试多字典深度合并功能...")
    dict1 = {'a': {'x': 1}}
    dict2 = {'a': {'y': 2}}
    dict3 = {'a': {'z': 3}}
    
    result = merge_multiple_dicts(dict1, dict2, dict3, deep=True)
    expected = {'a': {'x': 1, 'y': 2, 'z': 3}}
    
    assert result == expected, f"期望 {expected}, 得到 {result}"
    print("✓ 多字典深度合并测试通过")


def test_overwrite_behavior():
    """测试覆盖行为"""
    print("测试key相同时目标值覆盖源值...")
    source = {'key': 'old_value', 'keep': 'this'}
    target = {'key': 'new_value'}
    
    result = merge_dicts(source, target)
    expected = {'key': 'new_value', 'keep': 'this'}
    
    assert result == expected, f"期望 {expected}, 得到 {result}"
    assert result['key'] == 'new_value', "目标值应该覆盖源值"
    print("✓ 覆盖行为测试通过")


def test_empty_dicts():
    """测试空字典处理"""
    print("测试空字典处理...")
    
    # 两个空字典
    result1 = merge_dicts({}, {})
    assert result1 == {}, f"两个空字典合并应该返回空字典，得到 {result1}"
    
    # 源为空
    result2 = merge_dicts({}, {'a': 1})
    assert result2 == {'a': 1}, f"源为空时应该返回目标字典，得到 {result2}"
    
    # 目标为空
    result3 = merge_dicts({'a': 1}, {})
    assert result3 == {'a': 1}, f"目标为空时应该返回源字典，得到 {result3}"
    
    print("✓ 空字典处理测试通过")


def test_deep_vs_shallow():
    """测试深度合并vs浅层合并的区别"""
    print("测试深度合并vs浅层合并的区别...")
    source = {'config': {'debug': True, 'timeout': 30}}
    target = {'config': {'debug': False}}
    
    shallow_result = merge_dicts(source, target)
    deep_result = deep_merge_dicts(source, target)
    
    # 浅层合并应该完全替换config
    assert shallow_result == {'config': {'debug': False}}, f"浅层合并错误，得到 {shallow_result}"
    
    # 深度合并应该保留timeout
    assert deep_result == {'config': {'debug': False, 'timeout': 30}}, f"深度合并错误，得到 {deep_result}"
    
    print("✓ 深度vs浅层合并差异测试通过")


def run_all_tests():
    """运行所有测试"""
    print("=" * 50)
    print("运行 Dict Merger 包基本功能测试")
    print("=" * 50)
    
    tests = [
        test_basic_merge,
        test_deep_merge,
        test_inplace_merge,
        test_no_inplace_merge,
        test_multiple_dicts,
        test_multiple_dicts_deep,
        test_overwrite_behavior,
        test_empty_dicts,
        test_deep_vs_shallow,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} 失败: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} 错误: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"测试结果: {passed} 通过, {failed} 失败")
    print("=" * 50)
    
    if failed == 0:
        print("🎉 所有测试都通过了！")
        return True
    else:
        print("❌ 有测试失败，请检查代码")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1) 