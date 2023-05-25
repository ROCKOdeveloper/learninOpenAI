import openai
import typer
from rich import print

def main():

    # api key
    openai.api_key = "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"

    print("\n[bold green]ChatGPT API en Python[/bold green]")

    # Creas un acondicionamiento para provocar una respuesta más asertiva 
    messages = [{"role": "system","content": "Eres un asistente muy útil de programación nivel senior"}]

    while True :
        # Creas un imput para interactuar desde terminal
        content = input("\n > Realiza una pregunta: ")

        # Creamos condicional para salir del programa con la palabra clave exit
        if content == "exit":
            break

        # Le podemos agregar mensajes tras otro
        messages.append({"role": "user", "content": content})

        # Generamos una respuesta con el modelo seleccionado
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        # Respondemos a la pregunta 
        response_content = response.choices[0].message.content

        # Le guardamos las respuestas en asistente
        messages.append({"role": "assistant", "content": response_content})

        # print(response)
        print(f"\n[bold green]>>> [/bold green][green]{response_content}[/green]")

if __name__ == "__main__":
    typer.run(main)
