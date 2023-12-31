import os
import urllib.request
import json
import colorama

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def conseguir_respuesta(id):
    url = f"https://play.kahoot.it/rest/kahoots/{id}"
    lista_colores = [colorama.Fore.RED, colorama.Fore.BLUE, colorama.Fore.YELLOW, colorama.Fore.GREEN]

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
                            answer = choice['answer']
                            color = lista_colores[i]
                            colores_correctos.append((color, answer))
                            print(color)
                            print(f"{index + 1}: {answer}")
                            print()

                if colores_correctos:
                    print("Se encontraron respuestas correctas.")
                else:
                    print("No se encontraron respuestas correctas.")

            else:
                print("La estructura de la respuesta JSON no es la esperada.")

    except urllib.error.HTTPError:
        print("El Kahoot no existe. Lo estás poniendo mal o está privado.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clear_screen()
    colorama.init()

    def display_banner():
        banner = """
         ____   ________     __ __ ___    __  ______  ____ ______
        / __ \ /  _/ __ \   / //_//   |  / / / / __ \/ __ |_  __/
        / /_/ / / // /_/ /  / ,<  / /| | / /_/ / / / / / / // /
        / _, _/_/ // ____/  / /| |/ ___ |/ __  / /_/ / /_/ // /
        /_/ |_|/___/_/      /_/ |_/_/  |_/_/ /_/\____/\____//_/

                         :^~!~~^^^::.
                       ^~^:.....:^^.^^
                      .!          :^ ~:
                      .!          .~ :^
                      .~   Rip    .! .~
                       !           ! .!
                       !  KAHOOT   ! .~
                       !           ! .!
                       !.    BY    !  ~.
                       ~.   NEXUS  !. ~:
                   ::::^^:::::.... !. !:
                . ^~.      ....:::!^:^~
             :^^:.               :7 :~
            ~:                  :~^^:
         .^^:                .:~^^:
       .^^.               .^^^^~:
       .: . .            .^.:^:
         :::^^::::.:...   .^:
                   ....::^^

        https://kahoot.it/v2/?quizId="EL ID QUE HAY QUE PONER"

                EL KAHOOT DEBE SER PÚBLICO
        """
        print(colorama.Fore.RED + banner)
        print(colorama.Fore.WHITE)

    display_banner()

    while True:
        uuid = input(colorama.Fore.WHITE + "Pon la id del kahoot ('exit' para salir):")
        if uuid.lower() == 'exit':
            break
        conseguir_respuesta(uuid)
