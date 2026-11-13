# -*- coding: utf-8 -*-
"""Interface texts and project translations (EN, EU)."""

LANGS = ["fr", "en", "eu"]
LANG_NAMES = {"fr": "Français", "en": "English", "eu": "Euskara"}
PROJ_DIR = {"fr": "projets", "en": "projects", "eu": "proiektuak"}

THEME_LABELS = {
    "compilation": {"fr": "Compilation", "en": "Compilers", "eu": "Konpilazioa"},
    "hardware": {"fr": "Hardware", "en": "Hardware", "eu": "Hardwarea"},
    "software": {"fr": "Software", "en": "Software", "eu": "Softwarea"},
    "systeme": {"fr": "Système", "en": "Systems", "eu": "Sistemak"},
    "architecture": {"fr": "Architecture", "en": "Architecture", "eu": "Arkitektura"},
}

UI = {
  "fr": dict(
    nav_projects="Projets", nav_about="À propos", nav_contact="Contact",
    site_desc="Portfolio : systèmes embarqués, électronique, compilation et calcul GPU.",
    hero_a="Je construis des systèmes,", hero_b="du transistor au compilateur.",
    hero_lead="Je m'appelle {name}. J'aime les projets où le logiciel rencontre le matériel : firmware embarqué, conception de PCB, processeurs en VHDL, compilateurs et calcul sur GPU.",
    btn_projects="Voir les projets", filter_all="Tous", discover="Découvrir →",
    about=["Mes projets couvrent toute la pile : concevoir une carte électronique, écrire le firmware qui tourne dessus, décrire un processeur en VHDL, ou au contraire monter dans les couches pour écrire un compilateur.",
           "Ce qui me motive : comprendre comment les choses fonctionnent vraiment, et les faire marcher en conditions réelles — avec du bruit, des contraintes de temps et des ressources limitées."],
    skills=[("Embarqué", ["C", "ESP32 / ESP-IDF", "FreeRTOS", "I²C · ADC · PWM"]),
            ("Électronique", ["Conception PCB", "KiCad", "Capteurs", "Moteurs"]),
            ("Matériel numérique", ["VHDL", "Architecture CPU", "Simulation", "FPGA"]),
            ("Logiciel", ["C++", "CUDA", "Compilation", "Flex · Bison"])],
    contact_h="On en parle ?", contact_p="Stage, projet ou simple question technique : écris-moi.",
    footer="Fait main · hébergé sur GitHub Pages",
    back="← Tous les projets", view_code="Voir le code ↗",
    s_context="Contexte", s_arch="Architecture", s_points="Points techniques", s_code="Extrait de code", s_learned="Ce que j'en retiens",
    prev="← Précédent", next="Suivant →",
    mode="Basculer entre thème clair et sombre", lang="Langue",
  ),
  "en": dict(
    nav_projects="Projects", nav_about="About", nav_contact="Contact",
    site_desc="Portfolio: embedded systems, electronics, compilers and GPU computing.",
    hero_a="I build systems,", hero_b="from transistors to compilers.",
    hero_lead="I'm {name}. I love projects where software meets hardware: embedded firmware, PCB design, VHDL processors, compilers and GPU computing.",
    btn_projects="See projects", filter_all="All", discover="Explore →",
    about=["My projects span the whole stack: designing a circuit board, writing the firmware that runs on it, describing a processor in VHDL, or climbing up the layers to write a compiler.",
           "What drives me: understanding how things really work, and making them work in real conditions — with noise, timing constraints and limited resources."],
    skills=[("Embedded", ["C", "ESP32 / ESP-IDF", "FreeRTOS", "I²C · ADC · PWM"]),
            ("Electronics", ["PCB design", "KiCad", "Sensors", "Motors"]),
            ("Digital hardware", ["VHDL", "CPU architecture", "Simulation", "FPGA"]),
            ("Software", ["C++", "CUDA", "Compilers", "Flex · Bison"])],
    contact_h="Let's talk", contact_p="Internship, project or just a technical question: drop me a line.",
    footer="Handmade · hosted on GitHub Pages",
    back="← All projects", view_code="View code ↗",
    s_context="Context", s_arch="Architecture", s_points="Technical highlights", s_code="Code excerpt", s_learned="Key takeaways",
    prev="← Previous", next="Next →",
    mode="Toggle light / dark theme", lang="Language",
  ),
  "eu": dict(
    nav_projects="Proiektuak", nav_about="Niri buruz", nav_contact="Harremana",
    site_desc="Portfolioa: sistema txertatuak, elektronika, konpilazioa eta GPU bidezko kalkulua.",
    hero_a="Sistemak eraikitzen ditut,", hero_b="transistoretik konpilatzaileraino.",
    hero_lead="{name} naiz. Softwarea eta hardwarea elkartzen diren proiektuak gustatzen zaizkit: firmware txertatua, PCB diseinua, VHDL prozesadoreak, konpilatzaileak eta GPU bidezko kalkulua.",
    btn_projects="Proiektuak ikusi", filter_all="Denak", discover="Ezagutu →",
    about=["Nire proiektuek pila osoa hartzen dute: txartel elektroniko bat diseinatzea, haren gainean dabilen firmwarea idaztea, prozesadore bat VHDLz deskribatzea, edo, alderantziz, geruzetan gora igo eta konpilatzaile bat idaztea.",
           "Motibatzen nauena: gauzak benetan nola dabiltzan ulertzea, eta baldintza errealetan funtzionaraztea — zaratarekin, denbora-mugekin eta baliabide mugatuekin."],
    skills=[("Txertatua", ["C", "ESP32 / ESP-IDF", "FreeRTOS", "I²C · ADC · PWM"]),
            ("Elektronika", ["PCB diseinua", "KiCad", "Sentsoreak", "Motorrak"]),
            ("Hardware digitala", ["VHDL", "CPU arkitektura", "Simulazioa", "FPGA"]),
            ("Softwarea", ["C++", "CUDA", "Konpilazioa", "Flex · Bison"])],
    contact_h="Hitz egingo dugu?", contact_p="Praktikak, proiektu bat edo galdera tekniko soil bat: idatzidazu.",
    footer="Eskuz egina · GitHub Pages-en ostatatua",
    back="← Proiektu guztiak", view_code="Kodea ikusi ↗",
    s_context="Testuingurua", s_arch="Arkitektura", s_points="Puntu teknikoak", s_code="Kode-zatia", s_learned="Zer ikasi dudan",
    prev="← Aurrekoa", next="Hurrengoa →",
    mode="Gai argia / iluna aldatu", lang="Hizkuntza",
  ),
}

# Translated code comments (EN and EU use English in code)
CODE_EN = [
    ("// Un thread par pixel : écart maximal sur les trois canaux entre l'image et le fond", "// One thread per pixel: maximum difference over the three channels between frame and background"),
    ("-- Signaux de commande de chaque instruction", "-- Control signals of each instruction"),
    ("-- branche si N = 1", "-- branch if N = 1"),
    ("// Mise à jour de Kalman : mesure virtuelle « vitesse = 0 »", "// Kalman update: virtual measurement \"velocity = 0\""),
    ("// amag, gmag : normes de l'accélération et du gyroscope", "// amag, gmag: norms of the acceleration and of the gyroscope"),
    ("// Immobile : accélération ≈ g et rotation quasi nulle, ZUPT_WINDOW échantillons de suite", "// Stationary: acceleration ≈ g and almost no rotation, for ZUPT_WINDOW samples in a row"),
    ("// prédiction : intégration de l'accélération (idem pour y et z)", "// prediction: integrate the acceleration (same for y and z)"),
    ("// à l'arrêt : correction de Kalman (idem pour y et z)", "// when stopped: Kalman correction (same for y and z)"),
    ("// TIM2 : interruption périodique qui cadence les mesures", "// TIM2: periodic interrupt that paces the measurements"),
    ("// ADC1, canal 11 (PC1) : conversions lues par interruption", "// ADC1, channel 11 (PC1): conversions read through an interrupt"),
    ("// PC1 en entrée analogique", "// PC1 as analog input"),
    ("// TIM2 déclenche la conversion", "// TIM2 triggers the conversion"),
    ("// temps d'échantillonnage maximal", "// maximum sampling time"),
    ("// en g", "// in g"), ("// en rad/s", "// in rad/s"), ("// retire la gravité", "// remove gravity"),
    ("// Broche « flottante » : entrée sans pull-up ni pull-down (haute impédance)", "// \"Floating\" pin: input with no pull-up or pull-down (high impedance)"),
    ("// Allume une LED : anode à 1, cathode à 0, les autres broches restent flottantes", "// Turn on an LED: anode high, cathode low, all other pins stay floating"),
    ("// Balayage : une seule LED allumée à la fois, ~1 ms chacune", "// Scan: only one LED on at a time, ~1 ms each"),
    ("// éteint la LED précédente", "// turn off the previous LED"),
    ("// persistance rétinienne", "// persistence of vision"),
]

# Basque code comments (applied before CODE_EN for the EU pages; other comments fall back to CODE_EN)
CODE_EU = [
    ("// Un thread par pixel : écart maximal sur les trois canaux entre l'image et le fond", "// Hari bat pixel bakoitzeko: irudiaren eta hondoaren arteko alderik handiena hiru kanaletan"),
    ("-- Signaux de commande de chaque instruction", "-- Aginduen kontrol-seinaleak"),
    ("-- branche si N = 1", "-- jauzi egin N = 1 bada"),
    ("// Mise à jour de Kalman : mesure virtuelle « vitesse = 0 »", "// Kalman eguneraketa: \"abiadura = 0\" neurketa birtuala"),
    ("// amag, gmag : normes de l'accélération et du gyroscope", "// amag, gmag: azelerazioaren eta giroskopioaren moduluak"),
    ("// Immobile : accélération ≈ g et rotation quasi nulle, ZUPT_WINDOW échantillons de suite", "// Geldirik: azelerazioa ≈ g eta ia biraketarik gabe, ZUPT_WINDOW lagin jarraian"),
    ("// prédiction : intégration de l'accélération (idem pour y et z)", "// aurreikuspena: azelerazioaren integrazioa (berdin y eta z-rentzat)"),
    ("// à l'arrêt : correction de Kalman (idem pour y et z)", "// geldirik dagoenean: Kalman zuzenketa (berdin y eta z-rentzat)"),
    ("// retire la gravité", "// grabitatea kendu"),
    ("// TIM2 : interruption périodique qui cadence les mesures", "// TIM2: neurketak kadentziatzen dituen eten periodikoa"),
    ("// ADC1, canal 11 (PC1) : conversions lues par interruption", "// ADC1, 11. kanala (PC1): bihurketak etenen bidez irakurtzen dira"),
    ("// PC1 en entrée analogique", "// PC1 sarrera analogiko gisa"),
    ("// TIM2 déclenche la conversion", "// TIM2-k bihurketa abiarazten du"),
    ("// temps d'échantillonnage maximal", "// laginketa-denbora maximoa"),
    ("// Broche « flottante » : entrée sans pull-up ni pull-down (haute impédance)", "// Pin \"flotatzailea\": pull-up edo pull-down gabeko sarrera (inpedantzia altua)"),
    ("// Allume une LED : anode à 1, cathode à 0, les autres broches restent flottantes", "// LED bat piztu: anodoa 1ean, katodoa 0an, gainerako pinak flotatzen"),
    ("// Balayage : une seule LED allumée à la fois, ~1 ms chacune", "// Ekorketa: LED bakarra piztuta aldi berean, ~1 ms bakoitza"),
    ("// éteint la LED précédente", "// aurreko LEDa itzali"),
    ("// persistance rétinienne", "// ikusmenaren iraunkortasuna"),
]

TR = {"en": {}, "eu": {}}

# ============================ ENGLISH ============================
TR["en"]["tiger-compiler"] = dict(
  tagline="A complete compiler for the Tiger language, written in C++.", domain="Compilers",
  facts=[("Language", "C++17"), ("Tools", "Flex · Bison · Make"), ("Target", "Assembly / IR"), ("Type", "Team project")],
  context="""<p>Tiger is a small, statically typed imperative language from Andrew Appel's book <em>Modern Compiler Implementation</em>. It has structured types (records, arrays), nested functions, lexical scoping and explicit <code>let … in … end</code> blocks.</p>
<p>The goal: take a <code>.tig</code> source file and produce executable code, going through every stage of a real compiler — from lexical analysis all the way to register allocation.</p>""",
  pipeline=["Source .tig", "Lexer (Flex)", "Parser (Bison)", "AST", "Binding", "Type checking", "IR translation", "Canonicalization", "Instruction selection", "Register allocation", "Assembly"],
  pipeline_caption="Compilation pipeline, from source text to machine code.",
  points=[("Lexing & parsing", "Flex scanner and Bison grammar, with conflict resolution, operator precedence and located error messages (line / column)."),
          ("AST & visitors", "C++ abstract syntax tree traversed with the Visitor pattern: pretty-printer, binder, type checker and translator share the same hierarchy."),
          ("Name binding", "Identifier resolution with nested-scope symbol tables, and detection of variables that escape into inner functions."),
          ("Type checking", "Typing of expressions, recursive records and arrays; clear semantic errors instead of crashes."),
          ("Intermediate representation", "Translation to an IR tree, then linearization and canonicalization into basic blocks before code generation."),
          ("Back end", "Instruction selection by tree-pattern tiling, liveness analysis and register allocation by graph coloring.")],
  learned=["Understanding what really happens between source code and binary.", "Designing a large, modular and testable C++ codebase (test suites for every stage).", "Working as a team on a long project with code reviews and continuous integration."])

TR["en"]["light-tracker"] = dict(
  tagline="A robot that turns on its own toward the brightest light source.", domain="Robotics",
  tags=["Microcontroller", "C", "ADC", "Motor", "Control loop"],
  facts=[("Sensors", "2 photoresistors"), ("Actuator", "Motor + H-bridge"), ("Language", "Embedded C"), ("Type", "Hardware project")],
  context="""<p>The principle is simple: two light sensors on either side of the robot measure light intensity. If one side gets more light than the other, the motor turns to rebalance — and the robot ends up pointing at the source.</p>
<p>Behind that simplicity: analog acquisition, noise filtering, a dead zone to avoid oscillations, and bidirectional motor control.</p>""",
  pipeline=["Left sensor", "Right sensor", "Voltage dividers", "ADC", "Filtering", "Error = L − R", "Command", "H-bridge", "Motor"],
  pipeline_caption="Control loop: from light measurement to motor rotation.",
  points=[("Acquisition", "Each photoresistor forms a voltage divider; the voltage is read by the microcontroller's analog-to-digital converter."),
          ("Calibration", "The two sensors never respond exactly the same: an offset measured at startup compensates for the difference."),
          ("Filtering", "Moving average over several samples to smooth out noise (fluorescent lights, 50 Hz flicker)."),
          ("Dead zone", "Below a threshold, the motor stays still: the robot doesn't jitter once it's aligned."),
          ("Proportional control", "Speed (PWM) depends on the error: fast rotation when the light is far off, slowing down as it gets aligned."),
          ("Power stage", "An H-bridge isolates the microcontroller from the motor current and allows reversing the direction.")],
  learned=["Turning a simple idea into a physical system that actually works (noise, tolerances, mechanics).", "Control basics: error, gain, dead zone, stability.", "Cleanly separating control logic from the power stage."])

TR["en"]["object-detection-gpu"] = dict(
  tagline="Moving-object detection through background subtraction: a CUDA GStreamer filter, 30 to 41× faster than the CPU.", domain="Vision · GPU",
  tags=["CUDA", "C++20", "GStreamer", "Nsight", "CMake"],
  facts=[("Language", "C++ / CUDA"), ("Result", "×30 to ×41 vs CPU (1080p)"), ("Profiling", "Nsight Systems"), ("Type", "Group project (4)")],
  context="""<p>GPGPU project at EPITA, in a group of four: write a CUDA GStreamer filter that separates the background from moving objects in a video stream, then displays the moving pixels in red. It is a preliminary step in many video-processing chains.</p>
<p>We first wrote a reference CPU version, then a naive GPU port, which we optimized in eight steps (v1.1.0 → v1.1.8). Each step was measured with Nsight Systems before choosing the next one.</p>""",
  pipeline=["Video frame", "Background estimation (reservoirs)", "Mask max(|I − B|)", "Opening (erosion + dilation)", "Hysteresis", "Red overlay"],
  pipeline_caption="Filter pipeline, each stage being one or more CUDA kernels.",
  points=[("Background estimation", "Each pixel keeps k weighted candidate colors (a reservoir), updated by cuRAND random draws; the highest-weight color is the background."),
          ("Mask and hysteresis", "Maximum difference over the RGB channels, then low / high thresholds: a mid-level pixel is kept only if it is connected to a strong one."),
          ("Shared-memory hysteresis", "Propagation inside a tile until stable with __syncthreads_or, then skipping inactive blocks: from 172 launches per frame to about 11, hysteresis from 12.7 to 0.55 ms."),
          ("Separable opening", "A min / max over a square window becomes a horizontal then a vertical pass: 81 reads per pixel down to 18, then fused into a single shared-memory kernel with a halo."),
          ("Data stays on the GPU", "Frame and background stay in GPU memory, buffers are allocated once, the mask is uint8_t instead of float, and the reservoir is a structure of arrays for contiguous accesses."),
          ("Honest benchmark", "Three videos, same parameters, same machine. Past v1.1.3 the compute is only ~2.4 ms out of 14.6 ms per frame: decoding and transfers dominate.")],
  learned=["Thinking about an algorithm in terms of massive parallelism.", "Profile before optimizing: we first optimized copies (1.3 ms) while hysteresis cost 12.7.", "Reading a result honestly: an optimization can be neutral (v1.1.4) and still worth keeping for code clarity."])

TR["en"]["deriscage-esp32"] = dict(
  title="Dérisquage on ESP32",
  tagline="IMU motion estimation: Madgwick filter + ZUPT correction, on ESP32.", domain="Embedded systems",
  tags=["ESP32", "ESP-IDF", "FreeRTOS", "MPU6050", "I²C", "Sensor fusion"],
  facts=[("Board", "ESP32"), ("Framework", "ESP-IDF · FreeRTOS"), ("Sensor", "MPU6050 (accel + gyro)"), ("Algorithms", "Madgwick · ZUPT")],
  context="""<p>An MPU6050 provides 3-axis accelerations and angular rates. In theory, integrating acceleration twice gives you position. In practice, the slightest bias blows up: after a few seconds, the position drifts by several meters.</p>
<p>This project combines two techniques to make the estimate usable: the <strong>Madgwick filter</strong> to know the sensor's orientation, and <strong>ZUPT</strong> (Zero Velocity Update) correction to reset velocity to zero whenever the sensor is still.</p>""",
  pipeline=["MPU6050", "I²C read", "Bias calibration", "Madgwick filter", "World-frame accel.", "− gravity", "∫ velocity", "Stillness detection", "ZUPT: v = 0", "∫ position"],
  pipeline_caption="Processing chain running in real time on the ESP32.",
  points=[("I²C driver", "Communication with the MPU6050 through the ESP-IDF I²C API: range configuration (±g, °/s), burst register reads."),
          ("FreeRTOS tasks", "A fixed-rate acquisition task and a processing task, exchanging data through a queue for regular sampling."),
          ("Madgwick filter", "Gyro + accelerometer fusion via gradient descent on an orientation quaternion, tuned by the β parameter."),
          ("World frame", "Acceleration is rotated into the Earth frame using the quaternion, then gravity is subtracted to keep only linear acceleration."),
          ("Stillness detection", "Over a sliding window: acceleration norm close to g and near-zero rotation → the sensor is considered stationary."),
          ("ZUPT correction", "At each stationary phase, velocity is forced to zero: accumulated error is cut off and position drift stays bounded.")],
  learned=["Developing with ESP-IDF and structuring a real-time application with FreeRTOS.", "Understanding sensor fusion and the physical limits of a low-cost IMU.", "Correcting drift with prior knowledge (here: stationary phases)."])

TR["en"]["pcb-snake"] = dict(
  tagline="A Snake console on a custom PCB: microcontroller and charlieplexed LED matrix.", domain="Electronics",
  tags=["PCB", "KiCad", "Microcontroller", "Charlieplexing", "C"],
  facts=[("Design", "Schematic + PCB layout"), ("Display", "Charlieplexed LEDs"), ("Firmware", "Embedded C"), ("Type", "Full hardware project")],
  context="""<p>The goal: design from scratch a small console that runs Snake — schematic, PCB layout, soldering, then the game firmware.</p>
<p>The interesting constraint: driving many LEDs with very few pins. That's where <strong>charlieplexing</strong> comes in: it uses the high-impedance state of GPIOs to address <code>n × (n − 1)</code> LEDs with only <code>n</code> pins.</p>""",
  pipeline=["Schematic", "Footprints", "PCB layout", "Fabrication", "Soldering", "Firmware", "Snake game"],
  pipeline_caption="From schematic to a working console.",
  points=[("Charlieplexing", "To light an LED, one pin is driven high, another low, and all others are set as inputs (high impedance). With 9 pins: 9 × 8 = 72 addressable LEDs, enough for an 8 × 8 grid."),
          ("Scanning", "Only one LED (or one row) is on at a time, but scanning is fast enough for persistence of vision to show a stable image."),
          ("Layout", "Charlieplexing wiring is dense and counter-intuitive: LED placement and trace routing required particular care."),
          ("Inputs", "Direction buttons with software debouncing, read between refresh cycles."),
          ("Game logic", "Snake stored in a circular buffer, apple generation, collision detection and progressive speed-up."),
          ("Power", "Sizing of current-limiting resistors and power supply for even brightness.")],
  learned=["Designing a complete PCB, from schematic to soldered product.", "An elegant multiplexing technique that saves pins.", "The very concrete link between hardware constraints and software architecture."])

TR["en"]["cpu-monocycle"] = dict(
  title="Single-Cycle CPU",
  tagline="A 32-bit ARM-style single-cycle processor described in VHDL, validated in simulation and targeted at a MAX 10 board.", domain="Architecture · FPGA",
  tags=["VHDL", "Architecture", "ModelSim", "Quartus", "FPGA"],
  facts=[("Language", "VHDL"), ("Instruction set", "32-bit ARM subset"), ("Target", "DE10-Lite (MAX 10)"), ("Verification", "One testbench per block")],
  context="""<p>A single-cycle processor executes each instruction — fetch, decode, execute, memory access, write-back — in one clock cycle. It's the simplest architecture to reason about, and the foundation for understanding pipelining later on.</p>
<p>The project, done in two steps, describes each datapath block in VHDL with its unit tests, wires them together with an instruction decoder, then runs a real assembly program. The Quartus project targets a DE10-Lite board, with the result shown on its 7-segment displays.</p>""",
  pipeline=["PC + instruction memory", "Decoder", "Register file", "Sign extension", "ALU", "Data memory", "Write-back"],
  pipeline_caption="Datapath of the single-cycle processor.",
  points=[("ALU", "Four operations (A + B, A − B, A, B) and two flags, N (negative) and Z (zero), stored in a status register."),
          ("Register file", "16 registers of 32 bits, two asynchronous read ports, one write port synchronous on the clock edge."),
          ("Decoder", "Recognizes MOV, ADD (register or immediate), CMP, LDR, STR, B and BLT from the ARM condition, type and opcode fields, and drives nine control signals."),
          ("Separate memories", "64 words for instructions, 64 words for data (Harvard). The test program sums an array in memory with an LDR / ADD / CMP / BLT loop."),
          ("PC logic", "PC + 1 or a relative branch from a sign-extended 24-bit offset; BLT only branches when the N flag is set."),
          ("Verification", "A testbench and ModelSim script for each block (ALU, mux, extender, registers, memory, decoder, PC unit), then for the whole processor.")],
  learned=["Thinking in hardware: concurrency, signals, timing, rather than a sequence of instructions.", "Understanding concretely how a 32-bit word becomes control signals.", "Validating each block alone, then in integration, before assembling everything."])

# ============================ EUSKARA ============================
TR["eu"]["tiger-compiler"] = dict(
  tagline="Tiger lengoaiarako konpilatzaile osoa, C++-n idatzia.", domain="Konpilazioa",
  facts=[("Lengoaia", "C++17"), ("Tresnak", "Flex · Bison · Make"), ("Helburua", "Mihiztadura / IR"), ("Mota", "Talde-proiektua")],
  context="""<p>Tiger lengoaia inperatibo txiki eta tipatua da, Andrew Appel-en <em>Modern Compiler Implementation</em> liburutik datorrena. Datu-mota egituratuak (erregistroak, arrayak), funtzio habiaratuak, esparru lexikoak eta <code>let … in … end</code> blokeak ditu.</p>
<p>Helburua: <code>.tig</code> iturburu-fitxategi batetik abiatuta kode exekutagarria sortzea, benetako konpilatzaile baten urrats guztiak zeharkatuz — analisi lexikotik erregistroen esleipeneraino.</p>""",
  pipeline=["Iturburua .tig", "Lexerra (Flex)", "Parserra (Bison)", "AST", "Izenen lotura", "Tipo-egiaztapena", "IR itzulpena", "Kanonizazioa", "Agindu-hautaketa", "Erregistro-esleipena", "Mihiztadura"],
  pipeline_caption="Konpilazio-katea, iturburu-testutik makina-kodera.",
  points=[("Analisi lexikoa eta sintaktikoa", "Flex eskanerra eta Bison gramatika, gatazken kudeaketarekin, eragileen lehentasunekin eta kokatutako errore-mezuekin (lerroa / zutabea)."),
          ("AST eta bisitariak", "C++-ko zuhaitz sintaktiko abstraktua, Visitor diseinu-ereduaren bidez korritua: pretty-printerrak, binderrak, tipo-egiaztatzaileak eta itzultzaileak hierarkia bera partekatzen dute."),
          ("Izenen lotura", "Identifikatzaileen ebazpena esparru habiaratuetako ikur-taulekin, eta barneko funtzioetara «ihes egiten» duten aldagaien detekzioa."),
          ("Tipo-egiaztapena", "Adierazpenen, erregistro errekurtsiboen eta arrayen tipatzea; errore semantiko argiak, programa kraskatu beharrean."),
          ("Tarteko adierazpena", "IR zuhaitzera itzultzea, eta ondoren oinarrizko blokeen linealizazioa eta kanonizazioa, kodea sortu aurretik."),
          ("Back-enda", "Agindu-hautaketa zuhaitz-ereduen bidez, bizitasun-analisia eta erregistro-esleipena grafoen koloreztatzearen bidez.")],
  learned=["Iturburu-kodearen eta bitarraren artean benetan gertatzen dena ulertzea.", "C++ kode-base handi, modular eta probagarri bat diseinatzea (proba-multzoak urrats bakoitzeko).", "Taldean lan egitea proiektu luze batean, kode-berrikuspenekin eta integrazio jarraituarekin."])

TR["eu"]["light-tracker"] = dict(
  tagline="Argi-iturri biziena dagoen aldera bere kabuz biratzen den robota.", domain="Robotika",
  tags=["Mikrokontrolagailua", "C", "ADC", "Motorra", "Kontrol-begizta"],
  facts=[("Sentsoreak", "2 fotoerresistentzia"), ("Eragingailua", "Motorra + H zubia"), ("Lengoaia", "C txertatua"), ("Mota", "Hardware-proiektua")],
  context="""<p>Printzipioa sinplea da: robotaren alde banatan jarritako bi argi-sentsorek argi-intentsitatea neurtzen dute. Alde batek besteak baino argi gehiago jasotzen badu, motorrak biratu egiten du oreka berreskuratzeko — eta robota iturriari begira geratzen da.</p>
<p>Sinpletasun horren atzean: eskuratze analogikoa, zarataren iragazketa, oszilazioak saihesteko zona hila eta bi noranzkoetan dabilen motorraren kontrola.</p>""",
  pipeline=["Ezkerreko sentsorea", "Eskuineko sentsorea", "Tentsio-zatitzaileak", "ADC", "Iragazketa", "Errorea = Ezk − Esk", "Agindua", "H zubia", "Motorra"],
  pipeline_caption="Kontrol-begizta: argiaren neurketatik motorraren biraketara.",
  points=[("Eskuratzea", "Fotoerresistentzia bakoitzak tentsio-zatitzaile bat osatzen du; tentsioa mikrokontrolagailuaren bihurgailu analogiko-digitalak irakurtzen du."),
          ("Kalibrazioa", "Bi sentsoreek ez dute inoiz erantzun berdin-berdina: abiaraztean neurtutako desplazamendu batek aldea konpentsatzen du."),
          ("Iragazketa", "Batez besteko mugikorra hainbat laginen gainean, zarata leuntzeko (fluoreszenteak, 50 Hz-ko keinua)."),
          ("Zona hila", "Atalase batetik behera, motorra geldi geratzen da: lerrokatuta dagoenean robota ez da dardaraka ibiltzen."),
          ("Kontrol proportzionala", "Abiadura (PWM) errorearen araberakoa da: biraketa azkarra argia urrun dagoenean, motelagoa hurbiltzean."),
          ("Potentzia", "H zubi batek mikrokontrolagailua motorraren korrontetik isolatzen du eta biraketa-noranzkoa aldatzea ahalbidetzen du.")],
  learned=["Ideia sinple bat benetan funtzionatzen duen sistema fisiko bihurtzea (zarata, tolerantziak, mekanika).", "Kontrolaren oinarriak: errorea, irabazia, zona hila, egonkortasuna.", "Kontrol-logika eta potentzia-etapa garbiki bereiztea."])

TR["eu"]["object-detection-gpu"] = dict(
  tagline="Mugitzen diren objektuen detekzioa hondoaren kenketaren bidez: CPUa baino 30-41 aldiz azkarragoa den CUDA GStreamer iragazkia.", domain="Ikusmena · GPU",
  tags=["CUDA", "C++20", "GStreamer", "Nsight", "CMake"],
  facts=[("Lengoaia", "C++ / CUDA"), ("Emaitza", "×30-×41 CPUaren aldean (1080p)"), ("Profilatzea", "Nsight Systems"), ("Mota", "Talde-proiektua (4)")],
  context="""<p>GPGPU proiektua EPITAn, lau lagunen taldean: bideo-jario batean hondoa eta objektu mugikorrak bereizten dituen CUDA GStreamer iragazki bat idaztea, eta mugitzen diren pixelak gorriz erakustea. Bideo-prozesatze kate askoren aurreko urratsa da.</p>
<p>Lehenik CPU erreferentziazko bertsio bat idatzi genuen, gero GPU eramate sinple bat, eta zortzi urratsetan optimizatu (v1.1.0 → v1.1.8). Urrats bakoitza Nsight Systems-ekin neurtu zen hurrengoa aukeratu aurretik.</p>""",
  pipeline=["Bideo-irudia", "Hondoaren estimazioa (erreserbak)", "Maskara max(|I − B|)", "Irekiera (higadura + dilatazioa)", "Histeresia", "Gain gorria"],
  pipeline_caption="Iragazkiaren katea; urrats bakoitza CUDA kernel bat edo gehiago da.",
  points=[("Hondoaren estimazioa", "Pixel bakoitzak k kolore hautagai pisutu gordetzen ditu (erreserba), cuRAND zozketa aleatorioekin eguneratuak; pisu handieneko kolorea da hondoa."),
          ("Maskara eta histeresia", "RGB kanaletako alderik handiena, eta ondoren atalase baxua / altua: erdiko pixel bat atalase altuko pixel batekin konektatuta badago soilik mantentzen da."),
          ("Histeresia memoria partekatuan", "Lauza baten barruan hedapena egonkortu arte __syncthreads_or-ekin, gero bloke inaktiboak saltatuz: irudiko 172 abiarazletik 11ra inguru, histeresia 12,7 ms-tik 0,55 ms-ra."),
          ("Irekiera banagarria", "Leiho karratu baten min / max-a pasaldi horizontal eta bertikal bihurtzen da: pixeleko 81 irakurketa 18ra, eta gero memoria partekatuko kernel bakar batean batuta, ertzarekin."),
          ("Datuak GPUan geratzen dira", "Irudia eta hondoa GPUaren memorian daude, bufferrak behin esleituta, maskara float ordez uint8_t, eta erreserba array-egitura gisa sarbide jarraituetarako."),
          ("Benchmark zintzoa", "Hiru bideo, parametro berdinak, makina bera. v1.1.3-tik aurrera kalkulua irudiko 14,6 ms-tik ~2,4 ms baino ez da: deskodetzeak eta transferentziek menderatzen dute.")],
  learned=["Algoritmo bat paralelismo masiboaren ikuspegitik pentsatzea.", "Optimizatu aurretik profilatu: lehenik kopiak optimizatu genituen (1,3 ms) histeresiak 12,7 ms kostatzen zuenean.", "Emaitza bat zintzotasunez irakurtzea: optimizazio bat neutroa izan daiteke (v1.1.4) eta kodearen argitasunagatik mantentzea merezi du."])

TR["eu"]["deriscage-esp32"] = dict(
  title="Dérisquage ESP32an",
  tagline="Mugimenduaren estimazioa IMU bidez: Madgwick iragazkia + ZUPT zuzenketa, ESP32an.", domain="Sistema txertatuak",
  tags=["ESP32", "ESP-IDF", "FreeRTOS", "MPU6050", "I²C", "Sentsore-fusioa"],
  facts=[("Txartela", "ESP32"), ("Lan-markoa", "ESP-IDF · FreeRTOS"), ("Sentsorea", "MPU6050 (azelerometroa + giroskopioa)"), ("Algoritmoak", "Madgwick · ZUPT")],
  context="""<p>MPU6050 batek 3 ardatzeko azelerazioak eta abiadura angeluarrak ematen ditu. Teorian, azelerazioa bi aldiz integratzea nahikoa da posizioa lortzeko. Praktikan, alborapenik txikiena ere lehertu egiten da: segundo gutxiren buruan posizioa hainbat metro desbideratzen da.</p>
<p>Proiektu honek bi teknika uztartzen ditu estimazioa erabilgarria izan dadin: <strong>Madgwick iragazkia</strong>, sentsorearen orientazioa ezagutzeko, eta <strong>ZUPT</strong> zuzenketa (Zero Velocity Update), sentsorea geldi dagoen bakoitzean abiadura zerora itzultzeko.</p>""",
  pipeline=["MPU6050", "I²C irakurketa", "Alborapenen kalibrazioa", "Madgwick iragazkia", "Azel. munduko erreferentzian", "− grabitatea", "∫ abiadura", "Geldiune-detekzioa", "ZUPT: v = 0", "∫ posizioa"],
  pipeline_caption="ESP32an denbora errealean exekutatzen den prozesamendu-katea.",
  points=[("I²C driverra", "MPU6050arekiko komunikazioa ESP-IDFren I²C APIaren bidez: tarteen konfigurazioa (±g, °/s) eta erregistroen irakurketa jarraitua."),
          ("FreeRTOS atazak", "Maiztasun finkoko eskuratze-ataza bat eta prozesamendu-ataza bat; ilara baten bidez trukatzen dituzte datuak, laginketa erregularra bermatzeko."),
          ("Madgwick iragazkia", "Giroskopioaren eta azelerometroaren fusioa, orientazio-kuaternioi baten gaineko gradiente-jaitsieraren bidez, β parametroaz doitua."),
          ("Munduko erreferentzia", "Azelerazioa Lurraren erreferentzia-sistemara biratzen da kuaternioiari esker, eta grabitatea kentzen zaio azelerazio lineala soilik gordetzeko."),
          ("Geldiune-detekzioa", "Leiho irristakor batean: azelerazioaren norma g-tik hurbil eta biraketa ia nulua → sentsorea geldi dagoela jotzen da."),
          ("ZUPT zuzenketa", "Geldiune bakoitzean abiadura zerora behartzen da: metatutako errorea mozten da eta posizioaren desbideratzea mugatuta geratzen da.")],
  learned=["ESP-IDFrekin garatzea eta denbora errealeko aplikazio bat FreeRTOSekin egituratzea.", "Sentsore-fusioa eta kostu baxuko IMU baten muga fisikoak ulertzea.", "Desbideratze bat aurretiazko ezagutzaren bidez zuzentzea (hemen: geldiuneak)."])

TR["eu"]["pcb-snake"] = dict(
  tagline="Snake kontsola bat PCB propioan: mikrokontrolagailua eta charlieplexing bidezko LED matrizea.", domain="Elektronika",
  tags=["PCB", "KiCad", "Mikrokontrolagailua", "Charlieplexing", "C"],
  facts=[("Diseinua", "Eskema + PCB bideratzea"), ("Pantaila", "Charlieplexing LEDak"), ("Firmwarea", "C txertatua"), ("Mota", "Hardware-proiektu osoa")],
  context="""<p>Helburua: Snake jokoa exekutatzen duen kontsola txiki bat hutsetik diseinatzea — eskema elektronikoa, PCBaren bideratzea, soldadura, eta ondoren jokoaren firmwarea.</p>
<p>Erronka interesgarria: LED asko pin gutxirekin gidatzea. Hor sartzen da <strong>charlieplexing</strong>-a, GPIOen inpedantzia altuko egoera baliatzen duena <code>n × (n − 1)</code> LED <code>n</code> pin bakarrik erabiliz helbideratzeko.</p>""",
  pipeline=["Eskema", "Aztarnak", "PCB bideratzea", "Fabrikazioa", "Soldadura", "Firmwarea", "Snake jokoa"],
  pipeline_caption="Eskematik kontsola funtzionalera.",
  points=[("Charlieplexing", "LED bat pizteko, pin bat 1era jartzen da, beste bat 0ra, eta gainerako guztiak sarrera gisa (inpedantzia altua). 9 pinekin: 9 × 8 = 72 LED helbideragarri, 8 × 8 sare baterako nahikoa."),
          ("Ekorketa", "LED bakarra (edo lerro bakarra) pizten da aldi berean, baina ekorketa nahikoa azkarra da ikusmenaren iraunkortasunak irudi egonkorra erakusteko."),
          ("Bideratzea", "Charlieplexing-aren kableatua trinkoa eta ez oso intuitiboa da: LEDen kokapenak eta pisten bideratzeak arreta berezia eskatu dute."),
          ("Sarrerak", "Norabide-botoiak, software bidezko errebote-iragazkiarekin, freskatze-zikloen artean irakurriak."),
          ("Jokoaren logika", "Sugea buffer zirkular batean gordeta, sagarraren sorrera, talken detekzioa eta abiaduraren igoera mailakatua."),
          ("Elikadura", "Korronte-mugatzeko erresistentzien eta elikaduraren dimentsionamendua, distira homogeneoa lortzeko.")],
  learned=["PCB oso bat diseinatzea, eskematik soldatutako produktura arte.", "Pinak aurrezten dituen multiplexazio-teknika dotorea.", "Hardware-mugen eta software-arkitekturaren arteko lotura oso zehatza."])

TR["eu"]["cpu-monocycle"] = dict(
  title="Ziklo bakarreko CPUa",
  tagline="VHDLz deskribatutako ARM motako 32 biteko ziklo bakarreko prozesadorea, simulazioan balioztatua eta MAX 10 txartel baterako pentsatua.", domain="Arkitektura · FPGA",
  tags=["VHDL", "Arkitektura", "ModelSim", "Quartus", "FPGA"],
  facts=[("Lengoaia", "VHDL"), ("Agindu-multzoa", "ARM 32 biteko azpimultzoa"), ("Helburua", "DE10-Lite (MAX 10)"), ("Egiaztapena", "Testbench bat bloke bakoitzeko")],
  context="""<p>Ziklo bakarreko prozesadore batek agindu bakoitza — bilaketa, deskodetzea, exekuzioa, memoria-sarbidea, idazketa — erloju-ziklo bakar batean exekutatzen du. Arrazoitzeko arkitekturarik sinpleena da, eta ondoren pipeline-a ulertzeko oinarria.</p>
<p>Bi urratsetan egindako proiektuak datu-bideko bloke bakoitza VHDLz deskribatzen du bere proba unitarioekin, agindu-deskodetzaile batekin elkartzen ditu, eta gero benetako programa bat exekutatzen du mihiztadura-lengoaian. Quartus proiektuak DE10-Lite txartel bat du helburu, emaitza 7 segmentuko pantailetan erakutsiz.</p>""",
  pipeline=["PC + agindu-memoria", "Deskodetzailea", "Erregistro-bankua", "Zeinu-hedapena", "ALU", "Datu-memoria", "Idazketa (write-back)"],
  pipeline_caption="Ziklo bakarreko prozesadorearen datu-bidea.",
  points=[("ALU", "Lau eragiketa (A + B, A − B, A, B) eta bi adierazle, N (negatiboa) eta Z (nulua), egoera-erregistro batean gordeak."),
          ("Erregistro-bankua", "32 biteko 16 erregistro, bi irakurketa-ataka asinkrono eta idazketa-ataka bat, erloju-ertzean sinkronoa."),
          ("Deskodetzailea", "MOV, ADD (erregistroa edo berehalakoa), CMP, LDR, STR, B eta BLT ezagutzen ditu ARM baldintza, mota eta opcode eremuetatik, eta bederatzi kontrol-seinale sortzen ditu."),
          ("Memoria bereiziak", "64 hitz aginduentzat, 64 hitz datuentzat (Harvard). Proba-programak memoriako array bat batzen du LDR / ADD / CMP / BLT begizta batekin."),
          ("PCaren kudeaketa", "PC + 1 edo zeinuz hedatutako 24 biteko desplazamendu batetik jauzi erlatiboa; BLT-k N adierazlea altxatuta dagoenean soilik egiten du jauzi."),
          ("Egiaztapena", "Testbench eta ModelSim script bat bloke bakoitzeko (ALU, mux, hedatzailea, erregistroak, memoria, deskodetzailea, PC unitatea), eta gero prozesadore osoarentzat.")],
  learned=["Hardwarean pentsatzea: konkurrentzia, seinaleak, denbora, agindu-sekuentzia baten ordez.", "32 biteko hitz bat kontrol-seinale bihurtzen den modua zehazki ulertzea.", "Bloke bakoitza bakarka eta gero integrazioan balioztatzea, dena elkartu aurretik."])
