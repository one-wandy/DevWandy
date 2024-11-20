
import requests

WHATSAPP_TOKEN = "EAAY44mxgUocBO4L3NMzKbpxCtHGSLUus5QgTfwz8Vtp2baugFZAW6zDWZAz8NM7ZCyAItCgMQuIXME16zUife5b6PFWfZAI2ShOGQhIENDNFZBI8OLkxnj55lWIQ5mFzCc0hkOQKft2wH5L2CyCvjXdRxIHIY2ZCG3prrK5ewmo3Ozh887op3R4DbcZCYRaeMR7fVjZCdXKTN08cXpPLIMkYHL1B8EUZD"
WHATSAPP_URL = "https://graph.facebook.com/v21.0/456405560897284/messages"

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