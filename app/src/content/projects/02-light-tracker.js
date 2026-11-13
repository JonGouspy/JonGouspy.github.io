// Project 02: Light Tracker.
// Text is written per language (fr, en, eu). See projects/_template.js for the fields.
export default {
  slug: "light-tracker",
  num: "02",
  theme: "hardware",
  repo: "https://github.com/JonGouspy/light-tracker",
  image: "/img/light-tracker.png",
  fr: {
    title: "Light Tracker",
    tagline: "Un robot qui s'oriente tout seul vers la source de lumière la plus intense.",
    domain: "Robotique",
    tags: ["Microcontrôleur", "C", "ADC", "Moteur", "Asservissement"],
    facts: [
      ["Capteurs", "2 photorésistances"],
      ["Actionneur", "Moteur + pont en H"],
      ["Langage", "C embarqué"],
      ["Type", "Projet matériel"],
    ],
    context: `<p>Le principe est simple : deux capteurs de lumière placés de part et d'autre du robot mesurent l'intensité lumineuse. Si un côté reçoit plus de lumière que l'autre, le moteur tourne pour rééquilibrer — le robot finit pointé vers la source.</p>
<p>Derrière cette simplicité : acquisition analogique, filtrage du bruit, zone morte pour éviter les oscillations et pilotage d'un moteur dans les deux sens.</p>`,
    pipeline: [
      "Capteur gauche",
      "Capteur droit",
      "Diviseurs de tension",
      "ADC",
      "Filtrage",
      "Erreur = G − D",
      "Commande",
      "Pont en H",
      "Moteur",
    ],
    pipeline_caption: "Boucle de contrôle : de la mesure de lumière à la rotation du moteur.",
    points: [
      ["Acquisition", "Chaque photorésistance forme un pont diviseur ; la tension est lue par le convertisseur analogique-numérique du microcontrôleur."],
      ["Calibration", "Les deux capteurs n'ont jamais exactement la même réponse : un offset mesuré au démarrage compense l'écart."],
      ["Filtrage", "Moyenne glissante sur plusieurs échantillons pour lisser le bruit (néons, scintillement 50 Hz)."],
      ["Zone morte", "En dessous d'un seuil d'écart, le moteur reste à l'arrêt : le robot ne « tremble » pas une fois aligné."],
      ["Commande proportionnelle", "La vitesse (PWM) dépend de l'écart : rotation rapide quand la lumière est loin, ralentissement à l'approche."],
      ["Puissance", "Un pont en H isole le microcontrôleur du courant moteur et permet d'inverser le sens de rotation."],
    ],
    code_lang: "C",
    code: `// TIM2 : interruption périodique qui cadence les mesures
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
}`,
    learned: [
      "Passer d'une idée simple à un système physique qui marche vraiment (bruit, tolérances, mécanique).",
      "Les bases de l'asservissement : erreur, gain, zone morte, stabilité.",
      "Séparer proprement la logique de commande et l'étage de puissance.",
    ],
  },
  en: {
    title: "Light Tracker",
    tagline: "A robot that turns on its own toward the brightest light source.",
    domain: "Robotics",
    tags: ["Microcontroller", "C", "ADC", "Motor", "Control loop"],
    facts: [
      ["Sensors", "2 photoresistors"],
      ["Actuator", "Motor + H-bridge"],
      ["Language", "Embedded C"],
      ["Type", "Hardware project"],
    ],
    context: `<p>The principle is simple: two light sensors on either side of the robot measure light intensity. If one side gets more light than the other, the motor turns to rebalance — and the robot ends up pointing at the source.</p>
<p>Behind that simplicity: analog acquisition, noise filtering, a dead zone to avoid oscillations, and bidirectional motor control.</p>`,
    pipeline: [
      "Left sensor",
      "Right sensor",
      "Voltage dividers",
      "ADC",
      "Filtering",
      "Error = L − R",
      "Command",
      "H-bridge",
      "Motor",
    ],
    pipeline_caption: "Control loop: from light measurement to motor rotation.",
    points: [
      ["Acquisition", "Each photoresistor forms a voltage divider; the voltage is read by the microcontroller's analog-to-digital converter."],
      ["Calibration", "The two sensors never respond exactly the same: an offset measured at startup compensates for the difference."],
      ["Filtering", "Moving average over several samples to smooth out noise (fluorescent lights, 50 Hz flicker)."],
      ["Dead zone", "Below a threshold, the motor stays still: the robot doesn't jitter once it's aligned."],
      ["Proportional control", "Speed (PWM) depends on the error: fast rotation when the light is far off, slowing down as it gets aligned."],
      ["Power stage", "An H-bridge isolates the microcontroller from the motor current and allows reversing the direction."],
    ],
    code_lang: "C",
    code: `// TIM2: periodic interrupt that paces the measurements
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

// ADC1, channel 11 (PC1): conversions read through an interrupt
void initADC(void)
{
    GPIO_InitStruct.Pin  = GPIO_PIN_1;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;   // PC1 as analog input
    HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

    HAL_NVIC_SetPriority(ADC_IRQn, 5, 0);
    HAL_NVIC_EnableIRQ(ADC_IRQn);

    gAdcHandle.Instance = ADC1;
    gAdcHandle.Init.Resolution = ADC_RESOLUTION_12B;
    gAdcHandle.Init.ExternalTrigConv = ADC_EXTERNALTRIGCONV_T2_TRGO;  // TIM2 triggers the conversion
    HAL_ADC_Init(&gAdcHandle);

    ADC_ChannelStruct.Channel = ADC_CHANNEL_11;
    ADC_ChannelStruct.SamplingTime = ADC_SAMPLETIME_480CYCLES;  // maximum sampling time
    HAL_ADC_ConfigChannel(&gAdcHandle, &ADC_ChannelStruct);

    HAL_ADC_Start_IT(&gAdcHandle);
}`,
    learned: [
      "Turning a simple idea into a physical system that actually works (noise, tolerances, mechanics).",
      "Control basics: error, gain, dead zone, stability.",
      "Cleanly separating control logic from the power stage.",
    ],
  },
  eu: {
    title: "Light Tracker",
    tagline: "Argi-iturri biziena dagoen aldera bere kabuz biratzen den robota.",
    domain: "Robotika",
    tags: ["Mikrokontrolagailua", "C", "ADC", "Motorra", "Kontrol-begizta"],
    facts: [
      ["Sentsoreak", "2 fotoerresistentzia"],
      ["Eragingailua", "Motorra + H zubia"],
      ["Lengoaia", "C txertatua"],
      ["Mota", "Hardware-proiektua"],
    ],
    context: `<p>Printzipioa sinplea da: robotaren alde banatan jarritako bi argi-sentsorek argi-intentsitatea neurtzen dute. Alde batek besteak baino argi gehiago jasotzen badu, motorrak biratu egiten du oreka berreskuratzeko — eta robota iturriari begira geratzen da.</p>
<p>Sinpletasun horren atzean: eskuratze analogikoa, zarataren iragazketa, oszilazioak saihesteko zona hila eta bi noranzkoetan dabilen motorraren kontrola.</p>`,
    pipeline: [
      "Ezkerreko sentsorea",
      "Eskuineko sentsorea",
      "Tentsio-zatitzaileak",
      "ADC",
      "Iragazketa",
      "Errorea = Ezk − Esk",
      "Agindua",
      "H zubia",
      "Motorra",
    ],
    pipeline_caption: "Kontrol-begizta: argiaren neurketatik motorraren biraketara.",
    points: [
      ["Eskuratzea", "Fotoerresistentzia bakoitzak tentsio-zatitzaile bat osatzen du; tentsioa mikrokontrolagailuaren bihurgailu analogiko-digitalak irakurtzen du."],
      ["Kalibrazioa", "Bi sentsoreek ez dute inoiz erantzun berdin-berdina: abiaraztean neurtutako desplazamendu batek aldea konpentsatzen du."],
      ["Iragazketa", "Batez besteko mugikorra hainbat laginen gainean, zarata leuntzeko (fluoreszenteak, 50 Hz-ko keinua)."],
      ["Zona hila", "Atalase batetik behera, motorra geldi geratzen da: lerrokatuta dagoenean robota ez da dardaraka ibiltzen."],
      ["Kontrol proportzionala", "Abiadura (PWM) errorearen araberakoa da: biraketa azkarra argia urrun dagoenean, motelagoa hurbiltzean."],
      ["Potentzia", "H zubi batek mikrokontrolagailua motorraren korrontetik isolatzen du eta biraketa-noranzkoa aldatzea ahalbidetzen du."],
    ],
    code_lang: "C",
    code: `// TIM2: neurketak kadentziatzen dituen eten periodikoa
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

// ADC1, 11. kanala (PC1): bihurketak etenen bidez irakurtzen dira
void initADC(void)
{
    GPIO_InitStruct.Pin  = GPIO_PIN_1;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;   // PC1 sarrera analogiko gisa
    HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

    HAL_NVIC_SetPriority(ADC_IRQn, 5, 0);
    HAL_NVIC_EnableIRQ(ADC_IRQn);

    gAdcHandle.Instance = ADC1;
    gAdcHandle.Init.Resolution = ADC_RESOLUTION_12B;
    gAdcHandle.Init.ExternalTrigConv = ADC_EXTERNALTRIGCONV_T2_TRGO;  // TIM2-k bihurketa abiarazten du
    HAL_ADC_Init(&gAdcHandle);

    ADC_ChannelStruct.Channel = ADC_CHANNEL_11;
    ADC_ChannelStruct.SamplingTime = ADC_SAMPLETIME_480CYCLES;  // laginketa-denbora maximoa
    HAL_ADC_ConfigChannel(&gAdcHandle, &ADC_ChannelStruct);

    HAL_ADC_Start_IT(&gAdcHandle);
}`,
    learned: [
      "Ideia sinple bat benetan funtzionatzen duen sistema fisiko bihurtzea (zarata, tolerantziak, mekanika).",
      "Kontrolaren oinarriak: errorea, irabazia, zona hila, egonkortasuna.",
      "Kontrol-logika eta potentzia-etapa garbiki bereiztea.",
    ],
  },
};
