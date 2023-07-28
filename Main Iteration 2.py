import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

def broken_short():
    text.insert(tk.END,"""Broken Bone:

You must get medical help right away if you think you may have a broken bone. A broken bone, also known as a fracture, needs to be properly assessed, treated, and cared for in order to ensure appropriate healing and reduce any potential consequences. If you think you may have a broken bone, you should take the following actions:\n1.Halt all action\n2.Apply Ice\n3.Elevate the injured limb\n4.Diagnosis and treatment\n5.Adhere to medical advice\n6.Rest and recuperation
""")


def sprain_short():
    text.insert(tk.END,"""Sprain:

Take action right once to control the injury and encourage healthy healing if you think you've sprained something. When the ligaments that hold bones together are stretched or torn, a sprain takes place. Ankles, wrists, knees, and thumbs are typical locations for sprains. If you've sprained an ankle, you should follow these instructions:\n1.Rest\n2.Ice the injured area\n3.Elevate\n4.Pain management\n5.Avoing applying heat\n6.Remember the abbreviation H.A.R.M (Heat)(Alcohol)(Running)(Massage)\n7.Consult a doctor\n8.Observe medical advice\n9.Give your body time to recover gradually
""")    

def dislocation_short():
    text.insert(tk.END, """Dislocation:

You must get medical help right away if you think you may have a dislocation. When the bones in a joint are pushed out of their natural alignment, a dislocation happens. Self-treating a dislocation might result in additional injury and difficulties. If you or someone else has a dislocation, you should follow these instructions:\n1.Stop doing any activity\n2.Seek medial advice\n3.Keep the injured joint as still as you can\n4.Apply ice\n5.Elevate the limb\n6.Call for medical assistance\n7.Rest and recuperation
""")
    
def bruise_short():
    text.insert(tk.END,"""Bruise:

1.Rest the wound\n2.Ince the injure area\n3.Use a compression bandage\n4.Elevate the damaged area\n5.pain relief over-the-counter\n6.Aim to aviod applying heat\n7.Avoid alcohol and blood-thinning drugs\n8.Give your bruise time to heal\n9.Inspect the bruise\nA healthcare professional should be consulted for an accurate assessment and treatment plan if the bruise is severe, coupled with significant pain, swelling, or other alarming symptoms, or if you are unsure about the nature of the injury.
""")    

def broken():
    #text.delete("1.0", tk.END)
    text.insert(tk.END, """Broken Bone:

You must get medical help right away if you think you may have a broken bone. A broken bone, also known as a fracture, needs to be properly assessed, treated, and cared for in order to ensure appropriate healing and reduce any potential consequences. If you think you may have a broken bone, you should take the following actions:
1. Halt all actions: Stop all physical activity right once if you have excruciating pain, swelling, or deformity in a limb or any other area of your body following an injury.
2. Apply ice: Ice application to the injured region can help reduce discomfort and swelling. Never put ice on the skin; always wrap the ice pack in a cloth or towel. Apply it for 15 to 20 minutes at a time.
3. Elevate the injured limb: Elevating an injured arm or leg might also assist to minimise swelling. If you can, try to keep it elevated above your heart. Seek medical help: Call for emergency medical services or go to the nearest hospital or urgent care center for professional evaluation and treatment. 
4. Diagnosis and treatment: An orthopaedic specialist will inspect the injury at the medical facility and may request X-rays or other imaging tests to confirm the diagnosis. They will choose the best course of action based on the nature and severity of the fracture, which may result in surgery, splinting, or casting.
5. Adhere to medical advice: Pay close attention to the doctor's instructions. This can entail putting on a cast or splint, taking painkillers as directed, going to follow-up appointments, and carrying out any rehabilitation activities your doctor has advised.
6. Rest and recuperation: Give the bone enough time to mend completely. Avoid actions that can worsen the pain, such as putting weight on the injured area.
""")

def sprain():
    #text.delete("1.0", tk.END)
    text.insert(tk.END, """Sprain:

Take action right once to control the injury and encourage healthy healing if you think you've sprained something. When the ligaments that hold bones together are stretched or torn, a sprain takes place. Ankles, wrists, knees, and thumbs are typical locations for sprains. If you've sprained an ankle, you should follow these instructions:
1.Rest: Put an end to the activity that strained the damaged area, and refrain from putting any pressure or weight on it. For the first stage of recovery to be successful, rest is essential.
2.Ice: To minimise swelling and inflammation, apply ice to the injured region as quickly as feasible. Apply the ice pack for 15-20 minutes at a time, taking breaks as needed. Wrap it in a cloth or towel.
3.Elevation: Whenever you can, elevate the damaged area so that it is above the level of your heart. This may lessen edoema and improve circulation.
4.Pain management: Over-the-counter painkillers such acetaminophen or ibuprofen can help control pain and lessen inflammation. Always take the medication as directed and seek medical advice if you have any concerns or underlying medical conditions.
5.Avoid applying heat: Applying heat to the injured area can cause swelling to worsen in the first 48 hours following the accident.
6.Remember the abbreviation H.A.R.M., which stands for Heat, Alcohol, Running, and Massage, and avoid using it. When you first have a sprain, stay away from these activities since they can make the pain worse.
7.Consult a doctor: It's critical to get medical help if the sprain is severe or if you are unsure about its severity. A medical expert can accurately evaluate the injury, rule out any fractures, and suggest the best course of action.
8.Observe medical advice: Pay close attention to the directions provided by the healthcare provider. This may entail using a brace or support, carrying out particular exercises, or going to physical therapy.
9.Give your body time to recover gradually. To prevent re-injury, gradually reintroduce activities and movements as advised by your healthcare provider.
""")

def dislocation():
    #text.delete("1.0", tk.END)
    text.insert(tk.END, """Dislocation:

You must get medical help right away if you think you may have a dislocation. When the bones in a joint are pushed out of their natural alignment, a dislocation happens. Self-treating a dislocation might result in additional injury and difficulties. If you or someone else has a dislocation, you should follow these instructions:
1.Halt all motion: To avoid further harm to the affected area if you suspect a dislocation, halt all motion and physical activity right away. The dislocated joint will be examined by a medical practitioner, such as an orthopaedic specialist, who will also request X-rays or other imaging tests to determine the severity of the injury. The proper course of action will then be taken, which may include pain management, joint manipulation to realign the joint, or, in some circumstances, the use of a splint or sling to immobilise the joint during the healing period
2.Adhere to medical advice: Carefully adhere to the doctor's directions. This may entail using a splint or sling, taking painkillers as directed, going to follow-up appointments, and carrying out any rehabilitation activities suggested by your doctor.
3.Keep the injured joint as still as you can by immobilising it. Avoid attempting to pop the joint back into place on your own as this could lead to more damage.
4.Apply ice: Ice application can aid with pain alleviation. Apply the ice pack to the injured area for 15-20 minutes at a time, taking breaks as needed, using a cloth or towel to wrap it.
5.Elevate the affected limb - if the dislocation is in an arm or leg.
6.Call for emergency medical assistance or visit the closest hospital or urgent care facility for a professional assessment and treatment. It's essential to have a medical expert address the dislocation correctly.
7.Rest and recuperation: Give the joint enough time to heal completely. Refrain from placing pressure on the harmed area or indulging in
""")

def bruise():
    #text.delete("1.0", tk.END)
    text.insert(tk.END, """Bruise:

1.Rest the wounded area to help it heal correctly. Avoid placing undue weight on the injury.
2.Ice the injured area: During the first 48 hours, applying an ice pack wrapped in a cloth for 15-20 minutes every 1-2 hours will help reduce swelling and pain.
3.Use a compression bandage to assist reduce swelling, but be careful not to apply it too tightly as this could aggravate circulation.
4.Elevate the damaged area: Try to keep the bruised area higher than your heart. This may also aid in minimising edoema.
5.Pain relief over-the-counter: If you're in pain, you can take acetaminophen or ibuprofen, which are both available over-the-counter. Always take your prescriptions as directed, and if you have any questions or are taking other medications, talk to a doctor.
6.Aim to avoid applying heat to the damaged region for the first 48 hours as this could exacerbate swelling.
7.Avoiding alcohol and blood-thinning drugs is advisable until the bruise has healed because both substances might worsen bleeding and bruising.
8.Give your bruises some time to heal; bruises usually take a week or two to go away. Try to stay away from activities that can make the injury worse during this time.
9.Inspect the bruise for any indications of infection, such as a rise in redness or temperature or the formation of pus. Get medical help right away if you encounter these symptoms.
A healthcare professional should be consulted for an accurate assessment and treatment plan if the bruise is severe, coupled with significant pain, swelling, or other alarming symptoms, or if you are unsure about the nature of the injury.
""")

def on_dropdown_changed(event):
    global selected_problem
    selected_problem = dropdown_var.get()
    if selected_problem == 'Broken Bone':
        broken_short()
    elif selected_problem == 'Sprain':
        sprain_short()
    elif selected_problem == 'Dislocation':
        dislocation_short()
    elif selected_problem == 'Bruise':
        bruise_short()

def submit_info():
    global first_name
    global last_name
    global age
    global height
    global weight
    
    first_name = first_name_entry.get()
    if re.match(r'^[a-zA-Z\s]+$', first_name):
        pass
    else:
        messagebox.showinfo("Error", "Please enter a valid first name")
        return
    last_name = last_name_entry.get()
    if re.match(r'^[a-zA-Z\s]+$', last_name):
        pass
    else:
        messagebox.showinfo("Error", "Please enter a valid last name")
        return
    
    age = age_entry.get()
    if re.match(r'^\d+$', age):
        pass
    else:
        messagebox.showinfo("Error", "Please enter a valid age")
        return
        
    height = height_entry.get()
    if re.match(r'^\d+$', height):
        pass
    else:
        messagebox.showinfo("Error", "Please enter a valid height")
        return
    weight = weight_entry.get()
    if re.match(r'^\d+$', weight):
        pass
    else:
        messagebox.showinfo("Error", "Please enter a valid weight")
        return

    text.delete("1.0", tk.END)
    text.insert(tk.END, f"First Name: {first_name}\n")
    text.insert(tk.END, f"Last Name: {last_name}\n")
    text.insert(tk.END, f"Age: {age}\n")
    text.insert(tk.END, f"Height: {height}\n")
    text.insert(tk.END, f"Weight: {weight}\n")

def showMore():
    global first_name
    global last_name
    global age
    global height
    global weight
    global selected_problem
    text.delete("1.0",tk.END)
    text.insert(tk.END, f"First Name: {first_name}\n")
    text.insert(tk.END, f"Last Name: {last_name}\n")
    text.insert(tk.END, f"Age: {age}\n")
    text.insert(tk.END, f"Height: {height}\n")
    text.insert(tk.END, f"Weight: {weight}\n")
    if selected_problem == 'Broken Bone':
        broken()
    elif selected_problem == 'Sprain':
        sprain()
    elif selected_problem == 'Dislocation':
        dislocation()
    elif selected_problem == 'Bruise':
        bruise()

# Create the main GUI window
root = tk.Tk()
root.title("Health Problem Information")

# Dropdown menu for problem selection
problems = ['Broken Bone', 'Sprain', 'Dislocation', 'Bruise']
dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=problems, font=('Helvetica', 14))
dropdown.set("Select a Health Problem")
dropdown.grid(row=0, column=0, padx=10, pady=10)
dropdown.bind("<<ComboboxSelected>>", on_dropdown_changed)

# Entry fields for user information
first_name_label = tk.Label(root, text="First Name:")
first_name_label.grid(row=2, column=0, padx=10, pady=5)
first_name_entry = tk.Entry(root, font=('Helvetica', 12))
first_name_entry.grid(row=2, column=1, padx=10, pady=5)

last_name_label = tk.Label(root, text="Last Name:")
last_name_label.grid(row=3, column=0, padx=10, pady=5)
last_name_entry = tk.Entry(root, font=('Helvetica', 12))
last_name_entry.grid(row=3, column=1, padx=10, pady=5)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=4, column=0, padx=10, pady=5)
age_entry = tk.Entry(root, font=('Helvetica', 12))
age_entry.grid(row=4, column=1, padx=10, pady=5)

height_label = tk.Label(root, text="Height (cm):")
height_label.grid(row=5, column=0, padx=10, pady=5)
height_entry = tk.Entry(root, font=('Helvetica', 12))
height_entry.grid(row=5, column=1, padx=10, pady=5)

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=6, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root, font=('Helvetica', 12))
weight_entry.grid(row=6, column=1, padx=10, pady=5)

# Submit button to display user information
submit_button = tk.Button(root, text="Submit", command=submit_info)
submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Text area to display information
text = tk.Text(root, wrap=tk.WORD, width=60, height=20, padx=10, pady=10, font=('Helvetica', 12))
text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Add some padding and styling to the text area
text.tag_configure("title", font=("Helvetica", 14, "bold"))
text.tag_configure("list", font=("Helvetica", 12, "bold"))

show_more = tk.Button(root, text="Show More", command=showMore)
show_more.grid(row=8, column=4, columnspan=2, padx=10, pady=10)



root.mainloop()


