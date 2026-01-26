import tkinter as tk
from tkinter import messagebox, ttk
import datetime
import threading
import time

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("⏰ Alarm Clock Pro")
        self.root.geometry("400x500")
        self.root.resizable(True, True)
       
        self.active_alarms = []
       
        self.setup_ui()
        self.update_clock()
   
    def setup_ui(self):
        """إعداد الواجهة"""
        self.clock_label = ttk.Label(self.root, text="",
                                    font=("Arial", 24, "bold"))
        self.clock_label.pack(pady=20)
       
        setup_frame = ttk.LabelFrame(self.root, text="Set New Alarm", padding=15)
        setup_frame.pack(fill=tk.X, padx=20, pady=10)
       
        time_frame = ttk.Frame(setup_frame)
        time_frame.pack(fill=tk.X, pady=5)
       
        ttk.Label(time_frame, text="Hour:").grid(row=0, column=0)
        self.hour_var = tk.StringVar(value="12")
        hour_spin = ttk.Spinbox(time_frame, from_=0, to=23, width=5,
                               textvariable=self.hour_var, format="%02.0f")
        hour_spin.grid(row=0, column=1, padx=5)
       
        ttk.Label(time_frame, text="Minute:").grid(row=0, column=2)
        self.minute_var = tk.StringVar(value="00")
        minute_spin = ttk.Spinbox(time_frame, from_=0, to=59, width=5,
                                 textvariable=self.minute_var, format="%02.0f")
        minute_spin.grid(row=0, column=3, padx=5)
       
        ttk.Label(time_frame, text="Message:").grid(row=1, column=0, pady=(10,0))
        self.message_var = tk.StringVar(value="Wake up! ⏰")
        message_entry = ttk.Entry(time_frame, textvariable=self.message_var, width=20)
        message_entry.grid(row=1, column=1, columnspan=3, sticky="ew", pady=(10,0))
       
        ttk.Button(setup_frame, text="🚨 Set Alarm",
                  command=self.set_alarm).pack(pady=10)
       
        list_frame = ttk.LabelFrame(self.root, text="Active Alarms", padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
       
        listbox_frame = ttk.Frame(list_frame)
        listbox_frame.pack(fill=tk.BOTH, expand=True)
       
        self.alarms_listbox = tk.Listbox(listbox_frame, height=6)
        scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL,
                                 command=self.alarms_listbox.yview)
        self.alarms_listbox.configure(yscrollcommand=scrollbar.set)
       
        self.alarms_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
       
        ttk.Button(list_frame, text="🗑️ Delete Selected",
                  command=self.delete_alarm).pack(pady=5)
        ttk.Button(list_frame, text="⏹️ Stop All",
                  command=self.stop_all_alarms).pack(pady=2)
       
        self.status_var = tk.StringVar(value="No active alarms")
        status_bar = ttk.Label(self.root, textvariable=self.status_var,
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
   
    def update_clock(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=now)
        self.root.after(1000, self.update_clock)
   
    def alarm_thread(self, alarm_time, message):
        while alarm_time > datetime.datetime.now():
            time.sleep(1)
    
        self.root.after(0, lambda: self.trigger_alarm(message))
   
    def set_alarm(self):
        try:
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            message = self.message_var.get().strip()
           
            alarm_time = datetime.datetime.now().replace(
                hour=hour, minute=minute, second=0, microsecond=0
            )
           
            if alarm_time <= datetime.datetime.now():
                alarm_time += datetime.timedelta(days=1)
           
            alarm_id = len(self.active_alarms)
            self.active_alarms.append({
                'id': alarm_id,
                'time': alarm_time,
                'message': message
            })
           
            threading.Thread(target=self.alarm_thread,
                           args=(alarm_time, message), daemon=True).start()
           
            self.update_alarms_list()
            self.status_var.set(f"Alarm #{alarm_id} set for {alarm_time.strftime('%H:%M')}")
           
        except ValueError:
            messagebox.showerror("Error", "Invalid time format!")
   
    def trigger_alarm(self, message):
        
        messagebox.showinfo("⏰ ALARM!", message)
        self.status_var.set("Alarm triggered!")
   
    def update_alarms_list(self):
        self.alarms_listbox.delete(0, tk.END)
        for alarm in self.active_alarms:
            time_str = alarm['time'].strftime("%H:%M")
            self.alarms_listbox.insert(tk.END, f"{time_str} - {alarm['message'][:30]}...")
   
    def delete_alarm(self):
        selection = self.alarms_listbox.curselection()
        if selection:
            index = selection[0]
            del self.active_alarms[index]
            self.update_alarms_list()
            self.status_var.set("Alarm deleted")
   
    def stop_all_alarms(self):
        self.active_alarms.clear()
        self.update_alarms_list()
        self.status_var.set("All alarms stopped")

def main():
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()