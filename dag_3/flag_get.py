import xml.etree.ElementTree as ET

xml_file = "handout.xml"

tree = ET.parse(xml_file)
root = tree.getroot()

namespace = {"ns": "http://schemas.microsoft.com/win/2004/08/events/event"}

query_names = []
flag = ""
for event in root.findall("ns:Event", namespace):
    process_id = event.find('.//ns:Data[@Name="ProcessId"]', namespace)
    if process_id is not None and process_id.text == "8360":
        query_name = event.find('.//ns:Data[@Name="QueryName"]', namespace)
        if query_name is not None:
            query_names.append(query_name.text)
for query_name in query_names:
    flag += query_name[0]
print(flag)
