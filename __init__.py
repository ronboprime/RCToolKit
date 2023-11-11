import bpy

class NODE_OT_add_node(bpy.types.Operator):
    bl_idname = "node.add_node"
    bl_label = "Add Node"
    
    # Property to hold the name of the node to add
    node_name: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'GeometryNodeTree'

    def execute(self, context):
        # Get the active node tree
        node_tree = context.space_data.node_tree

        # Create a new node
        new_node = node_tree.nodes.new(type=self.node_name)

        # Position the new node
        new_node.location = (0, 0)

        return {'FINISHED'}

class NODE_PT_my_panel(bpy.types.Panel):
    bl_label = "Node Groups"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout

        # Iterate over node groups
        for ng in bpy.data.node_groups:
            # Iterate over nodes in the group
            #for node in ng.nodes:
                # Create a button for the node
            op = layout.operator("node.add_node", text=ng.name)
                
                # Set the operator's node_name property
            op.node_name = ng.name
            print(ng)
                
classes=[NODE_PT_my_panel, NODE_OT_add_node]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        

register()


"""old shit
import bpy
bl_info = {
    "name": "RCToolKit",
    "description": "Starting Toolkit, featuring custom node groups, with minor UI Inclusion",
    "author": "Ronboprime",
    "email":"ronboprime@gmail.com",
    "version": (1, 3),
    "blender": (4, 0, 0),
    "location": "Node Editor> Navigation Bar> RCToolKit",
    "warning": "relax! You'll never make it out, alive!", 
    "doc_url": "https://www.ronboprime.com/current/rct/docs",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Node",
}

nodes=["Thouies","Hundoes","Tenths","Smoothing","Half/Double","Third/3x","Quarter/4x","Fifth/5x","Eighth/8x","Puppet","Camera Mockup","Broken At Ranges","Curve To Mesh","QuickInvert","QuickStartIco","QuickStartCube","QuickStartCone","QuickStartCurve","QuickStartTorus","QuickStartGrid"]
icons=["EMPTY_ARROWS","EMPTY_ARROWS","EMPTY_ARROWS","LINENUMBERS_ON","PREV_KEYFRAME","FF","NEXT_KEYFRAME","REW","SELECT_DIFFERENCE","IPO_BEZIER","SYSTEM","GP_SELECT_POINTS","SEQ_CHROMA_SCOPE","OUTLINER_DATA_CAMERA","PROP_PROJECTED","ORIENTATION_GIMBAL","MOD_PARTICLE_INSTANCE","MESH_CUBE","PROP_OFF","PROP_ON","MESH_GRID"]

data ={node:icon for (node,icon) in zip(nodes,icons)}

node_properties=bpy.context.scene.node_properties

class NodeProperties(bpy.types.PropertyGroup):
    thingo:bpy.props.StringProperty(
    name="taco",
    default="tiddy",
    description="tuesday"
    )

class NODE_OT_RCToolKitOperator(bpy.types.Operator):
    bl_idname='node.rctoperator'
    bl_label='RCToolKit Operator'

    CNode:bpy.props.StringProperty(
        name="Custom Node Name",
        description="For Swapping properties",
        default="Thouies"
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
    bl_idname="NODE_PT_rctpanel"
    bl_label=" -= RCToolKit =- "
    bl_space_type='NODE_EDITOR'
    bl_region_type='UI'
    bl_category='Tool'

    def draw(self,context):
        col=self.layout.column(align=True)
        doodle(col)

def doodle(col):
   for k,v in data.items():
     templ8="RCT-"+str(k)
     NODE_OT_RCToolKitOperator.CNode=templ8
     NODE_OT_RCToolKitOperator.INode=v
     col.operator("node.rctoperator",text=f"{templ8}", icon=f"{v}")

classes = [NodeProperties,NODE_OT_RCToolKitOperator,NODE_PT_RCToolKitPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        print(str(cls)+" Loaded")
    bpy.types.Scene.node_properties=bpy.props.PointerProperty(type=NodeProperties)        
    print("Properties assigned.")    
    print("RCToolKit Loaded")

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    print("Goodbye, cruel world!")    

register()
"""
