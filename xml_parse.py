import xml.etree.ElementTree as ET
import sys

args = sys.argv

tree = ET.parse(args[1])
root = tree.getroot()

output = []
for item in root.findall('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Body/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Warning/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Item'):
  code = item.find('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Area/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Code')
  if code.text == '130011' or code.text == '130012':
    text = ''
    area_name = item.find('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Area/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Name')
    text += '【' + area_name.text + '】'
    list = []
    for kind in item.findall('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Kind'):
      kind_text = ''
      kind_name = kind.find('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Name')
      if not kind_name is None:
        kind_text += kind_name.text + '：'
      kind_status = kind.find('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Status')
      kind_text += kind_status.text
      list.append(kind_text)
    text += '、'.join(list)
    print(text)

print(output)
