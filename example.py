#!/usr/bin/env python3
"""
Dict Merger 使用示例
演示字典合并功能的各种用法
"""

from dict_merger import merge_dicts, deep_merge_dicts
from dict_merger.merger import merge_multiple_dicts


def main():
    print("=" * 50)
    print("Dict Merger 包使用示例")
    print("=" * 50)
    
    # 示例1: 基本浅层合并
    print("\n1. 基本浅层合并:")
    source1 = {'name': 'Alice', 'age': 25}
    target1 = {'age': 26, 'city': '北京'}
    result1 = merge_dicts(source1, target1)
    print(f"源字典: {source1}")
    print(f"目标字典: {target1}")
    print(f"合并结果: {result1}")
    print("注意: age被目标值26覆盖")
    
    # 示例2: 深度合并嵌套字典
    print("\n2. 深度合并嵌套字典:")
    source2 = {
        'user': {
            'name': 'Bob',
            'profile': {
                'age': 30,
                'hobby': ['读书']
            }
        },
        'settings': {
            'theme': 'dark'
        }
    }
    target2 = {
        'user': {
            'profile': {
                'age': 31,
                'location': '上海'
            },
            'email': 'bob@example.com'
        },
        'settings': {
            'language': 'zh-CN'
        }
    }
    result2 = deep_merge_dicts(source2, target2)
    print(f"源字典: {source2}")
    print(f"目标字典: {target2}")
    print(f"深度合并结果: {result2}")
    print("注意: 嵌套字典被递归合并，age被覆盖为31")
    
    # 示例3: 浅层vs深度合并的对比
    print("\n3. 浅层 vs 深度合并对比:")
    source3 = {'config': {'debug': True, 'timeout': 30}}
    target3 = {'config': {'debug': False}}
    
    shallow_result = merge_dicts(source3, target3)
    deep_result = deep_merge_dicts(source3, target3)
    
    print(f"源字典: {source3}")
    print(f"目标字典: {target3}")
    print(f"浅层合并: {shallow_result}")
    print(f"深度合并: {deep_result}")
    print("注意: 浅层合并完全替换config，深度合并保留timeout")
    
    # 示例4: 原地修改
    print("\n4. 原地修改示例:")
    source4 = {'a': 1, 'b': 2}
    target4 = {'b': 3, 'c': 4}
    print(f"修改前源字典: {source4}")
    
    result4 = merge_dicts(source4, target4, inplace=True)
    print(f"修改后源字典: {source4}")
    print(f"返回结果: {result4}")
    print(f"是同一个对象: {result4 is source4}")
    
    # 示例5: 合并多个字典
    print("\n5. 合并多个字典:")
    dict1 = {'基础配置': {'版本': '1.0'}}
    dict2 = {'数据库': {'host': 'localhost'}}
    dict3 = {'缓存': {'redis': 'enabled'}}
    dict4 = {'基础配置': {'作者': '开发者'}}
    
    # 浅层合并多个字典
    shallow_multi = merge_multiple_dicts(dict1, dict2, dict3, dict4)
    print(f"浅层合并多个字典: {shallow_multi}")
    
    # 深度合并多个字典
    deep_multi = merge_multiple_dicts(dict1, dict2, dict3, dict4, deep=True)
    print(f"深度合并多个字典: {deep_multi}")
    print("注意: 深度合并保留了基础配置中的版本信息")
    
    # 示例6: 处理不同数据类型
    print("\n6. 处理不同数据类型:")
    source6 = {
        'data': {
            'numbers': [1, 2, 3],
            'text': 'original'
        }
    }
    target6 = {
        'data': {
            'numbers': [4, 5, 6],  # 列表会被直接覆盖
            'flag': True
        }
    }
    result6 = deep_merge_dicts(source6, target6)
    print(f"源字典: {source6}")
    print(f"目标字典: {target6}")
    print(f"合并结果: {result6}")
    print("注意: 列表等非字典类型会被直接覆盖，不会合并")


if __name__ == "__main__":
    main() 