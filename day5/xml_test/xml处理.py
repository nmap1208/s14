#Auther nmap
import xml.etree.ElementTree as ET

# tree = ET.parse("xmltest.xml")
# root = tree.getroot()
# print(root.tag)
#
# #遍历xml文档
# for child in root:
#     print(child.tag, child.attrib)
#     for i in child:
#         print(i.tag,i.text)
#只遍历year 节点
# for node in root.iter('year'):
#     print(node.tag,node.text)

#
# #修改
# for node in root.iter('rank'):
#     new_rank = int(node.text) + 1
#     node.text = str(new_rank)
#     node.set("updated","second")
#
# tree.write("xmltest.xml")

# import xml.etree.ElementTree as ET
#
# tree = ET.parse("xmltest.xml")
# root = tree.getroot()
# #删除node
# for country in root.findall('country'):
#    rank = int(country.find('rank').text)
#    if rank > 50:
#      root.remove(country)
#
# tree.write('output.xml')



import xml.etree.ElementTree as ET


new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
sex.text = '33'
name2 = ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
age = ET.SubElement(name2,"age")
age.text = '19'

et = ET.ElementTree(new_xml) #生成文档对象
et.write("test.xml", encoding="utf-8",xml_declaration=True)

ET.dump(new_xml) #打印生成的格式





