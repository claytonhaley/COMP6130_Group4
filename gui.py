from tkinter.ttk import *
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
        self.variable_eff = StringVar(self.master)
        self.variable_eff.set("Effectiveness")
        self.eff_options = {"FedGen": "FedGen"}

        self.effectiveness_drop = OptionMenu(self.master, self.variable_eff, 
                                            *self.eff_options, command=self.displayEffectiveness)
        self.effectiveness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        self.effectiveness_drop.place(x=10, y=150)

        # ## Privacy Dropdown
        self.variable_privacy = StringVar(self.master)
        self.variable_privacy.set("Privacy")
        self.priv_options = {"Inverting Gradients": "Inverting Gradients"}

        self.privacy_drop = OptionMenu(self.master, self.variable_privacy, 
                                        *self.priv_options, command=self.displayPrivacy)
        self.privacy_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        self.privacy_drop.place(x=10, y=250)

        # Robustness Dropdown
        self.variable_rob = StringVar(self.master)
        self.variable_rob.set("Robustness")
        self.rob_options = {"Backdoor Attacks": "Backdoor Attacks", 
                "Data Poisoning Attacks": "Data Poisoning Attacks",
                "Model Poisoning Attacks": "Model Poisoning Attacks",
                "Free-rider Attacks": "Free-rider Attacks",
                "Inference Attacks": "Inference Attacks",
                "Byzantine Robustness": "Byzantine Robustness",
                "Sybil Robustness": "Sybil Robustness",
                "Certified Robustness": "Certified Robustness"}

        self.robustness_drop = OptionMenu(self.master, self.variable_rob, 
                                        *self.rob_options, command=self.displayRobustness)
        self.robustness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        self.robustness_drop.place(x=10, y=350)

        ## Fairness Dropdown
        self.variable_fair = StringVar(self.master)
        self.variable_fair.set("Fairness")
        self.fair_options = {"easyFL": "easyFL"}

        self.fairness_drop = OptionMenu(self.master, self.variable_fair, 
                                        *self.fair_options, command=self.displayFairness)
        self.fairness_drop.config(width=20, bg='dark blue', fg="white", font=("Arial", 15))
        self.fairness_drop.place(x=10, y=450)


    """
    Function for displaying the effectiveness model.
    Displays input boxes and a button to submit and save the results.
    It moves to the next page displaying the terminal results after running the model.
    """
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

            """
            Function for switching back to the .
            """
            def entry_frame():
                frame2.place(x=250, y=100)
                frame1.place_forget()

            """
            Function for switching to the second frame.
            """
            def results_frame():
                frame1.place(x=250, y=100)
                frame2.place_forget()
            
            submit_button = Button(frame1, text="Save Results", command=entry_frame)
            submit_button.place(x=450, y=400)

            progressBar = Progressbar(frame2, mode='indeterminate', length=300, style="green.Horizontal.TProgressbar")
            progressBar.place(x=325, y=325)

            status = StringVar(frame2)
            Label(frame2, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=325)

            text_box = Text(frame2, height=20, width=75, relief=RIDGE, borderwidth=2)
            text_box.place(x=200, y=25)

            """
            Function for updating the progress bar.
            """
            def progress_eff(process):
                progressBar.start()

                while process.poll() is None:
                    progressBar.update()
                
                progressBar.stop()


            """
            Function for running the model.
            """
            def run_effectiveness():

                os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen")
                os.chdir(f"/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen/data/{dataset_var.get()}")
                
                data_command = ["python3", "generate_niid_dirichlet.py", "--n_class", "10", \
                            "--sampling_ratio", str(ratio_var.get()), "--alpha", str(alpha_var.get()), "--n_user", "20"]

                status.set("Generating Dataset. . .")
                data = subprocess.Popen(data_command, stdout=subprocess.PIPE)
                progress_eff(data)

                os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Effectiveness/FedGen")

                model_command = ["python3", "main.py", "--dataset", str(dataset_var.get()) + "-alpha" + str(alpha_var.get()) + 
                        "-ratio" + str(ratio_var.get()), "--algorithm", "FedGen", "--batch_size", "32", "--num_glob_iters", str(epoch_var.get()), \
                        "--local_epochs", "20", "--num_users", str(client_var.get()), "--lamda", "1", "--learning_rate", str(lr_var.get()), \
                        "--model", "cnn", "--personal_learning_rate", "0.01", "--times", "3"]
                
                status.set("Running Model. . .")
                result = subprocess.Popen(model_command, stdout=subprocess.PIPE)
                progress_eff(result)
                text_box.insert(END, result.communicate()[0])

                status.set("Finished")
                
            run_button = Button(frame2, text="Run Model", command=run_effectiveness)
            run_button.place(x=430, y=355)

            back_button = Button(frame2, text="Back", command=results_frame)
            back_button.place(x=450, y=400)            

        except KeyError:
            self.sub_string.set(value)


    """
    Function for displaying the PrivacyPreserving algorithm
    """
    def displayPrivacy(self, value):
        try:
            self.sub_string.set(self.priv_options[value])

            frame1 = Frame(self.master, width=900, height=450, bg="white")
            frame1.place(x=250, y=100)

            Label(frame1, text="Input Image", fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=230, y=15)
            Label(frame1, text="Output Image", fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=600, y=15)

            Label(frame1, text="ResNet Type", fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=315, y=360)

            progressBar_privacy = Progressbar(frame1, mode='indeterminate', length=300, style="green.Horizontal.TProgressbar")
            progressBar_privacy.place(x=320, y=325)

            status = StringVar(frame1)
            Label(frame1, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=325)

            def get_resnet(choice):
                choice = resnet_var.get()
                return choice

            resnet_var = StringVar()
            resnet_options = ["ResNet18", "ResNet32-10", "ResNet152"]
            resnet_var.set("Choose")
            resnet = OptionMenu(frame1, resnet_var, *resnet_options, command=get_resnet).place(x=425, y=360)

            """
            Function for updating the progress bar.
            """
            def progress_privacy(process):
                progressBar_privacy.start()

                while process.poll() is None:
                    progressBar_privacy.update()
                
                progressBar_privacy.stop()


            """
            Function for running the model.
            """
            def run_privacy():

                os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/PrivacyPreserving/invertinggradients")

                input_image = ImageTk.PhotoImage(Image.open("auto.jpg").resize((250,250), Image.ANTIALIAS))
                image_label = Label(frame1, image = input_image)
                image_label.image = input_image
                image_label.place(x=150, y=40)

                status.set("Running Model. . .")

                priv_command = ["python3", "reconstruct_image.py", "--model", str(resnet_var.get()), "--dataset", \
                                "CIFAR10", "--trained_model", "--cost_fn", "sim", "--indices", "def", "--restarts", \
                                "32", "--save_image", "--target_id", "-1"]
                
                result = subprocess.Popen(priv_command, stdout=subprocess.PIPE)
                progress_privacy(result)

                status.set("Finished")

                output_image = ImageTk.PhotoImage(Image.open("images/a_ground_truth--1.png").resize((250,250), Image.ANTIALIAS))
                output_label = Label(frame1, image = output_image)
                output_label.image = output_image
                output_label.place(x=520, y=40)
                
            run_button = Button(frame1, text="Run Model", command=run_privacy)
            run_button.place(x=425, y=400)
            
        except KeyError:
            self.sub_string.set(value)
    
    """
    Function for Robustness algorithms
    """
    def displayRobustness(self, value):
        try:
            self.sub_string.set(self.rob_options[value])

            """
            Backdoor Attacks - NOT AVAILABLE BC CUDA NOT AVAILABLE
            """
            if self.rob_options[value] == "Backdoor Attacks":
                self.sub_string.set(self.rob_options[value])

                frame1 = Frame(self.master, width=900, height=450, bg="white")
                frame1.place(x=250, y=100)
                
                message = StringVar(frame1)
                message.set("Not Available")
                message_label = Label(frame1, textvariable=message, fg="dark blue", bg="white", font=("Arial", 25, 'bold'))
                message_label.place(x=400, y=200)

                message.set("Not Available")

            """
            Data Poisoning Attacks - LOGGED OUTPUT NOT STDOUT
            """
            if self.rob_options[value] == "Data Poisoning Attacks":
                self.sub_string.set(self.rob_options[value])

                frame1 = Frame(self.master, width=900, height=450, bg="white")
                frame1.place(x=250, y=100)

                progressBar_data_poison = Progressbar(frame1, mode='indeterminate', length=300, style="green.Horizontal.TProgressbar")
                progressBar_data_poison.place(x=320, y=325)

                status = StringVar(frame1)
                Label(frame1, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=325)

                text_box = Text(frame1, height=20, width=75, relief=RIDGE, borderwidth=2)
                text_box.place(x=200, y=25)
                
                """
                Function for updating the progress bar.
                """
                def progress_data_poison(process):
                    progressBar_data_poison.start()

                    while process.poll() is None:
                        progressBar_data_poison.update()
                          
                    progressBar_data_poison.stop()

                """
                Get Data Poisoning experiment
                """
                def get_experiment(choice):
                    choice = experiment_var.get()
                    return choice

                experiment_var = StringVar()
                experiment_options = ["Label Flipping Attack Feasibility", "Attack Timing in Label Flipping Attacks", 
                                        "Malicious Participant Availability", "Defending Against Label Flipping Attacks"]

                experiment_var.set("Choose")
                experiment = OptionMenu(frame1, experiment_var, *experiment_options, command=get_experiment).place(x=425, y=360)
                
                """
                Run Data Poisoning experiment
                """
                def run_experiment():
                    os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Robustness/DataPoisoning_FL")

                    if experiment_var.get() == "Label Flipping Attack Feasibility":
                        status.set("Running Model. . .")

                        feasibility = ["python3", "label_flipping_attack.py"]
                        
                        result = subprocess.Popen(feasibility, stdout=subprocess.PIPE, shell=False)
                        progress_data_poison(result)
                        text_box.insert(END, result.communicate()[0])
                        
                        status.set("Finished")

                    elif experiment_var.get() == "Attack Timing in Label Flipping Attacks":
                        status.set("Running Model. . .")

                        attack_timing = ["python3", "attack_timing.py"]
                        
                        result = subprocess.Popen(attack_timing, stdout=subprocess.PIPE, shell=False)
                        progress_data_poison(result)
                        text_box.insert(END, result.communicate()[0])

                        status.set("Finished")
                    
                    elif experiment_var.get() == "Malicious Participant Availability":
                        status.set("Running Model. . .")

                        malicious = ["python3", "malicious_participant_availability.py"]
                        
                        result = subprocess.Popen(malicious, stdout=subprocess.PIPE, shell=False)
                        progress_data_poison(result)
                        text_box.insert(END, result.communicate()[0])

                        status.set("Finished")
                    
                    else:
                        if experiment_var.get() == "Defending Against Label Flipping Attacks":
                            status.set("Model Not Available!")
                            
                exp_button = Button(frame1, text="Run Model", command=run_experiment)
                exp_button.place(x=430, y=400)

            """
            Model Poisoning Attacks - NOTEBOOKS AND UNLCEAR INSTRUCTIONS
            """ 
            if self.rob_options[value] == "Model Poisoning Attacks":
                self.sub_string.set(self.fair_options[value])

                frame1 = Frame(self.master, width=900, height=450, bg="white")
                frame1.place(x=250, y=100)
                
                message = StringVar(frame1)
                message.set("Not Available")
                message_label = Label(frame1, textvariable=message, fg="dark blue", bg="white", font=("Arial", 25, 'bold'))
                message_label.place(x=400, y=200)

                message.set("Not Available")
            """
            Free-rider Attacks - CAN'T CLONE REPOSITORY
            """
            if self.rob_options[value] == "Free-rider Attacks":
                self.sub_string.set(self.fair_options[value])

                frame1 = Frame(self.master, width=900, height=450, bg="white")
                frame1.place(x=250, y=100)
                
                message = StringVar(frame1)
                message.set("Not Available")
                message_label = Label(frame1, textvariable=message, fg="dark blue", bg="white", font=("Arial", 25, 'bold'))
                message_label.place(x=400, y=200)

                message.set("Not Available")
            """
            Inference Attacks
            """
            if self.rob_options[value] == "Inference Attacks":
                self.sub_string.set(self.rob_options[value])

                frame1 = Frame(self.master, width=900, height=450, bg="white")
                frame1.place(x=250, y=100)
                """
                Function for updating the progress bar.
                """
                def progress_inference(process):
                  progressBar_inference.start()

                  while process.poll() is None:
                      progressBar_inference.update()
                            
                  progressBar_inference.stop()

                progressBar_inference = Progressbar(frame1, mode='indeterminate', length=300, style="green.Horizontal.TProgressbar")
                progressBar_inference.place(x=320, y=325)

                status = StringVar(frame1)
                Label(frame1, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=325)

                text_box = Text(frame1, height=20, width=75, relief=RIDGE, borderwidth=2)
                text_box.place(x=200, y=25)

        
                """
                Get Data Inference experiment
                """
                def get_inference_attack(choice):
                    choice = experiment_var.get()
                    return choice

                experiment_var = StringVar()
                experiment_options = ["Equation Solving Attack", "Path Restriction Attack", 
                                        "Generative Regression Network Attack"]

                experiment_var.set("Choose")
                experiment = OptionMenu(frame1, experiment_var, *experiment_options, command=get_inference_attack).place(x=425, y=360)
                
                """
                Run Data Inference experiment
                """
                def run_inference_attack():
                    if experiment_var.get() == "Equation Solving Attack":
                        os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Robustness/featureinference-vfl/ESA")

                        status.set("Running Model. . .")

                        esa = ["python3", "main-esa.py"]

                        result = subprocess.Popen(esa, stdout=subprocess.PIPE)
                        progress_inference(result)
                        text_box.insert(END, result.communicate()[0])
                        
                        status.set("Finished")

                    elif experiment_var.get() == "Path Restriction Attack":
                        os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Robustness/featureinference-vfl/PRA")

                        status.set("Running Model. . .")

                        pra = ["python3", "main-pra.py"]
                        
                        result = subprocess.Popen(pra, stdout=subprocess.PIPE)
                        progress_inference(result)
                        text_box.insert(END, result.communicate()[0])

                        status.set("Finished")
                    
                    else:
                        if experiment_var.get() == "Generative Regression Network Attack":
                            os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Robustness/featureinference-vfl/GRNA")

                            status.set("Running Model. . .")

                            grna = ["python3", "main-grna.py"]
                            
                            result = subprocess.Popen(grna, stdout=subprocess.PIPE)
                            progress_inference(result)
                            text_box.insert(END, result.communicate()[0])

                            status.set("Finished")
                            
                inference_button = Button(frame1, text="Run Model", command=run_inference_attack)
                inference_button.place(x=430, y=400)

            """
            Byzantine Robusteness
            """
            if self.rob_options[value] == "Byzantine Robustness":
                self.sub_string.set(self.rob_options[value])
            
                frame1 = Frame(self.master, width=900, height=450, bg="white")
                frame1.place(x=250, y=100)   

                progressBar_byz = Progressbar(frame1, mode='indeterminate', length=300, style="green.Horizontal.TProgressbar")
                progressBar_byz.place(x=325, y=325)

                status = StringVar(frame1)
                Label(frame1, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=325)

                text_box = Text(frame1, height=20, width=75, relief=RIDGE, borderwidth=2)
                text_box.place(x=200, y=25)

                """
                Get Byzantine experiment
                """
                def get_byzantine_attack(choice):
                    choice = experiment_var.get()
                    return choice

                experiment_var = StringVar()
                experiment_options = ["No Attack", "Attack with 5 Devices", 
                                        "Attack with 10 Devices"]

                experiment_var.set("Choose")
                experiment = OptionMenu(frame1, experiment_var, *experiment_options, command=get_byzantine_attack).place(x=425, y=390)
                """
                Function for updating the progress bar.
                """
                def progress_byz(process):
                    progressBar_byz.start()

                    while process.poll() is None:
                        progressBar_byz.update()
                    
                    progressBar_byz.stop()


                """
                Function for running the model.
                """
                def run_byz():

                    os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Robustness/Byzantine_AirComp")
                    
                    if experiment_var.get() == "No Attack":
                        status.set("Running Model. . .")

                        no_attack = ["python3", "MNIST_Air_weight.py", "--var", "1e-2", "--mark", "0-50"]

                        result = subprocess.Popen(no_attack, stdout=subprocess.PIPE)
                        progress_byz(result)
                        text_box.insert(END, result.communicate()[0])
                        
                        status.set("Finished")

                    elif experiment_var.get() == "Attack with 5 Devices":
                        status.set("Running Model. . .")

                        five = ["python3", "MNIST_Air_weight.py", "--var", "1e-2", "--mark", "0-50", "--B", "5"]
                        
                        result = subprocess.Popen(five, stdout=subprocess.PIPE)
                        progress_byz(result)
                        text_box.insert(END, result.communicate()[0])

                        status.set("Finished")
                    
                    else:
                        if experiment_var.get() == "Attack with 10 Devices":
                            status.set("Running Model. . .")

                            ten = ["python3", "MNIST_Air_weight.py", "--var", "1e-2", "--mark", "0-50", "--B", "10"]
                            
                            result = subprocess.Popen(ten, stdout=subprocess.PIPE)
                            progress_byz(result)
                            text_box.insert(END, result.communicate()[0])

                            status.set("Finished")

                    status.set("Finished")
                    
                run_byz_button = Button(frame1, text="Run Model", command=run_byz)
                run_byz_button.place(x=430, y=355)

            """ 
            Sybil Robusteness
            """
            if self.rob_options[value] == "Sybil Robustness":
                self.sub_string.set(self.rob_options[value])
            
                frame1 = Frame(self.master, width=900, height=450, bg="white")
                frame1.place(x=250, y=100)   

                progressBar_sybil = Progressbar(frame1, mode='indeterminate', length=300, style="green.Horizontal.TProgressbar")
                progressBar_sybil.place(x=325, y=325)

                status = StringVar(frame1)
                Label(frame1, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=325)

                text_box = Text(frame1, height=20, width=75, relief=RIDGE, borderwidth=2)
                text_box.place(x=200, y=25)

                """
                Function for updating the progress bar.
                """
                def progress_sybil(process):
                    progressBar_sybil.start()

                    while process.poll() is None:
                        progressBar_sybil.update()
                    
                    progressBar_sybil.stop()


                """
                Function for running the model.
                """
                def run_sybil():

                    os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Robustness/FoolsGold/ML")
                    
                    sybil_command = ["python3", "code/ML_main.py", "mnist", "1000", "5_1_7"]

                    status.set("Running Model. . .")
                    sybil = subprocess.Popen(sybil_command, stdout=subprocess.PIPE)
                    progress_sybil(sybil)
                    text_box.insert(END, sybil.communicate()[0])

                    status.set("Finished")
                    
                run_button = Button(frame1, text="Run Model", command=run_sybil)
                run_button.place(x=430, y=355)

            """
            Certified Robusteness - NOT AVAILABlE
            """
            if self.rob_options[value] == "Certified Robustness":
                self.sub_string.set(self.fair_options[value])

                frame1 = Frame(self.master, width=900, height=450, bg="white")
                frame1.place(x=250, y=100)
                
                message = StringVar(frame1)
                message.set("Not Available")
                message_label = Label(frame1, textvariable=message, fg="dark blue", bg="white", font=("Arial", 25, 'bold'))
                message_label.place(x=400, y=200)

                message.set("Not Available")
                
        except KeyError:
            self.sub_string.set(value)
    
    """
    Function for easyFL algorithm - DOES NOT WORK
    """
    def displayFairness(self, value):
        try:
            self.sub_string.set(self.fair_options[value])

            frame1 = Frame(self.master, width=900, height=450, bg="white")
            frame1.place(x=250, y=100) 
                
            Label(frame1, text="Number of Rounds", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=100)
            Label(frame1, text="Learning Rate", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=200)
            Label(frame1, text="Number of Epochs", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=150, y=300)
            Label(frame1, text="Proportion", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=150)
            Label(frame1, text="Batch Size", fg="dark blue", bg="white", font=("Arial", 20, "bold")).place(x=550, y=250)

            round_var = IntVar()
            lr_var = DoubleVar()
            epoch_var = IntVar()
            prop_var = DoubleVar()
            batch_var = IntVar()

            Entry(frame1, textvariable=round_var, width=5).place(x=350, y=100)
            Entry(frame1, textvariable=lr_var, width=5).place(x=350, y=200)
            Entry(frame1, textvariable=epoch_var, width=5).place(x=350, y=300)
            Entry(frame1, textvariable=prop_var, width=5).place(x=700, y=150)            
            Entry(frame1, textvariable=batch_var, width=5).place(x=700, y=250)

            frame2 = Frame(self.master, width=900, height=450, bg="white")

            """
            Starting frame
            """
            def entry_frame():
                frame2.place(x=250, y=100)
                frame1.place_forget()

            """
            Second Frame
            """
            def results_frame():
                frame1.place(x=250, y=100)
                frame2.place_forget()

            submit_button = Button(frame1, text="Save Results", command=entry_frame)
            submit_button.place(x=450, y=400)

            progressBar_fair = Progressbar(frame2, mode='indeterminate', length=300, style="green.Horizontal.TProgressbar")
            progressBar_fair.place(x=325, y=325)

            status = StringVar(frame2)
            Label(frame2, textvariable=status, fg="dark blue", bg="white", font=("Arial", 15, "bold")).place(x=650, y=325)
            text_box = Text(frame2, height=20, width=75, relief=RIDGE, borderwidth=2)
            text_box.place(x=200, y=25)

            """
            Progress function
            """
            def progress_func_fair(process):
                progressBar_fair.start()

                while process.poll() is None:
                    progressBar_fair.update()
                
                progressBar_fair.stop()

            """
            Run the easyFL model
            """
            def run_easyFL():

                os.chdir("/Users/claytonhaley/Desktop/COMP6130/FinalProject/COMP6130_Group4/Fairness/easyFL")
                
                requirements1 = ["pip3", "install", "-r", "requirements.txt"]
                requirements2 = ["pip3", "install", "numpy==1.20.0"]
                requirements3 = ["pip3", "install", "ujson"]

                status.set("Installing Requirements. . .")
                req1 = subprocess.Popen(requirements1, stdout=subprocess.PIPE)
                req2 = subprocess.Popen(requirements2, stdout=subprocess.PIPE)
                req3 = subprocess.Popen(requirements3, stdout=subprocess.PIPE)
                progress_func_fair(req1)
                progress_func_fair(req2)
                progress_func_fair(req3)

                data_command = ["python3", "generate_fedtask.py"]
                
                status.set("Generating Data. . .")
                data = subprocess.Popen(data_command, stdout=subprocess.PIPE)
                progress_func_fair(data)

                run_model = ["python3", "main.py", "--task", "mnist_client100_dist0_beta0_noise0", "--model", "cnn", "--method", "fedavg", \
                        "--num_rounds", str(round_var.get()), "--num_epochs", str(epoch_var.get()), "--learning_rate", str(lr_var.get()), "--proportion", str(prop_var.get()), "--batch_size", str(batch_var.get()), \
                        "--train_rate", "1", "--eval_interval", "1"]

                status.set("Running Model. . .")
                model = subprocess.Popen(run_model, stdout=subprocess.PIPE)
                progress_func_fair(model) 
                text_box.insert(END, model.communicate()[0])

                status.set("Finished")

            run_button = Button(frame2, text="Run Model", command=run_easyFL)
            run_button.place(x=430, y=355)

            back_button = Button(frame2, text="Back", command=results_frame)
            back_button.place(x=450, y=400)

        except KeyError:
            self.sub_string.set(value)


root = Tk()
app = App(root)
root.mainloop()
