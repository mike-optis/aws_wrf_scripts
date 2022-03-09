import imageio
import glob
import sys

month = sys.argv[1]

# Create the frames
frames = []
imgs = glob.glob("./animations/ws_deficit_map/%s/*.jpg" % month)

for i in imgs:
    print(i)
    new_frame = imageio.imread(i)
    frames.append(new_frame)

# Save into a GIF file that loops forever
#frames[0].save('../animations/%s.gif' % month, format='GIF', append_images=frames[1:], save_all=True, duration=300, loop=0)
imageio.mimsave('./animations/%s.gif' % month, frames, fps = 6)
