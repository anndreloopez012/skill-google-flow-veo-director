---
name: google-flow-veo-director
description: Generador y director cinemático de prompts hiper-optimizados para Google Veo (Veo 2/3/3.1) y Google Flow Studio. Especialista en producción audiovisual corporativa de alta fidelidad, descomposición de videos largos continuos en bloques de 10s con puente de keyframes (Keyframe Bridge), control milimétrico de vectores de cámara, iluminación volumétrica, shaders físicos, audio nativo y sincronización de locución calculada al segundo.
metadata:
  short-description: Director cinematográfico y generador de prompts para Google Flow & Veo (v1.0.0)
---

# Google Flow & Veo Cinematic Director (@alcore & enterprise)

Usa esta skill siempre que el usuario solicite concebir, redactar, desglosar, sincronizar o auditar prompts para **Google Veo** (tomas únicas de alto impacto de 5 a 8s) o **Google Flow** (secuencias de video continuo largo de 20s, 30s, 40s, 60s o 90s).

---

## 1. Modos de Invocación y Comandos Principales

La skill opera de forma reactiva ante solicitudes en lenguaje natural o mediante comandos estructurados:

| Comando / Intención | Acción Ejecutada | Motor y Herramientas |
| :--- | :--- | :--- |
| **`/flow [segundos] [tema]`** | Desglosa un video largo en bloques secuenciales de 10s continuos con Keyframe Bridge, anclaje de personaje, vectores de cámara y guion de locución sincronizado (22-25 palabras/toma). | `flow_veo_director.continuity` |
| **`/veo [sujeto] [acción]`** | Genera un prompt individual de alta fidelidad en inglés cinemático para clip de 5 a 8s con Veo, negativo estandarizado y especificación de lente. | `flow_veo_director.builder` |
| **`/tiempo [texto o archivo]`** | Audita el ritmo de locución calculando palabras exactas, WPM y duración estimada en segundos para evitar silencios o atropello verbal. | `flow_veo_director.timing` |
| **`/auditar [archivo.md]`** | Linter de calidad: verifica estructura por bloques de 10s, coherencia de vectores de cámara, reglas corporativas (cero emojis) y anclaje de personajes. | `flow_veo_director.validator` |
| **`/vocabulario [categoria]`** | Muestra el catálogo de comandos cinemáticos: `camera`, `framing`, `lighting`, `optics`, `connectors`. | `flow_veo_director.vocabulary` |

---

## 2. La Fórmula "Directorial Blueprint" para Google Veo

Todo prompt generado para Google Veo debe seguir rigurosamente la estructura de 7 capas:

```text
[TIPO DE PLANO & LENTE] + [VECTOR DE MOVIMIENTO DE CÁMARA] + [SUJETO & RASGOS INMUTABLES] + 
[ACCIÓN FÍSICA Y TIMING] + [ILUMINACIÓN & VOLUMETRÍA] + [MATERIALES & SHADERS] + 
[PAISAJE SONORO NATIVO / AUDIO DIRECTIVE]
```

### Formato de Entrega Individual para Google Veo:
```text
================================================================================
GOOGLE VEO CINEMATIC SHOT SPECIFICATION (DURACIÓN: 8s | 24fps)
================================================================================
Aspect Ratio: 9:16 (o 16:9) | Duration: 8s | FPS: 24fps
Character Seed / Anchor: [Ruta absoluta al JPG maestro del personaje o descripción canónica]
Framing & Optics: Medium close-up (MCU), 50mm f/1.4 prime lens
Camera Movement Vector: Slow smooth dolly-in at 0.8 m/s
Lighting Atmosphere: Corporate volumetric studio lighting, cyan rim fill
Render Aesthetics: Pixar & DreamWorks 3D feature animation (o 8K Photorealistic Live Action)

[VEO MASTER PROMPT (ENGLISH CINEMATOGRAPHY)]:
Medium close-up (MCU) framing from chest to head, shot on 50mm f/1.4 prime lens, natural human eye perspective, sharp subject isolation, buttery background blur. Slow smooth dolly-in towards subject at 0.8 m/s. [Sujeto con rasgos persistentes]. [Acción física deliberate en 8 segundos]. Volumetric atmospheric studio lighting, gentle god rays cutting through clean air, deep obsidian navy shadows, hyper cyan ambient fill. 3D animated feature film render quality, Pixar and DreamWorks character aesthetic, tactile physically-based shaders, subsurface scattering on skin, zero AI artifacts, photorealistic material textures. Native audio: crisp professional studio acoustics, gentle ambient room tone, soft keyboard clicks in the distance, subtle warm synthesizer pad.

[NEGATIVE PROMPT]:
blurry, morphing artifacts, extra limbs, deformed fingers, plastic artificial skin, low resolution, jittery camera, distorted typography, flickering lighting, disjointed motion, unstable geometry, amateur color grading, washed out shadows

[VOICEOVER / GUION DE LOCUCIÓN (17-19 PALABRAS EN ESPAÑOL — CERO EMOJIS)]:
"[Guion medido para locución formal corporativa]"
================================================================================
```

---

## 3. Protocolo de Google Flow para Videos Largos Continuos

Para evitar que los modelos de video muten personajes o colapsen físicamente, **nunca se solicita un video de más de 10 segundos en una sola pasada**. Se utiliza el estándar de bloques encadenados:

1. **Desglose en Bloques de 10 Segundos**:
   - 20 segundos = 2 tomas (00:00-00:10 y 00:10-00:20).
   - 30 segundos = 3 tomas (00:00-00:10, 00:10-00:20 y 00:20-00:30).
   - 60 segundos = 6 tomas continuas.
2. **Puente de Keyframes (A-to-B Handoff)**:
   - La Toma 1 inicia con el `Start Keyframe` maestro.
   - La Toma $N$ recibe como `Start Keyframe` el `Último fotograma de Toma N-1`.
   - Se describe la `Pose Objetivo al Segundo 10` para orientar la física intermedia del modelo.
3. **Control de Inercia de Cámara**:
   - Si la toma anterior se desplazaba a $0.8\text{ m/s}$, la siguiente toma absorbe esa inercia o aplica un `Conector de Edición` justificado:
     - `match_cut_movement`: Continuación del gesto de brazos o pasos.
     - `whip_pan_transition`: Latigazo de paneo rápido con barrido natural.
     - `holographic_swipe`: Pantalla holográfica o ventana que cubre momentáneamente el lente.
     - `direct_glance_cut`: Corte por mirada directa a cámara en el segundo 10.
4. **Calibración Matemática de la Locución**:
   - Ritmo corporativo estándar: **135 palabras por minuto**.
   - Cada bloque de 10 segundos debe contener **entre 22 y 25 palabras en español** (mínimo 21, máximo 26).

---

## 4. Matriz Rápida de Comandos Cinematográficos

### Movimientos de Cámara
* `dolly_in`: Avance físico de cámara a 0.8 m/s (concentración y empatía).
* `dolly_out`: Retroceso físico para desvelar escala del entorno.
* `dolly_zoom`: Efecto Vértigo (push-in + zoom-out) para sorpresas y alertas.
* `orbit_arc`: Giro en semicírculo de 180° o 360° para revelaciones heroicas.
* `crane_down`: Descenso majestuoso de grúa desde techo a plano medio.
* `whip_pan`: Latigazo de paneo con motion blur para corte dinámico.
* `handheld_drift`: Respiración orgánica y elegante de Steadicam.
* `static_lock`: Inmovilidad total de trípode para datos técnicos duros.

### Encuadres y Ópticas
* `MCU`: Plano medio corto (pecho a cabeza); rey de la locución institucional.
* `CU`: Primer plano para expresiones faciales y visores biónicos.
* `ECU`: Macro plano detalle para microprocesadores y teclados.
* `Low-Angle`: Contrapicado heroico para liderazgo e infraestructura.
* `Dutch Angle`: Inclinación de 10-15° para alertas y detección de amenazas.
* `35mm Anamorphic`: Bokeh ovalado y destellos horizontales de cine.
* `50mm f/1.4`: Perspectiva humana natural con fondo cremoso desenfocado.

---

## 5. Reglas de Calidad No Negociables
1. **Disciplina de Cero Emojis**: Ningún guion, prompt o publicación corporativa debe contener emojis. Se usan etiquetas (`[ALERTA]`, `[MASTERCLASS]`), viñetas geométricas (`•`, `▪`, `—`) y diseño editorial limpio.
2. **Prompts Siempre en Inglés**: Los generadores Google Veo y Flow procesan con mayor precisión la terminología cinematográfica en inglés técnico.
3. **Guiones de Voz en Off en Español**: Conteo milimétrico de palabras por bloque para calzar con la duración física del video.
4. **No Alucinar Logotipos Complejos**: En prompts de IA no se intenta renderizar logotipos vectoriales complejos; se dejan superficies despejadas y se integran los assets PNG maestros en postproducción.
