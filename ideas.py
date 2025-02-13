ideas = []

def add_idea(title, description):
    ideas.append({"title": title, "description": description})

def view_ideas():
    for idea in ideas:
        print(f"{idea['title']}: {idea['description']}")

if __name__ == "__main__":
    add_idea("Smart Mirror", "A mirror that displays weather and notifications.")
    add_idea("AI Fitness Coach", "An AI-powered virtual trainer for personalized workouts.")
    view_ideas()
