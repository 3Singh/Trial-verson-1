import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
import re
import json
import datetime
import customtkinter as ck

ck.set_appearance_mode("dark")
ck.set_default_color_theme("blue")

class InjuryPreventionApp:
    def __init__(self, root):
        self.root_tk = ck.CTk()
        self.root = root
        self.root.title("Injury Prevention")
        self.root.geometry("840x600")
        self.root.config(bg = '#2b2b2b')

        self.root.grid_rowconfigure((0, 1, 2), weight=1)
        self.root.grid_columnconfigure((0), weight=1)

        self.top_frame = ck.CTkFrame(root, width=840, height=300)
        self.bottom_frame1 = ck.CTkFrame(root, width=840, height=300)
        self.bottom_frame2 = ck.CTkFrame(root, width=840, height=300)
        self.button_frame = ck.CTkFrame(root, width=840, height=100)

        self.top_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6 ,7), weight=1)
        self.top_frame.grid_columnconfigure((0, 1), weight=1)

        self.bottom_frame1.grid_rowconfigure((0), weight=0)
        self.bottom_frame1.grid_columnconfigure((0, 1), weight=1)

        self.bottom_frame2.grid_rowconfigure((0, 1, 2), weight=1)
        self.bottom_frame2.grid_columnconfigure((0, 1), weight=1)

        self.button_frame.grid_rowconfigure((0), weight=1)
        self.button_frame.grid_columnconfigure((0, 1), weight=1)

        self.top_frame.grid(row=0, column=0, sticky="ew")
        self.bottom_frame1.grid(row=1, column=0, sticky="ew")
        self.bottom_frame2.grid(row=1, column=0, sticky="ew")
        self.button_frame.grid(row=2, column=0, sticky="ew")

        self.first_name_entry = None
        self.last_name_entry = None
        self.age_entry = None
        self.height_entry = None
        self.weight_entry = None
        self.email_entry = None
        self.dropdown_var = None
        self.text = None
        self.selected_problem = None
        self.file_path = "DATABASE.json"

        self.create_widgets()

    def create_widgets(self):
        # Dropdown settings
        problems = ['Broken Bone', 'Sprain', 'Dislocation', 'Bruise']
        self.dropdown_var = tk.StringVar()
        dropdown = Combobox(self.top_frame, width=27, textvariable=self.dropdown_var, values=problems)
        dropdown.set("Select a Health Problem")
        dropdown.grid(row=5, column=1, padx=10, pady=5)
        dropdown_label = ck.CTkLabel(self.top_frame, text="Health problem:")
        dropdown_label.grid(row=5, column=0, padx=10, pady=5)

        self.title_label = ck.CTkLabel(master=self, text="CustomTkinter", font=ck.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Entry fields for user information
        first_name_label = ck.CTkLabel(self.top_frame, text="First Name:")
        first_name_label.grid(row=0, column=0, padx=10, pady=5)
        self.first_name_entry = ck.CTkEntry(self.top_frame, font=('Helvetica', 12))
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        last_name_label = ck.CTkLabel(self.top_frame, text="Last Name:")
        last_name_label.grid(row=1, column=0, padx=10, pady=5)
        self.last_name_entry = ck.CTkEntry(self.top_frame, font=('Helvetica', 12))
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        age_label = ck.CTkLabel(self.top_frame, text="Age:")
        age_label.grid(row=2, column=0, padx=10, pady=5)
        self.age_entry = ck.CTkEntry(self.top_frame, font=('Helvetica', 12))
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)

        height_label = ck.CTkLabel(self.top_frame, text="Height (cm):")
        height_label.grid(row=3, column=0, padx=10, pady=5)
        self.height_entry = ck.CTkEntry(self.top_frame, font=('Helvetica', 12))
        self.height_entry.grid(row=3, column=1, padx=10, pady=5)

        weight_label = ck.CTkLabel(self.top_frame, text="Weight (kg):")
        weight_label.grid(row=4, column=0, padx=10, pady=5)
        self.weight_entry = ck.CTkEntry(self.top_frame, font=('Helvetica', 12))
        self.weight_entry.grid(row=4, column=1, padx=10, pady=5)

        email_label = ck.CTkLabel(self.top_frame, text="Email:")
        email_label.grid(row=6, column=0, padx=10, pady=5)
        self.email_entry = ck.CTkEntry(self.top_frame, font=('Helvetica', 12))
        self.email_entry.grid(row=6, column=1, padx=10, pady=5)

        # Submit button to display user information
        submit_button = ck.CTkButton(self.top_frame, text="Submit", command=self.submit_info)
        submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        show_more = ck.CTkButton(self.button_frame, text="Show More", command=self.show_more)
        show_more.grid(row=0, column=0, padx=10, pady=10)

        self.bottom_frame1.tkraise()

    def broken_short(self):
        self.text.delete("1.0", tk.END)
        self.show_user_info()
        self.text.insert(tk.END, """Broken Bone:\n\nYou must get medical help right away if you think you may have a broken bone. A broken bone, also known as a fracture, needs to be properly assessed, treated, and cared for in order to ensure appropriate healing and reduce any potential consequences. If you think you may have a broken bone, you should take the following actions:\n1.Halt all action\n2.Apply Ice\n3.Elevate the injured limb\n4.Diagnosis and treatment\n5.Adhere to medical advice\n6.Rest and recuperation\n""")

    def sprain_short(self):
        self.text.delete("1.0", tk.END)
        self.show_user_info()
        self.text.insert(tk.END, """Sprain:\n\nTake action right once to control the injury and encourage healthy healing if you think you've sprained something. When the ligaments that hold bones together are stretched or torn, a sprain takes place. Ankles, wrists, knees, and thumbs are typical locations for sprains. If you've sprained an ankle, you should follow these instructions:\n1.Rest\n2.Ice the injured area\n3.Elevate\n4.Pain management\n5.Avoiding applying heat\n6.Remember the abbreviation H.A.R.M (Heat)(Alcohol)(Running)(Massage)\n7.Consult a doctor\n8.Observe medical advice\n9.Give your body time to recover gradually\n""")

    def dislocation_short(self):
        self.text.delete("1.0", tk.END)
        self.show_user_info()
        self.text.insert(tk.END, """Dislocation:\n\nYou must get medical help right away if you think you may have a dislocation. When the bones in a joint are pushed out of their natural alignment, a dislocation happens. Self-treating a dislocation might result in additional injury and difficulties. If you or someone else has a dislocation, you should follow these instructions:\n1.Stop doing any activity\n2.Seek medial advice\n3.Keep the injured joint as still as you can\n4.Apply ice\n5.Elevate the limb\n6.Call for medical assistance\n7.Rest and recuperation\n""")

    def bruise_short(self):
        self.text.delete("1.0", tk.END)
        self.show_user_info()
        self.text.insert(tk.END, """Bruise:\n\n1.Rest the wound\n2.Ice the injure area\n3.Use a compression bandage\n4.Elevate the damaged area\n5.pain relief over-the-counter\n6.Aim to aviod applying heat\n7.Avoid alcohol and blood-thinning drugs\n8.Give your bruise time to heal\n9.Inspect the bruise\nA healthcare professional should be consulted for an accurate assessment and treatment plan if the bruise is severe, coupled with significant pain, swelling, or other alarming symptoms, or if you are unsure about the nature of the injury.\n""")

    def broken(self):
        self.text.delete("1.0", tk.END)
        self.show_user_info()
        self.text.insert(tk.END, """Broken Bone:\n\nYou must get medical help right away if you think you may have a broken bone. A broken bone, also known as a fracture, needs to be properly assessed, treated, and cared for in order to ensure appropriate healing and reduce any potential consequences. If you think you may have a broken bone, you should take the following actions:\n\n1. Halt all actions: Stop all physical activity right once if you have excruciating pain, swelling, or deformity in a limb or any other area of your body following an injury.\n\n2. Apply ice: Ice application to the injured region can help reduce discomfort and swelling. Never put ice on the skin; always wrap the ice pack in a cloth or towel. Apply it for 15 to 20 minutes at a time.\n3. Elevate the injured limb: Elevating an injured arm or leg might also assist to minimize swelling. If you can, try to keep it elevated above your heart. Seek medical help: Call for emergency medical services or go to the nearest hospital or urgent care center for professional evaluation and treatment.\n\n4. Diagnosis and treatment: An orthopedic specialist will inspect the injury at the medical facility and may request X-rays or other imaging tests to confirm the diagnosis. They will choose the best course of action based on the nature and severity of the fracture, which may result in surgery, splinting, or casting.\n\n5. Adhere to medical advice: Pay close attention to the doctor's instructions. This can entail putting on a cast or splint, taking painkillers as directed, going to follow-up appointments, and carrying out any rehabilitation activities your doctor has advised.\n\n6. Rest and recuperation: Give the bone enough time to mend completely. Avoid actions that can worsen the pain, such as putting weight on the injured area.\n""")

    def sprain(self):
        self.text.delete("1.0", tk.END)
        self.show_user_info()
        self.text.insert(tk.END, """Sprain:\n\nTake action right once to control the injury and encourage healthy healing if you think you've sprained something. When the ligaments that hold bones together are stretched or torn, a sprain takes place. Ankles, wrists, knees, and thumbs are typical locations for sprains. If you've sprained an ankle, you should follow these instructions:\n\n1.Rest: Put an end to the activity that strained the damaged area, and refrain from putting any pressure or weight on it. For the first stage of recovery to be successful, rest is essential.\n\n2.Ice: To minimize swelling and inflammation, apply ice to the injured region as quickly as feasible. Apply the ice pack for 15-20 minutes at a time, taking breaks as needed. Wrap it in a cloth or towel.\n\n3.Elevation: Whenever you can, elevate the damaged area so that it is above the level of your heart. This may lessen edema and improve circulation.\n\n4.Pain management: Over-the-counter painkillers such as acetaminophen or ibuprofen can help control pain and lessen inflammation. Always take the medication as directed and seek medical advice if you have any concerns or underlying medical conditions.\n\n5.Avoid applying heat: Applying heat to the injured area can cause swelling to worsen in the first 48 hours following the accident.\n\n6.Remember the abbreviation H.A.R.M., which stands for Heat, Alcohol, Running, and Massage, and avoid using it. When you first have a sprain, stay away from these activities since they can make the pain worse.\n\n7.Consult a doctor: It's critical to get medical help if the sprain is severe or if you are unsure about its severity. A medical expert can accurately evaluate the injury, rule out any fractures, and suggest the best course of action.\n\n8.Observe medical advice: Pay close attention to the directions provided by the healthcare provider. This may entail using a brace or support, carrying out particular exercises, or going to physical therapy.\n\n9.Give your body time to recover gradually. To prevent re-injury, gradually reintroduce activities and movements as advised by your healthcare provider.\n""")

    def dislocation(self):
        self.text.delete("1.0", tk.END)
        self.show_user_info()
        self.text.insert(tk.END, """Dislocation:\n\nYou must get medical help right away if you think you may have a dislocation. When the bones in a joint are pushed out of their natural alignment, a dislocation happens. Self-treating a dislocation might result in additional injury and difficulties. If you or someone else has a dislocation, you should follow these instructions:\n\n1.Halt all motion: To avoid further harm to the affected area if you suspect a dislocation, halt all motion and physical activity right away. The dislocated joint will be examined by a medical practitioner, such as an orthopedic specialist, who will also request X-rays or other imaging tests to determine the severity of the injury. The proper course of action will then be taken, which may include pain management, joint manipulation to realign the joint, or, in some circumstances, the use of a splint or sling to immobilize the joint during the healing period\n\n2.Adhere to medical advice: Carefully adhere to the doctor's directions. This may entail using a splint or sling, taking painkillers as directed, going to follow-up appointments, and carrying out any rehabilitation activities suggested by your doctor.\n\n3.Keep the injured joint as still as you can by immobilizing it. Avoid attempting to pop the joint back into place on your own as this could lead to more damage.\n\n4.Apply ice: Ice application can aid with pain alleviation. Apply the ice pack to the injured area for 15-20 minutes at a time, taking breaks as needed, using a cloth or towel to wrap it.\n\n5.Elevate the affected limb - if the dislocation is in an arm or leg.\n\n6.Call for emergency medical assistance or visit the closest hospital or urgent care facility for a professional assessment and treatment. It's essential to have a medical expert address the dislocation correctly.\n\n7.Rest and recuperation: Give the joint enough time to heal completely. Refrain from placing pressure on the harmed area or indulging in\n""")

    def bruise(self):
        self.text.delete("1.0", tk.END)
        self.show_user_info()
        self.text.insert(tk.END, """Bruise:\n\n1.Rest the wounded area to help it heal correctly. Avoid placing undue weight on the injury.\n\n2.Ice the injured area: During the first 48 hours, applying an ice pack wrapped in a cloth for 15-20 minutes every 1-2 hours will help reduce swelling and pain.\n\n3.Use a compression bandage to assist reduce swelling, but be careful not to apply it too tightly as this could aggravate circulation.\n\n4.Elevate the damaged area: Try to keep the bruised area higher than your heart. This may also aid in minimizing edema.\n\n5.Pain relief over-the-counter: If you're in pain, you can take acetaminophen or ibuprofen, which are both available over-the-counter. Always take your prescriptions as directed, and if you have any questions or are taking other medications, talk to a doctor.\n\n6.Aim to avoid applying heat to the damaged region for the first 48 hours as this could exacerbate swelling.\n\n7.Avoiding alcohol and blood-thinning drugs is advisable until the bruise has healed because both substances might worsen bleeding and bruising.\n\n8.Give your bruises some time to heal; bruises usually take a week or two to go away. Try to stay away from activities that can make the injury worse during this time.\n\n9.Inspect the bruise for any indications of infection, such as a rise in redness or temperature or the formation of pus. Get medical help right away if you encounter these symptoms.\n\nA healthcare professional should be consulted for an accurate assessment and treatment plan if the bruise is severe, coupled with significant pain, swelling, or other alarming symptoms, or if you are unsure about the nature of the injury.\n""")

    def on_dropdown_changed(self, event):
        self.selected_problem = self.dropdown_var.get()
        if self.selected_problem == 'Broken Bone':
            self.broken_short()
        elif self.selected_problem == 'Sprain':
            self.sprain_short()
        elif self.selected_problem == 'Dislocation':
            self.dislocation_short()
        elif self.selected_problem == 'Bruise':
            self.bruise_short()

    def submit_info(self):
        text_frame = ck.CTkFrame(self.bottom_frame2)
        text_frame.grid(row=0, column=0, padx=10, pady=10)
        self.text = ck.CTkTextbox(text_frame, wrap=tk.WORD, width=300, height=250, padx=10, pady=10, font=('Helvetica', 12))
        self.text.pack()
        self.first_name = self.first_name_entry.get()

        if re.match(r'^[a-zA-Z\s]+$', self.first_name):
            pass
        else:
            messagebox.showinfo("Error", "Please enter a valid first name")
            return
        self.last_name = self.last_name_entry.get()
        if re.match(r'^[a-zA-Z\s]+$', self.last_name):
            pass
        else:
           messagebox.showinfo("Error", "Please enter a valid last name")
           return

        self.age = self.age_entry.get()
        if re.match(r'^\d+$', self.age):
            pass
        else:
            messagebox.showinfo("Error", "Please enter a valid age")
            return

        self.height = self.height_entry.get()
        if re.match(r'^\d+$', self.height):
            pass
        else:
            messagebox.showinfo("Error", "Please enter a valid height")
            return
        self.weight = self.weight_entry.get()
        if re.match(r'^\d+$', self.weight):
            pass
        else:
            messagebox.showinfo("Error", "Please enter a valid weight")
            return

        self.email_address = self.email_entry.get()
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email_address):
            pass
        else:
            messagebox.showinfo("Error", "Please enter a valid email address")
            return


        self.selected_problem = self.dropdown_var.get()
        if 'Select a Health Problem' in self.selected_problem:
            messagebox.showinfo("Error", "Please select a health problem")
            return


        self.text.delete("1.0", tk.END)

        if self.selected_problem == 'Broken Bone':
            self.broken_short()
        elif self.selected_problem == 'Sprain':
            self.sprain_short()
        elif self.selected_problem == 'Dislocation':
            self.dislocation_short()
        elif self.selected_problem == 'Bruise':
            self.bruise_short()
        self.bottom_frame2.tkraise()
        current_date = datetime.datetime.now()

        # Format the current date in "dd/mm/yyyy hour:minute" format
        formatted_date = current_date.strftime("%d/%m/%Y %H:%M")

        full_info = f'First name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age} years old\nHeight: {self.height} cm\nWeight: {self.weight} kg\nEmail: {self.email_address}\nHealth Problem: {self.selected_problem}\nDate: {formatted_date}\n\n'
        input_text = full_info

        def read_json_from_file(self,file_path):
            try:
                with open(file_path, 'r') as file:
                    try:
                        data = json.load(file)
                    except:
                        data = []
            except FileNotFoundError:
                data = []
            return data

        def write_json_to_file(self,file_path, data):
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)
        # Initialize an empty dictionary to store the data
        data = {}

        # Split the input text into lines and process each line
        lines = input_text.split('\n')
        for line in lines:
            if line.strip():  # Skip empty lines
                key, value = line.split(': ', 1)
                data[key] = value

        # Create a new dictionary with the email as the parent
        json_data = [{data['Email']: {k: v for k, v in data.items() if k != 'Email'}}]

        # File path for storing the JSON data
        file_path = "DATABASE.json"

        # Read existing JSON data from the file
        existing_data = read_json_from_file(self,file_path)

        # Append the new JSON data to the existing data
        existing_data.extend(json_data)

        # Write the updated JSON data back to the file
        write_json_to_file(self,file_path, existing_data)

        def show_medical(self):
            file_path = self.file_path
            existing_data = read_json_from_file(self,file_path)
            text = ck.CTkTextbox(self.bottom_frame2, wrap=tk.WORD, width=300, height=250, padx=5, pady=5, font=('Helvetica', 12))
            text.grid(row=0, column=1, padx=10, pady=10)
            for entry in existing_data:
                for email, details in entry.items():
                    if email == self.email_address:
                        self.text.insert(tk.END, f"Email: {email}\n")
                        for key, value in details.items():
                            text.insert(tk.END, f"{key}: {value}\n")
                        text.insert(tk.END, '\n')

        medical_history = ck.CTkButton(self.button_frame , text="Medical History", command=lambda:show_medical(self)) # stops command frmo automatically executing due to the self variable
        medical_history.grid(row=0, column=1, padx=10, pady=10)

    def show_more(self):
            if self.selected_problem == 'Broken Bone':
                self.broken()
            elif self.selected_problem == 'Sprain':
                self.sprain()
            elif self.selected_problem == 'Dislocation':
                self.dislocation()
            elif self.selected_problem == 'Bruise':
                self.bruise()

    def show_user_info(self):
        user_info = f'First name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age} years old\nHeight: {self.height} cm\nWeight: {self.weight} kg\nEmail: {self.email_address}\nHealth Problem: {self.selected_problem}\n\n'
        self.text.insert(tk.END, user_info)


if __name__ == "__main__":
    root = ck.CTk()
    app = InjuryPreventionApp(root)
    root.mainloop()
