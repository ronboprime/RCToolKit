import bpy  

bl_info = {
    "name": "Display Local Nodes",
    "description": "Adds a display in your Node Editor, to show local nodes, in the Tool section.",
    "author": "RonboPrime",
    "email":"ronboprime@gmail.com",
    "version": (1, 5),
    "blender": (4,0,0),
    "location": "Node Editor> Navigation Bar> Tool",
    "warning": "", 
    "doc_url": "",
    "tracker_url": "",
    "category": "Node",
}

class NODE_OT_add_node_group(bpy.types.Operator):
    bl_idname = "node_ot.add_node_group"
    bl_label = "Add Node Group"
    bl_options={"REGISTER","UNDO"}
    # Property to hold the name of the node group to add
    node_group_name: bpy.props.StringProperty()

    def execute(self, context):
    #sanity check
        obj=bpy.context.active_object
        print(obj.name)

    #is this thing on?
        if obj==None:
            self.report({'WARNING'},"How can you have any node tree, if you don't have your active object!")
            
            return{"CANCELLED"}

    # Get the node groups
        node_groups = bpy.data.node_groups
        
    # Get the active node tree
        node_tree = context.space_data.node_tree
        print(node_tree.name)
        
    # what if there's no node tree?        
        try:
    # Create a new group node
            new_node = node_tree.nodes.new(type='GeometryNodeGroup')

    # Set the node group of the new node
            if node_tree.name!=self.node_group_name:
                new_node.node_tree = bpy.data.node_groups[self.node_group_name]
                new_node.location = (420, 420)
            else:
                return {'FINISHED'}

    # Handled.
        except AttributeError:
            self.report({'WARNING'}, "No active node tree found... Good heavens, fix your life man!")
            return {'CANCELLED'}
        return {"FINISHED"}


    
class NODE_PT_my_panel(bpy.types.Panel):
    bl_idname="NODE_PT_panel"
    bl_label = "Local Node Groups"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Tool"

    def draw(self, context):
    # specify the node tree
        node_tree=context.space_data.node_tree
        
    # Get the node groups
        node_groups=bpy.data.node_groups
    
    # Initialize the UI
        col = self.layout.column(align=True)
    
    # Iterate over node groups
        for ng in bpy.data.node_groups:
    
    # Create a button for the node group
          if ng.name != node_tree.name:
            op = col.operator("node_ot.add_node_group", text=ng.name,icon="KEYTYPE_JITTER_VEC")
    
    # Set the operator's node_group_name property
            op.node_group_name = ng.name

    #Registration                
classes=[NODE_PT_my_panel, NODE_OT_add_node_group]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__=="__main__":
    register()







"""
old version
import bpy

bl_info = {
    "name": "Display Local Nodes",
    "description": "Adds a display in your Node Editor, to show local nodes, in the Tool section.",
    "author": "Ronboprime",
    "email":"ronboprime@gmail.com",
    "version": (1, 5),
    "blender": (4,0,0),
    "location": "Node Editor> Navigation Bar> Tool",
    "warning": "", 
    "doc_url": "",
    "tracker_url": "",
    "category": "Node",
}

# Get all node groups
#node_tree = bpy.context.space_data.node_tree

class NODE_OT_add_node_group(bpy.types.Operator):
    bl_idname = "node_ot.add_node_group"
    bl_label = "Add Node Group"
    
    # Property to hold the name of the node group to add
    node_group_name: bpy.props.StringProperty()

    def execute(self, context):
    #sanity check
        obj=bpy.context.active_object
        print(obj)

    #is this thing on?
        if obj==None:
            self.report({'WARNING'},"how can you have any node tree, if you don't have your active object!")
            return{"CANCELLED"}

    # Get the node groups
        node_groups = bpy.data.node_groups

    # Get the active node tree
        node_tree = context.space_data.node_tree

    # what if there's no node tree?        
        try:
    # Create a new group node
            new_node = node_tree.nodes.new(type='GeometryNodeGroup')

    # Set the node group of the new node
            new_node.node_tree = bpy.data.node_groups[self.node_group_name]

    # Position the new node
            new_node.location = (420, 420)

    # Handled.
        except AttributeError:
            self.report({'WARNING'}, "No active node tree found... Good heavens, fix your life man!")
            return {'CANCELLED'}

    # If can do, do!
        return {'FINISHED'}

    
class NODE_PT_my_panel(bpy.types.Panel):
    bl_idname="NODE_PT_panel"
    bl_label = "Local Node Groups"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Tool"

    def draw(self, context):
    # Get the node groups
        node_groups=bpy.data.node_groups
    
    # Initialize the UI
        col = self.layout.column(align=True)
    
    # Iterate over node groups
        for ng in bpy.data.node_groups:
    
    # Create a button for the node group
            op = col.operator("node_ot.add_node_group", text=ng.name,icon="KEYTYPE_JITTER_VEC")
    
    # Set the operator's node_group_name property
            op.node_group_name = ng.name

    #Registration                
classes=[NODE_PT_my_panel, NODE_OT_add_node_group]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__=="__main__":
register()
"""


