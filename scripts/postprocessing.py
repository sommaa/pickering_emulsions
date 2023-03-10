import bpy

#Import a txt file with the following format: x,y,z,Diameter
text_file = open("your_result.txt", "r")
lines = []

#Read in contents to a list
for line in text_file:
    lines.append(line.strip())

#create spheres
for e in lines:
    temp=e.split(',')
    bpy.ops.mesh.primitive_uv_sphere_add(segments = 64, ring_count = 32, location=(float(temp[0]),float(temp[1]),float(temp[2])),scale = (float(temp[3]),float(temp[3]),float(temp[3])))
    bpy.ops.object.shade_smooth()
    
text_file.close()
