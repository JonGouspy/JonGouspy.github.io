#!/usr/bin/env python3
"""Generates the static portfolio (GitHub Pages) in ./site"""
import html, os

NAME = "Jon Gouspy"
GITHUB = "https://github.com/jon-gouspy"
EMAIL = "jon.gouspy@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/jon-gouspy-futur-ingenieur"

OUT = "site"

PROJECTS = [
  dict(
    slug="tiger-compiler", num="01", title="Tiger Compiler",
    tagline="Un compilateur complet pour le langage Tiger, écrit en C++.",
    domain="Compilation", tags=["C++", "Flex", "Bison", "AST", "IR"],
    facts=[("Langage", "C++17"), ("Outils", "Flex · Bison · Make"), ("Cible", "Assembleur / IR"), ("Type", "Projet d'équipe")],
    context="""<p>Tiger est un petit langage impératif typé, issu du livre <em>Modern Compiler Implementation</em> d'Andrew Appel. Il possède des types structurés (records, tableaux), des fonctions imbriquées, des portées lexicales et une gestion explicite de <code>let … in … end</code>.</p>
<p>L'objectif : partir d'un fichier source <code>.tig</code> et produire du code exécutable, en traversant toutes les étapes d'un vrai compilateur — de l'analyse lexicale jusqu'à l'allocation de registres.</p>""",
    pipeline=["Source .tig", "Lexer (Flex)", "Parser (Bison)", "AST", "Binding", "Type-checking", "Traduction IR", "Canonisation", "Sélection d'instructions", "Allocation de registres", "Assembleur"],
    pipeline_caption="Chaîne de compilation, du texte source au code machine.",
    points=[
      ("Analyse lexicale & syntaxique", "Scanner Flex et grammaire Bison, avec gestion des conflits, des priorités d'opérateurs et des messages d'erreur localisés (ligne / colonne)."),
      ("AST & visiteurs", "Arbre syntaxique abstrait en C++ parcouru via le design pattern Visitor : pretty-printer, binder, type-checker et traducteur partagent la même hiérarchie."),
      ("Liaison des noms", "Résolution des identifiants avec tables de symboles à portées imbriquées, détection des variables qui « s'échappent » vers des fonctions internes."),
      ("Vérification de types", "Typage des expressions, des records récursifs et des tableaux ; erreurs sémantiques claires plutôt qu'un crash."),
      ("Représentation intermédiaire", "Traduction en arbre IR, linéarisation et canonisation des blocs de base avant la génération de code."),
      ("Back-end", "Sélection d'instructions par tuilage de motifs, analyse de vivacité et allocation de registres par coloration de graphe."),
    ],
    code_lang="Tiger", code="""let
  type intlist = { head: int, tail: intlist }
  function sum(l: intlist): int =
    if l = nil then 0
    else l.head + sum(l.tail)
  var l := intlist { head = 1,
           tail = intlist { head = 2, tail = nil } }
in
  print_int(sum(l))
end""",
    learned=["Comprendre ce qui se passe réellement entre le code source et le binaire.", "Concevoir une grosse base de code C++ modulaire et testable (suites de tests par étape).", "Travailler en équipe sur un projet long avec revues de code et intégration continue."],
  ),
  dict(
    slug="light-tracker", num="02", title="Light Tracker", repo="https://github.com/JonGouspy/light-tracker", image="/img/light-tracker.png",
    tagline="Un robot qui s'oriente tout seul vers la source de lumière la plus intense.",
    domain="Robotique", tags=["Microcontrôleur", "C", "ADC", "Moteur", "Asservissement"],
    facts=[("Capteurs", "2 photorésistances"), ("Actionneur", "Moteur + pont en H"), ("Langage", "C embarqué"), ("Type", "Projet matériel")],
    context="""<p>Le principe est simple : deux capteurs de lumière placés de part et d'autre du robot mesurent l'intensité lumineuse. Si un côté reçoit plus de lumière que l'autre, le moteur tourne pour rééquilibrer — le robot finit pointé vers la source.</p>
<p>Derrière cette simplicité : acquisition analogique, filtrage du bruit, zone morte pour éviter les oscillations et pilotage d'un moteur dans les deux sens.</p>""",
    pipeline=["Capteur gauche", "Capteur droit", "Diviseurs de tension", "ADC", "Filtrage", "Erreur = G − D", "Commande", "Pont en H", "Moteur"],
    pipeline_caption="Boucle de contrôle : de la mesure de lumière à la rotation du moteur.",
    points=[
      ("Acquisition", "Chaque photorésistance forme un pont diviseur ; la tension est lue par le convertisseur analogique-numérique du microcontrôleur."),
      ("Calibration", "Les deux capteurs n'ont jamais exactement la même réponse : un offset mesuré au démarrage compense l'écart."),
      ("Filtrage", "Moyenne glissante sur plusieurs échantillons pour lisser le bruit (néons, scintillement 50 Hz)."),
      ("Zone morte", "En dessous d'un seuil d'écart, le moteur reste à l'arrêt : le robot ne « tremble » pas une fois aligné."),
      ("Commande proportionnelle", "La vitesse (PWM) dépend de l'écart : rotation rapide quand la lumière est loin, ralentissement à l'approche."),
      ("Puissance", "Un pont en H isole le microcontrôleur du courant moteur et permet d'inverser le sens de rotation."),
    ],
    code_lang="C", code="""// TIM2 : interruption périodique qui cadence les mesures
void initTimer(void)
{
    __TIM2_CLK_ENABLE();

    gTimHandle.Instance = TIM2;
    gTimHandle.Init.Period = 1000 - 1;
    gTimHandle.Init.Prescaler = (90000000 / 40000000) - 1;
    gTimHandle.Init.CounterMode = TIM_COUNTERMODE_UP;
    HAL_TIM_Base_Init(&gTimHandle);

    __HAL_TIM_ENABLE_IT(&gTimHandle, TIM_IT_UPDATE);
    HAL_NVIC_SetPriority(TIM2_IRQn, 0, 0);
    HAL_NVIC_EnableIRQ(TIM2_IRQn);
    HAL_TIM_Base_Start_IT(&gTimHandle);
}

// ADC1, canal 11 (PC1) : conversions lues par interruption
void initADC(void)
{
    GPIO_InitStruct.Pin  = GPIO_PIN_1;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;   // PC1 en entrée analogique
    HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

    HAL_NVIC_SetPriority(ADC_IRQn, 5, 0);
    HAL_NVIC_EnableIRQ(ADC_IRQn);

    gAdcHandle.Instance = ADC1;
    gAdcHandle.Init.Resolution = ADC_RESOLUTION_12B;
    gAdcHandle.Init.ExternalTrigConv = ADC_EXTERNALTRIGCONV_T2_TRGO;  // TIM2 déclenche la conversion
    HAL_ADC_Init(&gAdcHandle);

    ADC_ChannelStruct.Channel = ADC_CHANNEL_11;
    ADC_ChannelStruct.SamplingTime = ADC_SAMPLETIME_480CYCLES;  // temps d'échantillonnage maximal
    HAL_ADC_ConfigChannel(&gAdcHandle, &ADC_ChannelStruct);

    HAL_ADC_Start_IT(&gAdcHandle);
}""",
    learned=["Passer d'une idée simple à un système physique qui marche vraiment (bruit, tolérances, mécanique).", "Les bases de l'asservissement : erreur, gain, zone morte, stabilité.", "Séparer proprement la logique de commande et l'étage de puissance."],
  ),
  dict(
    slug="object-detection-gpu", num="03", title="Object Detection GPU", repo="https://github.com/JonGouspy/gpgpu",
    tagline="Détection d'objets en mouvement par soustraction de fond : un filtre GStreamer CUDA, 30 à 41× plus rapide que le CPU.",
    domain="Vision · GPU", tags=["CUDA", "C++20", "GStreamer", "Nsight", "CMake"],
    facts=[("Langage", "C++ / CUDA"), ("Résultat", "×30 à ×41 vs CPU (1080p)"), ("Profilage", "Nsight Systems"), ("Type", "Projet de groupe (4)")],
    context="""<p>Projet GPGPU à l'EPITA, en groupe de quatre : écrire un filtre GStreamer CUDA qui sépare le fond des objets mobiles dans un flux vidéo, puis affiche les pixels en mouvement en rouge. C'est une étape préliminaire de nombreuses chaînes de traitement vidéo.</p>
<p>Nous avons d'abord écrit une version CPU de référence, puis un portage GPU naïf, que nous avons optimisé en huit étapes (v1.1.0 → v1.1.8). Chaque étape a été mesurée avec Nsight Systems avant d'en choisir la suivante.</p>""",
    pipeline=["Frame vidéo", "Estimation du fond (réservoirs)", "Masque max(|I − B|)", "Ouverture (érosion + dilatation)", "Hystérésis", "Surbrillance rouge"],
    pipeline_caption="Pipeline du filtre, chaque étape étant un ou plusieurs kernels CUDA.",
    points=[
      ("Estimation du fond", "Chaque pixel garde k couleurs candidates pondérées (réservoir), mises à jour par tirage aléatoire cuRAND ; la couleur de plus fort poids est le fond."),
      ("Masque et hystérésis", "Écart maximal sur les canaux RGB, puis seuil bas / seuil haut : un pixel moyen n'est retenu que s'il est connecté à un pixel fort."),
      ("Hystérésis en mémoire partagée", "Propagation dans une tuile jusqu'à stabilité avec __syncthreads_or, puis saut des blocs inactifs : de 172 lancements par frame à environ 11, hystérésis de 12,7 à 0,55 ms."),
      ("Ouverture séparable", "Un min / max sur fenêtre carrée devient un passage horizontal puis vertical : 81 lectures par pixel ramenées à 18, puis fusionné en un kernel en mémoire partagée avec halo."),
      ("Données sur le GPU", "Frame et fond restent en mémoire GPU, buffers alloués une seule fois, masque en uint8_t au lieu de float, et réservoir en structure de tableaux pour des accès contigus."),
      ("Benchmark honnête", "Trois vidéos, mêmes paramètres, même machine. Au-delà de v1.1.3 le calcul ne pèse plus que ~2,4 ms sur 14,6 ms par frame : le décodage et les transferts dominent."),
    ],
    code_lang="CUDA", code="""// Un thread par pixel : écart maximal sur les trois canaux entre l'image et le fond
__global__ void mask_kernel(ImageView<rgb8> in, ImageView<rgb8> bg,
                            ImageView<uint8_t> mask)
{
    const int x = blockDim.x * blockIdx.x + threadIdx.x;
    const int y = blockDim.y * blockIdx.y + threadIdx.y;

    if (x >= in.width || y >= in.height)
        return;

    const int dr = std::abs(int(in.at(x, y).r) - int(bg.at(x, y).r));
    const int dg = std::abs(int(in.at(x, y).g) - int(bg.at(x, y).g));
    const int db = std::abs(int(in.at(x, y).b) - int(bg.at(x, y).b));

    mask.at(x, y) = max(dr, max(dg, db));
}""",
    learned=["Penser un algorithme en termes de parallélisme massif.", "Profiler avant d'optimiser : nous avions d'abord optimisé les copies (1,3 ms) alors que l'hystérésis en coûtait 12,7.", "Lire un résultat sans se mentir : une optimisation peut être neutre (v1.1.4) et rester utile pour la clarté du code."],
  ),
  dict(
    slug="deriscage-esp32", num="04", title="Dérisquage sur ESP32", repo="https://github.com/JonGouspy/gap",
    tagline="Estimation de mouvement par IMU : filtre de Madgwick + correction ZUPT, sur ESP32.",
    domain="Systèmes embarqués", tags=["ESP32", "ESP-IDF", "FreeRTOS", "MPU6050", "I²C", "Fusion de capteurs"],
    facts=[("Carte", "ESP32"), ("Framework", "ESP-IDF · FreeRTOS"), ("Capteur", "MPU6050 (accéléro + gyro)"), ("Algorithmes", "Madgwick · ZUPT")],
    context="""<p>Un MPU6050 fournit des accélérations et des vitesses angulaires sur 3 axes. En théorie, il suffit d'intégrer deux fois l'accélération pour obtenir la position. En pratique, le moindre biais explose : après quelques secondes la position dérive de plusieurs mètres.</p>
<p>Ce projet combine deux techniques pour rendre l'estimation exploitable : le <strong>filtre de Madgwick</strong> pour connaître l'orientation du capteur, et la correction <strong>ZUPT</strong> (Zero Velocity Update) pour remettre la vitesse à zéro dès que le capteur est immobile.</p>""",
    pipeline=["MPU6050", "Lecture I²C", "Calibration des biais", "Filtre de Madgwick", "Accél. repère monde", "− gravité", "∫ vitesse", "Détection immobilité", "ZUPT : v = 0", "∫ position"],
    pipeline_caption="Chaîne de traitement exécutée en temps réel sur l'ESP32.",
    points=[
      ("Driver I²C", "Communication avec le MPU6050 via l'API I²C d'ESP-IDF : configuration des plages (±g, °/s), lecture en rafale des registres."),
      ("Tâches FreeRTOS", "Une tâche d'acquisition à fréquence fixe, une tâche de traitement ; échange par file (queue) pour un échantillonnage régulier."),
      ("Filtre de Madgwick", "Fusion gyro + accéléromètre par descente de gradient sur un quaternion d'orientation, réglée par le paramètre β."),
      ("Repère monde", "L'accélération est tournée dans le repère terrestre grâce au quaternion, puis la gravité est soustraite pour garder l'accélération linéaire."),
      ("Détection d'immobilité", "Sur une fenêtre glissante : norme de l'accélération proche de g et rotation quasi nulle → le capteur est considéré à l'arrêt."),
      ("Correction ZUPT", "À chaque phase d'arrêt, la vitesse est forcée à zéro : l'erreur accumulée est coupée, la dérive de position reste bornée."),
    ],
    code_lang="C", code="""// Mise à jour de Kalman : mesure virtuelle « vitesse = 0 »
void axis_zupt(float *p, float *v, matrix2x2_t *cov_matrix)
{
    float y = -(*v);
    float S = cov_matrix->x4 + ZUPT_R;
    float K0 = cov_matrix->x2 / S;
    float K1 = cov_matrix->x4 / S;
    *p += K0 * y;
    *v += K1 * y;
    cov_matrix->x1 -= K0 * cov_matrix->x3;
    cov_matrix->x2 -= K0 * cov_matrix->x4;
    cov_matrix->x3 -= K1 * cov_matrix->x2;
    cov_matrix->x4 -= K1 * cov_matrix->x4;
}

void position_update(inertial_state_t *data, float dt)
{
    vec3_t a_body = {data->mpu_data.acc.x, data->mpu_data.acc.y, data->mpu_data.acc.z};
    vec3_t a_world;
    quaternion_rotate_to_world(&data->quat, &a_body, &a_world);
    a_world.z -= GRAVITY;                         // retire la gravité

    // amag, gmag : normes de l'accélération et du gyroscope
    // Immobile : accélération ≈ g et rotation quasi nulle, ZUPT_WINDOW échantillons de suite
    if (fabsf(amag - GRAVITY) < ZUPT_ACCEL_TOL && gmag < ZUPT_GYRO_TOL)
        data->zupt_count++;
    else
        data->zupt_count = 0;
    data->zupt_active = (data->zupt_count >= ZUPT_WINDOW);

    // prédiction : intégration de l'accélération (idem pour y et z)
    axis_predict(&data->relative_pos.x, &data->velocity.x, &data->covariance[0], a_world.x, dt);

    // à l'arrêt : correction de Kalman (idem pour y et z)
    if (data->zupt_active)
        axis_zupt(&data->relative_pos.x, &data->velocity.x, &data->covariance[0]);
}""",
    learned=["Développer sur ESP-IDF et structurer une application temps réel avec FreeRTOS.", "Comprendre la fusion de capteurs et les limites physiques d'une centrale inertielle bas coût.", "Corriger une dérive par des connaissances a priori (ici : les phases d'arrêt)."],
  ),
  dict(
    slug="pcb-snake", num="05", title="PCB Snake", repo="https://github.com/JonGouspy/Snake",
    tagline="Une console Snake sur PCB maison : microcontrôleur, matrice de LEDs en charlieplexing.",
    domain="Électronique", tags=["PCB", "KiCad", "Microcontrôleur", "Charlieplexing", "C"],
    facts=[("Conception", "Schéma + routage PCB"), ("Affichage", "LEDs en charlieplexing"), ("Firmware", "C embarqué"), ("Type", "Projet matériel complet")],
    context="""<p>Le but : concevoir de A à Z une petite console qui fait tourner Snake — schéma électronique, routage du PCB, soudure, puis firmware du jeu.</p>
<p>La contrainte intéressante : piloter beaucoup de LEDs avec très peu de broches. C'est là qu'intervient le <strong>charlieplexing</strong>, qui exploite l'état haute impédance des GPIO pour adresser <code>n × (n − 1)</code> LEDs avec seulement <code>n</code> broches.</p>""",
    pipeline=["Schéma", "Empreintes", "Routage PCB", "Fabrication", "Soudure", "Firmware", "Jeu Snake"],
    pipeline_caption="Du schéma à la console fonctionnelle.",
    points=[
      ("Charlieplexing", "Pour allumer une LED, une broche est mise à 1, une autre à 0, toutes les autres en entrée (haute impédance). Avec 9 broches : 9 × 8 = 72 LEDs adressables, assez pour une grille 8 × 8."),
      ("Balayage", "Une seule LED (ou une ligne) est allumée à la fois, mais le balayage est assez rapide pour que la persistance rétinienne affiche une image stable."),
      ("Routage", "Le câblage du charlieplexing est dense et peu intuitif : le placement des LEDs et des pistes a demandé un soin particulier."),
      ("Entrées", "Boutons de direction avec anti-rebond logiciel, lus entre deux cycles de rafraîchissement."),
      ("Logique de jeu", "Serpent stocké dans un buffer circulaire, génération de la pomme, détection des collisions et accélération progressive."),
      ("Alimentation", "Dimensionnement des résistances de limitation et de l'alimentation pour une luminosité homogène."),
    ],
    code_lang="C", code="""// Broche « flottante » : entrée sans pull-up ni pull-down (haute impédance)
static void pin_hiz(uint16_t pin)
{
    GPIO_InitTypeDef cfg = {0};
    cfg.Pin  = pin;
    cfg.Mode = GPIO_MODE_INPUT;
    cfg.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOA, &cfg);
}

// Allume une LED : anode à 1, cathode à 0, les autres broches restent flottantes
void light_up(led_info *led)
{
    pin_output(led->anode);
    HAL_GPIO_WritePin(GPIOA, led->anode, GPIO_PIN_SET);

    pin_output(led->cathode);
    HAL_GPIO_WritePin(GPIOA, led->cathode, GPIO_PIN_RESET);
}

// Balayage : une seule LED allumée à la fois, ~1 ms chacune
void print_matrix(const bool number[LED_COUNT])
{
    led_info prev = LEDS[LED_COUNT - 1];

    for (int i = 0; i < LED_COUNT; ++i)
    {
        led_info curr = LEDS[i];

        if (number[i])
        {
            turn_off(&prev);     // éteint la LED précédente
            light_up(&curr);
            prev = curr;
            HAL_Delay(1);        // persistance rétinienne
        }
    }
    turn_off(&prev);
}""",
    learned=["Concevoir un PCB complet, du schéma au produit soudé.", "Une technique de multiplexage élégante qui économise les broches.", "Le lien très concret entre contraintes matérielles et architecture logicielle."],
  ),
  dict(
    slug="cpu-monocycle", num="06", title="CPU Monocycle", repo="https://github.com/JonGouspy/cpu-monocycle",
    tagline="Un processeur 32 bits monocycle de type ARM décrit en VHDL, validé en simulation et prévu pour une carte MAX 10.",
    domain="Architecture · FPGA", tags=["VHDL", "Architecture", "ModelSim", "Quartus", "FPGA"],
    facts=[("Langage", "VHDL"), ("Jeu d'instructions", "Sous-ensemble ARM 32 bits"), ("Cible", "DE10-Lite (MAX 10)"), ("Vérification", "Un testbench par bloc")],
    context="""<p>Un processeur monocycle exécute chaque instruction — lecture, décodage, exécution, accès mémoire, écriture — en un seul cycle d'horloge. C'est l'architecture la plus simple à raisonner, et la base pour comprendre ensuite le pipeline.</p>
<p>Le projet, réalisé en deux étapes, décrit chaque bloc du chemin de données en VHDL avec ses tests unitaires, les assemble avec un décodeur d'instructions, puis exécute un vrai programme en assembleur. Le projet Quartus cible une carte DE10-Lite, avec le résultat affiché sur des afficheurs 7 segments.</p>""",
    pipeline=["PC + mémoire d'instructions", "Décodeur", "Banc de registres", "Extension de signe", "ALU", "Mémoire de données", "Write-back"],
    pipeline_caption="Chemin de données du processeur monocycle.",
    points=[
      ("ALU", "Quatre opérations (A + B, A − B, A, B) et deux drapeaux, N (négatif) et Z (nul), stockés dans un registre d'état."),
      ("Banc de registres", "16 registres de 32 bits, deux ports de lecture asynchrones, un port d'écriture synchrone sur front d'horloge."),
      ("Décodeur", "Reconnaît MOV, ADD (registre ou immédiat), CMP, LDR, STR, B et BLT à partir de la condition, du type et de l'opcode ARM, et génère neuf signaux de commande."),
      ("Mémoires séparées", "64 mots pour les instructions, 64 mots pour les données (Harvard). Le programme de test somme un tableau en mémoire avec une boucle LDR / ADD / CMP / BLT."),
      ("Gestion du PC", "PC + 1 ou branchement relatif à partir d'un déplacement de 24 bits étendu en signe ; BLT ne branche que si le drapeau N est levé."),
      ("Vérification", "Testbench et script ModelSim pour chaque bloc (ALU, mux, extension, registres, mémoire, décodeur, gestion du PC), puis pour le processeur complet."),
    ],
    code_lang="VHDL", code="""entity DECODER is
    port(
      Instruction : in std_logic_vector(31 downto 0);
      RegPSR      : in std_logic_vector(3 downto 0);
      nPCSel, RegWr, ALUSrc, PSREn, MemWr, WrSrc, RegSel, RegAff : out std_logic;
      ALUCtr      : out std_logic_vector(1 downto 0)
    );
end entity;

-- Signaux de commande de chaque instruction
case current_instr is
  when MOV  => RegWr <= '1'; ALUSrc <= '1'; ALUCtr <= "01";
  when ADDi => RegWr <= '1'; ALUSrc <= '1';
  when ADDr => RegWr <= '1';
  when CMP  => ALUSrc <= '1'; ALUCtr <= "10"; PSREn <= '1';
  when LDR  => RegWr <= '1'; ALUSrc <= '1'; WrSrc <= '1';
  when STR  => ALUSrc <= '1'; MemWr <= '1'; RegSel <= '1'; RegAff <= '1';
  when BAL  => nPCSel <= '1';
  when BLT  => nPCSel <= RegPSR(3);  -- branche si N = 1
  when others => null;
end case;""",
    learned=["Penser en matériel : concurrence, signaux, timing, plutôt qu'en séquence d'instructions.", "Comprendre concrètement comment un mot de 32 bits devient des signaux de commande.", "Valider chaque bloc seul, puis en intégration, avant d'assembler le tout."],
  ),
]

