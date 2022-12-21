import tkinter as tk
import ExpressionsConverter
import binarytree as bt


class UserInterface:
    def __init__(self):
        self.EC = ExpressionsConverter.Converter()
        self.postfix_str = ""
        self.prefix_str = ""
        self.infix_str = ""
        self.expression = "Expression: "
        self.is_tree_enabled = False
        self.master = tk.Tk()
        self.master.eval('tk::PlaceWindow . center')
        self.master.title("Expressions Converter")
        self.master.geometry("850x400")
        self.master.configure(bg="#192841")
        self.converter()
        self.master.mainloop()

    def menu(self):
        tk.Button(self.master, bg="#192841", foreground="#FFFFFF", font="Fixedsys", text="Converter",
                  command=self.converter).grid(row=1, column=0, sticky="nswe")
        tk.Button(self.master, bg="#192841", foreground="#FFFFFF", font="Fixedsys", text="Priorities",
                  command=self.priorities).grid(row=2, column=0, sticky="nswe")
        tree = tk.Button(self.master, bg="#192841", foreground="#FFFFFF", font="Fixedsys", text="Tree",
                  command=self.tree)
        tree .grid(row=3, column=0,sticky="nswe")
        if not self.is_tree_enabled:
            tree.config(state="disabled")

    def converter(self, previous_choice: int = 2):
        def convert():
            if inputt.get().strip() == "":
                self.is_tree_enabled = False
                return
            self.expression = inputt.get().strip()
            if int(option.get()) == 2:
                self.postfix_str = self.EC.infix_to_postfix(inputt.get())
                self.prefix_str = self.EC.infix_to_prefix(inputt.get())
                self.infix_str = inputt.get()
            elif int(option.get()) == 3:
                self.postfix_str = self.EC.prefix_to_postfix(inputt.get())
                self.prefix_str = inputt.get()
                self.infix_str = self.EC.prefix_to_infix(inputt.get())
            elif int(option.get()) == 4:
                self.postfix_str = inputt.get()
                self.prefix_str = self.EC.postfix_to_prefix(inputt.get())
                self.infix_str = self.EC.postfix_to_infix(inputt.get())
            self.is_tree_enabled= True
            self.converter(int(option.get()))

        self.clear_master()
        self.menu()
        tk.Label(self.master, text="Infix: "+self.infix_str, bg="#192841", foreground="#FFFFFF", font="Fixedsys").grid(row=1,
                                                                                                         column=6,
                                                                                                         sticky=tk.W,
                                                                                                         padx=15)
        tk.Label(self.master, text="Postfix: "+self.postfix_str, bg="#192841", foreground="#FFFFFF", font="Fixedsys").grid(row=2,
                                                                                                           column=6,
                                                                                                           sticky=tk.W,
                                                                                                           padx=15)
        tk.Label(self.master, text="Prefix: "+self.prefix_str, bg="#192841", foreground="#FFFFFF", font="Fixedsys").grid(row=3,
                                                                                                          column=6,
                                                                                                          sticky=tk.W,
                                                                                                          padx=15)
        inputt = tk.Entry(self.master)
        inputt.grid(row=1, column=2,padx=15)
        inputt.insert(0, self.expression)
        options = ["Infix", "Prefix", "Postfix"]
        option = tk.StringVar(self.master)
        i = 2
        for o in options:
            tk.Radiobutton(self.master, text=o, variable=option, value=i, bg="#192841", foreground="#FFFFFF",
                           selectcolor="#192841", activebackground="#192841", activeforeground="white").grid(row=2,
                                                                                                             column=i,
                                                                                                             ipady=3)
            i += 1
        option.set(previous_choice)
        tk.Button(self.master, bg="#192841", foreground="#FFFFFF", font="Fixedsys", text="Convert",
                  command=convert).grid(row=1, column=3,
                                        sticky="nswe",
                                        padx=15)
        tk.Button(self.master, bg="#192841", foreground="#FFFFFF", font="Fixedsys", text="Clear",
                  command=self.clear_results).grid(row=1, column=4,
                                        sticky="nswe",
                                        padx=15)

    def clear_results(self):
        self.postfix_str=""
        self.prefix_str=""
        self.infix_str =""
        self.is_tree_enabled = False
        self.expression = "Expression: "
        self.converter()

    def priorities(self):
        def edit():
            try:
                self.EC.edit_priorities(char_input.get(), int(priority_input.get()))
            except Exception as e:
                print(str(e))
            self.priorities()

        self.clear_master()
        self.menu()
        text1 = ""
        text2 = ""
        label1 = tk.Label(self.master, bg="#192841", foreground="#FFFFFF", font="Fixedsys")
        label1.grid(row=4, column=2, sticky=tk.W, padx=15)
        label2 = tk.Label(self.master, bg="#192841", foreground="#FFFFFF", font="Fixedsys")
        label2.grid(row=4, column=3, sticky=tk.W, padx=15)
        index = 0
        for key in self.EC.priorities.keys():
            if key != ")" and key != "(":
                if index % 2 == 0:
                    text1 += key + " : " + str(self.EC.priorities.get(key)) + "\n"
                else:
                    text2 += key + " : " + str(self.EC.priorities.get(key)) + "\n"
                index += 1
        label1.config(text=text1)
        label2.config(text=text2)
        tk.Label(self.master, bg="#192841", foreground="#FFFFFF", font="Fixedsys", text="Edit:").grid(row=1, column=2,
                                                                                                      sticky=tk.W,
                                                                                                      padx=15)
        char_input = tk.Entry(self.master)
        char_input.grid(row=2, column=2, sticky=tk.W, padx=15)
        char_input.insert(0, "single character:")
        priority_input = tk.Entry(self.master)
        priority_input.grid(row=2, column=3, sticky=tk.W, padx=15)
        priority_input.insert(0, "priority:")
        tk.Button(self.master, bg="#192841", foreground="#FFFFFF", font="Fixedsys", text="edit",
                  command=edit).grid(row=2, column=5)

    def clear_master(self):
        for child in self.master.winfo_children():
            child.destroy()

    def binary_tree(self):
        stack = []
        for char in self.postfix_str:
            if char.isalnum():
                stack.append(bt.Node(char))
            else:
                node = bt.Node(char)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        return stack.pop()

    def tree(self):
        self.clear_master()
        self.menu()
        bt_node = self.binary_tree()
        # frame = tk.Frame(self.master, bg="#192841")
        # frame.grid(row=4, column=1, ipadx=150)
        MAX_HEIGHT = (bt_node.height + 1) * 50
        MAX_WIDTH = (2 ** (bt_node.height + 1)) * 50
        canvas = tk.Canvas(self.master, height=300, width=700, bg="#192841", scrollregion=(0,0,MAX_WIDTH,MAX_HEIGHT))
        canvas.grid(row=4, column=1)
        scroll_bar_x = tk.Scrollbar(self.master, orient=tk.HORIZONTAL)
        scroll_bar_x.grid(row=5, column=1, sticky="nswe")
        scroll_bar_x.config(command=canvas.xview)
        scroll_bar_x.set(0,MAX_WIDTH)
        scroll_bar_y = tk.Scrollbar(self.master, orient=tk.VERTICAL)
        scroll_bar_y.grid(row=4, column=2, sticky="nswe")
        scroll_bar_y.config(command=canvas.yview)
        scroll_bar_y.set(0, MAX_HEIGHT)
        canvas.config(xscrollcommand=scroll_bar_x.set)
        canvas.config(yscrollcommand=scroll_bar_y.set)

        def display_tree(node: bt.Node, min_height: int, max_width: int, chunk: int):
            canvas.create_oval(max_width / 2 - 10, min_height - 10, max_width / 2 + 10, min_height + 10, fill="white")
            if node.left is not None:
                canvas.create_line(max_width / 2, min_height, int(max_width / 2) - int(chunk / 2), min_height + 35, fill="white")
                display_tree(node.left, min_height + 35, max_width - int(chunk), int(chunk / 2))
            if node.right is not None:
                canvas.create_line(max_width / 2, min_height, int(max_width / 2) + int(chunk / 2), min_height + 35,
                                   fill="white")
                display_tree(node.right, min_height + 35, max_width + int(chunk), int(chunk / 2))
            canvas.create_text(max_width / 2, min_height, text=node.value, fill="#192841")

        if self.expression.strip() != "" and self.expression != "Expression: ":
            display_tree(bt_node, 20, MAX_WIDTH, MAX_WIDTH/2)
        else :
            canvas.create_text(MAX_HEIGHT/2, MAX_WIDTH/2, text="Nothing to show!!", fill="white")


