# Seminario IA
Seminario de Inteligencia Artificial

# 🧠 Entrenamiento Emocional Asistido con Visión Artificial

Este proyecto tiene como objetivo apoyar a personas con **síndrome de Down o en el espectro autista** a **reconocer e imitar emociones faciales**, utilizando una herramienta de visión artificial en tiempo real. Se basa en una actividad terapéutica tradicional (usar cartas con expresiones) y la moderniza con inteligencia artificial y cámaras web.

---

## 🎯 Objetivo

- Mostrar una emoción como carta visual (imagen).
- Detectar en tiempo real la emoción facial del usuario.
- Comparar ambas y brindar retroalimentación inmediata.
- Permitir que el usuario practique tantas veces como desee.

---

## 🖥️ Tecnologías Utilizadas

- Python
- Flask (backend web)
- OpenCV (captura de video)
- DeepFace (reconocimiento emocional con CNN)
- HTML, CSS (interfaz visual)
- Estructura tipo MVC con carpetas `static/`, `templates/`

---

## 🚀 ¿Cómo funciona?

1. El usuario accede a la aplicación desde el navegador.
2. Selecciona una emoción a practicar (ej. "happy").
3. Se muestra su rostro en tiempo real junto a una imagen de referencia.
4. El sistema analiza su expresión facial con **DeepFace**.
5. Si la emoción detectada coincide con la elegida → mensaje positivo.
6. Si no coincide → se indica cuál emoción fue detectada.



