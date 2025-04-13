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
    bl_category = 'Export'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        settings = scene.cactus_settings
        config_settings = scene.cactus_config_settings

        # Export All button
        row = layout.row()
        row.operator("cactus_export.export_all", text="Export All")

        layout.separator()

        """ Packages List """
        row = layout.row()
        column = row.column()
        column.template_list(
            "ConfigList",
            "cactus_config_list",
            scene.quick_exporter,
            "configs",
            scene.quick_exporter,
            "config_index"
        )

        column = row.column()
        column.operator("quick_exporter.add_item", text="", icon="ADD")
        column.operator("quick_exporter.remove_item", text="", icon="REMOVE")
        column.operator("quick_exporter.duplicate_item", text="", icon="DUPLICATE")
        column.operator("quick_exporter.move_item", text="", icon="TRIA_UP").direction = 'UP'
        column.operator("quick_exporter.move_item", text="", icon="TRIA_DOWN").direction = 'DOWN'

        # Define configs
        row = layout.row()
        row.operator('cactus_export.create_config', text='Add config')
        
        col = layout.column()
        col.prop(config_settings, 'name')
        col.prop(config_settings, 'directory')
        col.prop(config_settings, 'format')
        col.prop(config_settings, 'apply_modifiers')
        col.prop(config_settings, 'center_collections')