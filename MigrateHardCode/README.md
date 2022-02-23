# 硬编码抽取小工具

利用Python自动抽取安卓的布局文件或者其他文件中的`android:title`或者`android:summary`中的硬编码。

抽取完成的`string.xml`添加项会保存在f`ix_strings.xml`，而布局文件会保存在`fix_xml.xml`中。

配合`idea`的外部工具功能可以实现自动抽取功能，方便进行应用翻译。