import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import threading
import sys

alarm_running = False


# -------- SOUND --------
def play_sound():
    try:
        if sys.platform.startswith("win"):
            import winsound
            for _ in range(6):
                winsound.Beep(1200, 400)
        else:
            print("\a")
    except:
        pass


def update_clock():
    now = datetime.now().strftime("%H:%M:%S")
    lbl_clock.config(text=now)
    root.after(1000, update_clock)


def start_alarm():
    global alarm_running
    alarm_time = entry_time.get()

    try:
        datetime.strptime(alarm_time, "%H:%M:%S")
    except:
        messagebox.showerror("Error", "Use format HH:MM:SS")
        return

    alarm_running = True
    lbl_status.config(text=f"Alarm set for {alarm_time}")

    threading.Thread(target=check_alarm, args=(alarm_time,), daemon=True).start()


def stop_alarm():
    global alarm_running
    alarm_running = False
    lbl_status.config(text="Alarm stopped")


def check_alarm(alarm_time):
    global alarm_running
    while alarm_running:
        now = datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            play_sound()
            messagebox.showinfo("Alarm", "⏰ Wake up!")
            alarm_running = False
            break
        time.sleep(1)


root = tk.Tk()
root.title("Modern Alarm Clock")
root.geometry("350x300")
root.config(bg="#1e1e2f")

tk.Label(root, text="Modern Alarm Clock", font=("Arial", 18, "bold"),
         fg="white", bg="#1e1e2f").pack(pady=10)

lbl_clock = tk.Label(root, font=("Arial", 28, "bold"),
                     fg="#00ffcc", bg="#1e1e2f")
lbl_clock.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

tk.Label(frame, text="Set Time (HH:MM:SS)", fg="white",
         bg="#1e1e2f").pack()

entry_time = tk.Entry(frame, font=("Arial", 14), justify="center")
entry_time.pack(pady=5)

btn_start = tk.Button(root, text="Start Alarm", width=15,
                      bg="#00ffcc", command=start_alarm)
btn_start.pack(pady=5)

btn_stop = tk.Button(root, text="Stop Alarm", width=15,
                     bg="#ff6666", command=stop_alarm)
btn_stop.pack(pady=5)

lbl_status = tk.Label(root, text="", fg="white", bg="#1e1e2f")
lbl_status.pack(pady=10)

update_clock()
root.mainloop()