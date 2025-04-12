import bpy

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

        # Export All button
        row = layout.row()
        row.operator("cactus_export.export_all", text="Export All")
        
        col = layout.column()
        col.prop(settings, 'directory')
        col.prop(settings, 'format')
        col.prop(settings, 'apply_modifiers')
        col.prop(settings, 'center_collections')