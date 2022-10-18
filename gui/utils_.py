import random
import sys
from itertools import zip_longest

from matplotlib import pyplot as plt

import constants
# from gui_entities import QueryT

import main
from entities import QueryState
from gui_entities import GuiElement
from entities.queries import QueryT

class GUI:
    x = [0]

    def drow_elements(self):
        self.ax.cla()
        plt.yticks(list(reversed(range(self.gui_level))), [el.type for el in self.elements])
        self.ax.set_xlim(self.x[-1]-5, self.x[-1]+5)
        self.ax.set_ylim(0,self.gui_level+1)
        self.x.append(self.x[-1]+1)
        gui_level = self.gui_level - 1
        for el in self.elements:
            self.ax.step(self.x, [gui_level+val for val in el.values])
            for i in range(len(el.values)):
                # pass
                self.ax.annotate(el.texts[i], (self.x[i], el.values[i]+gui_level))
            gui_level -= 1

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.fig.canvas.mpl_connect('key_press_event', self.press)
        self.gui_sources = [GuiElement("Source") for _ in range(constants.N_SOURCES)]
        self.gui_buffers = [GuiElement("Buffer") for _ in range(constants.N_BUFFERS)]
        self.gui_instruments = [GuiElement("Instrument") for _ in range(constants.N_INSTUMENTS)]
        self.gui_refuse = GuiElement("Refuse")
        self.elements = self.gui_sources + self.gui_buffers + self.gui_instruments + [self.gui_refuse]
        self.gui_level = constants.N_SOURCES + constants.N_BUFFERS + constants.N_INSTUMENTS + constants.N_REFUSE
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0,self.gui_level)
        plt.yticks(list(reversed(range(self.gui_level))), [el.type for el in self.elements])

    def update_source(self, query: QueryT):
        [el.add(0) for el in self.gui_sources]
        if query.state == QueryState.FROM_SOURCE:
            self.gui_sources[query.n_source].change_current(1, text=query.point_to_str())

    def update_buffer(self):
        for gui_b, b in zip_longest(self.gui_buffers, main.put_disp.buffers):
            if b:
                gui_b.add(1, text=b.point_to_str())
            else:
                gui_b.add(0)

    def update_instruments(self):
        for gui_i, i in zip(self.gui_instruments, main.instruments):
            if i.is_busy:
                gui_i.add(1, text=i.query.point_to_str())
            else:
                gui_i.add(0)

    def update_refuse(self):
        q = main.put_disp.refused_query
        if q:
            self.gui_refuse.add(1, q.point_to_str())
        else:
            self.gui_refuse.add(0)


    def press(self, event):
        print('press', event.key)
        if event.key == 'enter':
            q = main.update()
            print("DROW INPUT", q)
            self.update_source(q)
            self.update_buffer()
            self.update_instruments()
            self.update_refuse()
            self.drow_elements()
            print(self.gui_sources)
            print(self.x)
            plt.show()


gui = GUI()

plt.show()
