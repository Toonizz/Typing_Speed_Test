from tkinter import *


# page to record the user test history in a text file
class ResultsPage(Frame):

    def __init__(self, container):
        Frame.__init__(self, container)
        self.container = container
        self.config(bg="#50CB93")
        self.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.read_results_data()

    def read_results_data(self):
        with open("test_results.txt", "r") as results:
            self.results = results.readlines()
            if self.results == []:
                self.empty_page()
            else:
                self.results = [line.strip() for line in self.results]
                self.results = [self.results[i].split(",") for i in range(len(self.results)) if i > 0]
                self.create_page(self.results)

    def empty_page(self):
        empty_label = Label(self, text="You don't have any saved test results. \n Please take the"
                                       " typing speed test first.",
                            bg="#50CB93", font=("Times New Roman", 14, "bold"),
                            fg="#54436B")
        empty_label.pack(fill="both", padx=120, pady=150)

    def create_page(self, results):
        dates = [line[0] for line in results]
        total_number_of_tests = len(results)
        sum_wpm = [float(line[1]) for line in results]
        average_wpm = round((sum(sum_wpm)) / total_number_of_tests)
        sum_cpm = [float(line[2]) for line in results]
        average_cpm = round((sum(sum_cpm)) / total_number_of_tests)
        sum_accuracy = [float(line[3]) for line in results]
        average_accuracy = round((sum(sum_accuracy)) / total_number_of_tests)
        self.results_summary_label = Label(self,
                                           text=f"Here's your results from previous typing speed tests: \n"
                                                f"\nTotal Number of Tests Completed: "
                                                f"{total_number_of_tests}\n"
                                                f"Average Words/min: {average_wpm}\n"
                                                f"Average Char/min: {average_cpm}\n"
                                                f"Average Accuracy: {average_accuracy}%",
                                           bg="#71EFA3", font=("Times New Roman", 14, "bold"),
                                           fg="#54436B", justify="left", anchor="nw")
        self.results_summary_label.pack(fill="x", padx=20, pady=20)
