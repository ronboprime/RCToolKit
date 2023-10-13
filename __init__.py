import bpy

bl_info = {
    "name": "RCToolKit",
    "description": "Starting Toolkit, featuring custom node groups, with minor UI Inclusion",
    "author": "Ronboprime",
    "email":"ronboprime@gmail.com",
    "version": (1, 2),
    "blender": (3, 6, 4),
    "location": "Node Editor> Navigation Bar> RCToolKit",
    "warning": "relax! You'll never make it out, alive!", 
    "doc_url": "https://www.ronboprime.com/current/rct/docs",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Node",
}

class NODE_OT_FinTouOperator(bpy.types.Operator):
    """Utilizing the String Property, FNode , set by UI operator, to call node group, then a slight transform"""
    bl_idname = "node.fintouoperator"
    bl_label = "Finishing Touches"

    FNode:bpy.props.StringProperty(
    name="Finishing Touches NodeGroups",
    description="The Placeholder to call a given node group",
    default="Set Proxy Material"    
    )

    def execute(self, context):
        bpy.ops.node.add_node(
        use_transform=False,
        settings=[{"name":"node_tree",
        "value":f"bpy.data.node_groups['{self.FNode}']"}],
        type="GeometryNodeGroup")
        newnode = context.active_node
        newnode.location.x -= 400
        return {'FINISHED'}


class NODE_OT_ConstructsOperator(bpy.types.Operator):
    """Utilizing a String Property, ONode , set by UI operator, to call node group, and slight transform"""
    bl_idname = "node.constructsoperator"
    bl_label = "Constucts"

    ONode:bpy.props.StringProperty(
    name="Complex Constructs NodeGroups",
    description="Placeholder to call constructed groups",
    default="Puppet"    
    )

    def execute(self, context):
        bpy.ops.node.add_node(
        use_transform=False,
        settings=[{"name":"node_tree",
        "value":f"bpy.data.node_groups['{self.ONode}']"}],
        type="GeometryNodeGroup")
        newnode = context.active_node
        newnode.location.x -= 400
        return {'FINISHED'}

class NODE_OT_ShapesOperator(bpy.types.Operator):
    """Utilizing a String Property, SNode, set by UI operator, to call node group, and slight transform"""
    bl_idname = "node.shapesoperator"
    bl_label = "Shapes"

    SNode:bpy.props.StringProperty(
    name="Basic Shape NodeGroups",
    description="Placeholder to call shape groups",
    default="QuickStartCube"    
    )

    def execute(self, context):
        bpy.ops.node.add_node(
        use_transform=False,
        settings=[{"name":"node_tree",
        "value":f"bpy.data.node_groups['{self.SNode}']"}],
        type="GeometryNodeGroup")
        newnode = context.active_node
        newnode.location.x -= 400
        return {'FINISHED'}
    

class NODE_OT_MathsOperator(bpy.types.Operator):
    """Utilizing a String Property, CNode, set by UI operator, to call node group, with transform"""
    bl_idname = "node.mathsoperator"
    bl_label = "Add Custom NodeGroups"

    CNode:bpy.props.StringProperty(
    name="Simple Maths NodeGroups",
    description="Placeholder to call math groups",
    default="Thouies"
    )

    def execute(self, context):

        bpy.ops.node.add_node(
        use_transform=True,
        settings=[{"name":"node_tree",
                   "value":f"bpy.data.node_groups['{self.CNode}']"}]
                   ,type="GeometryNodeGroup")
        newnode = context.active_node
        newnode.location.x -= 400
        return {'FINISHED'}

class NODE_PT_MathPanel(bpy.types.Panel):
    bl_label="Simple Maths"
    bl_space_type="NODE_EDITOR"
    bl_region_type='UI'
    bl_category='RCToolKit'
    bl_idname='node.mathpanel'
    
    def draw(self, context):
        col=self.layout.column(align=True)
        props=col.operator("node.mathsoperator",text="Thouies", icon="EMPTY_ARROWS" )
        props.CNode="RCT-Thouies"
        props=col.operator("node.mathsoperator",text="Tenths", icon="EMPTY_ARROWS" )
        props.CNode="RCT-Tenths"
        props=col.operator("node.mathsoperator",text="Hundoes", icon="EMPTY_ARROWS" )
        props.CNode="RCT-Hundoes"
        props=col.operator("node.mathsoperator",text="Half/Double", icon="LINENUMBERS_ON" )
        props.CNode="RCT-Half/Double"
        props=col.operator("node.mathsoperator",text="Third/3x", icon="PREV_KEYFRAME" )
        props.CNode="RCT-Third/3x"
        props=col.operator("node.mathsoperator",text="Quarter/4x", icon="FF" )
        props.CNode="RCT-Quarter/4x"
        props=col.operator("node.mathsoperator",text="Fifth/5x", icon="NEXT_KEYFRAME" )
        props.CNode="RCT-Fifth/5x"
        props=col.operator("node.mathsoperator",text="Eighth/8x", icon="REW" )
        props.CNode="RCT-Eighth/8x"
        props=col.operator("node.mathsoperator",text="QuickInvert", icon="SELECT_DIFFERENCE" )
        props.CNode="RCT-QuickInvert"

class NODE_PT_ShapesPanel(bpy.types.Panel):
    bl_label="Shapes"
    bl_space_type="NODE_EDITOR"
    bl_region_type='UI'
    bl_category='RCToolKit'
    bl_idname='node.shapespanel'

    def draw(self,context):
        col=self.layout.column(align=True)
        props=col.operator("node.shapesoperator",text="Cube", icon="MESH_CUBE" )
        props.SNode="RCT-QuickStartCube"
        props=col.operator("node.shapesoperator",text="Cone", icon="PROP_OFF" )
        props.SNode="RCT-QuickStartCone"
        props=col.operator("node.shapesoperator",text="Icosphere", icon="PROP_ON" )
        props.SNode="RCT-QuickStartIco"
        props=col.operator("node.shapesoperator",text="Grid", icon="MESH_GRID" )
        props.SNode="RCT-QuickStartGrid"

class NODE_PT_ConstructsPanel(bpy.types.Panel):
    bl_label="Constructs"
    bl_space_type="NODE_EDITOR"
    bl_region_type='UI' 
    bl_category='RCToolKit'
    bl_idname='node.constructspanel'  

    def draw(self,context):
        col=self.layout.column(align=True)
        props=col.operator("node.constructsoperator",text="Puppet", icon="IPO_BEZIER" )
        props.ONode="RCT-Puppet"
        props=col.operator("node.constructsoperator",text="Broken At Ranges", icon="SYSTEM" )
        props.ONode="RCT-Broken At Ranges"
        props=col.operator("node.constructsoperator",text="Curved Line", icon="GP_SELECT_POINTS" )
        props.ONode="RCT-QuickStart Curve"
        props=col.operator("node.constructsoperator",text="Curved Icosphere", icon="SEQ_CHROMA_SCOPE" )
        props.ONode="RCT-Curve Ico"
        props=col.operator("node.constructsoperator",text="Camera Mockup", icon="OUTLINER_DATA_CAMERA")
        props.ONode="RCT-Camera Mockup"

class NODE_PT_FinTouPanel(bpy.types.Panel):
    bl_label="Finishing Touches"
    bl_space_type="NODE_EDITOR"
    bl_region_type='UI' 
    bl_category='RCToolKit'
    bl_idname='node.fintoupanel'

    def draw(self,context):
        col=self.layout.column(align=True)
        props=col.operator("node.fintouoperator",text="Set Proxy Material", icon="PROP_PROJECTED" )
        props.FNode="RCT-Set Proxy Material"
        props=col.operator("node.fintouoperator",text="Twisted Curves To Mesh", icon="ORIENTATION_GIMBAL" )
        props.FNode="RCT-Curve To Mesh"
        props=col.operator("node.fintouoperator",text="Dialed Smoothing", icon="MOD_PARTICLE_INSTANCE")
        props.FNode="RCT-Smoothing"


def register():
    bpy.utils.register_class(NODE_OT_MathsOperator)
    bpy.utils.register_class(NODE_OT_ShapesOperator)
    bpy.utils.register_class(NODE_OT_ConstructsOperator)
    bpy.utils.register_class(NODE_OT_FinTouOperator)
    print("Operators loaded")
    
    bpy.utils.register_class(NODE_PT_MathPanel)
    bpy.utils.register_class(NODE_PT_ShapesPanel)
    bpy.utils.register_class(NODE_PT_ConstructsPanel)
    bpy.utils.register_class(NODE_PT_FinTouPanel)
    print("UI Loaded")
    
def unregister():
    bpy.utils.unregister_class(NODE_OT_MathsOperator)
    bpy.utils.unregister_class(NODE_OT_ShapesOperator)
    bpy.utils.unregister_class(NODE_PT_MathPanel)
    bpy.utils.unregister_class(NODE_PT_ShapesPanel)
    bpy.utils.unregister_class(NODE_OT_ConstructsOperator) 
    bpy.utils.unregister_class(NODE_OT_FinTouOperator) 
    bpy.utils.unregister_class(NODE_PT_ConstructsPanel) 
    bpy.utils.unregister_class(NODE_PT_FinTouPanel) 
    print("Goodbye, cruel world!")
