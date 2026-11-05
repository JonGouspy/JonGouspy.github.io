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
    ("// en g", "// in g"), ("// en rad/s", "// in rad/s"), ("// retire la gravité", "// remove gravity"),
    ("// Allume la LED reliée entre la broche `hi` (anode) et `lo` (cathode)", "// Turn on the LED between pin `hi` (anode) and `lo` (cathode)"),
    ("// toutes les broches en haute impédance", "// all pins high-impedance"),
    ("// seules hi et lo deviennent des sorties", "// only hi and lo become outputs"),
    ("// hi = 1, lo = 0 -> courant dans la LED", "// hi = 1, lo = 0 -> current through LED"),
    ("// rafraîchissement de l'écran", "// display refresh"),
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
  tagline="Moving-object detection through background subtraction, GPU-accelerated.", domain="Vision · GPU",
  tags=["CUDA", "C++", "Image processing", "Parallelism"],
  facts=[("Language", "C++ / CUDA"), ("Method", "Background subtraction"), ("Target", "NVIDIA GPU"), ("Type", "Performance project")],
  context="""<p>In a video shot by a fixed camera, anything that isn't part of the scenery is an object of interest. The idea: learn a model of the background, then isolate, in each frame, the pixels that deviate from it.</p>
<p>Since the computation is independent for each pixel, it's a perfect fit for the GPU. The project consists of writing a reference CPU version, porting it to CUDA kernels and measuring the speed-up.</p>""",
  pipeline=["Video frame", "Background model", "Difference |I − B|", "Thresholding (hysteresis)", "Morphology (opening)", "Connected components", "Bounding boxes"],
  pipeline_caption="Detection pipeline, each stage being one or more CUDA kernels.",
  points=[("Background model", "Background estimated and updated over the video (running average) to adapt to slow lighting changes."),
          ("Motion mask", "Distance between the current frame and the background, then hysteresis thresholding: a high threshold to seed, a low one to propagate."),
          ("Morphology", "Erosion then dilation to remove isolated noise and fill holes in objects."),
          ("One thread per pixel", "Each kernel maps one thread to one pixel; 2D grids and coalesced memory accesses."),
          ("Shared memory", "Neighborhood operations (morphology) load a tile plus its halo into shared memory to avoid re-reading global memory."),
          ("Benchmark", "CPU vs GPU comparison and profiling (Nsight) to identify bandwidth-bound kernels.")],
  learned=["Thinking about an algorithm in terms of massive parallelism.", "The huge impact of memory access patterns on GPU performance.", "Measure before optimizing: profile, compare, iterate."])

TR["en"]["deriscage-esp32"] = dict(
  title="Dériscage on ESP32",
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
  tagline="A single-cycle processor described in VHDL: every instruction executes in one clock cycle.", domain="Architecture · FPGA",
  facts=[("Language", "VHDL"), ("Architecture", "Single-cycle"), ("Verification", "Testbenches / simulation"), ("Type", "Digital design")],
  context="""<p>A single-cycle processor executes each whole instruction — fetch, decode, execute, memory access, write-back — in one clock cycle. It's the simplest architecture to reason about, and the foundation for understanding pipelining later on.</p>
<p>The project consists of describing each datapath block in VHDL, wiring them together with a control unit, then validating everything in simulation on real programs.</p>""",
  pipeline=["PC", "Instruction memory", "Decoder / Control", "Register file", "Sign extension", "ALU", "Data memory", "Write-back"],
  pipeline_caption="Datapath of the single-cycle processor.",
  points=[("ALU", "Arithmetic and logic operations, with flags (N, Z, C, V) used for conditional branches."),
          ("Register file", "Two asynchronous read ports, one write port synchronous on the clock edge."),
          ("Control unit", "Decodes the opcode into control signals: mux selection, register / memory write, ALU operation."),
          ("Memories", "Instruction memory initialized with the program, separate data memory (Harvard architecture)."),
          ("PC logic", "Increment, relative branches and jumps, selected by a multiplexer based on the flags."),
          ("Verification", "One testbench per entity, then a global testbench that runs a program and checks the registers at the end of execution.")],
  learned=["Thinking in hardware: concurrency, signals, timing, rather than a sequence of instructions.", "Understanding concretely how an instruction turns into electrical signals.", "The importance of simulation-based verification before any synthesis."])

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
  tagline="Mugitzen diren objektuen detekzioa hondoaren kenketaren bidez, GPUan azeleratua.", domain="Ikusmena · GPU",
  tags=["CUDA", "C++", "Irudi-prozesamendua", "Paralelismoa"],
  facts=[("Lengoaia", "C++ / CUDA"), ("Metodoa", "Hondoaren kenketa"), ("Helburua", "NVIDIA GPUa"), ("Mota", "Errendimendu-proiektua")],
  context="""<p>Kamera finko batek grabatutako bideo batean, dekoratuaren parte ez den guztia objektu interesgarria da. Ideia: hondoaren eredu bat ikastea, eta ondoren irudi bakoitzean hartatik aldentzen diren pixelak isolatzea.</p>
<p>Kalkulua pixel bakoitzerako independentea denez, ezin hobeto egokitzen zaio GPUari. Proiektuan CPU erreferentziazko bertsio bat idatzi, CUDA kernel-etara eraman eta irabazia neurtzen da.</p>""",
  pipeline=["Bideo-irudia", "Hondoaren eredua", "Aldea |I − B|", "Atalasea (histeresia)", "Morfologia (irekiera)", "Osagai konexuak", "Muga-kutxak"],
  pipeline_caption="Detekzio-katea; urrats bakoitza CUDA kernel bat edo gehiago da.",
  points=[("Hondoaren eredua", "Hondoa bideoan zehar estimatu eta eguneratzen da (batez besteko mugikorra), argiztapenaren aldaketa geldoetara egokitzeko."),
          ("Mugimendu-maskara", "Uneko irudiaren eta hondoaren arteko distantzia, eta ondoren histeresidun atalasea: atalase altua abiatzeko, baxua hedatzeko."),
          ("Morfologia", "Higadura eta ondoren dilatazioa, zarata isolatua kentzeko eta objektuetako zuloak betetzeko."),
          ("Hari bat pixel bakoitzeko", "Kernel bakoitzak hari bat lotzen dio pixel bakoitzari; 2D sareak eta memoria-sarbide bateratuak."),
          ("Memoria partekatua", "Auzo-eragiketek (morfologia) lauza bat eta haren ertza memoria partekatuan kargatzen dituzte, memoria globala berriro ez irakurtzeko."),
          ("Benchmarka", "CPU eta GPU arteko konparazioa eta profilatzea (Nsight), banda-zabaleraren mende dauden kernelak identifikatzeko.")],
  learned=["Algoritmo bat paralelismo masiboaren ikuspegitik pentsatzea.", "Memoria-sarbideek GPUaren errendimenduan duten eragin izugarria.", "Optimizatu aurretik neurtu: profilatu, konparatu, iteratu."])

TR["eu"]["deriscage-esp32"] = dict(
  title="Dériscage ESP32an",
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
  tagline="VHDLz deskribatutako ziklo bakarreko prozesadorea: agindu bakoitza erloju-ziklo bakar batean exekutatzen da.", domain="Arkitektura · FPGA",
  tags=["VHDL", "Arkitektura", "ALU", "Simulazioa", "FPGA"],
  facts=[("Lengoaia", "VHDL"), ("Arkitektura", "Ziklo bakarrekoa"), ("Egiaztapena", "Testbench-ak / simulazioa"), ("Mota", "Diseinu digitala")],
  context="""<p>Ziklo bakarreko prozesadore batek agindu bakoitza osorik — bilaketa, deskodetzea, exekuzioa, memoria-sarbidea, idazketa — erloju-ziklo bakar batean exekutatzen du. Arrazoitzeko arkitekturarik sinpleena da, eta ondoren pipeline-a ulertzeko oinarria.</p>
<p>Proiektuan datu-bideko bloke bakoitza VHDLz deskribatu, kontrol-unitate batekin elkartu eta dena simulazioan balioztatzen da benetako programekin.</p>""",
  pipeline=["PC", "Agindu-memoria", "Deskodetzailea / Kontrola", "Erregistro-bankua", "Zeinu-hedapena", "ALU", "Datu-memoria", "Idazketa (write-back)"],
  pipeline_caption="Ziklo bakarreko prozesadorearen datu-bidea.",
  points=[("ALU", "Eragiketa aritmetiko eta logikoak, eta baldintzapeko jauzietarako erabiltzen diren adierazleak (N, Z, C, V)."),
          ("Erregistro-bankua", "Bi irakurketa-ataka asinkrono eta idazketa-ataka bat, erloju-ertzean sinkronoa."),
          ("Kontrol-unitatea", "Opcode-a kontrol-seinaletan deskodetzea: multiplexoreen hautaketa, erregistro / memoria idazketa, ALU eragiketa."),
          ("Memoriak", "Programarekin hasieratutako agindu-memoria eta datu-memoria bereizia (Harvard arkitektura)."),
          ("PCaren kudeaketa", "Inkrementua, jauzi erlatiboak eta saltoak, adierazleen arabera multiplexore batek hautatuak."),
          ("Egiaztapena", "Testbench bat entitate bakoitzeko, eta ondoren testbench global bat, programa bat exekutatu eta amaieran erregistroak egiaztatzen dituena.")],
  learned=["Hardwarean pentsatzea: konkurrentzia, seinaleak, denbora, agindu-sekuentzia baten ordez.", "Agindu bat seinale elektriko bihurtzen den modua zehazki ulertzea.", "Simulazio bidezko egiaztapenaren garrantzia edozein sintesi egin aurretik."])
