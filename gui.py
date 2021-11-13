from tkinter.ttk import *
from tkinter import *
import os
from PIL import Image, ImageTk
import subprocess
import logging


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Group 4 Final Project")
        self.master.geometry("1200x600")
        self.master.configure(bg="light cyan")

        ## Main Title
        self.label_title = Label(self.master, text="Trustworthy Federated Learning", fg="dark blue", 
                                    bg="light cyan", font=("Arial", 25, 'bold'))
        self.label_title.place(x=500, y=25)
        
        ## Subtitle
        self.sub_string = StringVar(self.master)
        self.sub_string.set("Choose Model")
        self.sub_title_label = Label(self.master, textvariable=self.sub_string, fg="dark blue", bg="light cyan", font=("Arial", 25, 'bold'))
        self.sub_title_label.place(x=600, y=60)

        ## Create the frame
        self.frame = Frame(self.master, width=900, height=450, bg="white")
        self.frame.place(x=250, y=100)
        self.welcome = StringVar(self.master)
        self.welcome.set("Welcome Page")
        self.welcome_label = Label(self.frame, textvariable=self.welcome, fg="dark blue", bg="white", font=("Arial", 25, 'bold'))
        self.welcome_label.place(x=400, y=200)

        ## Effectiveness Dropdown
        # self.variable_eff = StringVar(self.master)
        # self.variable_eff.set("Effectiveness")
        # self.eff_options = {"FedGen": "FedGen"}

        # self.effectiveness_drop = OptionMenu(self.master, self.variable_eff, 
        #                                     *self.eff_options, command=self.displayEffectiveness)
        # self.effectiveness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        # self.effectiveness_drop.place(x=10, y=150)

        # Privacy Dropdown
        # self.variable_privacy = StringVar(self.master)
        # self.variable_privacy.set("Privacy")
        # self.priv_options = {"Inverting Gradients": "Inverting Gradients"}

        # self.privacy_drop = OptionMenu(self.master, self.variable_privacy, 
        #                                 *self.priv_options, command=self.displayPrivacy)
        # self.privacy_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        # self.privacy_drop.place(x=10, y=250)

        self.variable_rob = StringVar(self.master)
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

        self.robustness_drop = OptionMenu(self.master, self.variable_rob, 
                                        *self.rob_options, command=self.displayRobustness)
        self.robustness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        self.robustness_drop.place(x=10, y=350)

        # self.variable_fair = StringVar(self.master)
        # self.variable_fair.set("Fairness")
        # self.fair_options = {"easyFL": "easyFL"}

        # self.fairness_drop = OptionMenu(self.master, self.variable_fair, 
        #                                 *self.fair_options, command=self.displayFairness)
        # self.fairness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        # self.fairness_drop.place(x=10, y=450)


    """
    Function for displaying the effectiveness model.
    Displays input boxes and a button to submit and save the results.
    It moves to the next page displaying the terminal results after running the model.
    """
    # def displayEffectiveness(self, value):
    #     try:
    #         self.sub_string.set(self.eff_options[value])
            
    #         frame1 = Frame(self.master, width=900, height=450, bg="white")
    #         frame1.place(x=250, y=100)   

    #         Label(frame1, text="Number of Clients", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=100)
    #         Label(frame1, text="Learning Rate", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=200)
    #         Label(frame1, text="Total Epochs", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=300)
    #         Label(frame1, text="Dataset", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=100)
    #         Label(frame1, text="Alpha", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=200)
    #         Label(frame1, text="Sampling Rate", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=300)

    #         client_var = IntVar()
    #         lr_var = DoubleVar()
    #         epoch_var = IntVar()
    #         dataset_var = StringVar()
    #         data_options = ["Mnist", "EMnist"]
    #         dataset_var.set("Choose")
    #         alpha_var = DoubleVar()
    #         ratio_var = DoubleVar()
    #         num_clients = Entry(frame1, textvariable=client_var, width=5).place(x=350, y=100)
    #         learning_rate = Entry(frame1, textvariable=lr_var, width=5).place(x=350, y=200)
    #         total_epochs = Entry(frame1, textvariable=epoch_var, width=5).place(x=350, y=300)

    #         def get_dataset(choice):
    #             choice = dataset_var.get()
    #             return choice

    #         dataset = OptionMenu(frame1, dataset_var, *data_options, command=get_dataset).place(x=700, y=100)
    #         alpha = Entry(frame1, textvariable=alpha_var, width=5).place(x=700, y=200)
    #         sampling_ratio = Entry(frame1, textvariable=ratio_var, width=5).place(x=700, y=300)

    #         frame2 = Frame(self.master, width=900, height=450, bg="white")

    #         """
    #         Function for switching back to the .
    #         """
    #         def entry_frame():
    #             frame2.place(x=250, y=100)
    #             frame1.place_forget()

    #         """
    #         Function for switching to the second frame.
    #         """
    #         def results_frame():
    #             frame1.place(x=250, y=100)
    #             frame2.place_forget()
            
    #         submit_button = Button(frame1, text="Save Results", command=entry_frame)
    #         submit_button.place(x=450, y=400)

    #         progressBar = Progressbar(frame2, mode='indeterminate', length=300, style="green.Horizontal.TProgressbar")
    #         progressBar.place(x=325, y=325)

    #         status = StringVar(frame2)
    #         Label(frame2, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=325)

    #         text_box = Text(frame2, height=20, width=75, relief=RIDGE, borderwidth=2)
    #         text_box.place(x=200, y=25)

    #         """
    #         Function for running the model.
    #         """
    #         def run_model():

    #             os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen")
    #             os.chdir(f"/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen/data/{dataset_var.get()}")
                
    #             data_command = ["python3", "generate_niid_dirichlet.py", "--n_class", "10", \
    #                         "--sampling_ratio", str(ratio_var.get()), "--alpha", str(alpha_var.get()), "--n_user", "20"]

    #             status.set("Generating Dataset. . .")
    #             data = subprocess.Popen(data_command, stdout=subprocess.PIPE)
    #             progress_func(data)

    #             os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen")

    #             model_command = ["python3", "main.py", "--dataset", str(dataset_var.get()) + "-alpha" + str(alpha_var.get()) + 
    #                     "-ratio" + str(ratio_var.get()), "--algorithm", "FedGen", "--batch_size", "32", "--num_glob_iters", str(epoch_var.get()), \
    #                     "--local_epochs", "20", "--num_users", str(client_var.get()), "--lamda", "1", "--learning_rate", str(lr_var.get()), \
    #                     "--model", "cnn", "--personal_learning_rate", "0.01", "--times", "3"]
                
    #             status.set("Running Model. . .")
    #             result = subprocess.Popen(model_command, stdout=subprocess.PIPE)
    #             progress_func(result)
    #             text_box.insert(END, result.communicate()[0])

    #             status.set("Finished")

    #         """
    #         Function for updating the progress bar.
    #         """
    #         def progress_func(process):
    #             progressBar.start()

    #             while process.poll() is None:
    #                 progressBar.update()
                
    #             progressBar.stop()
                
    #         run_button = Button(frame2, text="Run Model", command=run_model)
    #         run_button.place(x=430, y=355)

    #         back_button = Button(frame2, text="Back", command=results_frame)
    #         back_button.place(x=450, y=400)            

    #     except KeyError:
    #         self.sub_string.set(value)


    """
    Function for displaying the PrivacyPreserving algorithm
    """
    # def displayPrivacy(self, value):
    #     try:
    #         self.sub_string.set(self.priv_options[value])

    #         frame1 = Frame(self.master, width=900, height=450, bg="white")
    #         frame1.place(x=250, y=100)

    #         Label(frame1, text="Input Image", fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=230, y=15)
    #         Label(frame1, text="Output Image", fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=600, y=15)

    #         Label(frame1, text="ResNet Type", fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=315, y=360)

    #         progressBar = Progressbar(frame1, mode='indeterminate', length=300, style="green.Horizontal.TProgressbar")
    #         progressBar.place(x=320, y=325)

    #         status = StringVar(frame1)
    #         Label(frame1, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=325)

    #         def get_resnet(choice):
    #             choice = resnet_var.get()
    #             return choice

    #         resnet_var = StringVar()
    #         resnet_options = ["ResNet18", "ResNet32-10", "ResNet152"]
    #         resnet_var.set("Choose")
    #         resnet = OptionMenu(frame1, resnet_var, *resnet_options, command=get_resnet).place(x=425, y=360)

    #         """
    #         Function for running the model.
    #         """
    #         def run_model():

    #             os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/PrivacyPreserving/invertinggradients")

    #             input_image = ImageTk.PhotoImage(Image.open("auto.jpg").resize((250,250), Image.ANTIALIAS))
    #             image_label = Label(frame1, image = input_image)
    #             image_label.image = input_image
    #             image_label.place(x=150, y=40)

    #             status.set("Running Model. . .")

    #             model_command = ["python3", "reconstruct_image.py", "--model", str(resnet_var.get()), "--dataset", \
    #                             "CIFAR10", "--trained_model", "--cost_fn", "sim", "--indices", "def", "--restarts", \
    #                             "32", "--save_image", "--target_id", "-1"]
                
    #             result = subprocess.Popen(model_command, stdout=subprocess.PIPE)
    #             progress_func(result)

    #             status.set("Finished")

    #             output_image = ImageTk.PhotoImage(Image.open("images/a_ground_truth--1.png").resize((250,250), Image.ANTIALIAS))
    #             output_label = Label(frame1, image = output_image)
    #             output_label.image = output_image
    #             output_label.place(x=520, y=40)

    #         """
    #         Function for updating the progress bar.
    #         """
    #         def progress_func(process):
    #             progressBar.start()

    #             while process.poll() is None:
    #                 progressBar.update()
                
    #             progressBar.stop()
                
    #         run_button = Button(frame1, text="Run Model", command=run_model)
    #         run_button.place(x=425, y=400)
            
    #     except KeyError:
    #         self.sub_string.set(value)
    
    """
    Function for Robustness algorithms
    """
    # def displayRobustness(self, value):
        # try:
        #     self.sub_string.set(self.rob_options[value])

        #     """
        #     Function for updating the progress bar.
        #     """
        
        #     """
        #     Backdoor Attacks
        #     """
        #     # if self.rob_options[value] == "Backdoor Attacks":
        #     #     self.welcome.set("Does not work :(")

        #     """
        #     Data Poisoning Attacks
        #     """
            # if self.rob_options[value] == "Data Poisoning Attacks":
            #     self.sub_string.set(self.rob_options[value])

            #     frame1 = Frame(self.master, width=900, height=450, bg="white")
            #     frame1.place(x=250, y=100)

            #     progressBar = Progressbar(frame1, mode='indeterminate', length=300, style="green.Horizontal.TProgressbar")
            #     progressBar.place(x=320, y=325)

            #     status = StringVar(frame1)
            #     Label(frame1, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=325)

            #     text_box = Text(frame1, height=20, width=75, relief=RIDGE, borderwidth=2)
            #     text_box.place(x=200, y=25)

            #     """
            #     Get Data Poisoning experiment
            #     """
            #     def get_experiment(choice):
            #         choice = experiment_var.get()
            #         return choice

            #     experiment_var = StringVar()
            #     experiment_options = ["Label Flipping Attack Feasibility", "Attack Timing in Label Flipping Attacks", 
            #                             "Malicious Participant Availability", "Defending Against Label Flipping Attacks"]

            #     experiment_var.set("Choose")
            #     experiment = OptionMenu(frame1, experiment_var, *experiment_options, command=get_experiment).place(x=425, y=360)
                
            #     """
            #     Run Data Poisoning experiment
            #     """
            #     def run_experiment():
            #         if experiment_var.get() == "Label Flipping Attack Feasibility":
            #             status.set("Running Model. . .")

            #             feasibility = ["python3", "label_flipping_attack.py"]
                        
            #             result = subprocess.Popen(feasibility, stdout=subprocess.PIPE)
            #             progress_func(result)
            #             text_box.insert(END, logging.getLogger().setLevel(logging.INFO))
                        
            #             status.set("Finished")

            #         elif experiment_var.get() == "Attack Timing in Label Flipping Attacks":
            #             status.set("Running Model. . .")

            #             attack_timing = ["python3", "attack_timing.py"]
                        
            #             result = subprocess.Popen(attack_timing, stdout=subprocess.PIPE)
            #             progress_func(result)
            #             text_box.insert(END, result.communicate())

            #             status.set("Finished")
                    
            #         elif experiment_var.get() == "Malicious Participant Availability":
            #             status.set("Running Model. . .")

            #             malicious = ["python3", "malicious_participant_availability.py"]
                        
            #             result = subprocess.Popen(malicious, stdout=subprocess.PIPE)
            #             progress_func(result)
            #             text_box.insert(END, result.communicate())

            #             status.set("Finished")
                    
            #         else:
            #             if experiment_var.get() == "Defending Against Label Flipping Attacks":
            #                 text_box.insert("Model Not Available")
                            
            #     run_button = Button(frame1, text="Run Model", command=run_experiment)
            #     run_button.place(x=430, y=400)
            # elif self.rob_options[value] == "Model Poisoning Attacks":
            # elif self.rob_options[value] == "Byzantine Attacks":
            # elif self.rob_options[value] == "Free-rider Attacks":
        #     if self.rob_options[value] == "Inference Attacks":
        #         self.sub_string.set(self.rob_options[value])

        #         frame1 = Frame(self.master, width=900, height=450, bg="white")
        #         frame1.place(x=250, y=100)

        #         progressBar = Progressbar(frame1, mode='indeterminate', length=300, style="green.Horizontal.TProgressbar")
        #         progressBar.place(x=320, y=325)

        #         status = StringVar(frame1)
        #         Label(frame1, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=325)

        #         text_box = Text(frame1, height=20, width=75, relief=RIDGE, borderwidth=2)
        #         text_box.place(x=200, y=25)

            """
            Progress Bar Function
            """
        #   def progress_func(process):
        #       progressBar.start()

        #       while process.poll() is None:
        #           progressBar.update()
                            
        #       progressBar.stop()
        
        #         """
        #         Get Data Inference experiment
        #         """
        #         def get_experiment(choice):
        #             choice = experiment_var.get()
        #             return choice

        #         experiment_var = StringVar()
        #         experiment_options = ["Equation Solving Attack", "Path Restriction Attack", 
        #                                 "Generative Regression Network Attack"]

        #         experiment_var.set("Choose")
        #         experiment = OptionMenu(frame1, experiment_var, *experiment_options, command=get_experiment).place(x=425, y=360)
                
        #         """
        #         Run Data Inference experiment
        #         """
        #         def run_experiment():
        #             if experiment_var.get() == "Equation Solving Attack":
        #                 os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Robustness/featureinference-vfl/ESA")

        #                 status.set("Running Model. . .")

        #                 esa = ["python3", "main-esa.py"]

        #                 result = subprocess.Popen(esa, stdout=subprocess.PIPE)
        #                 progress_func(result)
        #                 text_box.insert(END, result.communicate()[0])
                        
        #                 status.set("Finished")

        #             elif experiment_var.get() == "Path Restriction Attack":
        #                 os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Robustness/featureinference-vfl/PRA")

        #                 status.set("Running Model. . .")

        #                 pra = ["python3", "main-pra.py"]
                        
        #                 result = subprocess.Popen(pra, stdout=subprocess.PIPE)
        #                 progress_func(result)
        #                 text_box.insert(END, result.communicate()[0])

        #                 status.set("Finished")
                    
        #             else:
        #                 if experiment_var.get() == "Generative Regression Network Attack":
        #                     os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Robustness/featureinference-vfl/GRNA")

        #                     status.set("Running Model. . .")

        #                     grna = ["python3", "main-grna.py"]
                            
        #                     result = subprocess.Popen(grna, stdout=subprocess.PIPE)
        #                     progress_func(result)
        #                     text_box.insert(END, result.communicate()[0])

        #                     status.set("Finished")
                            
        #         run_button = Button(frame1, text="Run Model", command=run_experiment)
        #         run_button.place(x=430, y=400)
        #     # elif self.rob_options[value] == "Byzantine Robustness":
        #     # elif self.rob_options[value] == "Sybil Robustness":
        #     # else:
        #     #     if self.rob_options[value] == "Certified Robustness":

        # except KeyError:
        #     self.sub_string.set(value)
    
    """
    Function for easyFL algorithm
    """
    # def displayFairness(self, value):
    #     try:
    #         self.sub_string.set(self.fair_options[value])

    #         frame1 = Frame(self.master, width=900, height=450, bg="white")
    #         frame1.place(x=250, y=100) 
                
    #         Label(frame1, text="Total Epochs", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=100)
    #         Label(frame1, text="Learning Rate", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=200)
    #         Label(frame1, text="Batch Size", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=300)
    #         Label(frame1, text="Optimizer", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=150)
    #         Label(frame1, text="Momentum", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=250)

    #         epoch_var = IntVar()
    #         lr_var = DoubleVar()
    #         batch_var = IntVar()
    #         opt_var = StringVar()
    #         opt_options = ["Adam", "SGD"]
    #         opt_var.set("Choose")
    #         mom_var = DoubleVar()
    #         num_epochs = Entry(frame1, textvariable=epoch_var, width=5).place(x=350, y=100)
    #         learning_rate = Entry(frame1, textvariable=lr_var, width=5).place(x=350, y=200)
    #         batch_size = Entry(frame1, textvariable=batch_var, width=5).place(x=350, y=300)

    #         """
    #         Get model optimizer
    #         """
    #         def get_optimizer(choice):
    #             choice = opt_var.get()
    #             return choice

    #         optimizer = OptionMenu(frame1, opt_var, *opt_options, command=get_optimizer).place(x=700, y=150)
    #         momentum = Entry(frame1, textvariable=mom_var, width=5).place(x=700, y=250)

    #         frame2 = Frame(self.master, width=900, height=450, bg="white")

    #         """
    #         Starting frame
    #         """
    #         def entry_frame():
    #             frame2.place(x=250, y=100)
    #             frame1.place_forget()

    #         """
    #         Second Frame
    #         """
    #         def results_frame():
    #             frame1.place(x=250, y=100)
    #             frame2.place_forget()

    #         submit_button = Button(frame1, text="Save Results", command=entry_frame)
    #         submit_button.place(x=450, y=400)

    #         progressBar = Progressbar(frame2, mode='indeterminate', length=300, style="green.Horizontal.TProgressbar")
    #         progressBar.place(x=325, y=325)

    #         status = StringVar(frame2)
    #         Label(frame2, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=325)
    #         text_box = Text(frame2, height=20, width=75, relief=RIDGE, borderwidth=2)
    #         text_box.place(x=200, y=25)

    #         """
    #         Run the easyFL model
    #         """
    #         def run_easyFL():
                
    #             def progress_func(process):
    #                 progressBar.start()

    #                 while process.poll() is None:
    #                     progressBar.update()
                    
    #                 progressBar.stop()

    #             os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Fairness/easyFL")
                
    #             requirements = ["pip3", "install", "-r", "requirements.txt"]

    #             status.set("Installing Requirements. . .")
    #             req = subprocess.Popen(requirements, stdout=subprocess.PIPE)
    #             progress_func(req)

    #             data_command = ["python3", "generate_fedtask.py"]
                
    #             status.set("Generating Data. . .")
    #             data = subprocess.Popen(data_command, stdout=subprocess.PIPE)
    #             progress_func(data)

    #             run_model = ["python3", "main.py", "--task", "mnist_client100_dist0_beta0_noise0", "--model" "cnn", "--method", "fedavg", \
    #                     "--num_rounds", "20", "--num_epochs", str({epoch_var.get()}), "--learning_rate", str(lr_var.get()), "--proportion", "0.1", "--batch_size", str(batch_var.get()), \
    #                     "--train_rate", "1", "--eval_interval", "1", "--momentum", str(mom_var.get()), "--optimizer", str(opt_var.get())]

    #             status.set("Running Model. . .")
    #             model = subprocess.Popen(run_model, stdout=subprocess.PIPE)
    #             progress_func(model)
    #             text_box.insert(END, model.communicate()[0])

    #             status.set("Finished")

    #         run_button = Button(frame2, text="Run Model", command=run_easyFL)
    #         run_button.place(x=430, y=355)

    #         back_button = Button(frame2, text="Back", command=results_frame)
    #         back_button.place(x=450, y=400)

    #     except KeyError:
    #         self.sub_string.set(value)


root = Tk()
app = App(root)
root.mainloop()
