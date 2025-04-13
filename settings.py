import bpy
from bpy.props import *

def on_update_name(self, context):
    print('update name')
    print(self.name)
    export_type = 'C'
    self.name = f'[{export_type}] {self.prefix}*{self.suffix}.{self.format}'

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
            ('FBX', 'FBX', '', 2),
        ],
        default = 'glTF',
        update = on_update_name
    )

    prefix: StringProperty(
        name    = 'Prefix',
        default = '',
        update = on_update_name
    )

    suffix: StringProperty(
        name    = 'Suffix',
        default = '',
        update = on_update_name
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

    config_index: IntProperty(
        name    = 'Config index',
        default = 0
    )
