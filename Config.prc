# Force a software-compatible Panda3D display fallback
# This helps when the machine has no usable OpenGL/DirectX pipe.
load-display p3tinydisplay
aux-display pandagl
aux-display pandadx9

win-origin -2 -2
win-size 1280 720
fullscreen #f

framebuffer-hardware #f
framebuffer-software #t

depth-bits 24
color-bits 24 24 24
alpha-bits 0
stencil-bits 0
multisamples 0

want-directtools #f
want-tk #f
show-frame-rate-meter #f
want-pstats #f

notify-level warning
default-directnotify-level warning
