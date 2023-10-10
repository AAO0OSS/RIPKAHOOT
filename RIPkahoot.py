import urllib.request
import json
import colorama
import pyautogui
import pyautogui
pyautogui.FAILSAFE = False
import keyboard

def get_coordinates(color):
    # Define coordinates for different answer colors
    if color == colorama.Fore.RED:  # Red
        return 300, 300
    elif color == colorama.Fore.BLUE:  # Blue
        return 1500, 300
    elif color == colorama.Fore.YELLOW:  # Yellow
        return 300, 900
    elif color == colorama.Fore.GREEN:  # Green
        return 1500, 900
    else:
        return 0, 0  # Default coordinates when color is not found

def conseguir_respuesta(id):
    url = f"https://play.kahoot.it/rest/kahoots/{id}"
    lista_colores = {
        "rojo": colorama.Fore.RED,
        "azul": colorama.Fore.BLUE,
        "amarillo": colorama.Fore.YELLOW,
        "verde": colorama.Fore.GREEN
    }
    default_color = colorama.Fore.WHITE  # Default color if answer color is not found
    colores_correctos = []

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            response_json = json.loads(data)

            if "questions" in response_json and "quizType" in response_json:
                preguntas = response_json["questions"]

                for index, slide in enumerate(preguntas):
                    for i, choice in enumerate(slide.get("choices", [])):
                        if choice.get("correct", False):
                            answer = choice.get('answer')
                            color = lista_colores.get(answer, default_color)
                            colores_correctos.append((color, answer))
                            print(f"{color}")
                            print(f"{index+1}: {answer}")
                            print()

                if colores_correctos:
                    print("Presiona la tecla shift para auto responder cuando esté preparado")

                    keyboard.wait('shift')

                    for lugar_color, _ in colores_correctos:
                        x, y = get_coordinates(lugar_color)
                        pyautogui.moveTo(x, y, duration=1)  # Move to absolute coordinates (x, y) over a 1-second duration
                        pyautogui.click(x, y)

                else:
                    print("No se encontraron respuestas correctas.")

            else:
                print("La estructura de la respuesta JSON no es la esperada.")

    except urllib.error.HTTPError:
        print("El Kahoot no existe. Lo estás poniendo mal o está privado.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    colorama.init()

    while True:
        uuid = input(colorama.Fore.WHITE + "Enter uuid (or 'exit' to quit):")
        if uuid.lower() == 'exit':
            break
        conseguir_respuesta(uuid)
