import json
import tkinter as tk
from tkinter import Toplevel, simpledialog, messagebox
from PIL import Image, ImageTk
import os

# Load JSON data
json_file = "districts_data.json"
assets_folder = "assets/images"

with open(json_file, "r", encoding="utf-8") as file:
    data = json.load(file)


# Function to save changes to the JSON file
def save_data():
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Function to open district details with responsive categories
def show_district_details(district_name, district_data):
    details_window = Toplevel(root)
    details_window.title(district_name)
    details_window.geometry("600x600")
    details_window.configure(bg="#f0f0f0")

    # Dynamically place category buttons in a responsive grid
    city_key = next(iter(district_data["cities"]))
    categories = ["attractions", "food", "stores", "activities"]
    row, col = 0, 0

    for category in categories:
        if category in district_data["cities"][city_key]:
            button = tk.Button(
                details_window,
                text=f"{category.capitalize()}",
                command=lambda c=category: show_category_menu(district_data["cities"][city_key][category],
                                                              category.capitalize(), district_name, city_key),
                font=("Helvetica", 12),
                width=20,
                pady=5
            )
            button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            col += 1
            if col > 2:  # Change number of columns to adapt layout
                col = 0
                row += 1


# Function to open category menu and provide options to add, edit, or remove items
def show_category_menu(items, category_name, district_name, city_key):
    category_window = Toplevel(root)
    category_window.title(f"{category_name} in {district_name}")
    category_window.geometry("600x600")
    category_window.configure(bg="#fafafa")

    title_label = tk.Label(category_window, text=f"{category_name} in {district_name}", font=("Helvetica", 16, "bold"),
                           bg="#fafafa")
    title_label.pack(pady=10)

    # Display items in a responsive grid layout
    row, col = 0, 0
    for item in items:
        item_frame = tk.Frame(category_window, bg="#fafafa", bd=1, relief="solid")
        item_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Display name and description
        name_label = tk.Label(item_frame, text=item["name"], font=("Helvetica", 14, "bold"), bg="#fafafa")
        name_label.pack(anchor="w")

        description_label = tk.Label(item_frame, text=item["description"], wraplength=250, bg="#fafafa")
        description_label.pack(anchor="w")

        # Display image if available
        image_path = os.path.join(assets_folder, item.get("image", ""))
        if item.get("image") and os.path.exists(image_path):
            image = Image.open(image_path).resize((100, 75), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(item_frame, image=photo, bg="#fafafa")
            image_label.image = photo
            image_label.pack(anchor="w", pady=5)

        # Edit and Remove buttons for each item
        edit_button = tk.Button(item_frame, text="Edit", command=lambda i=item: edit_item(i, category_name, city_key),
                                width=10)
        edit_button.pack(side="left", padx=5)

        remove_button = tk.Button(item_frame, text="Remove",
                                  command=lambda i=item: remove_item(items, i, category_window), width=10)
        remove_button.pack(side="right", padx=5)

        col += 1
        if col > 1:  # Adjust column count for responsiveness
            col = 0
            row += 1

    # Add new item button
    add_button = tk.Button(category_window, text=f"Add {category_name[:-1]}",
                           command=lambda: add_item(items, category_name, city_key), font=("Helvetica", 12))
    add_button.pack(pady=20)


# Functions to add, edit, and remove items (same as before)
def add_item(items, category_name, city_key):
    name = simpledialog.askstring("Add Item", f"Enter {category_name[:-1]} name:")
    if name:
        description = simpledialog.askstring("Add Item", f"Enter description for {name}:")
        image_name = simpledialog.askstring("Add Item", f"Enter image filename (in {assets_folder}):")
        new_item = {"name": name, "description": description, "image": image_name}
        items.append(new_item)
        save_data()
        messagebox.showinfo("Added", f"{category_name[:-1]} added successfully!")


def edit_item(item, category_name, city_key):
    new_name = simpledialog.askstring("Edit Item", "Edit name:", initialvalue=item["name"])
    if new_name:
        item["name"] = new_name
    new_description = simpledialog.askstring("Edit Item", "Edit description:", initialvalue=item["description"])
    if new_description:
        item["description"] = new_description
    new_image = simpledialog.askstring("Edit Item", "Edit image filename:", initialvalue=item.get("image", ""))
    if new_image:
        item["image"] = new_image
    save_data()
    messagebox.showinfo("Updated", "Item updated successfully!")


def remove_item(items, item, category_window):
    if messagebox.askyesno("Confirm", f"Are you sure you want to delete {item['name']}?"):
        items.remove(item)
        save_data()
        category_window.destroy()
        show_category_menu(items, item["name"], "", "")


# Main window
root = tk.Tk()
root.title("Districts of Portugal")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Districts of Portugal", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Frame for scrollable menu with grid layout
canvas = tk.Canvas(root, bg="#f0f0f0")
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scroll_frame = tk.Frame(canvas, bg="#f0f0f0")

scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Load districts and display in a responsive grid
row, col = 0, 0
for district_name, district_info in data.items():
    color_rgb = district_info["color"]
    color_hex = f'#{color_rgb[0]:02x}{color_rgb[1]:02x}{color_rgb[2]:02x}'

    district_button = tk.Button(
        scroll_frame,
        text=district_name,
        bg=color_hex,
        fg="black",
        font=("Helvetica", 14, "bold"),
        command=lambda dn=district_name, di=district_info: show_district_details(dn, di),
        width=20,
        height=2
    )
    district_button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    col += 1
    if col > 2:  # Adjust the column count here for responsiveness
        col = 0
        row += 1

# Pack canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Start main loop
root.mainloop()
