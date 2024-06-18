#!/bin/bash

# 初始化序号
counter=1

# 查找当前目录及子目录下所有以 _test.py 结尾的文件
find . -type f -name "*_test.py" | while read -r file; do
    # 移除文件路径前的 './'
    trimmed_path=$(echo "$file" | sed 's|^\./||')
    # 将路径中的 '/' 替换为 '.'
    module_path=$(echo "$trimmed_path" | sed 's|/|.|g' | sed 's|.py$||')

    # 打印序号和测试命令
    echo -e "\n[$counter] Testing command: python -m unittest $module_path"

    # 执行测试命令
    python -m unittest "$module_path"

    # 序号递增
    ((counter++))
done
