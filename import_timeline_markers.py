import bpy
from xml.dom.minidom import parse, parseString
from os.path import expanduser
import time

home = expanduser("~")
scene = bpy.context.scene

xml = parse(home + "/timeline_markers.xml")
markers = xml.getElementsByTagName("timeline_marker") 

markers_dict = {}

for c in range(len(markers)): 
    markers_dict[markers[c].attributes['name'].value] = {"frame":int(markers[c].attributes['frame'].value), "camera":markers[c].attributes['camera'].value}
    
for name, m_data in markers_dict.items():
    marker = scene.timeline_markers.new(name, frame=m_data["frame"])
    marker.camera = scene.objects.get(m_data["camera"])