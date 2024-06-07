import random
import tkinter as tk

word_lists = {
    "Fruits": ["apple", "banana", "orange", "kiwi", "pineapple", "strawberry", "grape","watermelon", "mango","pear",
               "cherry", "blueberry", "apricot", "peach", "plum", "raspberry", "lemon", "lime", "grapefruit", "pomegranate"],

    "Coding Languages": ["python", "java", "javascript", "php", "ruby", "html", "css", "c", "cpp", "csharp", "swift",
                         "kotlin", "typescript", "rust", "go", "scala", "perl", "r", "sql", "bash"],
    "Vegetables": ["carrot", "tomato", "broccoli", "spinach", "potato", "cucumber", "bell pepper", "onion", "lettuce",
            "celery", "zucchini", "eggplant", "cauliflower", "green beans", "asparagus", "cabbage", "radish", "sweet potato", "peas", "brussels sprouts"],
    "Constellations": ["Orion", "Ursa Major", "Cassiopeia", "Leo", "Pegasus", "Gemini", "Virgo", "Taurus", "Scorpius",
                       "Canis Major", "Aquarius", "Sagittarius", "Pisces", "Cygnus", "Lyra", "Aries", "Capricornus", "Libra", "Hydra", "Perseus"],
    "Classic Singers (Hollywood)": ["Frank Sinatra", "Ella Fitzgerald", "Nat King Cole", "Billie Holiday", "Louis Armstrong", "Bing Crosby", "Aretha Franklin",
            "Dean Martin", "Johnny Cash", "Sam Cooke", "Etta James", "Elvis Presley", "Ray Charles", "Nina Simone", "Duke Ellington", "Patsy Cline", "Judy Garland", "Tony Bennett", "Bobby Darin", "Doris Day"],
    "Classic Singers (Bollywood)": ["Lata Mangeshkar", "Mohammed Rafi", "Kishore Kumar", "Asha Bhosle", "Mukesh", "Hemanta Kumar Mukhopadhyay", "Geeta Dutt", "Talat Mahmood", "Manna Dey", "Kumar Sanu",
            "Alka Yagnik", "Udit Narayan", "Arijit Singh", "Sonu Nigam", "Shreya Ghoshal", "KJ Yesudas", "SP Balasubrahmanyam", "Laxmikant Pyarelal", "RD Burman", "Madan Mohan"],
    "Classic Actors (Hollywood)": ["Humphrey Bogart", "Marilyn Monroe", "James Stewart", "Audrey Hepburn", "Clark Gable", "Katharine Hepburn", "Cary Grant", "Bette Davis", "Marlon Brando", "Ingrid Bergman",
            "Spencer Tracy", "Greta Garbo", "Charlie Chaplin", "Elizabeth Taylor", "John Wayne", "Grace Kelly", "Humphrey Bogart", "Laurence Olivier", "Joan Crawford", "Gary Cooper"],
    "Classic Actors (Bollywood)": ["Dilip Kumar", "Raj Kapoor", "Dev Anand", "Amitabh Bachchan", "Rajesh Khanna", "Guru Dutt", "Balraj Sahni", "Ashok Kumar", "Rajendra Kumar", "Shammi Kapoor", "Sunil Dutt",
            "Dharmendra", "Mohanlal", "Naseeruddin Shah", "Sanjeev Kumar", "Manoj Kumar", "Amrish Puri", "Anupam Kher", "Vinod Khanna", "Rishi Kapoor"],
}

def choose_word(category=None):
    if category is None:
        category = random.choice(list(word_lists.keys()))
    word_list = word_lists[category]
    return random.choice(word_list)

class MrIncredibleGame:
    def __init__(self, word):
        self.word = word.upper()
        self.guesses_left = 6
        self.letters_guessed = []
        guess_index = random.randint(0, len(self.word) - 1)
        self.display_word = "-" * len(self.word)
        self.display_word = self.display_word[:guess_index] + self.word[guess_index] + self.display_word[guess_index+1:]
        
        self.create_gui()

    def update_display_word(self):
        new_display_word = ""
        for i in range(len(self.word)):
            if self.word[i] == self.display_word[i]:
                new_display_word += self.word[i]
            elif self.word[i] in self.letters_guessed:
                new_display_word += self.word[i]
            else:
                new_display_word += "-"
        self.display_word = new_display_word
        self.word_label.config(text=self.display_word)

    def guess_letter(self, letter):
        if letter in self.letters_guessed:
            self.info_label.config(text="You already guessed that letter!")
        else:
            self.letters_guessed.append(letter)
            if letter in self.word:
                self.update_display_word()
                if "-" not in self.display_word:
                    self.info_label.config(text="Congratulations, you won!")
                    self.disable_buttons()
            else:
                self.guesses_left -= 1
                self.info_label.config(text="Sorry, wrong letter!")
                self.update_mrincredible()
                if self.guesses_left == 0:
                    self.info_label.config(text="Sorry, you lost! The word was {}".format(self.word))
                    self.disable_buttons()

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Mr. Incredible")
        self.category_var = tk.StringVar()
        self.category_var.set("Select category")
        categories = ["All"] + list(word_lists.keys())
        self.category_menu = tk.OptionMenu(self.root, self.category_var, *categories, command=self.change_category)
        self.category_menu.grid(row=0, column=0, columnspan=2)

        self.canvas = tk.Canvas(self.root, width=200, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2)
        
        self.images = [
            tk.PhotoImage(file="Images/mrincredible/1.png"),
            tk.PhotoImage(file="Images/mrincredible/2.png"),
            tk.PhotoImage(file="Images/mrincredible/3.png"),
            tk.PhotoImage(file="Images/mrincredible/4.png"),
            tk.PhotoImage(file="Images/mrincredible/5.png"),
            tk.PhotoImage(file="Images/mrincredible/6.png"),
            tk.PhotoImage(file="Images/mrincredible/7.png")
        ]
        self.mrincredible_image = self.canvas.create_image(100, 110, image=self.images[0])

        self.word_label = tk.Label(self.root, text=self.display_word, font=("Arial", 24))
        self.word_label.grid(row=2, column=0, columnspan=2)

        self.info_label = tk.Label(self.root, text="Guess a letter!", font=("Arial", 16))
        self.info_label.grid(row=3, column=0, columnspan=2)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=4, column=0, columnspan=2)
        
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, bg="green", fg="white", font=("Forte", 16), relief="ridge")
        self.restart_button.grid(row=5, column=0, columnspan=2)


        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            bg_color = '#ADD8E6'
            fg_color = 'black'
            button = tk.Button(self.button_frame, text=letter, width=3, bg=bg_color, fg=fg_color, command=lambda l=letter: self.guess_letter(l))
            button.pack(side="left")
    def disable_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.config(state="disabled")
    def update_mrincredible(self):
        self.canvas.itemconfig(self.mrincredible_image, image=self.images[6-self.guesses_left])
    
    def change_category(self, category):
        word = choose_word(None if category == "All" else category)
        self.root.destroy()
        game = MrIncredibleGame(word)
        game.start_game()
    
    def start_game(self):
        self.root.mainloop()

    def restart_game(self):
        self.root.destroy()
        word = choose_word()
        self.__init__(word)
        self.start_game()

word = choose_word()
game = MrIncredibleGame(word)
game.start_game()
