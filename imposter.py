import tkinter as tk
from tkinter import ttk, messagebox
import random


class ImposterGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Imposter Game")
        self.geometry("600x400")
        self.resizable(False, False)

        # Categories and words
        self.categories = {
            "Creatures": [
                # These are just examples, you can expand or modify the lists as needed
                "dog", "cat", "bird", "fish", "hamster", "rabbit", "turtle", "snake",
            ],

            "Food": [
                "pizza", "hamburger", "hot dog", "taco", "burrito", "sandwich", "pasta", "spaghetti",
                "lasagna", "steak", "fried chicken", "sushi", "ramen", "salad", "soup", "omelette",
                "pancakes", "waffles", "cereal", "bagel", "donut", "croissant", "apple", "banana",
                "strawberry", "grape", "melon", "peach", "pear", "orange", "lemon", "lime",
                "pineapple", "mango", "blueberry", "raspberry", "carrot", "broccoli", "lettuce",
                "spinach", "potato", "corn", "rice", "beans", "noodles", "chocolate", "candy",
                "ice cream", "cookie", "brownie", "protein bar",
            ],

            "Objects": [
                "chair", "table", "couch", "bed", "lamp", "mirror", "window", "door", "backpack",
                "wallet", "phone", "laptop", "keyboard", "mouse", "remote", "television", "camera",
                "bottle", "cup", "mug", "plate", "fork", "spoon", "knife", "blanket", "pillow",
                "clock", "fan", "toaster", "microwave", "trash can", "vacuum", "helmet",
                "gloves", "scissors", "pen", "pencil", "marker", "notebook", "book", "calendar",
                "folder", "towel", "suitcase", "umbrella", "flashlight", "binoculars", "hammer",
                "drill", "screwdriver", "ruler", "guitar", "drums", "piano", "violin", "flute",
                "trumpet", "saxophone", "microphone", "headphones", "record player", "car", "bus",
                "train", "airplane", "boat", "helicopter", "bicycle", "motorcycle", "subway",
                "scooter", "skateboard", "hot air balloon", "spaceship", "canoe", "yacht",
                "ambulance", "police car", "fire truck", "wand", "potion", "broom", "sword",
            ],

            "Movies": [
                "Titanic", "Avatar", "Star Wars", "The Matrix", "Inception", "The Lion King", "Frozen",
                "Toy Story", "Jurassic Park", "Harry Potter", "The Avengers", "Iron Man",
                "Black Panther", "Finding Nemo", "Shrek", "The Dark Knight", "Spider-Man", "Rocky",
                "Ghostbusters", "Back to the Future", "Indiana Jones", "The Godfather", "Jaws",
                "E.T.", "Cinderella", "Moana", "Coco", "The Terminator", "Alien", "Fast and Furious",
                "Mission Impossible", "The Hunger Games", "The Notebook", "Up", "Inside Out", "Cars",
                "WALL-E",
            ],

            "Locations": [
                "mountain", "forest", "desert", "island", "city", "village", "airport",
                "school", "hospital", "mall", "stadium", "museum", "zoo", "restaurant", "cafe",
                "library", "castle", "bridge", "harbor", "subway", "highway", "park", "playground",
                "office", "church", "temple", "hotel", "campground", "ski resort", "garden", "garage",
                "basement", "attic", "living room", "kitchen", "bathroom", "rooftop", "warehouse",
                "kitchen", "bathroom", "bedroom", "garage", "basement", "attic",
                "laundry room", "dining room", "hallway", "office", "pantry", "garden shed",
                "Eiffel Tower", "Statue of Liberty", "Great Wall of China", "Pyramids of Giza",
                "Big Ben", "Colosseum", "Mount Rushmore", "Golden Gate Bridge", "Sydney Opera House",
                "Taj Mahal", "castle", "living room",
            ],

            "Sports": [
                "soccer", "basketball", "baseball", "football", "tennis", "golf", "hockey",
                "volleyball", "swimming", "boxing", "wrestling", "karate", "taekwondo", "archery",
                "gymnastics", "skiing", "snowboarding", "surfing", "skateboarding", "cycling",
                "running", "marathon", "track and field", "rowing", "fishing", "bowling", "badminton",
                "ping pong", "rugby", "cricket", "water polo", "handball", "lacrosse",
            ],

            "Professions": [
                "doctor", "nurse", "teacher", "chef", "pilot", "police officer", "firefighter",
                "engineer", "scientist", "lawyer", "mechanic", "electrician", "plumber", "carpenter",
                "artist", "musician", "actor", "writer", "photographer", "farmer", "driver",
                "architect", "dentist", "cashier", "waiter", "barista", "coach", "librarian",
                "veterinarian", "paramedic", "soldier", "astronaut", "principal", "teacher", "janitor",
                "lunch lady", "coach", "nurse", "counselor", "librarian", "crossing guard",
                "knight", "DJ",
            ],

            "Weather": [
                "rain", "snow", "thunderstorm", "hurricane", "tornado", "sunshine", "fog",
                "windy day", "hail", "blizzard", "heat wave", "cold front", "rainbow",
                "cloudy sky", "lightning",
            ],

            "Video Games": [
                "Minecraft", "Fortnite", "Call of Duty", "Mario", "Zelda", "Pokemon", "Halo",
                "Overwatch", "Roblox", "League of Legends", "Elden Ring",
                "Grand Theft Auto", "Among Us", "Tetris", "Pac-Man",
            ],
        }

        self.player_assignments = []
        self.secret_word = None
        self.selected_category = tk.StringVar(value="Locations")

        # Random category toggle
        self.random_category = tk.BooleanVar(value=False)

        # Store last game settings for "Run it back"
        self.last_players = None
        self.last_imposters = None
        self.last_category = None
        self.last_random = False

        self._build_setup_screen()

    def _clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def _build_setup_screen(self):
        self._clear_window()

        title = ttk.Label(self, text="Setup", font=("Arial", 18, "bold"))
        title.pack(pady=20)

        form_frame = ttk.Frame(self)
        form_frame.pack(pady=10)

        # Total players
        ttk.Label(form_frame, text="Total players (3+):").grid(
            row=0, column=0, sticky="e", padx=5, pady=5
        )
        self.players_var = tk.IntVar(value=3)
        players_spin = ttk.Spinbox(
            form_frame, from_=3, to=20, textvariable=self.players_var, width=5
        )
        players_spin.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        # Imposters
        ttk.Label(form_frame, text="Number of imposters:").grid(
            row=1, column=0, sticky="e", padx=5, pady=5
        )
        self.imposters_var = tk.IntVar(value=1)
        imposters_spin = ttk.Spinbox(
            form_frame, from_=1, to=10, textvariable=self.imposters_var, width=5
        )
        imposters_spin.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        # Category selection
        ttk.Label(form_frame, text="Category:").grid(
            row=2, column=0, sticky="e", padx=5, pady=5
        )
        category_combo = ttk.Combobox(
            form_frame,
            textvariable=self.selected_category,
            values=list(self.categories.keys()),
            state="readonly",
            width=20,
        )
        category_combo.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        # Random category option
        random_check = ttk.Checkbutton(
            form_frame,
            text="Random category",
            variable=self.random_category,
        )
        random_check.grid(row=3, column=0, columnspan=2, pady=5)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)

        start_btn = ttk.Button(button_frame, text="Start Game", command=self.start_game)
        start_btn.grid(row=0, column=0, padx=10)

        quit_btn = ttk.Button(button_frame, text="Quit", command=self.destroy)
        quit_btn.grid(row=0, column=1, padx=10)

    def start_game(self):
        total_players = self.players_var.get()
        imposters = self.imposters_var.get()

        if total_players < 3:
            messagebox.showerror("Error", "You need at least 3 players.")
            return

        if imposters < 1:
            messagebox.showerror("Error", "There must be at least 1 imposter.")
            return

        if imposters >= total_players:
            messagebox.showerror(
                "Error", "Imposters must be fewer than total players."
            )
            return

        # Decide category
        if self.random_category.get():
            category = random.choice(list(self.categories.keys()))
            messagebox.showinfo("Category chosen", f"Random category: {category}")
        else:
            category = self.selected_category.get()

        words = self.categories.get(category, [])
        if not words:
            messagebox.showerror("Error", "No words found for this category.")
            return

        # Pick a random word from the chosen category
        self.secret_word = random.choice(words)

        # Save last game settings for "Run it back"
        self.last_players = total_players
        self.last_imposters = imposters
        self.last_category = category
        self.last_random = self.random_category.get()

        # Create assignments: some imposters, rest get the word
        self.player_assignments = (
            ["IMPOSTER"] * imposters + [self.secret_word] * (total_players - imposters)
        )
        random.shuffle(self.player_assignments)

        self._build_player_screen()

    def _build_player_screen(self):
        self._clear_window()

        header_frame = ttk.Frame(self)
        header_frame.pack(pady=10, fill="x")

        title = ttk.Label(
            header_frame, text="Player Reveal Screen", font=("Arial", 16, "bold")
        )
        title.pack(pady=5)

        subtitle = ttk.Label(
            header_frame,
            text="Pass the screen around. Each player taps their box to see their role.",
        )
        subtitle.pack()

        players_frame = ttk.Frame(self)
        players_frame.pack(expand=True, fill="both", padx=20, pady=20)

        total_players = len(self.player_assignments)
        max_per_row = 4  # Arrange buttons nicely in a grid

        for i in range(total_players):
            row = i // max_per_row
            col = i % max_per_row
            btn = ttk.Button(
                players_frame,
                text=f"Player {i+1}",
                command=lambda idx=i: self.show_player_role(idx),
                width=15,
            )
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        for c in range(min(max_per_row, total_players)):
            players_frame.grid_columnconfigure(c, weight=1)

        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(pady=10)

        reset_btn = ttk.Button(
            bottom_frame, text="Reset", command=self._build_setup_screen
        )
        reset_btn.grid(row=0, column=0, padx=10)

        run_back_btn = ttk.Button(
            bottom_frame, text="Run it back", command=self.run_it_back
        )
        run_back_btn.grid(row=0, column=1, padx=10)

        show_word_btn = ttk.Button(
            bottom_frame, text="Show Secret Word", command=self.show_secret_word
        )
        show_word_btn.grid(row=0, column=2, padx=10)

    def run_it_back(self):
        # Make sure we have previous game settings
        if self.last_players is None or self.last_imposters is None:
            messagebox.showinfo("Run it back", "No previous game to repeat.")
            return

        total_players = self.last_players
        imposters = self.last_imposters

        # Decide category (same mode as last time)
        if self.last_random:
            category = random.choice(list(self.categories.keys()))
            messagebox.showinfo("Category chosen", f"Random category: {category}")
        else:
            category = self.last_category

        words = self.categories.get(category, [])
        if not words:
            messagebox.showerror("Error", "No words found for this category.")
            return

        # New random word, same player/imposter counts
        self.secret_word = random.choice(words)
        self.player_assignments = (
            ["IMPOSTER"] * imposters + [self.secret_word] * (total_players - imposters)
        )
        random.shuffle(self.player_assignments)

        # Rebuild the player screen with new assignments
        self._build_player_screen()

    def show_player_role(self, idx: int):
        role = self.player_assignments[idx]

        popup = tk.Toplevel(self)
        popup.title(f"Player {idx+1}")
        popup.geometry("400x200")
        popup.resizable(False, False)

        msg = (
            "You are the IMPOSTER!"
            if role == "IMPOSTER"
            else f"Your word is:\n\n{role.upper()}"
        )
        label = ttk.Label(
            popup, text=msg, font=("Arial", 16, "bold"), justify="center"
        )
        label.pack(expand=True, pady=30, padx=20)

        close_btn = ttk.Button(popup, text="Got it", command=popup.destroy)
        close_btn.pack(pady=10)

        popup.transient(self)
        popup.grab_set()
        self.wait_window(popup)

    def show_secret_word(self):
        if not self.secret_word:
            messagebox.showinfo("Secret word", "No game in progress.")
            return

        messagebox.showinfo("Secret word", f"The current word is: {self.secret_word.upper()}")


if __name__ == "__main__":
    app = ImposterGame()
    app.mainloop()
