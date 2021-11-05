from tkinter.ttk import *
from tkinter import *
import os
from PIL import Image, ImageTk
import subprocess
import time
import threading

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

        self.variable_fair = StringVar(self.master)
        self.variable_fair.set("Fairness")
        self.fair_options = {"easyFL": "easyFL"}

        self.fairness_drop = OptionMenu(self.master, self.variable_fair, 
                                        *self.fair_options, command=self.displayFairness)
        self.fairness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        self.fairness_drop.place(x=10, y=450)

    def displayEffectiveness(self, value):
        try:
            self.sub_string.set(self.eff_options[value])
            
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
            
            submit_button = Button(frame1, text="Save Results", command=entry_frame)
            submit_button.place(x=450, y=400)

            progressBar = Progressbar(frame2, mode='indeterminate', length=300)
            progressBar.place(x=325, y=300)

            status = StringVar(frame2)
            Label(frame2, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=300)
            # text_box = Text(frame2, height=20, width=50)
            # text_box.place(x=275, y=25)

            def run_model():
                os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen")
                os.chdir(f"/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen/data/{dataset_var.get()}")
                
                data_command = ["python3", "generate_niid_dirichlet.py", "--n_class", "10", \
                            "--sampling_ratio", str(ratio_var.get()), "--alpha", str(alpha_var.get()), "--n_user", "20"]

                status.set("Generating Dataset. . .")
                data = subprocess.Popen(data_command, stdout=subprocess.PIPE)
                progress_func(data)

                os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen")

                model_command = ["python3", "main.py", "--dataset", str(dataset_var.get()) + "-alpha" + str(alpha_var.get()) + 
                        "-ratio" + str(ratio_var.get()), "--algorithm", "FedGen", "--batch_size", "32", "--num_glob_iters", str(epoch_var.get()), \
                        "--local_epochs", "20", "--num_users", str(client_var.get()), "--lamda", "1", "--learning_rate", str(lr_var.get()), \
                        "--model", "cnn", "--personal_learning_rate", "0.01", "--times", "3"]
                
                status.set("Running Model. . .")
                result = subprocess.Popen(model_command, stdout=subprocess.PIPE)
                progress_func(result)
                # text_box.insert(END, result.communicate()[0])
                status.set("Finished")
                # plot_command = ["python3", "main_plot.py", "--dataset", str(dataset_var.get()) + "-alpha" + str(alpha_var.get()) + "-ratio" + str(ratio_var.get()), "--algorithms", "FedGen", 
                #                 "--batch_size", "32", "--local_epochs", "20", "--num_users", str(client_var.get()), "--num_glob_iters", "200", "--plot_legend", "1"]               

                # plot = subprocess.Popen(plot_command, stdout=subprocess.PIPE)

                # status.set("Finished")
                # input_image = Image.open(f"/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen/figs/{str(dataset_var.get())}/ratio{str(ratio_var.get())}/{str(dataset_var.get())}-ratio{str(ratio_var.get())}.png")

                # image_tk = ImageTk.PhotoImage(input_image)

                # image_label = Label(frame2, image=image_tk)
                # image_label.image = image_tk
                # image_label.place(x=325, y=100)

            def progress_func(process):
                progressBar.start()

                while process.poll() is None:
                    progressBar.update()
                
                progressBar.stop()
                
            run_button = Button(frame2, text="Run Model", command=run_model)
            run_button.place(x=425, y=350)

            back_button = Button(frame2, text="Back", command=results_frame)
            back_button.place(x=450, y=400)            

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
    
    def displayFairness(self, value):
        try:
            self.sub_string.set(self.fair_options[value])

            frame1 = Frame(self.master, width=900, height=450, bg="white")
            frame1.place(x=250, y=100) 
                
            Label(frame1, text="Total Epochs", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=100)
            Label(frame1, text="Learning Rate", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=200)
            Label(frame1, text="Batch Size", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=300)
            Label(frame1, text="Optimizer", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=150)
            Label(frame1, text="Momentum", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=250)

            epoch_var = IntVar()
            lr_var = DoubleVar()
            batch_var = IntVar()
            opt_var = StringVar()
            opt_options = ["Adam", "SGD"]
            opt_var.set("Choose")
            mom_var = DoubleVar()
            num_epochs = Entry(frame1, textvariable=epoch_var, width=5).place(x=350, y=100)
            learning_rate = Entry(frame1, textvariable=lr_var, width=5).place(x=350, y=200)
            batch_size = Entry(frame1, textvariable=batch_var, width=5).place(x=350, y=300)

            def get_optimizer(choice):
                choice = opt_var.get()
                return choice

            optimizer = OptionMenu(frame1, opt_var, *opt_options, command=get_optimizer).place(x=700, y=150)
            momentum = Entry(frame1, textvariable=mom_var, width=5).place(x=700, y=250)

            frame2 = Frame(self.master, width=900, height=450, bg="white")

            def entry_frame():
                frame2.place(x=250, y=100)
                frame1.place_forget()

            def results_frame():
                frame1.place(x=250, y=100)
                frame2.place_forget()

            submit_button = Button(frame1, text="Save Results", command=entry_frame)
            submit_button.place(x=450, y=400)

            progressBar = Progressbar(frame2, mode='indeterminate', length=300)
            progressBar.place(x=325, y=300)

            status = StringVar(frame2)
            Label(frame2, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=300)

            def run_easyFL():
                
                def progress_func(process):
                    progressBar.start()

                    while process.poll() is None:
                        progressBar.update()
                    
                    progressBar.stop()

                os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Fairness/easyFL")
                
                requirements = ["pip3", "install", "-r", "requirements.txt"]

                status.set("Installing Requirements. . .")
                req = subprocess.Popen(requirements, stdout=subprocess.PIPE)
                progress_func(req)

                data_command = ["python3", "generate_fedtask.py"]
                
                status.set("Generating Data. . .")
                data = subprocess.Popen(data_command, stdout=subprocess.PIPE)
                progress_func(data)
                # text_box.insert(END, result.communicate()[0])

                run_model = ["python3", "main.py", "--task", "mnist_client100_dist0_beta0_noise0", "--model" "cnn", "--method", "fedavg", \
                        "--num_rounds", "20", "--num_epochs", str({epoch_var.get()}), "--learning_rate", str(lr_var.get()), "--proportion", "0.1", "--batch_size", str(batch_var.get()), \
                        "--train_rate", "1", "--eval_interval", "1", "--momentum", str(mom_var.get()), "--optimizer", str(opt_var.get())]

                status.set("Running Model. . .")
                model = subprocess.Popen(run_model, stdout=subprocess.PIPE)
                progress_func(model)

                status.set("Finished")

            run_button = Button(frame2, text="Run Model", command=run_easyFL)
            run_button.place(x=425, y=350)

            back_button = Button(frame2, text="Back", command=results_frame)
            back_button.place(x=450, y=400) 

        except KeyError:
            self.sub_string.set(value)


root = Tk()
app = App(root)
root.mainloop()
