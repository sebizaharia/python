import tkinter as tk
import random

# CONFIGURATII DE DESIGN
COLOR_BG = "#2b2d42"  # Fundal principal (Navy inchis)
COLOR_FRAME = "#8d99ae"  # Fundal zona intrebarii (Gri-Albastrui)
COLOR_BTN_DEFAULT = "#edf2f4"  # Butoane (Alb-Ghiocel)
COLOR_BTN_TEXT = "#2b2d42"  # Text butoane
COLOR_TEXT_MAIN = "#ffffff"  # Text alb
COLOR_CORRECT = "#2ecc71"  # Verde (Corect)
COLOR_WRONG = "#e74c3c"  # Rosu (Gresit)
FONT_Q = ("Verdana", 13, "bold")
FONT_BTN = ("Verdana", 10)


class ModernQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia Challenge")
        self.root.geometry("750x600")
        self.root.configure(bg=COLOR_BG)
        self.root.resizable(False, False)

        # DATABASE: INTREBARI
        self.all_questions = [
            # GEOGRAFIE
            {"q": "Care este capitala Braziliei?", "opt": ["Rio de Janeiro", "Brasilia", "Sao Paulo", "Buenos Aires"],
             "ans": "Brasilia"},
            {"q": "Care este cel mai lung fluviu din Europa?", "opt": ["Dunarea", "Volga", "Rin", "Sena"],
             "ans": "Volga"},
            {"q": "In ce continent se afla Desertul Sahara?", "opt": ["Asia", "Africa", "Australia", "America de Sud"],
             "ans": "Africa"},
            {"q": "Care este capitala Canadei?", "opt": ["Toronto", "Vancouver", "Ottawa", "Montreal"],
             "ans": "Ottawa"},
            {"q": "Ce tara are forma unei cizme?", "opt": ["Spania", "Grecia", "Italia", "Portugalia"],
             "ans": "Italia"},
            {"q": "Muntele Everest se afla la granita dintre Nepal si...?",
             "opt": ["China (Tibet)", "India", "Pakistan", "Bhutan"], "ans": "China (Tibet)"},
            {"q": "Care este cel mai mare ocean al planetei?", "opt": ["Atlantic", "Pacific", "Indian", "Arctic"],
             "ans": "Pacific"},
            {"q": "Ce stramtoare desparte Europa de Africa?", "opt": ["Bosfor", "Gibraltar", "Bering", "Magellan"],
             "ans": "Gibraltar"},

            # ISTORIE
            {"q": "In ce an a inceput Primul Razboi Mondial?", "opt": ["1914", "1918", "1939", "1945"], "ans": "1914"},
            {"q": "Cine a fost primul presedinte al SUA?",
             "opt": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "JFK"], "ans": "George Washington"},
            {"q": "Cine a fost conducatorul dacilor in timpul razboaielor cu romanii?",
             "opt": ["Burebista", "Decebal", "Traian", "Deceneu"], "ans": "Decebal"},
            {"q": "In ce an a avut loc Marea Unire de la Alba Iulia?", "opt": ["1859", "1918", "1877", "1989"],
             "ans": "1918"},
            {"q": "Cine a descoperit America in 1492?",
             "opt": ["Vasco da Gama", "Cristofor Columb", "Magellan", "Amerigo Vespucci"], "ans": "Cristofor Columb"},
            {"q": "Cum se numea calul lui Alexandru cel Mare?", "opt": ["Bucefal", "Pegas", "Incitatus", "Rocinante"],
             "ans": "Bucefal"},
            {"q": "In ce an a cazut Zidul Berlinului?", "opt": ["1987", "1989", "1991", "1995"], "ans": "1989"},

            # STIINTA & NATURA
            {"q": "Ce simbol chimic are Aurul?", "opt": ["Ag", "Au", "Fe", "Cu"], "ans": "Au"},
            {"q": "Care este cea mai rapida pasare din lume (in picaj)?",
             "opt": ["Vulturul plesuv", "Soimul calator", "Pinguinul", "Strutul"], "ans": "Soimul calator"},
            {"q": "Cate planete are Sistemul Solar?", "opt": ["7", "8", "9", "10"], "ans": "8"},
            {"q": "Ce gaz respiram noi in principal (din ce e compusa atmosfera)?",
             "opt": ["Oxigen", "Azot", "Dioxid de Carbon", "Heliu"], "ans": "Azot"},
            {"q": "Care este cel mai dur material natural?", "opt": ["Fierul", "Diamantul", "Granitul", "Cuartul"],
             "ans": "Diamantul"},
            {"q": "Formula chimica a apei este...", "opt": ["CO2", "H2O", "O2", "NaCl"], "ans": "H2O"},
            {"q": "Ce organ pompeaza sangele in corp?", "opt": ["Ficatul", "Inima", "Creierul", "Plamanii"],
             "ans": "Inima"},
            {"q": "Viteza luminii este aproximativ...",
             "opt": ["300.000 km/s", "100.000 km/s", "1.000 km/h", "340 m/s"], "ans": "300.000 km/s"},

            # IT & TEHNOLOGIE
            {"q": "Cine a fondat Microsoft?", "opt": ["Steve Jobs", "Elon Musk", "Bill Gates", "Mark Zuckerberg"],
             "ans": "Bill Gates"},
            {"q": "Ce inseamna 'CPU' intr-un calculator?",
             "opt": ["Central Processing Unit", "Computer Personal Unit", "Central Power Unit", "Core Program Utility"],
             "ans": "Central Processing Unit"},
            {"q": "Care este cel mai popular sistem de operare pentru PC?",
             "opt": ["Linux", "macOS", "Windows", "Android"], "ans": "Windows"},
            {"q": "Ce limbaj de programare are ca logo un sarpe?", "opt": ["Java", "C++", "Python", "Ruby"],
             "ans": "Python"},
            {"q": "In ce an a fost lansat primul iPhone?", "opt": ["2005", "2007", "2010", "2000"], "ans": "2007"},
            {"q": "Cine detine compania SpaceX?", "opt": ["Jeff Bezos", "Elon Musk", "Tim Cook", "Richard Branson"],
             "ans": "Elon Musk"},
            {"q": "Ce inseamna 'WWW'?", "opt": ["World Wide Web", "World Web Wide", "Web World Wide", "Wild Wild West"],
             "ans": "World Wide Web"},

            # CULTURA GENERALA & DIVERTISMENT
            {"q": "Cine a scris 'Romeo si Julieta'?", "opt": ["Moliere", "William Shakespeare", "Victor Hugo", "Dante"],
             "ans": "William Shakespeare"},
            {"q": "Cate laturi are un hexagon?", "opt": ["5", "6", "8", "10"], "ans": "6"},
            {"q": "In ce an s-a scufundat Titanicul?", "opt": ["1910", "1912", "1915", "1920"], "ans": "1912"},
            {"q": "Care este moneda Japoniei?", "opt": ["Yuan", "Won", "Yen", "Dolar"], "ans": "Yen"},
            {"q": "Ce culoare obtii daca amesteci Rosu cu Galben?", "opt": ["Verde", "Portocaliu", "Mov", "Maron"],
             "ans": "Portocaliu"},
            {"q": "Cate piese are un joc complet de sah (la start)?", "opt": ["32", "30", "36", "28"], "ans": "32"},
            {"q": "Care este cel mai vizitat muzeu din lume (Paris)?",
             "opt": ["British Museum", "Luvru", "Prado", "Ermitaj"], "ans": "Luvru"},
            {"q": "Cine a pictat 'Mona Lisa'?", "opt": ["Picasso", "Van Gogh", "Da Vinci", "Rembrandt"],
             "ans": "Da Vinci"},

            # ROMANIA
            {"q": "Care este cel mai inalt varf din Romania?", "opt": ["Negoiu", "Moldoveanu", "Omu", "Parangu Mare"],
             "ans": "Moldoveanu"},
            {"q": "In ce judet se afla Castelul Peles?", "opt": ["Brasov", "Prahova", "Sibiu", "Mures"],
             "ans": "Prahova"},
            {"q": "Ce sculptor roman a realizat 'Coloana Infinitului'?",
             "opt": ["Constantin Brancusi", "Nicolae Grigorescu", "Stefan Luchian", "Ion Andreescu"],
             "ans": "Constantin Brancusi"},
            {"q": "Ce oras este supranumit 'Micul Paris'?", "opt": ["Iasi", "Cluj-Napoca", "Bucuresti", "Timisoara"],
             "ans": "Bucuresti"},
            {"q": "Delta Dunarii se varsa in...?",
             "opt": ["Marea Rosie", "Marea Neagra", "Marea Mediterana", "Marea Caspica"], "ans": "Marea Neagra"},

            # INTREBARI EXTRA
            {"q": "Care este cel mai mare animal din lume?",
             "opt": ["Elefantul African", "Balena Albastra", "Rechinul Balena", "Girafa"], "ans": "Balena Albastra"},
            {"q": "Cate secunde are o ora?", "opt": ["360", "3600", "6000", "600"], "ans": "3600"},
            {"q": "In ce tara se afla Taj Mahal?", "opt": ["Thailanda", "India", "Iran", "Egipt"], "ans": "India"},
            {"q": "Cine este autorul seriei Harry Potter?",
             "opt": ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Stephen King"], "ans": "J.K. Rowling"},
            {"q": "Ce vitamina luam in principal de la Soare?",
             "opt": ["Vitamina C", "Vitamina D", "Vitamina A", "Vitamina B12"], "ans": "Vitamina D"},
            {"q": "Care este capitala Italiei?", "opt": ["Milano", "Venetia", "Roma", "Napoli"], "ans": "Roma"},
            {"q": "Cate inimi are o caracatita?", "opt": ["1", "2", "3", "9"], "ans": "3"},
            {"q": "Care este cel mai rapid animal terestru?", "opt": ["Leul", "Ghepardul", "Antilopa", "Iepurele"],
             "ans": "Ghepardul"},
            {"q": "Unde au avut loc Jocurile Olimpice antice?", "opt": ["Roma", "Atena", "Olympia", "Sparta"],
             "ans": "Olympia"},
            {"q": "Ce planeta este numita 'Planeta Rosie'?", "opt": ["Venus", "Marte", "Jupiter", "Saturn"],
             "ans": "Marte"},
            {"q": "Cine a scris 'Luceafarul'?",
             "opt": ["Ion Creanga", "Mihai Eminescu", "George Cosbuc", "Lucian Blaga"], "ans": "Mihai Eminescu"},
            {"q": "Care este unitatea de masura pentru curentul electric?", "opt": ["Volt", "Watt", "Amper", "Ohm"],
             "ans": "Amper"},
            {"q": "Cate zile are un an bisect?", "opt": ["364", "365", "366", "367"], "ans": "366"},
            {"q": "Cine a inventat becul (comercial)?",
             "opt": ["Nikola Tesla", "Thomas Edison", "Graham Bell", "Albert Einstein"], "ans": "Thomas Edison"}
        ]

        # 1. Amestecam TOATA lista mare
        random.shuffle(self.all_questions)

        # 2. Selectam doar primele 15 pentru acest joc
        self.questions = self.all_questions[:15]

        self.score = 0
        self.current_q_index = 0
        self.buttons = []

        # --- INTERFATA GRAFICA
        self.create_ui()
        self.load_question()

    def create_ui(self):
        """Construieste elementele vizuale"""

        # Header (Titlu si Scor)
        header_frame = tk.Frame(self.root, bg=COLOR_BG)
        header_frame.pack(pady=20, fill="x", padx=30)

        self.lbl_progress = tk.Label(header_frame, text="Intrebarea 1/15", font=("Arial", 12), bg=COLOR_BG,
                                     fg="#8d99ae")
        self.lbl_progress.pack(side="left")

        self.lbl_score = tk.Label(header_frame, text="Scor: 0", font=("Arial", 14, "bold"), bg=COLOR_BG,
                                  fg=COLOR_CORRECT)
        self.lbl_score.pack(side="right")

        # Zona Intrebarii (Card)
        question_frame = tk.Frame(self.root, bg=COLOR_FRAME, bd=0)
        question_frame.pack(pady=20, padx=40, fill="both", expand=True)

        self.lbl_question = tk.Label(
            question_frame,
            text="...",
            font=FONT_Q,
            bg=COLOR_FRAME,
            fg=COLOR_BG,
            wraplength=650,
            justify="center"
        )
        self.lbl_question.pack(expand=True, fill="both", padx=20, pady=20)

        # Zona Butoanelor (Grid 2x2)
        buttons_frame = tk.Frame(self.root, bg=COLOR_BG)
        buttons_frame.pack(pady=30, padx=40, fill="x")

        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        for i in range(4):
            btn = tk.Button(
                buttons_frame,
                text="",
                font=FONT_BTN,
                bg=COLOR_BTN_DEFAULT,
                fg=COLOR_BTN_TEXT,
                activebackground="#d0d0d0",
                bd=0,
                cursor="hand2",
                height=3,
                command=lambda idx=i: self.check_answer(idx)
            )
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="ew")
            self.buttons.append(btn)

    def load_question(self):
        """Afiseaza intrebarea curenta"""
        if self.current_q_index < len(self.questions):
            data = self.questions[self.current_q_index]

            # Reset butoane
            for btn in self.buttons:
                btn.config(bg=COLOR_BTN_DEFAULT, state="normal")

            # Update UI
            self.lbl_progress.config(text=f"Intrebarea {self.current_q_index + 1} / {len(self.questions)}")
            self.lbl_question.config(text=data['q'])

            # Amestecam optiunile pe butoane
            options = data['opt'].copy()  # Facem o copie ca sa nu stricam originalul
            random.shuffle(options)

            for i, btn in enumerate(self.buttons):
                btn.config(text=options[i])
        else:
            self.end_game()

    def check_answer(self, btn_index):
        """Verifica raspunsul"""
        selected_btn = self.buttons[btn_index]
        selected_text = selected_btn.cget("text")
        correct_text = self.questions[self.current_q_index]['ans']

        # Blocam click-urile
        for btn in self.buttons:
            btn.config(state="disabled")

        if selected_text == correct_text:
            self.score += 1
            selected_btn.config(bg=COLOR_CORRECT)
            self.lbl_score.config(text=f"Scor: {self.score}")
        else:
            selected_btn.config(bg=COLOR_WRONG)
            # Aratam varianta corecta
            for btn in self.buttons:
                if btn.cget("text") == correct_text:
                    btn.config(bg=COLOR_CORRECT)
                    break

        # Pauza mica apoi urmatoarea intrebare
        self.root.after(1500, self.next_question)

    def next_question(self):
        self.current_q_index += 1
        self.load_question()

    def end_game(self):
        """Ecranul de final"""
        percentage = int((self.score / len(self.questions)) * 100)

        # Curatam ecranul
        for widget in self.root.winfo_children():
            widget.destroy()

        final_frame = tk.Frame(self.root, bg=COLOR_BG)
        final_frame.pack(expand=True, fill="both")

        tk.Label(final_frame, text="REZULTAT FINAL", font=("Arial", 26, "bold"), bg=COLOR_BG, fg="white").pack(pady=20)

        color = COLOR_CORRECT if percentage >= 50 else COLOR_WRONG
        tk.Label(final_frame, text=f"{percentage}%", font=("Arial", 60, "bold"), bg=COLOR_BG, fg=color).pack(pady=10)

        msg = f"Ai raspuns corect la {self.score} din {len(self.questions)}"
        tk.Label(final_frame, text=msg, font=("Arial", 14), bg=COLOR_BG, fg="#bdc3c7").pack(pady=10)

        # Buton Replay
        tk.Button(
            final_frame, text="Joaca din nou ↻", font=("Arial", 14, "bold"),
            bg=COLOR_BTN_DEFAULT, fg=COLOR_BTN_TEXT, width=15, height=2, bd=0, cursor="hand2",
            command=self.restart
        ).pack(pady=30)

        # Buton Iesire
        tk.Button(
            final_frame, text="Iesire", font=("Arial", 11),
            bg="#e74c3c", fg="white", width=10, bd=0, cursor="hand2",
            command=self.root.destroy
        ).pack(pady=5)

    def restart(self):
        self.root.destroy()
        main()


def main():
    root = tk.Tk()
    app = ModernQuizApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()