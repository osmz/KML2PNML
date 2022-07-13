import xml.etree.ElementTree as ET

def write_Xml():
    # Father of the network - has no children
    xml = ET.Element('xml')
    xml.set('version', '1.0')
    xml.set('encoding', 'ISO-8859-1')
   
    return xml