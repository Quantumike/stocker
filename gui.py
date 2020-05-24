#Dependencies start
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
#Dependencies end

#Class definition
class GUI():
    #Method to show the main window
    def showGUI(self):
        #Initialize main loop and also set simple attributes to the main window
        window = tk.Tk()
        window.state('zoomed')
        window.resizable(False, False)
        window.title('Stocker')
        return window

    #Method to plot all the selected data
    def plotmatplot(self, windowObject):
        #Create a figure containing the plot
        fig, axs = plt.subplots(3, 1)
        fig.tight_layout()
        
        t = np.arange(0, 3, .01)
        #Setup subplot 1 - Closes
        axs[0].plot(t, 2 * np.sin(2 * np.pi * t))
        axs[0].set_title('Closes')
        axs[0].set_xlabel('Days')
        axs[0].set_ylabel('Value')
        #Setup subplot 2 - MACD
        axs[1].plot(t, 2 * np.sin(2 * np.pi * t))
        axs[1].set_title('MACD')
        axs[1].set_xlabel('Days')
        axs[1].set_ylabel('Value')
        #Setup subplot 3 - RSI
        axs[2].plot(t, 2 * np.sin(2 * np.pi * t))
        axs[2].set_title('RSI')
        axs[2].set_xlabel('Days')
        axs[2].set_ylabel('Value')

        #Create a canvas expanded to its master window extents
        canvas = FigureCanvasTkAgg(fig, master=windowObject)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,expand=1)
        #Create a navigation toolbar
        toolbar = NavigationToolbar2Tk(canvas,windowObject)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,expand=1)




