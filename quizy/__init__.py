from rich import print
__version__ = '0.1.0'
class Quiz:
    def __init__(self, name: str):
        self.data = []
        self.name = name
    def add_question(self, question: str, options: list, answer: int):
        self.data.append({"question": question, "options": options, "answer": answer})
    def run(self):
        for q in self.data:
            correct = False
            print(q["question"])
            for option in range(len(q["options"])):
                print(f"({option}) {q['options'][option]}")
            while correct == False:
                answer = input("Choose an option number from the list above: ")
                if answer == q["answer"]:
                    print("[green]:star:correct!:star:")
                    correct = True
                else:
                    print("[red]incorrect!")
