# Directory Tree Generator

這個 Python 程式碼用於生成一個特定目錄下的資料夾結構樹並將其輸出到一個文本文件中。

## 使用方式

直接運行這個 Python 腳本即可。它將會讀取當前工作目錄並生成一個與該目錄相對應的資料夾結構樹，然後將這個結構樹寫入到一個名為 "output.txt" 的文件中。

```bash
python directory_tree_generator.py
```

## 功能特性

生成資料夾結構樹：這個腳本使用 Python 的 os 模塊來遍歷當前工作目錄下的所有子目錄和文件，並將這些信息格式化為一個資料夾結構樹。

忽略隱藏資料夾和特定文件：這個腳本會忽略名稱以 "." 開頭的所有資料夾和文件（即隱藏資料夾和文件），以及名為 "directory_tree_generator.py" 的文件。

輸出格式：資料夾結構樹將被寫入到一個文本文件中，每個資料夾和文件都位於一行，並且根據其在目錄樹中的位置進行適當的縮排。資料夾名稱後面會加上 '/'，並且在資料夾名稱前添加了"-"符號。

## 注意事項

此程式碼需要在具有讀寫文件系統權限的環境中運行。
