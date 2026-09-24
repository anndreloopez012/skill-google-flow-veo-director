# Google Flow & Veo Cinematic Director

> **Suite y Skill de Dirección Cinematográfica para Google Veo (2 / 3 / 3.1) y Google Flow Studio.**  
> Especialista en generación de prompts hiper-optimizados, producción de videos largos continuos sin deriva temporal (bloques de 10 segundos), control de cámara en vectores físicos, iluminación volumétrica, audio nativo y sincronización matemática de locución.

---

## 1. Visión General: ¿Qué resuelve esta Skill?

Los generadores de video basados en inteligencia artificial (como Google Veo, Sora, Runway o Luma) presentan un desafío fundamental en entornos corporativos: **la deriva temporal (temporal drift)**. Cuando se solicita un video de 30 o 60 segundos en un solo prompt, el modelo tiende a mutar la ropa de los personajes, deformar extremidades, alterar la iluminación y generar movimientos caóticos de cámara.

**Google Flow & Veo Cinematic Director** resuelve este problema implementando el estándar de la industria:
1. **La Fórmula Directorial de 7 Capas**: Redacta prompts en inglés cinematográfico riguroso que instruyen al modelo como a un equipo de rodaje profesional (lente, cámara, sujeto, acción, iluminación, shaders y audio nativo).
2. **Arquitectura de Continuidad para Videos Largos (Google Flow)**: Descompone cualquier producción (20s, 30s, 40s, 60s o 90s) en **bloques sincronizados de 10 segundos**, conectados mediante un **Puente de Keyframes (Start Frame a End Frame)**, inercia de cámara coordinada y anclajes fijos de personajes.
3. **Calibración Matemática de Locución**: Asegura que el guion en off contenga exactamente **22 a 25 palabras en español por cada bloque de 10 segundos** (basado en el estándar corporativo de 135 palabras por minuto), eliminando silencios incómodos o atropello verbal.
4. **Disciplina Corporativa Estricta**: Formateo editorial de alta gama con política de **CERO EMOJIS**, uso de tipografía técnica (`JetBrains Mono`, `Inter`, `Plus Jakarta Sans`) y etiquetas limpias (`[PRENSA]`, `[MASTERCLASS]`, `[ALERTA]`).

---

## 2. Capacidades Principales

```
+-------------------------------------------------------------------------------------------------+
|                       GOOGLE FLOW & VEO CINEMATIC DIRECTOR SUITE                                |
+-------------------------------+---------------------------------+-------------------------------+
|      MOTOR DE PROMPTS VEO     |     CONTINUIDAD GOOGLE FLOW     |      AUDITOR & LINTER         |
|  • Fórmula de 7 capas         |  • Desglose en bloques de 10s   |  • Detector estricto de emojis|
|  • Ópticas (35mm, 50mm, 85mm) |  • Keyframe Bridge (A-to-B)     |  • Validador WPM de locución  |
|  • Vectores en m/s            |  • Character Anchor Matrix      |  • Chequeo de inercia y física|
|  • Negativos estandarizados   |  • Conectores de transición     |  • Exportación en Markdown    |
+-------------------------------+---------------------------------+-------------------------------+
```

### A. El "Directorial Blueprint" de 7 Capas
Cada prompt individual generado para Google Veo articula:
```text
[TIPO DE PLANO & LENTE] + [VECTOR DE MOVIMIENTO DE CÁMARA] + [SUJETO & RASGOS INMUTABLES] + 
[ACCIÓN FÍSICA Y TIMING] + [ILUMINACIÓN & VOLUMETRÍA] + [MATERIALES & SHADERS] + 
[PAISAJE SONORO NATIVO / AUDIO DIRECTIVE]
```

### B. Arquitectura de Bloques de 10s para Videos Largos
Para videos de 30 segundos, genera una estructura de 3 tomas de 10 segundos:
* **Toma 1 (00:00 - 00:10)**: Gancho visual, Start Keyframe maestro, acción hacia Pose Objetivo 1.
* **Toma 2 (00:10 - 00:20)**: Start Keyframe = *Último fotograma de Toma 1*, orbital arc o match cut, Pose Objetivo 2.
* **Toma 3 (00:20 - 00:30)**: Start Keyframe = *Último fotograma de Toma 2*, dolly-out heroico, llamada a la acción y fade a tarjeta corporativa.

### C. Control de Inercia y Conectores de Transición
* `match_cut_movement`: Emparejamiento de movimiento de brazos o gesticulación.
* `whip_pan_transition`: Latigazo de paneo con desenfoque natural para saltar de ángulo.
* `holographic_swipe`: Ventana holográfica o interfaz que cubre la lente al segundo 9.8 para revelar el siguiente plano.
* `direct_glance_cut`: Sujeto clava la mirada en cámara al segundo 10, cortando a plano cerrado.

---

## 3. Catálogo de Comandos Cinemáticos

### Movimientos de Cámara (Camera Motion Vectors)
| Comando | Parámetros Típicos | Función Cinemática |
| :--- | :--- | :--- |
| `dolly_in` | `0.6 m/s - 1.2 m/s` | Acercamiento frontal suave; intensifica atención y concentración. |
| `dolly_out` | `0.5 m/s - 0.8 m/s` | Retroceso frontal; revela entorno monumental y autoridad. |
| `dolly_zoom` | `Vertigo effect` | Dolly físico hacia adelante + zoom óptico inverso; dramatismo crítico. |
| `orbit_arc` | `30° - 180° - 360°` | Giro orbital alrededor del sujeto; tomas heroicas de producto. |
| `crane_down` | `Ceiling to MCU` | Descenso fluido de grúa estableciendo el escenario y bajando al sujeto. |
| `whip_pan` | `Fast motion blur` | Latigazo horizontal para transiciones enérgicas sin corte aparente. |
| `handheld_drift` | `Organic Steadicam` | Respiración sutil de cámara en mano estabilizada; realismo documental. |
| `static_lock` | `Zero drift tripod` | Trípode 100% inmóvil para dashboards, código y demostraciones analíticas. |

### Encuadres y Lentes Ópticas
* `Medium Close-Up (MCU)` con `50mm f/1.4`: Encuadre estándar de oro para locución corporativa y confianza.
* `Close-Up (CU)` con `85mm Macro`: Enfoque sobre visores HUD, microexpresiones y detalles biométricos.
* `Low-Angle Hero Shot` con `35mm Anamorphic`: Contrapicado monumental con destellos horizontales y compresión elegante.
* `Canted Dutch Angle` (10-15°): Plano inclinado para incidentes de ciberseguridad y cuellos de botella.
* `Over-The-Shoulder (OTS)`: Plano sobre el hombro para interacciones con pantallas y clientes.

### Iluminación y Render
* `corporate_volumetric`: Rayos de luz volumétrica (god rays), sombras en azul obsidiana y acentos cian.
* `high_tech_cleanroom`: Iluminación diurna balanceada a 5600K con softboxes y reflejos ray-traced sobre cristal.
* `chiaroscuro_security`: Alto contraste dramático con rim light ámbar cortando la silueta del sujeto.
* `pixar_dreamworks_3d`: Render de largometraje animado 3D, shaders físicos táctiles y dispersión subsuperficial (SSS).
* `cinematic_live_action`: Simulación de sensor Arri Alexa Mini LF 8K, color grade ACES y textura hiperrealista.

---

## 4. Instalación y Uso del Motor CLI (`flow-veo`)

El motor está escrito en Python 3 puro (sin dependencias externas obligatorias) y se ejecuta instantáneamente:

```bash
# Clonar el repositorio
git clone https://github.com/anndreloopez012/skill-google-flow-veo-director.git
cd skill-google-flow-veo-director

# Dar permisos de ejecución a la CLI
chmod +x flow_veo_director/cli.py
```

### Comandos de la CLI:

#### 1. Generar un Prompt Individual para Google Veo
```bash
python3 -m flow_veo_director.cli prompt \
  --subject "Senior Cloud Architect reviewing telemetry logs" \
  --action "gestures toward a floating cyan holographic cluster map" \
  --framing medium_close_up \
  --camera dolly_in \
  --lighting corporate_volumetric \
  --render pixar_dreamworks_3d \
  --vo "Nuestra arquitectura distribuida garantiza resiliencia inmediata y elimina caídas de sistema en momentos críticos."
```

#### 2. Desglosar un Video Largo en Bloques Continuos de 10s (Google Flow)
```bash
python3 -m flow_veo_director.cli sequence \
  --duration 30 \
  --title "Optimizacion de Costes Cloud" \
  --concept "Demostración de ahorro del 60% en servidores dedicados" \
  --character "Alki the Cyber Wolf" \
  --style 3d \
  --output guion_cloud_30s.md
```

#### 3. Auditar un Guion o Storyboard Markdown
```bash
python3 -m flow_veo_director.cli validate templates/saas_product_tour.md
```

#### 4. Consultar el Diccionario Cinematográfico
```bash
python3 -m flow_veo_director.cli vocab camera
python3 -m flow_veo_director.cli vocab framing
python3 -m flow_veo_director.cli vocab lighting
python3 -m flow_veo_director.cli vocab connectors
```

---

## 5. Estructura del Repositorio

```
skill-google-flow-veo-director/
├── .agents/                        # Configuración para ecosistema de agentes
├── .gitignore                      # Exclusiones de Git
├── AGENTS.md                       # Protocolo unificado para Antigravity y Codex
├── CLAUDE.md                       # Protocolo unificado para Claude Code
├── README.md                       # Documentación maestra del repositorio
├── SKILL.md                        # Definición canónica de la Skill para agentes AI
├── requirements.txt                # Dependencias recomendadas para desarrollo
├── pyproject.toml                  # Metadata del paquete Python CLI
├── flow_veo_director/              # Motor Python ejecutable
│   ├── __init__.py                 # Exportaciones y versión
│   ├── cli.py                      # CLI interactiva y por comandos (`flow-veo`)
│   ├── builder.py                  # Generador determinista de prompts (Veo & Flow)
│   ├── continuity.py               # Generador de secuencias de 10s (Keyframe Bridge)
│   ├── timing.py                   # Calculador de cadencia de locución y conteo de palabras
│   ├── validator.py                # Linter de física, cámaras, reglas corporativas y timing
│   └── vocabulary.py               # Diccionario exhaustivo de comandos cinematográficos
├── references/                     # Manuales de referencia técnica
│   ├── 01_comandos_camara_y_lentes.md
│   ├── 02_iluminacion_fisica_y_render.md
│   ├── 03_arquitectura_flow_videos_largos.md
│   ├── 04_audio_nativo_y_locucion.md
│   └── 05_matriz_consistencia_personajes.md
├── templates/                      # Plantillas listas para usar en producción
│   ├── saas_product_tour.md        # Video de 30s de recorrido de producto SaaS
│   ├── cybersecurity_alert.md      # Video de 20s de mitigación de incidente de red
│   ├── fintech_dashboard_reveal.md # Video de 30s de retail POS y SAT FEL
│   ├── cloud_infrastructure_scale.md# Video de 30s de optimización y ahorro cloud
│   ├── corporate_brand_manifesto.md# Video de 40s manifiesto institucional
│   └── kinetic_explainer_split.md  # Video de 20s animado explicativo con pantalla dividida
└── tests/                          # Suite de pruebas unitarias
    ├── test_builder.py
    ├── test_continuity.py
    ├── test_timing.py
    └── test_validator.py
```

---

## 6. Pruebas Automatizadas

El proyecto incluye pruebas unitarias con el módulo estándar `unittest` de Python:

```bash
python3 -m unittest discover -s tests -v
```

Resultado verificado:
```text
test_builder_format_manifest (test_builder.TestBuilder.test_builder_format_manifest) ... ok
test_builder_generate_prompt_text (test_builder.TestBuilder.test_builder_generate_prompt_text) ... ok
test_flow_continuity_valid (test_continuity.TestContinuity.test_flow_continuity_valid) ... ok
test_count_words (test_timing.TestTiming.test_count_words) ... ok
test_evaluate_segment_timing_optimal (test_timing.TestTiming.test_evaluate_segment_timing_optimal) ... ok
test_evaluate_segment_timing_too_fast (test_timing.TestTiming.test_evaluate_segment_timing_too_fast) ... ok
test_evaluate_segment_timing_too_slow (test_timing.TestTiming.test_evaluate_segment_timing_too_slow) ... ok
test_target_word_range (test_timing.TestTiming.test_target_word_range) ... ok
test_emoji_detection (test_validator.TestValidator.test_emoji_detection) ... ok
test_prompt_auditor (test_validator.TestValidator.test_prompt_auditor) ... ok

Ran 10 tests in 0.001s
OK
```

---

## 7. Integración Multi-Agente (Antigravity, Codex y Claude)

Este repositorio está preparado para trabajar en sincronía con cualquier asistente de IA en el ecosistema del usuario:
* **Antigravity**: Lee `.agents/rules/`, `AGENTS.md`, `SKILL.md` y las instrucciones en `references/`.
* **Codex**: Consume `AGENTS.md` y las herramientas en `flow_veo_director/`.
* **Claude Code**: Consume `CLAUDE.md` y la definición modular de comandos.

---

## 8. Licencia y Créditos
* **Desarrollo**: Andre Lopez (@anndreloopez012) & ALCORE Technologies Solutions.
* **Licencia**: MIT License. Libre para uso comercial, corporativo y de investigación.
