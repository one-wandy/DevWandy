
import requests

WHATSAPP_TOKEN = "EAAY44mxgUocBOz3V1jgjJsSq8AX5CtOycbKzpy1fHwSKOIROUhPOR7ovq99t3M8TIyfrwCkUKJfZCfxfUc3r0rfRTFRss7gHma28wG1QWReJ17QK9iCtFLkvqh3YMEjkPUtOzWG0PQ2VCuVdOOWGkbVGDJDoz8bGRanJcNWWCDzxyFcxn9hwa2z3w4EtZAmPSigXB0ZC65APuA7xIZCcBVpOeIcZD"
WHATSAPP_URL = " https://graph.facebook.com/v21.0/456405560897284/messages"

def enviar_respuesta(mensaje, numero):
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": mensaje},
    }
    response = requests.post(WHATSAPP_URL, headers=headers, json=payload)
    print('Enviando mensaje', response.json())
    return response.json()






def procesar_mensaje(mensaje):
      if "hola" in mensaje.lower():
            return "¡Hola! ¿En qué puedo ayudarte?"
      elif "precio" in mensaje.lower():
            return "Nuestros precios están en https://mi-sitio.com."
      else:
            return "Lo siento, no entiendo tu pregunta."