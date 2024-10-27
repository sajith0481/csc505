class PrototypePage:
    def __init__(self, name, page_number, next_page=None):
        self.name = name
        self.page_number = page_number
        self.next_page = next_page

    def display_info(self):
        print(f"Page {self.page_number}: {self.name}")
        if self.next_page:
            print(f"Next Page: {self.next_page.name}")

# Define prototype pages and their flow
home_page = PrototypePage("Home Screen", 1)
add_item_page = PrototypePage("Add Item Screen", 2)
view_list_page = PrototypePage("View List Screen", 3)
settings_page = PrototypePage("Settings Screen", 4)

# Set the flow
home_page.next_page = add_item_page
add_item_page.next_page = view_list_page
view_list_page.next_page = settings_page

# List of pages in the sequence
pages = [home_page, add_item_page, view_list_page, settings_page]

# Print out the information for each page
print("Shopping List App Prototype:")
for page in pages:
    page.display_info()
    print("------")
