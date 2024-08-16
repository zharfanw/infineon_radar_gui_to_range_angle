import random
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

import matplotlib.animation as animation


fps = 30
nSeconds = 5
snapshots = [ np.random.rand(5,6) for _ in range( nSeconds * fps ) ]
snapshots2 = [ np.random.rand(5,6) for _ in range( nSeconds * fps ) ]
snapshots3 = [ np.random.rand(5,6) for _ in range( nSeconds * fps ) ]

# First set up the figure, the axis, and the plot element we want to animate
# fig = plt.figure( figsize=(8,8) )
fig, axes = plt.subplots(1, 3, figsize=(8, 12))  # Adjust figsize for better layout

# Initialize plots (one for each subplot)
ims = []
for ax in axes:
    a = snapshots[0]
    print(np.shape(a))
    im = ax.imshow(a, interpolation='none', aspect='auto', vmin=0, vmax=1)
    ims.append(im)

# a = snapshots[0]
# im = plt.imshow(a, interpolation='none', aspect='auto', vmin=0, vmax=1)

def animate_func(i):
    if i % fps == 0:
        print( '.', end ='' )

    ims[0].set_array(snapshots[i])
    ims[1].set_array(snapshots2[i])
    ims[2].set_array(snapshots3[i])
    # return [im]

anim = animation.FuncAnimation(
                               fig, 
                               animate_func, 
                               frames = nSeconds * fps,
                               interval = 1000 / fps, # in ms
                               )

# anim.save('test_anim.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])

print('Done!')

plt.show()  # Not required, it seems!