import bpy

nodes=["Thouies","Hundoes","Tenths","Smoothing","Half/Double","Third/3x","Quarter/4x","Fifth/5x","Eighth/8x","Puppet","Camera Mockup","Broken At Ranges","Curve To Mesh","QuickInvert","QuickStartIco","QuickStartCube","QuickStartCone","QuickStartCurve","QuickStartTorus","QuickStartGrid"]

class tuneupProperties(bpy.types.PropertyGroup):
    thingo:bpy.props.StringProperty(
    name="taco",
    default="tiddy",
    description=func("tuesday")
    )
class NODE_OT_RCToolKitOperator(bpy.types.Operator):
    bl_idname='node.rctoperator'
    bl_label='RCToolKit Operator'

    CNode:bpy.props.StringProperty(
        name="Custom Node",
        description="For Swapping properties",
        default="RCT-Thouies"
        )
    INode:bpy.props.StringProperty(
        name="Icon for menu",
        description="also for the swapping",
        default="EMPTY_ARROWS"
    )
    
    def execute(self,context):
        bpy.ops.node.add_node(
        use_transform=True,
        settings=[{"name":"node_tree",
               "value":f"bpy.data.node_groups['{self.CNode}']"}]
               ,type="GeometryNodeGroup")
        newnode = context.active_node
        newnode.location.x -= 400
        return {'FINISHED'}
    

class NODE_PT_RCToolKitPanel(bpy.types.Panel):
    bl_idname="NODE_OT_rctpanel"
    bl_label="RCToolKit Panel"
    bl_space_type='NODE_EDITOR'
    bl_region_type='UI'
    bl_category='RCToolKit'

    def draw(self,context):
        col=self.layout.column(align=True)
        doodle(col)
        
        
def doodle(col):
   for node in nodes:
     print(node)       
     templ8="RCT-"+str(node)
     NODE_OT_RCToolKitOperator.CNode=templ8
     col.operator("node.rctoperator",text=f"{templ8}",icon="EMPTY_ARROWS")
        
classes = [tuneupProperties,NODE_OT_RCToolKitOperator,NODE_PT_RCToolKitPanel]

def thing():
    tuneup_properties=bpy.context.scene.tuneup_properties
    
    print(tuneup_properties)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.tuneup_properties=bpy.props.PointerProperty(type=tuneupProperties)        

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == "__main__":
    register()
    
thing()
