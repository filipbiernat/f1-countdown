from datetime import datetime
from publish_entry import publish_post

TEXT_BEFORE = "🏁 Wykopowe odliczanie do powrutu Rajdów Formuły Pierwszej:\n"

TEXT_AFTER = "\nf1 #odliczanief1"

def f1_countdown():
    today = datetime.now().date()
    
    events = {
        "Do testów w Barcelonie pozostało": datetime(2026, 1, 26).date(),
        "Do testów w Bahrajnie pozostało": datetime(2026, 2, 11).date(),
        "Do Grand Prix Australii pozostało": datetime(2026, 3, 8).date(),
    }
    
    upcoming = {name: date for name, date in events.items() if date >= today}
    
    if not upcoming:
        return ""
    
    post_lines = [TEXT_BEFORE]
    
    for event_name, event_date in sorted(upcoming.items(), key=lambda x: x[1]):
        days_left = (event_date - today).days
        post_lines.append(f"⏱️ {event_name}: {days_left} dni")
    
    post_lines.append(TEXT_AFTER)
    
    post = "\n".join(post_lines)
    
    return post

def main():
    content = f1_countdown()
    
    if content:
        print(content)
        publish_post(content)
    else:
        print("Brak nadchodzących eventów F1")

if __name__ == "__main__":
    main()
