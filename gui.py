from tkinter import *
import os
from PIL import Image, ImageTk
import subprocess

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Group 4 Final Project")
        self.master.geometry("1200x600")
        self.master.configure(bg="light cyan")

        self.label_title = Label(self.master, text="Trustworthy Federated Learning", fg="dark blue", 
                                    bg="light cyan", font=("Arial", 25, 'bold'))
        self.label_title.place(x=500, y=25)

        self.sub_string = StringVar(self.master)
        self.sub_string.set("Choose Model")
        self.sub_title_label = Label(self.master, textvariable=self.sub_string, fg="dark blue", bg="light cyan", font=("Arial", 25, 'bold'))
        self.sub_title_label.place(x=600, y=60)

        self.frame = Frame(self.master, width=900, height=450, bg="white")
        self.frame.place(x=250, y=100)
        self.welcome = StringVar(self.master)
        self.welcome.set("Welcome Page")
        self.welcome_label = Label(self.frame, textvariable=self.welcome, fg="dark blue", bg="white", font=("Arial", 25, 'bold'))
        self.welcome_label.place(x=400, y=200)

        self.variable_eff = StringVar(self.master)
        self.variable_eff.set("Effectiveness")
        self.eff_options = {"FedGen": "FedGen"}

        self.effectiveness_drop = OptionMenu(self.master, self.variable_eff, 
                                            *self.eff_options, command=self.displayEffectiveness)
        self.effectiveness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        self.effectiveness_drop.place(x=10, y=150)

        # self.variable_privacy = StringVar(self.master)
        # self.variable_privacy.set("Privacy")
        # self.priv_options = {"Inverting Gradients": "Inverting Gradients"}

        # self.privacy_drop = OptionMenu(self.master, self.variable_privacy, 
        #                                 *self.priv_options, command=self.displayPrivacy)
        # self.privacy_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        # self.privacy_drop.place(x=10, y=250)

        # self.variable_rob = StringVar(self.master)
        # self.variable_rob.set("Robustness")
        # self.rob_options = {"Backdoor Attacks": "Backdoor Attacks", 
        #         "Data Poisoning Attacks": "Data Poisoning Attacks",
        #         "Model Poisoning Attacks": "Model Poisoning Attacks",
        #         "Byzantine Attacks": "Byzantine Attacks",
        #         "Free-rider Attacks": "Free-rider Attacks",
        #         "Inference Attacks": "Inference Attacks",
        #         "Byzantine Robustness": "Byzantine Robustness",
        #         "Sybil Robustness": "Sybil Robustness",
        #         "Certified Robustness": "Certified Robustness"}

        # self.robustness_drop = OptionMenu(self.master, self.variable_rob, 
        #                                 *self.rob_options, command=self.displayRobustness)
        # self.robustness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        # self.robustness_drop.place(x=10, y=350)

        # self.variable_fair = StringVar(self.master)
        # self.variable_fair.set("Fairness")
        # self.fair_options = {"easyFL": "easyFL"}

        # self.fairness_drop = OptionMenu(self.master, self.variable_fair, 
        #                                 *self.fair_options, command=self.displayFairness)
        # self.fairness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        # self.fairness_drop.place(x=10, y=450)

    def displayEffectiveness(self, value):
        try:
            self.sub_string.set(self.eff_options[value])
            
            # for widget in self.canvas.winfo_children():
            #     widget.place_forget()
            frame1 = Frame(self.master, width=900, height=450, bg="white")
            frame1.place(x=250, y=100)   

            Label(frame1, text="Number of Clients", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=100)
            Label(frame1, text="Learning Rate", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=200)
            Label(frame1, text="Total Epochs", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=300)
            Label(frame1, text="Dataset", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=100)
            Label(frame1, text="Alpha", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=200)
            Label(frame1, text="Sampling Rate", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=300)

            client_var = IntVar()
            lr_var = DoubleVar()
            epoch_var = IntVar()
            dataset_var = StringVar()
            data_options = ["Mnist", "EMnist"]
            dataset_var.set("Choose")
            alpha_var = DoubleVar()
            ratio_var = DoubleVar()
            num_clients = Entry(frame1, textvariable=client_var, width=5).place(x=350, y=100)
            learning_rate = Entry(frame1, textvariable=lr_var, width=5).place(x=350, y=200)
            total_epochs = Entry(frame1, textvariable=epoch_var, width=5).place(x=350, y=300)

            def get_dataset(choice):
                choice = dataset_var.get()
                return choice

            dataset = OptionMenu(frame1, dataset_var, *data_options, command=get_dataset).place(x=700, y=100)
            alpha = Entry(frame1, textvariable=alpha_var, width=5).place(x=700, y=200)
            sampling_ratio = Entry(frame1, textvariable=ratio_var, width=5).place(x=700, y=300)

            frame2 = Frame(self.master, width=900, height=450, bg="white")

            def entry_frame():
                frame2.place(x=250, y=100)
                frame1.place_forget()

            def results_frame():
                frame1.place(x=250, y=100)
                frame2.place_forget()
            
            submit_button = Button(frame1, text="Submit", command=entry_frame)
            submit_button.place(x=450, y=400)

            back_button = Button(frame2, text="Back", command=results_frame)
            back_button.place(x=450, y=400)

            # def run_fed_gen():
            #     os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen")
            #     os.chdir(f"/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen/data/{dataset_var.get()}")
            #     os.system(f"python3 generate_niid_dirichlet.py --n_class 10 \
            #                 --sampling_ratio {ratio_var.get()} --alpha {alpha_var.get()} --n_user 20")

            #     os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen")
            #     command = ["python3", "main.py", "--dataset", str(dataset_var.get()) + "-alpha" + str(alpha_var.get()) + 
            #             "-ratio" + str(ratio_var.get()), "--algorithm", "FedGen", "--batch_size", "32", "--num_glob_iters", str(epoch_var.get()), \
            #             "--local_epochs", "20", "--num_users", str(client_var.get()), "--lamda", "1", "--learning_rate", str(lr_var.get()), \
            #             "--model", "cnn", "--personal_learning_rate", "0.01", "--times", "3"]

            #     result = subprocess.run(command, stdout=subprocess.PIPE)

            #     T = Text(frame2, height=100, width=300)
            #     T.place(x=700,y=400)
            #     T.insert(END, result.stdout.decode('utf-8'))


        except KeyError:
            self.sub_string.set(value)

    # def displayPrivacy(self, value):
    #     try:
    #         self.sub_string.set(self.priv_options[value])

    #         for widget in self.canvas.winfo_children():
    #             widget.place_forget()

    #         input_image = Image.open("PrivacyPreserving/invertinggradients/11794_ResNet18_ImageNet_input.png")
    #         image_tk = ImageTk.PhotoImage(input_image)

    #         image_label = Label(self.canvas, image=image_tk)
    #         image_label.image = image_tk
    #         image_label.place(x=150, y=100)


    #     except KeyError:
    #         self.sub_string.set(value)
    
    # def displayRobustness(self, value):
    #     try:
    #         self.sub_string.set(self.rob_options[value])
    #     except KeyError:
    #         self.sub_string.set(value)
    
    # def displayFairness(self, value):
    #     try:
    #         self.sub_string.set(self.fair_options[value])

    #         for widget in self.canvas.winfo_children():
    #             widget.place_forget()
                
    #         Label(self.canvas, text="Total Epochs", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=100)
    #         Label(self.canvas, text="Learning Rate", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=200)
    #         Label(self.canvas, text="Batch Size", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=300)
    #         Label(self.canvas, text="Optimizer", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=150)
    #         Label(self.canvas, text="Momentum", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=250)

    #         epoch_var = IntVar()
    #         lr_var = DoubleVar()
    #         batch_var = IntVar()
    #         opt_var = StringVar()
    #         opt_options = ["Adam", "SGD"]
    #         opt_var.set("Choose")
    #         mom_var = DoubleVar()
    #         num_epochs = Entry(self.canvas, textvariable=epoch_var, width=5).place(x=350, y=100)
    #         learning_rate = Entry(self.canvas, textvariable=lr_var, width=5).place(x=350, y=200)
    #         batch_size = Entry(self.canvas, textvariable=batch_var, width=5).place(x=350, y=300)

    #         def get_optimizer(choice):
    #             choice = opt_var.get()
    #             return choice

    #         optimizer = OptionMenu(self.canvas, opt_var, *opt_options, command=get_optimizer).place(x=700, y=150)
    #         momentum = Entry(self.canvas, textvariable=mom_var, width=5).place(x=700, y=250)

    #         def run_easyFL():
    #             os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Fairness/easyFL")
    #             requirements = Threading("pip3 install -r requirements.txt")

    #             generate_data = Threading("python generate_fedtask.py")
                
    #             run_model = Threading(f"python3 main.py --task mnist_client100_dist0_beta0_noise0 --model cnn --method fedavg \
    #                     --num_rounds 20 --num_epochs {epoch_var.get()} --learning_rate {lr_var.get()} --proportion 0.1 --batch_size {batch_var.get()} \
    #                     --train_rate 1 --eval_interval 1 --momentum {mom_var.get()} --optimizer {opt_var.get()}")

    #         submit_button = Button(self.canvas, text="Submit", command=run_easyFL).place(x=450, y=400)

    #     except KeyError:
    #         self.sub_string.set(value)


root = Tk()
app = App(root)
root.mainloop()
