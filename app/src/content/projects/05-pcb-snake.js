// Project 05: PCB Snake.
// Text is written per language (fr, en, eu). See projects/_template.js for the fields.
export default {
  slug: "pcb-snake",
  num: "05",
  theme: "hardware",
  repo: "https://github.com/JonGouspy/Snake",
  fr: {
    title: "PCB Snake",
    tagline: "Une console Snake sur PCB maison : microcontrôleur, matrice de LEDs en charlieplexing.",
    domain: "Électronique",
    tags: ["PCB", "KiCad", "Microcontrôleur", "Charlieplexing", "C"],
    facts: [
      ["Conception", "Schéma + routage PCB"],
      ["Affichage", "LEDs en charlieplexing"],
      ["Firmware", "C embarqué"],
      ["Type", "Projet matériel complet"],
    ],
    context: `<p>Le but : concevoir de A à Z une petite console qui fait tourner Snake — schéma électronique, routage du PCB, soudure, puis firmware du jeu.</p>
<p>La contrainte intéressante : piloter beaucoup de LEDs avec très peu de broches. C'est là qu'intervient le <strong>charlieplexing</strong>, qui exploite l'état haute impédance des GPIO pour adresser <code>n × (n − 1)</code> LEDs avec seulement <code>n</code> broches.</p>`,
    pipeline: ["Schéma", "Empreintes", "Routage PCB", "Fabrication", "Soudure", "Firmware", "Jeu Snake"],
    pipeline_caption: "Du schéma à la console fonctionnelle.",
    points: [
      ["Charlieplexing", "Pour allumer une LED, une broche est mise à 1, une autre à 0, toutes les autres en entrée (haute impédance). Avec 9 broches : 9 × 8 = 72 LEDs adressables, assez pour une grille 8 × 8."],
      ["Balayage", "Une seule LED (ou une ligne) est allumée à la fois, mais le balayage est assez rapide pour que la persistance rétinienne affiche une image stable."],
      ["Routage", "Le câblage du charlieplexing est dense et peu intuitif : le placement des LEDs et des pistes a demandé un soin particulier."],
      ["Entrées", "Boutons de direction avec anti-rebond logiciel, lus entre deux cycles de rafraîchissement."],
      ["Logique de jeu", "Serpent stocké dans un buffer circulaire, génération de la pomme, détection des collisions et accélération progressive."],
      ["Alimentation", "Dimensionnement des résistances de limitation et de l'alimentation pour une luminosité homogène."],
    ],
    code_lang: "C",
    code: `// Broche « flottante » : entrée sans pull-up ni pull-down (haute impédance)
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
}`,
    learned: [
      "Concevoir un PCB complet, du schéma au produit soudé.",
      "Une technique de multiplexage élégante qui économise les broches.",
      "Le lien très concret entre contraintes matérielles et architecture logicielle.",
    ],
  },
  en: {
    title: "PCB Snake",
    tagline: "A Snake console on a custom PCB: microcontroller and charlieplexed LED matrix.",
    domain: "Electronics",
    tags: ["PCB", "KiCad", "Microcontroller", "Charlieplexing", "C"],
    facts: [
      ["Design", "Schematic + PCB layout"],
      ["Display", "Charlieplexed LEDs"],
      ["Firmware", "Embedded C"],
      ["Type", "Full hardware project"],
    ],
    context: `<p>The goal: design from scratch a small console that runs Snake — schematic, PCB layout, soldering, then the game firmware.</p>
<p>The interesting constraint: driving many LEDs with very few pins. That's where <strong>charlieplexing</strong> comes in: it uses the high-impedance state of GPIOs to address <code>n × (n − 1)</code> LEDs with only <code>n</code> pins.</p>`,
    pipeline: ["Schematic", "Footprints", "PCB layout", "Fabrication", "Soldering", "Firmware", "Snake game"],
    pipeline_caption: "From schematic to a working console.",
    points: [
      ["Charlieplexing", "To light an LED, one pin is driven high, another low, and all others are set as inputs (high impedance). With 9 pins: 9 × 8 = 72 addressable LEDs, enough for an 8 × 8 grid."],
      ["Scanning", "Only one LED (or one row) is on at a time, but scanning is fast enough for persistence of vision to show a stable image."],
      ["Layout", "Charlieplexing wiring is dense and counter-intuitive: LED placement and trace routing required particular care."],
      ["Inputs", "Direction buttons with software debouncing, read between refresh cycles."],
      ["Game logic", "Snake stored in a circular buffer, apple generation, collision detection and progressive speed-up."],
      ["Power", "Sizing of current-limiting resistors and power supply for even brightness."],
    ],
    code_lang: "C",
    code: `// "Floating" pin: input with no pull-up or pull-down (high impedance)
static void pin_hiz(uint16_t pin)
{
    GPIO_InitTypeDef cfg = {0};
    cfg.Pin  = pin;
    cfg.Mode = GPIO_MODE_INPUT;
    cfg.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOA, &cfg);
}

// Turn on an LED: anode high, cathode low, all other pins stay floating
void light_up(led_info *led)
{
    pin_output(led->anode);
    HAL_GPIO_WritePin(GPIOA, led->anode, GPIO_PIN_SET);

    pin_output(led->cathode);
    HAL_GPIO_WritePin(GPIOA, led->cathode, GPIO_PIN_RESET);
}

// Scan: only one LED on at a time, ~1 ms each
void print_matrix(const bool number[LED_COUNT])
{
    led_info prev = LEDS[LED_COUNT - 1];

    for (int i = 0; i < LED_COUNT; ++i)
    {
        led_info curr = LEDS[i];

        if (number[i])
        {
            turn_off(&prev);     // turn off the previous LED
            light_up(&curr);
            prev = curr;
            HAL_Delay(1);        // persistence of vision
        }
    }
    turn_off(&prev);
}`,
    learned: [
      "Designing a complete PCB, from schematic to soldered product.",
      "An elegant multiplexing technique that saves pins.",
      "The very concrete link between hardware constraints and software architecture.",
    ],
  },
  eu: {
    title: "PCB Snake",
    tagline: "Snake kontsola bat PCB propioan: mikrokontrolagailua eta charlieplexing bidezko LED matrizea.",
    domain: "Elektronika",
    tags: ["PCB", "KiCad", "Mikrokontrolagailua", "Charlieplexing", "C"],
    facts: [
      ["Diseinua", "Eskema + PCB bideratzea"],
      ["Pantaila", "Charlieplexing LEDak"],
      ["Firmwarea", "C txertatua"],
      ["Mota", "Hardware-proiektu osoa"],
    ],
    context: `<p>Helburua: Snake jokoa exekutatzen duen kontsola txiki bat hutsetik diseinatzea — eskema elektronikoa, PCBaren bideratzea, soldadura, eta ondoren jokoaren firmwarea.</p>
<p>Erronka interesgarria: LED asko pin gutxirekin gidatzea. Hor sartzen da <strong>charlieplexing</strong>-a, GPIOen inpedantzia altuko egoera baliatzen duena <code>n × (n − 1)</code> LED <code>n</code> pin bakarrik erabiliz helbideratzeko.</p>`,
    pipeline: ["Eskema", "Aztarnak", "PCB bideratzea", "Fabrikazioa", "Soldadura", "Firmwarea", "Snake jokoa"],
    pipeline_caption: "Eskematik kontsola funtzionalera.",
    points: [
      ["Charlieplexing", "LED bat pizteko, pin bat 1era jartzen da, beste bat 0ra, eta gainerako guztiak sarrera gisa (inpedantzia altua). 9 pinekin: 9 × 8 = 72 LED helbideragarri, 8 × 8 sare baterako nahikoa."],
      ["Ekorketa", "LED bakarra (edo lerro bakarra) pizten da aldi berean, baina ekorketa nahikoa azkarra da ikusmenaren iraunkortasunak irudi egonkorra erakusteko."],
      ["Bideratzea", "Charlieplexing-aren kableatua trinkoa eta ez oso intuitiboa da: LEDen kokapenak eta pisten bideratzeak arreta berezia eskatu dute."],
      ["Sarrerak", "Norabide-botoiak, software bidezko errebote-iragazkiarekin, freskatze-zikloen artean irakurriak."],
      ["Jokoaren logika", "Sugea buffer zirkular batean gordeta, sagarraren sorrera, talken detekzioa eta abiaduraren igoera mailakatua."],
      ["Elikadura", "Korronte-mugatzeko erresistentzien eta elikaduraren dimentsionamendua, distira homogeneoa lortzeko."],
    ],
    code_lang: "C",
    code: `// Pin "flotatzailea": pull-up edo pull-down gabeko sarrera (inpedantzia altua)
static void pin_hiz(uint16_t pin)
{
    GPIO_InitTypeDef cfg = {0};
    cfg.Pin  = pin;
    cfg.Mode = GPIO_MODE_INPUT;
    cfg.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOA, &cfg);
}

// LED bat piztu: anodoa 1ean, katodoa 0an, gainerako pinak flotatzen
void light_up(led_info *led)
{
    pin_output(led->anode);
    HAL_GPIO_WritePin(GPIOA, led->anode, GPIO_PIN_SET);

    pin_output(led->cathode);
    HAL_GPIO_WritePin(GPIOA, led->cathode, GPIO_PIN_RESET);
}

// Ekorketa: LED bakarra piztuta aldi berean, ~1 ms bakoitza
void print_matrix(const bool number[LED_COUNT])
{
    led_info prev = LEDS[LED_COUNT - 1];

    for (int i = 0; i < LED_COUNT; ++i)
    {
        led_info curr = LEDS[i];

        if (number[i])
        {
            turn_off(&prev);     // aurreko LEDa itzali
            light_up(&curr);
            prev = curr;
            HAL_Delay(1);        // ikusmenaren iraunkortasuna
        }
    }
    turn_off(&prev);
}`,
    learned: [
      "PCB oso bat diseinatzea, eskematik soldatutako produktura arte.",
      "Pinak aurrezten dituen multiplexazio-teknika dotorea.",
      "Hardware-mugen eta software-arkitekturaren arteko lotura oso zehatza.",
    ],
  },
};
