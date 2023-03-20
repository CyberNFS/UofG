import tkinter as tk
import openai
import re
import random

# Set OpenAI API key – find the key in dashboard/ view API keys
openai.api_key = "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"


class App:
    def __init__(self, master):
        self.master = master
        master.title("Poem Generator")
        # master.geometry("300x200")

        # Create input fields
        tk.Label(master, text="Noun:").grid(row=0)
        self.noun_entry = tk.Entry(master)
        self.noun_entry.grid(row=0, column=1)

        tk.Label(master, text="Verb:").grid(row=1)
        self.verb_entry = tk.Entry(master)
        self.verb_entry.grid(row=1, column=1)

        tk.Label(master, text="Adjective:").grid(row=2)
        self.adj_entry = tk.Entry(master)
        self.adj_entry.grid(row=2, column=1)

        tk.Label(master, text="Preposition:").grid(row=3)
        self.prep_entry = tk.Entry(master)
        self.prep_entry.grid(row=3, column=1)

        tk.Label(master, text="Adverb:").grid(row=4)
        self.adv_entry = tk.Entry(master)
        self.adv_entry.grid(row=4, column=1)

        # Create generate button
        self.generate_button = tk.Button(
            master, text="Generate", command=self.generate_poem)
        self.generate_button.grid(row=5, column=1)

        # Create poem output
        self.poem_output = tk.Label(master, text="", font=("Arial", 12))
        self.poem_output.grid(row=6, columnspan=2)

    def generate_poem(self):
        # Get input values
        noun = self.noun_entry.get()
        verb = self.verb_entry.get()
        adj = self.adj_entry.get()
        prep = self.prep_entry.get()
        adv = self.adv_entry.get()

        # # Check for duplicates
        # words = [noun, verb, adj, prep, adv]
        # if len(words) != len(set(words)):
        #     self.poem_output.config(
        #         text="Please enter unique words for all input fields.")

        # Check for empty input fields
        if not noun or not verb or not adj or not prep or not adv:
            self.poem_output.config(text="Please provide all input values.")

        # Check for empty input fields
        if not noun or len(noun.split()) < 3:
            self.poem_output.config(
                text="Please provide a noun with at least two words.")

        # Check for empty or too short input fields
        if not verb or len(verb.split()) < 3:
            self.poem_output.config(
                text="Please provide a verb with at least two words.")

        if not adj or len(adj.split()) < 3:
            self.poem_output.config(
                text="Please provide an adjective with at least two words.")
            return
        if not prep or len(prep.split()) < 3:
            self.poem_output.config(
                text="Please provide a preposition with at least two words.")

        if not adv or len(adv.split()) < 1:
            self.poem_output.config(
                text="Please provide an adverb with at least two words.")

        # # Randomly select three words from each category
        # noun = random.sample(noun, 3)
        # verb = random.sample(verb, 3)
        # adj = random.sample(adj, 3)
        # prep = random.sample(prep, 3)
        # adv = random.choice(adv)

        # Use Davinci to generate poem
        prompt = f"Write a poem about {noun} {verb}ing {adj} {prep} {adv}. \
        Keep all the nouns, verbs, adjectives, prepositions and adverbs in their original form. \
        Make the poem fun and likeable."
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract poem text from response
        poem_text = response.choices[0].text.strip()
        poem_text = re.sub(r"\s+", " ", poem_text)

        # Update poem output
        self.poem_output.config(text=poem_text, wraplength=500)


root = tk.Tk()
app = App(root)
root.mainloop()
