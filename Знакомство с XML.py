import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse(r'‪D:\Downloads\map1.osm')
root = tree.getroot()

count_tags = []
for val in root.findall('node'):
    tag = val.find('tag')
    count_tags.append('empty' if tag is None else 'have')

print(count_tags.count('have'), count_tags.count('empty'))