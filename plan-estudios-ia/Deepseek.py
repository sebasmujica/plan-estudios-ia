from openai import OpenAI
client = OpenAI(api_key="sk-9568b9d96bcd4c9a8818a7752038f8b8",base_url="https://api.deepseek.com")
historial = [{"role":"system","content":""}]
def Open_IA(user_promt):
  historial.append({"role":"user","content":user_promt}) #Agregamos el formato del mensaje con el prompt del user al historial 
  chat= client.chat.completions.create(
      model= "deepseek-chat",
      messages=historial,
      stream= False,
      temperature= 0.7
  )   
  ia_response = chat.choices[0].message.content #guardamos la respuesta 
  # historial.append({"role":"assistant","content": ia_response}) #agregamos la respuesta al historial para que la IA recuerde la conversacion
  return ia_response

def Open_IA_nivel(respuetas):
  historial.append({"role":"user","content":f"evaluaras las respuestas dadas {respuetas} por el usuario y luego devuelve un nivel entre principiante,intermedio o experto."}) #Agregamos el formato del mensaje con el prompt del user al historial 
  chat= client.chat.completions.create(
      model= "deepseek-chat",
      messages=historial,
      stream= False,
      temperature= 0.7
  )   
  ia_response_level = chat.choices[0].message.content #guardamos la respuesta 
  # historial.append({"role":"assistant","content": ia_response}) #agregamos la respuesta al historial para que la IA recuerde la conversacion
  return ia_response_level

def Open_IA_eval(respuetas):
  historial.append({"role":"user","content":f"eres un experto en python y evaluas las siguientes respuestas del usuario: {respuetas}. Devuelve una opinion de temas de estudio para mejorar dicho nivel, evita enumerar las opciones y usar caracteres inecesarios y emojis y de introducir texto extra de lo que se pide,tampoco vuelvas a devolver las preguntas o respuestas enviadas "}) #Agregamos el formato del mensaje con el prompt del user al historial 
  chat= client.chat.completions.create(
      model= "deepseek-chat",
      messages=historial,
      stream= False,
      temperature= 1
  )   
  ia_response_plan = chat.choices[0].message.content #guardamos la respuesta 
  # historial.append({"role":"assistant","content": ia_response}) #agregamos la respuesta al historial para que la IA recuerde la conversacion
  return ia_response_plan