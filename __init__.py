bl_info = {
    "name": "Cactus Export",
    "version" : (0, 0, 1),
    "blender": (4, 4, 0),
    "category": "Import-Export",
}

import bpy, os, mathutils
from bpy.props import *

from . import operators, settings, ui

ordered_classes = [operators.CactusExportAll, operators.CactusConfigAdd, operators.CactusConfigRemove, operators.CactusExportSelected,
                   ui.CactusPanel, ui.ConfigList, 
                   settings.CactusExportSettings, settings.CactusSettings]

def register():
    for cls in ordered_classes:
        bpy.utils.register_class(cls)
        
    bpy.types.Scene.cactus_settings = PointerProperty(type=settings.CactusSettings)
    bpy.types.Scene.cactus_config_settings = PointerProperty(type=settings.CactusExportSettings)

def unregister():
    for cls in reversed(ordered_classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
