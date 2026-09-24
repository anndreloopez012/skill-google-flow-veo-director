# CLAUDE.md: Guía para Claude Code

## Protocolo de Producción de Video: Google Flow & Veo Cinematic Director

Claude Code debe interactuar con este proyecto siguiendo las directivas cinematográficas y de continuidad:

### 1. Comandos Principales
- **Ejecutar Pruebas Unitarias**:
  ```bash
  python3 -m unittest discover -s tests -v
  ```
- **Generar Prompt Veo**:
  ```bash
  python3 -m flow_veo_director.cli prompt --subject "..." --action "..."
  ```
- **Generar Secuencia Flow**:
  ```bash
  python3 -m flow_veo_director.cli sequence --duration 30 --title "..." --concept "..."
  ```
- **Auditar Archivo Markdown**:
  ```bash
  python3 -m flow_veo_director.cli validate <archivo.md>
  ```

### 2. Normas de Estilo y Rigor
- **Cero Emojis**: Prohibición estricta de emojis en prompts, guiones o documentación.
- **Timing Matemático**: Siempre calcular entre 22 y 25 palabras por cada bloque de 10s en español (135 WPM).
- **Puente de Keyframes**: Asegurar que cada toma $N$ reciba como Start Keyframe el fotograma final de la toma $N-1$.
