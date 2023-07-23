import os

def list_files(startpath, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(startpath):
            # 移除隱藏資料夾
            dirs[:] = [d for d in dirs if not d[0] == '.']
            level = root.replace(startpath, '').count(os.sep)
            indent = '-' * 4 * (level)
            f.write('{}-{}/\n'.format(indent, os.path.basename(root)))
            subindent = '-' * 4 * (level + 1)
            for file in files:
                if file[0] != '.' and file != 'directory_tree.py':  # 不包括隱藏文件和這個腳本
                    f.write('{}{}\n'.format(subindent, file))

startpath = os.getcwd()  # 使用當前路徑
output_file = 'output.txt'
list_files(startpath, output_file)

