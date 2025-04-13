import bpy
from bpy.props import *


class CactusExportSettings(bpy.types.PropertyGroup):
    name: StringProperty(
        name    = 'Name',
        default = 'Untitled'
    )

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

    collections: CollectionProperty(
        name    = 'Collections',
        type    = bpy.types.PropertyGroup
    )

    export_type: EnumProperty(
        name    = 'Export all collections',
        items   = [
            ('ALL COLLECTIONS', 'All collections', '', 1),
            ('COLLECTIONS', 'Collections', '', 2),
        ],
        default = 'ALL COLLECTIONS'
    )


class CactusSettings(bpy.types.PropertyGroup):
    configs: CollectionProperty(
        name    = 'Configs',
        type    = CactusExportSettings
    )
