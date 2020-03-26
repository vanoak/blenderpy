# show timeline markers name, frame, time and binded camera name. 

import bpy

scene = bpy.context.scene

fps = scene.render.fps
fps_base = scene.render.fps_base

def frame_to_time(frame_number):
    raw_time = (frame_number - 1) / fps
    return round(raw_time, 2)

for k, v in scene.timeline_markers.items():
    frame = v.frame
    camera = v.camera.name
    frame_time = frame_to_time(frame)
    print("marker name: %s" % k, "frame: %i" % frame, "time: %f" % frame_time, "camera name: %s " % camera)