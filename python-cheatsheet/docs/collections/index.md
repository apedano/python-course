#  🐍Collections

Notes and examples for `list`, `dict`, `set`, `tuple`, and friends.

!!! warning "Common pitfall"
    `list.append()` returns `None`

| Collection Type | Ordered | Mutable | Allows Duplicates | Indexed Access | Key-Value | Syntax Example      | Notes                                                 |
|-----------------|---------|---------|-------------------|----------------|-----------|---------------------|-------------------------------------------------------|
| list            | Yes     | Yes     | Yes               | Yes            | No        | [1, 2, 3]           | Dynamic array, most commonly used sequence            |
| tuple           | Yes     | No      | Yes               | Yes            | No        | (1, 2, 3)           | Immutable sequence, hashable if elements are hashable |
| set             | No*     | Yes     | No                | No             | No        | {1, 2, 3}           | Unordered collection of unique elements               |
| frozenset       | No*     | No      | No                | No             | No        | frozenset({1,2,3})  | Immutable version of set                              |
| dict            | Yes**   | Yes     | No (keys)         | Yes (by key)   | Yes       | {"a": 1}            | Key-value pairs, keys must be unique and hashable     |
| str             | Yes     | No      | Yes               | Yes            | No        | "hello"             | Immutable sequence of characters                      |
| bytes           | Yes     | No      | Yes               | Yes            | No        | b"hello"            | Immutable sequence of bytes                           |
| bytearray       | Yes     | Yes     | Yes               | Yes            | No        | bytearray(b"hello") | Mutable version of bytes                              |
| range           | Yes     | No      | No                | Yes            | No        | range(5)            | Immutable sequence of numbers                         |
