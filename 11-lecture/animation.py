import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

u0 = lambda x : np.exp(-100*(x-0.5)**2) # Начальное условие
# xx = np.linspace(0,1,100)
# plt.plot(xx, u0(xx))

N = 100 # число интервалов по x
T = 1 # Конечный момент времени
nt = 100 # Число шагов по времени
h = 1/N
dt = T/nt
x = np.linspace(0, 1, N+1)
t = np.linspace(0, T, nt+1)
U = np.zeros((nt + 1, N + 1)) # Численное решение
U[0,:] = u0(x)

# 
# Реализация метода здесь
#


# 
# Так можно сделать анимацию (нужно запустить не в Jupyter)
#

# Удалите это, когда получите численное решение
for i in range(1, N+1):
    U[i,:] = U[0,:] * (N - i)/N

fig, ax = plt.subplots()

line, = ax.plot(x, u0(x))

def init():
    line.set_ydata([np.nan] * len(x))
    return line,

def animate(i):
    line.set_ydata(U[i,:])  # update the data.
    return line,
# interval - расстояние между кадрами в миллисекундах
ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=100, frames = np.arange(nt+1), blit=True, save_count=50)

# To save the animation, use e.g.
#
#ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()