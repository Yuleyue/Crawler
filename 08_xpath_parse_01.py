#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/8 12:03
Email : adamyue@163.com
'''

from lxml import etree

xml = '''
<!--Users是一个根标签，必须只能有一个，而Users里面的子属性可以有多个-->
<!--根标签名字随意取-->
<Users>
    <user id="1">
        <name>张三</name>
        <age>18</age>
        <address>广州</address>
    </user>
    <userAttribute>都是爱学习的人</userAttribute>
    <user id="2">
        <name>李四</name>
        <age>25</age>
        <address>哈尔滨</address>
    </user>
 
    <!--以下是带有大于号小于号等特殊字符的写法-->
    <special>
        <![CDATA[
        5 > 2 && 3 < 5
    ]]>
    </special>
    <!--特殊字符用法二-->
    <special>  5 &gt; 2 &amp;&amp; 3 &lt; 5 </special>
</Users>
'''

et = etree.XML(xml)
# result = et.xpath('/Users/user/name/text()')[1]
result = et.xpath('/Users/user[@id="1"]/name/text()')
print(result)
