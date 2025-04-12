import bpy
from bpy.props import *

class CactusSettings(bpy.types.PropertyGroup):
    directory: StringProperty(
        name    = 'Directory',
        subtype = 'DIR_PATH',
        default = '//'
    )
    
    format: EnumProperty(
        name    = 'Format',
        items   = [
            ('glTF', 'glTF (.glb/.gltf)', '', 1),
        ],
        default = 'glTF'
    )
    
    apply_modifiers: BoolProperty(
        name    = 'Apply modifiers',
        default = True
    )
    
    center_collections: BoolProperty(
        name    = 'Center collections',
        default = True
    )
