# Dict Merger

一个简单而强大的Python包，用于合并字典。支持浅层合并和深度合并，当key相同时目标值会覆盖源值。

## 特性

- 🔄 **浅层合并**: 简单的字典合并，目标值覆盖源值
- 🏗️ **深度合并**: 递归合并嵌套字典结构
- 📦 **多字典合并**: 一次性合并多个字典
- ⚡ **高性能**: 优化的合并算法
- 🛡️ **类型安全**: 完整的类型提示支持

## 安装

```bash
pip install dict-merger
```

## 使用方法

### 导入

```python
from dict_merger import merge_dicts, deep_merge_dicts
```

### 浅层合并

```python
source = {'a': 1, 'b': 2}
target = {'b': 3, 'c': 4}

result = merge_dicts(source, target)
print(result)  # {'a': 1, 'b': 3, 'c': 4}
```

### 深度合并

```python
source = {
    'user': {
        'name': 'Alice',
        'age': 25
    },
    'settings': {
        'theme': 'dark'
    }
}

target = {
    'user': {
        'age': 26,
        'email': 'alice@example.com'
    },
    'settings': {
        'language': 'zh-CN'
    }
}

result = deep_merge_dicts(source, target)
print(result)
# {
#     'user': {
#         'name': 'Alice',
#         'age': 26,
#         'email': 'alice@example.com'
#     },
#     'settings': {
#         'theme': 'dark',
#         'language': 'zh-CN'
#     }
# }
```

### 原地修改

```python
source = {'a': 1, 'b': 2}
target = {'b': 3, 'c': 4}

# 修改原始字典
merge_dicts(source, target, inplace=True)
print(source)  # {'a': 1, 'b': 3, 'c': 4}
```

### 合并多个字典

```python
from dict_merger.merger import merge_multiple_dicts

dict1 = {'a': 1}
dict2 = {'b': 2}
dict3 = {'c': 3}

result = merge_multiple_dicts(dict1, dict2, dict3)
print(result)  # {'a': 1, 'b': 2, 'c': 3}

# 深度合并多个字典
result = merge_multiple_dicts(dict1, dict2, dict3, deep=True)
```

## API参考

### merge_dicts(source, target, inplace=False)

浅层合并两个字典。

**参数:**
- `source` (dict): 源字典
- `target` (dict): 目标字典，其值会覆盖source中相同key的值
- `inplace` (bool): 是否在原地修改source字典，默认False

**返回:** 合并后的字典

### deep_merge_dicts(source, target, inplace=False)

深度合并两个字典，递归处理嵌套结构。

**参数:**
- `source` (dict): 源字典
- `target` (dict): 目标字典，其值会覆盖source中相同key的值
- `inplace` (bool): 是否在原地修改source字典，默认False

**返回:** 深度合并后的字典

### merge_multiple_dicts(*dicts, deep=False, inplace=False)

合并多个字典。

**参数:**
- `*dicts`: 要合并的字典列表
- `deep` (bool): 是否进行深度合并，默认False
- `inplace` (bool): 是否在原地修改第一个字典，默认False

**返回:** 合并后的字典

## 开发

### 运行测试

```bash
python -m pytest tests/
```

### 安装开发依赖

```bash
pip install -e .[dev]
```

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！ 