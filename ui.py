import bpy
""" Packages List """
class ConfigList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name, icon = "PACKAGE")

class CactusPanel(bpy.types.Panel):
    bl_idname = 'CACTUS_PT_panel'
    bl_label = 'Cactus Export'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Cactus'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        settings = scene.cactus_settings
        config_settings = scene.cactus_config_settings

        # Export All button
        row = layout.row()
        row.operator("cactus_export.export_all", text="Export All")
        row.operator("cactus_export.export_selected", text="Export Selected")

        layout.separator()

        """ Packages List """
        row = layout.row()
        column = row.column()
        column.template_list(
            "ConfigList",
            "cactus_config_list",
            scene.cactus_settings,
            "configs",
            scene.cactus_settings,
            "config_index"
        )

        column = row.column()
        column.operator("cactus_export.config_add", text="", icon="ADD")
        column.operator("cactus_export.config_remove", text="", icon="REMOVE")

        # row = layout.row()
        # row.operator('cactus_export.create_config', text='Add config')

        config_index = scene.cactus_settings.config_index
        configs = scene.cactus_settings.configs

        if len(configs) > 0:
            config = configs[config_index]

            col = layout.column()
            col.prop(config, 'export_type')

            if config.export_type == 'SELECTED_COLLECTIONS':
                col.prop(config, 'selected_collections')
            elif config.export_type == 'SELECTED_OBJECTS':
                col.prop(config, 'selected_objects')

            col.prop(config, 'directory')
            col.prop(config, 'format')
            col.prop(config, 'prefix')
            col.prop(config, 'suffix')
            col.prop(config, 'apply_modifiers')
            col.prop(config, 'center_collections')
