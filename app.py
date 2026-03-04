from handlers import *

# GUI setup code starts here
window = Tk()

# Main window configuration
window.title("My Application")
window.geometry("800x600")

# Menu bar creation
menu_bar = Menu(window)

# Toolbar setup
toolbar = Frame(window)

# Layout configuration
layout = Frame(window)
layout.pack(fill=BOTH, expand=True)

# Start the main event loop
window.mainloop()