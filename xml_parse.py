import xml.etree.ElementTree as ET
import sys
import glob

for xml_file in glob.glob("./samples/*"):
  print('---------------------------------')
  print(xml_file)
  tree = ET.parse(xml_file)
  root = tree.getroot()
  
  for item in root.findall('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Body/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Warning/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Item'):
    code = item.find('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Area/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Code')
    if code.text == '130011' or code.text == '130012' or True:
      area_name = item.find('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Area/{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Name')
      list = []
      for kind in item.findall('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Kind'):
        kind_text = ''
        kind_name = kind.find('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Name')
        if kind_name is None:
          continue
        if not '警報' in kind_name.text:
          continue
        kind_text += kind_name.text + '：'
        kind_status = kind.find('./{http://xml.kishou.go.jp/jmaxml1/body/meteorology1/}Status')
        kind_text += kind_status.text
        list.append(kind_text)
      if not list:
        continue
      text = '【' + area_name.text + '】' + '、'.join(list)
      print(text)
