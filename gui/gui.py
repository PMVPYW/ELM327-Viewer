import dearpygui.dearpygui as dpg

class GUI:
    def __init__(self):
        dpg.create_context()
        
        with dpg.window(label="Tutorial"):
            with dpg.table(header_row=False, tag="root_table"):
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()
            with dpg.table_row():
                Card("Card 1", "Descrição do Card 1")
            with dpg.table_row():
                Card("Card 2", "Descrição do Card 2")
            with dpg.table_row():
                Card("Card 3", "Descrição do Card 3")
        
        dpg.create_viewport(title="Minha GUI", width=600, height=400, resizable=True)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def on_button_click(self, sender, app_data, user_data):
        print("Botão clicado!")


class Card:
    def __init__(self, name, description, width=300, height=200):
        self.name = name
        self.description = description
        self.width = width
        self.height = height

        # Create a window (card) with a label and defined size
        with dpg.window(label=name, width=self.width, height=self.height):
            dpg.add_text(self.name)
            dpg.add_text(self.description)
            pass

    def close(self):
        dpg.delete_item(self.__window)

# Executa a GUI
if __name__ == "__main__":
    gui = GUI()
