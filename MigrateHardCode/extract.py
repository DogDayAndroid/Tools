import sys
import re

# 读取参数
filePath=sys.argv[1]

# 输出列表
outputStrings = []
fixFile=""

try:
    fileXML = open(filePath, 'r')
    contents = fileXML.readlines()
    pattern=re.compile(r'android:(title|summary)="([^@].+)"')
    pattern_fix=re.compile(r'[^(a-zA-Z)]')
    for content in contents:
        for match in pattern.finditer(content):
            origin_content = match.group(0)
            extract_content = match.group(2)
            fix_extract_content = pattern_fix.sub("_",extract_content)
            outputStrings.append('<string name="%s">%s</string>'%(fix_extract_content,extract_content))
            fix_origin_content = origin_content.replace(extract_content,"@string/"+fix_extract_content)
            content = content.replace(origin_content,fix_origin_content)
        fixFile+=content
    print(fixFile)
    # 打开一个文件
    fo = open("fix_xml.xml", "w")
    fo.write(fixFile)
    # 关闭打开的文件
    fo.close()
    print("\n".join(outputStrings))
    # 打开一个文件
    fo = open("fix_strings.xml", "w")
    fo.write("\n".join(outputStrings))
    # 关闭打开的文件
    fo.close()
    
    ### 输出 ###
    # hello
finally:
    if fileXML:
        fileXML.close()