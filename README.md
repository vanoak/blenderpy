# Import-Export Timeline Markers Add-On

* **print markers** - prints markers name, frame, time (using fps) and binded camera in blender console.
* **export markers** - outputs the same info as print markers, but saves it to a XML file in the home directory.
* **import markers** - imports the XML file data from the home directory, recreate the markers and bind the cameras. 

Built them in order to allow students to save their work between several versions of a composition/montage exercise I teach. The goal is to have a full add-on.

## Requirements

* Blender 2.76b

## Usage

The scripts run independently from each other, in blender's text editor. Just add a new text data block, paste the code and press "Run Script".