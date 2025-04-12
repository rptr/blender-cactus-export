import bpy, os, mathutils

class CactusExportAll(bpy.types.Operator):
    bl_idname = "cactus_export.export_all"
    bl_label = "Export All"

    def execute(self, context):
        self.report({'INFO'}, "Exporting all selected objects...")
        
        settings = context.scene.cactus_settings
        base_dir = settings.directory
        base_dir = bpy.path.abspath(base_dir)

        selection = context.selected_objects
        
        if not os.path.isdir(base_dir):
            self.report({'ERROR'}, 'Invalid export directory')
            return {'FINISHED'}

        # Collection export
        for collection in bpy.data.collections.values():
            bpy.ops.object.select_all(action='DESELECT')
            
            for object in collection.objects:
                object.select_set(True)
                
            if context.selected_objects:
                self.export_selection(collection.name, context, base_dir)
        
        # Reset selection
        bpy.ops.object.select_all(action='DESELECT')
        
        for object in selection:
            object.select_set(True)
        
        return {'FINISHED'}
    

    def export_selection(self, name, context, directory):
        selected = context.selected_objects
        settings = context.scene.cactus_settings
        locations = []
        collection_center = mathutils.Vector((-1, 0, 0))
        
        if settings.center_collections:
            for object in selected:
                collection_center += object.location
                
            collection_center /= len(selected)
        
        for object in selected:
            locations.append(object.location.copy())
            
            # This will export every collection at (-1, 0, 0)
            object.location = object.location - collection_center
        
        filepath = os.path.join(directory, name)
        
        options = {}
        options['filepath'] = filepath
        options['use_selection'] = True
        options['export_apply'] = True
        bpy.ops.export_scene.gltf(**options)
        
        for i in range(len(selected)):
            selected[i].location = locations[i] 
