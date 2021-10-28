from tkinter import *


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("Group 4 Final Project")
        master.geometry("1200x600")
        master.configure(bg="light cyan")

        self.label_title = Label(master, text="Trustworthy Federated Learning", fg="dark blue", 
                                    bg="light cyan", font=("Arial", 25, 'bold'))
        self.label_title.place(x=500, y=25)

        self.sub_string = StringVar(master)
        self.sub_string.set("Choose Model")
        self.sub_title_label = Label(master, textvariable=self.sub_string, fg="dark blue", bg="light cyan", font=("Arial", 25, 'bold'))
        self.sub_title_label.place(x=600, y=60)

        self.canvas = Canvas(master, width=900, height=450, bg="white")
        self.canvas.place(x=250, y=100)

        self.variable_eff = StringVar(master)
        self.variable_eff.set("Effectiveness")
        self.eff_options = {"FedGen": "FedGen"}

        self.effectiveness_drop = OptionMenu(master, self.variable_eff, "Effectiveness", 
                                            *self.eff_options, command=self.displayEffectiveness)
        self.effectiveness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        self.effectiveness_drop.place(x=10, y=150)

        self.variable_privacy = StringVar(master)
        self.variable_privacy.set("Privacy")
        self.priv_options = {"Inverting Gradients": "Inverting Gradients"}

        self.privacy_drop = OptionMenu(master, self.variable_privacy, "Privacy", 
                                        *self.priv_options, command=self.displayPrivacy)
        self.privacy_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        self.privacy_drop.place(x=10, y=250)

        self.variable_rob = StringVar(master)
        self.variable_rob.set("Robustness")
        self.rob_options = {"Backdoor Attacks": "Backdoor Attacks", 
                "Data Poisoning Attacks": "Data Poisoning Attacks",
                "Model Poisoning Attacks": "Model Poisoning Attacks",
                "Byzantine Attacks": "Byzantine Attacks",
                "Free-rider Attacks": "Free-rider Attacks",
                "Inference Attacks": "Inference Attacks",
                "Byzantine Robustness": "Byzantine Robustness",
                "Sybil Robustness": "Sybil Robustness",
                "Certified Robustness": "Certified Robustness"}

        self.robustness_drop = OptionMenu(master, self.variable_rob, "Robustness", 
                                        *self.rob_options, command=self.displayRobustness)
        self.robustness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        self.robustness_drop.place(x=10, y=350)

        self.variable_fair = StringVar(master)
        self.variable_fair.set("Fairness")
        self.fair_options = {"easyFL": "easyFL"}

        self.fairness_drop = OptionMenu(master, self.variable_fair, "Fairness", 
                                        *self.fair_options, command=self.displayFairness)
        self.fairness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        self.fairness_drop.place(x=10, y=450)

    def displayEffectiveness(self, value):
        try:
            if self.eff_options[value] == "FedGen":
                self.sub_string.set(self.eff_options[value])
                
        except KeyError:
            self.sub_string.set(value)

    def displayPrivacy(self, value):
        try:
            self.sub_string.set(self.priv_options[value])
        except KeyError:
            self.sub_string.set(value)
    
    def displayRobustness(self, value):
        try:
            self.sub_string.set(self.rob_options[value])
        except KeyError:
            self.sub_string.set(value)
    
    def displayFairness(self, value):
        try:
            self.sub_string.set(self.fair_options[value])
        except KeyError:
            self.sub_string.set(value)

root = Tk()
app = App(root)
root.mainloop()