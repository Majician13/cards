import random
import tkinter as tk
from PIL import ImageTk, Image

# Define the deck of cards
deck = [
    'as', 'ad', 'ac', 'ah', '2s', '2d', '2c', '2h', '3s', '3d', '3c', '3h', '4s', '4d', '4c', '4h', '5s', '5d', '5c', '5h', '6s', '6d', '6c', '6h', '7s', '7d', '7c', '7h', '8s', '8d', '8c', '8h', '9s', '9d', '9c', '9h', '10s', '10d', '10c', '10h', 'js', 'jd', 'jc', 'jh', 'qs', 'qd', 'qc', 'qh', 'ks', 'kd', 'kc', 'kh',  # Add more cards as needed
    # ...
]

# Create the main window
window = tk.Tk()

# Define separate piles for drawn and discarded cards
drawn_cards = []
discarded_cards = []

# Shuffle the deck
def shuffle_deck():
    global deck
    
    if len(drawn_cards) > 0:
        deck.extend(drawn_cards)  # Add the previously drawn cards back to the deck
        drawn_cards.clear()  # Clear the drawn cards
    
    # if len(discarded_cards) > 0:
    #     deck.extend(discarded_cards)  # Add the discarded cards back to the deck
    #     discarded_cards.clear()  # Clear the discarded cards
    
    random.shuffle(deck)
    
    card_label.configure(image=None)  # Clear the displayed card image
    card_label.image = None  # Clear the reference to the image
    
    print('Deck Shuffled')
    print(deck)

# Draw a card from the top of the deck
def draw_card():
    global deck
    global drawn_cards
    
    if len(deck) > 0:
        card = deck.pop(0)
        drawn_cards.append(card)
        
        # Display the card image
        image_path = f"images/cards/{card}.png"
        image = Image.open(image_path)
        image = image.resize((100, 150))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(image)
        
        card_label.configure(image=photo)
        card_label.image = photo  # Store a reference to the photo object
        
        print('card drawn: ', card)
        print('Drawn cards:', drawn_cards)
        print('Discarded cards:', discarded_cards)
    else:
        shuffle_deck()

# Discard the currently drawn card
def discard_card():
    global drawn_cards
    global discarded_cards
    
    if len(drawn_cards) > 0:
        card = drawn_cards.pop(-1)  # Remove the last card drawn
        discarded_cards.append(card)
        
        card_label.configure(image=None)  # Clear the displayed card image
        card_label.image = None  # Clear the reference to the image
        
        print('card discarded: ', card)
        print('Drawn cards:', drawn_cards)
        print('Discarded cards:', discarded_cards)
        
        # Display the discarded card image
        discarded_card = Image.open(f"images/cards/{card}.png")
        discarded_card = discarded_card.resize((100, 150))  # Adjust the size as needed
        discarded_card_photo = ImageTk.PhotoImage(discarded_card)
        discarded_card_label.configure(image=discarded_card_photo)
        discarded_card_label.image = discarded_card_photo
        
        # Show the previously drawn card in the drawn pile again
        if len(drawn_cards) > 0:
            previous_card = drawn_cards[-1]
            previous_card_image_path = f"images/cards/{previous_card}.png"
            previous_card_image = Image.open(previous_card_image_path)
            previous_card_image = previous_card_image.resize((100, 150))  # Adjust the size as needed
            previous_card_photo = ImageTk.PhotoImage(previous_card_image)
            
            card_label.configure(image=previous_card_photo)
            card_label.image = previous_card_photo
        
    else:
        print('No card to discard.')

# Return all discarded cards to the deck and clear the discard pile/list
def return_cards():
    global deck
    global discarded_cards
    
    if len(discarded_cards) > 0:
        deck.extend(discarded_cards)  # Add the discarded cards back to the deck
        discarded_cards.clear()  # Clear the discarded cards
        deck.extend(drawn_cards)  # Add the drawn cards back to the deck
        drawn_cards.clear()  # Clear the drawn cards
    
    discarded_card_label.configure(image=None)  # Clear the displayed discarded card image
    discarded_card_label.image = None  # Clear the reference to the image

# # Create label for Window
window_label = tk.Label(window, text="CARD DEALER")
window_label.pack()

# Create a button to shuffle the deck
shuffle_button = tk.Button(window, text="Shuffle", command=shuffle_deck)
shuffle_button.pack()

# Create a button to draw a card
draw_button = tk.Button(window, text="Draw", command=draw_card)
draw_button.pack()

# Create a button to discard the currently drawn card
discard_button = tk.Button(window, text="Discard", command=discard_card)
discard_button.pack()

# Create a label to display the card image
card_label = tk.Label(window)
card_label.pack()

# Create a label to display the discarded card image
discarded_card_label = tk.Label(window)
discarded_card_label.pack()

# Create Reset Button to reset the deck
reset_button = tk.Button(window, text="Reset", command=return_cards)
reset_button.pack()

window.mainloop()