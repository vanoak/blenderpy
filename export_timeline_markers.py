# save timeline markers name, frame, time and binded camera name to xml file. 

import bpy
from os.path import expanduser

scene = bpy.context.scene

fps = scene.render.fps
fps_base = scene.render.fps_base

def frame_to_time(frame_number):
    raw_time = (frame_number - 1) / fps
    return round(raw_time, 2)

xml = '<?xml version="1.0"?><root>'

for k, v in scene.timeline_markers.items():
    
    xml += '<timeline_marker name="' + str(k) + '" frame="' + str(v.frame) + '" camera="' + v.camera.name + '" frame_time="' + str(frame_to_time(v.frame)) + '"></timeline_marker>'


xml += '</root>'    

home = expanduser("~")
f =  open(home + "/timeline_markers.xml", "wt")
f.write(xml)
f.close()