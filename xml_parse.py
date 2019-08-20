import xml.etree.ElementTree as ET
tree = ET.parse('kisyou.xml')
root = tree.getroot()

output = []
for item in root.findall('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Body/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Warning/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Item'):
  code = item.find('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Area/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Code')
  if code.text == '130011' or code.text == '130012':
    text = ''
    area_name = item.find('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Area/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Name')
    text += '【' + area_name.text + '】'
    kind_name = item.find('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Kind/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Name')
    if not kind_name is None:
      text += kind_name.text + '：'
    kind_status = item.find('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Kind/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Status')
    text += kind_status.text
    print(text)

print(output)
