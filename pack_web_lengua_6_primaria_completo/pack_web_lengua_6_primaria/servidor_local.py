#!/usr/bin/env python3
"""
Servidor web local para el Pack de Estudio de Lengua 6º Primaria
Permite acceso desde cualquier dispositivo en la misma red WiFi
"""

import http.server
import socketserver
import socket
import webbrowser
import os
import sys
from pathlib import Path

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Permitir acceso desde cualquier origen (CORS)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def get_local_ip():
    """Obtiene la IP local del ordenador"""
    try:
        # Conectar a un servidor externo para obtener la IP local
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def create_index_page():
    """Crea una página de inicio con enlaces a todos los materiales"""
    index_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pack de Estudio - Lengua 6º Primaria</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
        }
        
        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .categories {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }
        
        .category-card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            border-left: 6px solid;
            transition: transform 0.3s ease;
        }
        
        .category-card:hover {
            transform: translateY(-5px);
        }
        
        .category-title {
            font-size: 1.4rem;
            font-weight: bold;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .file-list {
            list-style: none;
        }
        
        .file-list li {
            margin: 8px 0;
        }
        
        .file-list a {
            display: block;
            padding: 10px 15px;
            background: #f8f9fa;
            border-radius: 8px;
            text-decoration: none;
            color: #2c3e50;
            transition: background 0.2s ease;
        }
        
        .file-list a:hover {
            background: #e9ecef;
            color: #495057;
        }
        
        .infografias { border-left-color: #3498db; }
        .infografias .category-title { color: #3498db; }
        
        .quiz { border-left-color: #e74c3c; }
        .quiz .category-title { color: #e74c3c; }
        
        .examenes { border-left-color: #f39c12; }
        .examenes .category-title { color: #f39c12; }
        
        .respuestas { border-left-color: #27ae60; }
        .respuestas .category-title { color: #27ae60; }
        
        .mapas { border-left-color: #9b59b6; }
        .mapas .category-title { color: #9b59b6; }
        
        .instructions {
            background: #e8f4fd;
            border-left: 5px solid #3498db;
            padding: 20px;
            border-radius: 10px;
            margin-top: 30px;
        }
        
        .instructions h3 {
            color: #2980b9;
            margin-bottom: 15px;
        }
        
        .instructions ul {
            margin-left: 20px;
        }
        
        .instructions li {
            margin: 8px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 Pack de Estudio Completo</h1>
            <p>Lengua Española 6º Primaria - Acceso Web</p>
        </div>
        
        <div class="categories">
            <div class="category-card infografias">
                <div class="category-title">
                    <i class="📊"></i> Infografías
                </div>
                <ul class="file-list">
                    <li><a href="infografias/infografia_lengua_6_interactiva.html">📱 Infografía Interactiva</a></li>
                    <li><a href="infografias/infografia_lengua_6_imprimible.html">🖨️ Infografía Imprimible</a></li>
                </ul>
            </div>
            
            <div class="category-card quiz">
                <div class="category-title">
                    <i class="🧠"></i> Quiz de Práctica
                </div>
                <ul class="file-list">
                    <li><a href="quiz/quiz_conceptos.html">📖 Quiz Conceptos (50 preguntas)</a></li>
                    <li><a href="quiz/quiz_practica.html">✏️ Quiz Práctico (50 ejercicios)</a></li>
                </ul>
            </div>
            
            <div class="category-card examenes">
                <div class="category-title">
                    <i class="📝"></i> Modelos de Examen
                </div>
                <ul class="file-list">
                    <li><a href="examenes/examen_modelo_1_basico.html">📚 Modelo 1 - Básico</a></li>
                    <li><a href="examenes/examen_modelo_2_intermedio.html">📖 Modelo 2 - Intermedio</a></li>
                    <li><a href="examenes/examen_modelo_3_avanzado.html">📘 Modelo 3 - Avanzado</a></li>
                    <li><a href="examenes/examen_modelo_4_completo.html">📙 Modelo 4 - Completo</a></li>
                    <li><a href="examenes/examen_modelo_5_practico.html">📗 Modelo 5 - Práctico</a></li>
                    <li><a href="examenes/examen_modelo_6_avanzado.html">📕 Modelo 6 - Avanzado Plus</a></li>
                    <li><a href="examenes/examen_modelo_7_experto.html">📓 Modelo 7 - Experto</a></li>
                </ul>
            </div>
            
            <div class="category-card respuestas">
                <div class="category-title">
                    <i class="✅"></i> Respuestas
                </div>
                <ul class="file-list">
                    <li><a href="respuestas/respuestas_examenes_modelos.html">📋 Soluciones Completas</a></li>
                </ul>
            </div>
            
            <div class="category-card mapas">
                <div class="category-title">
                    <i class="🗺️"></i> Mapas Mentales
                </div>
                <ul class="file-list">
                    <li><a href="mapas_mentales/mapa_mental_repaso_examen.html">🧠 Mapa Mental Interactivo</a></li>
                    <li><a href="mapas_mentales/mapa_mental_imprimible.html">🖨️ Mapa Mental Imprimible</a></li>
                </ul>
            </div>
        </div>
        
        <div class="instructions">
            <h3>📱 Cómo Acceder desde Otros Dispositivos</h3>
            <ul>
                <li><strong>Mismo WiFi:</strong> Usa la IP que aparece en la consola del servidor</li>
                <li><strong>Móvil/Tablet:</strong> Abre el navegador y escribe la dirección IP</li>
                <li><strong>Otro ordenador:</strong> Funciona igual que en móvil</li>
                <li><strong>Offline:</strong> Descarga los archivos HTML para usar sin internet</li>
            </ul>
            
            <h3>🎯 Recomendación de Uso</h3>
            <ul>
                <li><strong>Estudiar:</strong> Comienza con las infografías</li>
                <li><strong>Practicar:</strong> Realiza los quiz regularmente</li>
                <li><strong>Evaluar:</strong> Usa los modelos de examen</li>
                <li><strong>Repasar:</strong> Consulta los mapas mentales</li>
            </ul>
        </div>
    </div>
</body>
</html>"""
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_content)

def main():
    # Configuración del servidor
    PORT = 8000
    
    # Cambiar al directorio del pack descomprimido
    pack_dir = "pack_final_lengua_6_primaria_completo"
    if os.path.exists(pack_dir):
        os.chdir(pack_dir)
        print(f"📁 Cambiando al directorio: {pack_dir}")
    else:
        print("⚠️ Directorio del pack no encontrado. Asegúrate de descomprimir el ZIP primero.")
        return
    
    # Crear página de inicio si no existe
    if not os.path.exists("index.html"):
        create_index_page()
        print("📄 Página de inicio creada")
    
    # Obtener IP local
    local_ip = get_local_ip()
    
    # Configurar y iniciar servidor
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print("\n" + "="*60)
        print("🚀 SERVIDOR DE ESTUDIO INICIADO")
        print("="*60)
        print(f"📱 Acceso LOCAL: http://localhost:{PORT}")
        print(f"🌐 Acceso REMOTO: http://{local_ip}:{PORT}")
        print("="*60)
        print("\n📋 INSTRUCCIONES:")
        print("• Para acceder desde ESTE ordenador: http://localhost:8000")
        print(f"• Para acceder desde MÓVIL/TABLET: http://{local_ip}:8000")
        print(f"• Para acceder desde OTRO ORDENADOR: http://{local_ip}:8000")
        print("\n⚠️ IMPORTANTE:")
        print("• Todos los dispositivos deben estar en la MISMA red WiFi")
        print("• Mantén esta ventana abierta mientras uses el servidor")
        print("• Presiona Ctrl+C para detener el servidor")
        print("\n🎯 El servidor se abrirá automáticamente en tu navegador...")
        print("="*60)
        
        # Abrir navegador automáticamente
        webbrowser.open(f'http://localhost:{PORT}')
        
        try:
            print(f"\n✅ Servidor ejecutándose en puerto {PORT}")
            print("📱 Accede desde cualquier dispositivo en tu red WiFi")
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Servidor detenido por el usuario")
            print("¡Gracias por usar el Pack de Estudio!")

if __name__ == "__main__":
    main()