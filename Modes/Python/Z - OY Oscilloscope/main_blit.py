import audioop
import time
from functools import partial

import alsaaudio
import numpy as np
import pygame
import pygame.gfxdraw

import sound

max_stereo_buffer_size = 1000


def get_avg_sample(data, i):
    avg = audioop.getsample(data, 2, i * 3)
    avg += audioop.getsample(data, 2, (i * 3) + 1)
    avg += audioop.getsample(data, 2, (i * 3) + 2)
    avg = avg / 3
    return avg


def stereo_recv(etc):
    start = time.time()
    # get audio
    l, data = sound.inp.read()
    peak = 0
    while l:
        try:
            # Extract right channel
            mono_data = audioop.tomono(data, 2, 1, 1)
            left_data = audioop.tomono(data, 2, 1, 0)
            right_data = audioop.tomono(data, 2, 0, 1)
        except:
            continue

        for i in range(0, 100):
            try:
                # Add to stereo buffer
                etc.audio_lin.append(get_avg_sample(left_data, i))
                etc.audio_rin.append(get_avg_sample(right_data, i))

                # "Original" code
                avg = get_avg_sample(mono_data, i)

                # scale it
                avg = int(avg * etc.audio_scale)
                if(avg > 20000):
                    sound.trig_this_time = time.time()
                    if (sound.trig_this_time - sound.trig_last_time) > .05:
                        if etc.audio_trig_enable: etc.audio_trig = True
                        sound.trig_last_time = sound.trig_this_time
                if avg > peak:
                    etc.audio_peak = avg
                    peak = avg
                # if the trigger button is held
                if(etc.trig_button):
                    etc.audio_in[i] = sound.sin[i]
                else:
                    etc.audio_in[i] = avg
            except:
                pass
        l, data = sound.inp.read()

    if len(etc.audio_lin) > max_stereo_buffer_size:
        etc.audio_lin = etc.audio_lin[-max_stereo_buffer_size:]
    if len(etc.audio_rin) > max_stereo_buffer_size:
        etc.audio_rin = etc.audio_rin[-max_stereo_buffer_size:]
    # log_time('recv', start)


def patch_sound_inp_recv(etc):
    # Set 2 new variable : left/right audio in
    etc.audio_lin = []
    etc.audio_rin = []

    # Close Mono PCM
    sound.inp = None

    # Open Stero PCM
    sound.inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)
    sound.inp.setchannels(2)
    # sound.inp.setrate(11025)
    sound.inp.setrate(11025)  # 44100
    sound.inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    sound.inp.setperiodsize(300)

    # Patch sound.recv to handle stereo
    sound.recv = partial(stereo_recv, etc)


def setup(screen, etc):
    patch_sound_inp_recv(etc)


def draw(screen, etc):
    start = time.time()
    etc.color_picker_bg(etc.knob5)

    gain = 5 * etc.knob1

    width = max(1, int(etc.knob2 * 20))
    closed = False
    radius = max(1, int(etc.knob2 * 20))
    color = etc.color_picker(etc.knob4)

    nb_samples = len(etc.audio_rin)
    nb_points = int(etc.knob3 * nb_samples)

    # pixels = np.zeros((etc.xres, etc.yres, 3), dtype=np.int16)
    # points = []
    for idx in range(nb_points):
        x, y = _get_xy(etc.xres, etc.yres, etc.audio_lin, etc.audio_rin, idx)
        # points.append((x, y))
        # pixels[x, y] = color
        screen.set_at((x, y), color)
        # pygame.draw.circle(screen, color, (x, y), radius)
    # pygame.surfarray.blit_array(screen, pixels)

    """
    if len(points) > 1:
        pygame.draw.lines(screen, color, closed, points, width)
    """
    # log_time('draw', start)


def _get_value(gain, res, channel, idx):
    return int(res * (0.5 + gain * 2.0 * channel[idx] / 32767.0 / 2))


def _get_xy(xres, yres, lin, rin, idx):
    x = int(xres * (0.5 + lin[idx] / 32767.0 / 2))
    y = int(yres * (0.5 + rin[idx] / 32767.0 / 2))
    return x, y


def log_time(name, start):
    if int(time.time() * 1000) % 10 == 1:
        print('%s %s ms' % (name, int((time.time() - start) * 1000)))

