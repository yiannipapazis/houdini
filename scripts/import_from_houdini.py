import bpy
import os
object_path = os.environ['OBJPATH']
export_path = os.environ['EXPPATH']

bpy.ops.import_scene.obj(filepath=object_path)

def draw_buttons(self, context):
    if context.region.alignment != 'RIGHT':
        layout = self.layout
        row = layout.row(align=True)

        row.operator(operator="scene.send_to_houdini", text="Done",
            emboss=True, icon="CHECKMARK")

class SendToHoudini(bpy.types.Operator):
    bl_idname = "scene.send_to_houdini"
    bl_label = "Send Back to Houdini"

    def execute(self, context):
        bpy.ops.export_scene.obj(filepath=export_path, use_selection=False)
        return {'FINISHED'}

def register():
    bpy.types.TOPBAR_HT_upper_bar.append(draw_buttons)
    bpy.utils.register_class(SendToHoudini)

def unregister():
    bpy.types.TOPBAR_HT_upper_bar.remove(draw_buttons)
    bpy.utils.unregister_class(SendToHoudini)

if __name__ == "__main__":
    register()
