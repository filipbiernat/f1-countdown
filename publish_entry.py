from wykop_sdk_reloaded.v3.client import AuthClient, WykopApiClient
import os

# Pobierz dane z zmiennych środowiskowych
APP_KEY = os.getenv("WYKOP_APP_KEY")
APP_SECRET = os.getenv("WYKOP_APP_SECRET")
USER_REFRESH_TOKEN = os.getenv("WYKOP_USER_TOKEN")

def publish_post(content: str) -> None:
    """
    Publikuje post na mikroblogu Wykop.
    
    Args:
        content (str): Treść posta (może zawierać wiele linii)
    """
    try:
        auth = AuthClient()
        auth.authenticate_user(USER_REFRESH_TOKEN)
        api = WykopApiClient(auth)
        
        response = api.entries_create_entry(content)
        
        if response:
            print(f"✓ Post opublikowany pomyślnie!")
            print(f"Pełna odpowiedź: {response}")
        else:
            print("✗ Błąd: Pusty response")
            
    except Exception as e:
        print(f"✗ Błąd podczas publikacji: {e}")

def main():
    """Główna funkcja - przykład użycia"""
    
    content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. #testfevo"""
    
    publish_post(content)

if __name__ == "__main__":
    main()
