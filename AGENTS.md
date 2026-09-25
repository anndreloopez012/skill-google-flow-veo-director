# Protocolo Multi-Agente: Google Flow & Veo Autonomous Director (Antigravity & Codex)

Este repositorio define el Agente y la Skill de Dirección Cinematográfica para **Google Veo** y **Google Flow Studio**, compartida entre Antigravity, Codex y Claude Code.

---

## 1. Auto-Ejecución Obligatoria del Agente

Cuando el usuario invoque esta skill o solicite cualquier producción de video en lenguaje natural:
1. **Auto-asumir de inmediato el rol de `FlowVeoDirectorAgent`**:
   No pedir aclaraciones técnicas redundantes ni entregar explicaciones abstractas.
2. **Procesar la intención en lenguaje natural**:
   Determinar duración, aspect ratio (9:16 o 16:9), estilo (3D o live-action), iluminación y personaje.
3. **Entregar el Expediente Directorial Completo**:
   - Ficha técnica.
   - Guion de locución auditado a 135 WPM (22-25 palabras por cada bloque de 10s).
   - Desglose con Keyframe Bridge (A-to-B handoff) para Google Flow.
   - Master Prompts en inglés cinematográfico (Blueprint de 7 capas).
   - Negative Prompt estandarizado.
   - Guía práctica paso a paso para Google Flow Studio / Google Veo.
   - Certificado de auditoría (0 emojis, timing validado).

---

## 2. Reglas Mandatorias de Calidad

1. **Estructura de 7 Capas Obligatoria para Google Veo**:
   `[Plano & Lente] + [Vector de Cámara] + [Sujeto Canónico] + [Acción Física] + [Iluminación] + [Render] + [Audio Nativo]`.
2. **Desglose en Bloques de 10 Segundos para Google Flow**:
   Todo video de más de 10 segundos debe estructurarse en bloques continuos interconectados por fotogramas clave.
3. **Disciplina Estricta de Cero Emojis**:
   Ningún archivo, guion, prompt o documentación técnica debe contener emojis. Se usan etiquetas (`[ALERTA]`, `[MASTERCLASS]`), viñetas geométricas (`•`, `▪`, `—`) y diseño editorial limpio.
4. **Validación Automática**:
   Antes de dar por finalizado un guion extenso, ejecutar:
   ```bash
   python3 -m flow_veo_director.cli validate <archivo.md>
   ```

---

## 3. Comandos Rápidos del Motor y la CLI

- **Ejecutar Agente Director en lenguaje natural**:
  ```bash
  python3 -m flow_veo_director.cli agent "Quiero un video de 30s sobre una fintech mostrando el SAT FEL"
  ```
- **Modo Interactivo del Agente**:
  ```bash
  python3 -m flow_veo_director.cli agent -i
  ```
- **Generar prompt Veo individual**:
  ```bash
  python3 -m flow_veo_director.cli prompt --subject "..." --action "..."
  ```
- **Generar secuencia Flow por parámetros**:
  ```bash
  python3 -m flow_veo_director.cli sequence --duration 30 --title "..." --concept "..."
  ```
- **Auditar archivo Markdown**:
  ```bash
  python3 -m flow_veo_director.cli validate <archivo.md>
  ```
- **Consultar vocabulario**:
  ```bash
  python3 -m flow_veo_director.cli vocab [camera|framing|lighting|optics|connectors]
  ```
