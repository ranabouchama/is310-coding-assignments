import cloudscraper
import csv
import re
from bs4 import BeauitfulSoup
from rich.console import Console
from rich.table import Table

response = scraper.get("https://sailormoon.fandom.com/wiki/Category:Characters_(Crystal)", timeout=10)

soup = BeautifulSoup(response.text, "html.parser")
new_characters = soup.find_all('a', class_='category-page__member-link')

new_characters_data = []

for character in new_characters:
    character_data = {"character": character.get_text(), "character_link": character.get('href')}
    character_data['alignment'] = get_character_alignments("https://sailormoon.fandom.com" + character_data['character_link']
    character_data['relations'] = get_character_relations("https://sailormoon.fandom.com" + character_data['character_link')
    character_data['character_alignment'] = len(character_data['alignment']
    character_data['character_relations' = len(character_data['relations')
    new_characters_data.append(character_data)

with open('bssm_new_characters.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['character', 'character_link', 'character_alignment', 'character_relations'])
    for character in new_characters_data:
        writer.writerow([character['character'], character['character_link'], character['character_alignment', character['character_relations'])

from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="")
table.add_column("Character", style="pink")
table.add_column("Character Alignment", style="white")
table.add_column("Character Relations", style="yellow")

for character in characters_data:
    table.add_row(character['character'], str(character['character_alignment', character['character_relations']))

console.print(table)
