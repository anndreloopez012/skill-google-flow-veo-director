# Protocolo Multi-Agente: Google Flow & Veo Cinematic Director (Antigravity & Codex)

Este repositorio define la Skill de Dirección Cinematográfica para **Google Veo** y **Google Flow Studio**, compartida entre Antigravity, Codex y Claude Code.

---

## 1. Reglas Mandatorias para Agentes

1. **Estructura de 7 Capas Obligatoria para Google Veo**:
   Al redactar un prompt para Google Veo, nunca entregar un texto plano o ambiguo. Formular siempre el *Directorial Blueprint*:
   `[Plano & Lente] + [Vector de Cámara] + [Sujeto Canónico] + [Acción Física] + [Iluminación] + [Render] + [Audio Nativo]`.
2. **Desglose en Bloques de 10 Segundos para Google Flow**:
   Si el usuario solicita un video de más de 10 segundos (20s, 30s, 40s, 60s), desglosarlo obligatoriamente en bloques de 10 segundos con:
   - `Start Keyframe` y `End Keyframe Goal`.
   - `Character Anchor` canónico.
   - `Vector de Cámara`.
   - `Conector de Edición`.
   - `Guion de Locución Calibrado`: entre **22 y 25 palabras en español** por cada 10 segundos.
3. **Disciplina Estricta de Cero Emojis**:
   Ningún archivo, guion, prompt o documentación técnica debe contener emojis. Se usan etiquetas (`[ALERTA]`, `[MASTERCLASS]`), viñetas geométricas (`•`, `▪`, `—`) y diseño editorial limpio.
4. **Validación Automática**:
   Antes de dar por finalizado un guion extenso, ejecutar:
   ```bash
   python3 -m flow_veo_director.cli validate <archivo.md>
   ```

---

## 2. Comandos Rápidos del Motor
- Generar prompt Veo: `python3 -m flow_veo_director.cli prompt --subject "..." --action "..."`
- Generar secuencia Flow: `python3 -m flow_veo_director.cli sequence --duration 30 --title "..." --concept "..."`
- Auditar archivo: `python3 -m flow_veo_director.cli validate <archivo.md>`
- Consultar vocabulario: `python3 -m flow_veo_director.cli vocab [camera|framing|lighting|optics|connectors]`
