import csv
import os
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()

# Example data
example_fav_dishes = [
    {
        "dish_name": "Bánh Cuốn",
        "origin_country": "Vietnam",
        "contributor_nickname": "The Introverted Foodie",
        "contributor_comment": "As a Vietnamese, this is our most underrated and should deserve more recognition than Pho or Banh Mi",
    },
    {
        "dish_name": "Baklava",
        "origin_country": "Turkey",
        "contributor_nickname": "The Introverted Foodie",
        "contributor_comment": "My favorite international pastry dishes!",
    },
    {
        "dish_name": "Pizza Capricciosa",
        "origin_country": "Italy",
        "contributor_nickname": "The Introverted Foodie",
        "contributor_comment": "I used to don't like pizza but this has completely changed that!",
    },
]

# Display example data
def show_example_data():
    console.print("\n[bold cyan]📋 Example Dishes Already in Dataset:[/bold cyan]\n")

    table = Table(title="Tasty Dishes Around The World!🍽️🌎", show_lines=True)
    table.add_column("Dish", style="magenta", no_wrap=True)
    table.add_column("Origin", style="cyan")
    table.add_column("Contributor", style="green")
    table.add_column("Contributor's Comment", style="green")

    for dish in example_fav_dishes:
        table.add_row(
            dish["dish_name"],
            dish["origin_country"],
            dish["contributor_nickname"],
            dish["contributor_comment"]
        )

    console.print(table)

# Collect 
def get_dish_entry():
    console.print("\n[bold yellow]Enter details for a your favorite dish:[/bold yellow]\n")

    fields = {
        "dish_name": "Your dish name (ex, 'Birria Tacos')",
        "origin_country": "Which country is it from? (e.g., 'Mexico')",
        "contributor_nickname": "Your chosen made-up name! Please be appripriate though",
        "contributor_comment": "Your very brief comment about the dish",
    }

    entry = {}
    for key, prompt in fields.items():
        entry[key] = console.input(f"[bold]{prompt}:[/bold] ").strip()

    return entry

# Display
# Display a single entry as a confirmation table
def display_entry(entry):
    table = Table(title=f"Your Entry: {entry['dish_name']}", show_lines=True)
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="white")

    for key, value in entry.items():
        table.add_row(key.replace("_", " ").title(), value)

    console.print(table)

# Save all entries to CSV
def save_to_csv(entries):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"favorite_dishes_{timestamp}.csv"
    filepath = os.path.abspath(filename)

    fieldnames = ["dish_name", "origin_country", "contributor_nickname", "contributor_comment"]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)

    console.print(f"\n[bold green]✅ Data saved successfully![/bold green]")
    console.print(f"[bold]File location:[/bold] [underline]{filepath}[/underline]\n")

# Main program loop
def main():
    console.print("[bold magenta]\n🌍 Tasty Dishes Around The World — Data Entry Tool[/bold magenta]")
    show_example_data()

    collected_entries = []

    while True:
        console.print("\n[bold cyan]Would you like to add a dish?[/bold cyan]")
        start = console.input("[bold]Type 'yes' to add a dish, or 'done' to finish and save: [/bold]").strip().lower()

        if start == "done":
            break
        elif start != "yes":
            console.print("[red]Please type 'yes' or 'done'.[/red]")
            continue

        # Inner loop: keep re-asking until user confirms the entry is correct
        while True:
            entry = get_dish_entry()

            console.print("\n[bold yellow]Here is what you entered:[/bold yellow]")
            display_entry(entry)

            confirm = console.input("\n[bold]Is this correct? (yes/no): [/bold]").strip().lower()

            if confirm == "yes":
                collected_entries.append(entry)
                console.print(f"[green]✔ Entry confirmed! You've added {len(collected_entries)} dish(es) so far.[/green]")
                break
            else:
                console.print("[red]No problem! Let's re-enter the data.[/red]")
                # loops back to get_dish_entry()

    # Save or exit
    if collected_entries:
        save_to_csv(collected_entries)
    else:
        console.print("\n[yellow]No entries were added. Nothing saved.[/yellow]")

if __name__ == "__main__":
    main()