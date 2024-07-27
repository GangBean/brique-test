# Example default data
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.ticker as ticker

class TableGraph:
    def __init__(self, root):
        self.root = root
        self.root.title("Monthly Temperature and Humidity")

        self.entries = []
        self.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        self.default_temperatures = [4.5, 5.2, 8.7, 14.4, 18.9, 22.7, 26.4, 27.8, 24.1, 18.1, 12.2, 7]
        self.default_humidities = [64, 61, 59, 60, 65, 71, 74, 70, 71, 68, 66, 65]

        # Create frames for table and graph
        self.table_frame = tk.Frame(root)
        self.table_frame.grid(row=0, column=0, padx=10, pady=10, sticky='n')
        
        self.graph_frame = tk.Frame(root)
        self.graph_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        # Configure grid weight to adjust resizing behavior
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.create_widgets()
        
    def create_widgets(self):
        # Create table inside table_frame
        tk.Label(self.table_frame, text="Month", borderwidth=1, relief="solid").grid(row=0, column=0, sticky='ew')
        tk.Label(self.table_frame, text="Average Temperature (°C)", borderwidth=1, relief="solid").grid(row=0, column=1, sticky='ew')
        tk.Label(self.table_frame, text="Average Humidity (%)", borderwidth=1, relief="solid").grid(row=0, column=2, sticky='ew', padx=(0, 20))  # Added padx for right alignment

        # Data entry fields with default values
        for i, month in enumerate(self.months):
            tk.Label(self.table_frame, text=month, borderwidth=1, relief="solid").grid(row=i+1, column=0, sticky='ew')
            temp_entry = tk.Entry(self.table_frame)
            temp_entry.grid(row=i+1, column=1, sticky='ew')
            temp_entry.insert(0, str(self.default_temperatures[i]))  # Set default value
            hum_entry = tk.Entry(self.table_frame)
            hum_entry.grid(row=i+1, column=2, sticky='ew')
            hum_entry.insert(0, str(self.default_humidities[i]))  # Set default value
            temp_entry.bind("<KeyRelease>", self.on_data_change)
            hum_entry.bind("<KeyRelease>", self.on_data_change)
            self.entries.append((temp_entry, hum_entry))

        # Create graph inside graph_frame
        self.fig, self.ax1 = plt.subplots(figsize=(10, 10))  # Adjust size to fit screen
        self.ax2 = self.ax1.twinx()  # Create second y-axis

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.config(width=800, height=600)
        self.canvas_widget.grid(row=0, column=0)

        # Initial plot
        self.plot_graph()
        
    def on_data_change(self, event):
        self.plot_graph()
    
    def plot_graph(self):
        months = self.months
        temperatures = []
        humidities = []

        for temp_entry, hum_entry in self.entries:
            try:
                temp = float(temp_entry.get())
                humidity = float(hum_entry.get())
                temperatures.append(temp)
                humidities.append(humidity)
            except ValueError:
                temperatures.append(None)
                humidities.append(None)

        self.ax1.clear()
        self.ax2.clear()
        
        lines = []
        labels = []

        if any(t is not None for t in temperatures):
            line1, = self.ax1.plot(months, temperatures, marker='o', color='tab:blue', label='Temperature (°C)')
            lines.append(line1)
            labels.append('Temperature (°C)')
            self.ax1.set_ylabel('Temperature (°C)', color='tab:blue')
            self.ax1.tick_params(axis='y', labelcolor='tab:blue')

        if any(h is not None for h in humidities):
            line2, = self.ax2.plot(months, humidities, marker='x', color='tab:green', label='Humidity (%)')
            lines.append(line2)
            labels.append('Humidity (%)')
            self.ax2.set_ylabel('Humidity (%)', color='tab:green', labelpad=20)  # Adjust the pad for y-axis label
            self.ax2.tick_params(axis='y', labelcolor='tab:green')

        self.ax1.set_title('Monthly Average Temperature and Humidity')
        self.ax1.set_xlabel('Month')

        # Set x-axis labels and tick positions
        self.ax1.set_xticks(range(len(months)))
        self.ax1.set_xticklabels(months, rotation=45, ha='right')

        # Add a single legend for both lines
        lines.extend(self.ax2.get_lines())
        self.ax1.legend(lines, labels, loc='upper left', bbox_to_anchor=(0, 1), frameon=True)

        # Adjust layout to fit within the window
        self.fig.tight_layout()

        self.canvas.draw()      
