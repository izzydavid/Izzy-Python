import customtkinter


class AppFunctions:
    def __init__(self):
        super().__init__()

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:",
                                              title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


app_functions = AppFunctions()
app_functions.open_input_dialog_event()
app_functions.change_appearance_mode_event("dark")
app_functions.change_scaling_event("150%")
app_functions.sidebar_button_event()
