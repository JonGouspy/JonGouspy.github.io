// Project 04: Dérisquage sur ESP32.
// Text is written per language (fr, en, eu). See projects/_template.js for the fields.
export default {
  slug: "deriscage-esp32",
  num: "04",
  theme: "systeme",
  repo: "https://github.com/JonGouspy/gap",
  fr: {
    title: "Dérisquage sur ESP32",
    tagline: "Estimation de mouvement par IMU : filtre de Madgwick + correction ZUPT, sur ESP32.",
    domain: "Systèmes embarqués",
    tags: ["ESP32", "ESP-IDF", "FreeRTOS", "MPU6050", "I²C", "Fusion de capteurs"],
    facts: [
      ["Carte", "ESP32"],
      ["Framework", "ESP-IDF · FreeRTOS"],
      ["Capteur", "MPU6050 (accéléro + gyro)"],
      ["Algorithmes", "Madgwick · ZUPT"],
    ],
    context: `<p>Un MPU6050 fournit des accélérations et des vitesses angulaires sur 3 axes. En théorie, il suffit d'intégrer deux fois l'accélération pour obtenir la position. En pratique, le moindre biais explose : après quelques secondes la position dérive de plusieurs mètres.</p>
<p>Ce projet combine deux techniques pour rendre l'estimation exploitable : le <strong>filtre de Madgwick</strong> pour connaître l'orientation du capteur, et la correction <strong>ZUPT</strong> (Zero Velocity Update) pour remettre la vitesse à zéro dès que le capteur est immobile.</p>`,
    pipeline: [
      "MPU6050",
      "Lecture I²C",
      "Calibration des biais",
      "Filtre de Madgwick",
      "Accél. repère monde",
      "− gravité",
      "∫ vitesse",
      "Détection immobilité",
      "ZUPT : v = 0",
      "∫ position",
    ],
    pipeline_caption: "Chaîne de traitement exécutée en temps réel sur l'ESP32.",
    points: [
      ["Driver I²C", "Communication avec le MPU6050 via l'API I²C d'ESP-IDF : configuration des plages (±g, °/s), lecture en rafale des registres."],
      ["Tâches FreeRTOS", "Une tâche d'acquisition à fréquence fixe, une tâche de traitement ; échange par file (queue) pour un échantillonnage régulier."],
      ["Filtre de Madgwick", "Fusion gyro + accéléromètre par descente de gradient sur un quaternion d'orientation, réglée par le paramètre β."],
      ["Repère monde", "L'accélération est tournée dans le repère terrestre grâce au quaternion, puis la gravité est soustraite pour garder l'accélération linéaire."],
      ["Détection d'immobilité", "Sur une fenêtre glissante : norme de l'accélération proche de g et rotation quasi nulle → le capteur est considéré à l'arrêt."],
      ["Correction ZUPT", "À chaque phase d'arrêt, la vitesse est forcée à zéro : l'erreur accumulée est coupée, la dérive de position reste bornée."],
    ],
    code_lang: "C",
    code: `// Mise à jour de Kalman : mesure virtuelle « vitesse = 0 »
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
}`,
    learned: [
      "Développer sur ESP-IDF et structurer une application temps réel avec FreeRTOS.",
      "Comprendre la fusion de capteurs et les limites physiques d'une centrale inertielle bas coût.",
      "Corriger une dérive par des connaissances a priori (ici : les phases d'arrêt).",
    ],
  },
  en: {
    title: "Dérisquage on ESP32",
    tagline: "IMU motion estimation: Madgwick filter + ZUPT correction, on ESP32.",
    domain: "Embedded systems",
    tags: ["ESP32", "ESP-IDF", "FreeRTOS", "MPU6050", "I²C", "Sensor fusion"],
    facts: [
      ["Board", "ESP32"],
      ["Framework", "ESP-IDF · FreeRTOS"],
      ["Sensor", "MPU6050 (accel + gyro)"],
      ["Algorithms", "Madgwick · ZUPT"],
    ],
    context: `<p>An MPU6050 provides 3-axis accelerations and angular rates. In theory, integrating acceleration twice gives you position. In practice, the slightest bias blows up: after a few seconds, the position drifts by several meters.</p>
<p>This project combines two techniques to make the estimate usable: the <strong>Madgwick filter</strong> to know the sensor's orientation, and <strong>ZUPT</strong> (Zero Velocity Update) correction to reset velocity to zero whenever the sensor is still.</p>`,
    pipeline: [
      "MPU6050",
      "I²C read",
      "Bias calibration",
      "Madgwick filter",
      "World-frame accel.",
      "− gravity",
      "∫ velocity",
      "Stillness detection",
      "ZUPT: v = 0",
      "∫ position",
    ],
    pipeline_caption: "Processing chain running in real time on the ESP32.",
    points: [
      ["I²C driver", "Communication with the MPU6050 through the ESP-IDF I²C API: range configuration (±g, °/s), burst register reads."],
      ["FreeRTOS tasks", "A fixed-rate acquisition task and a processing task, exchanging data through a queue for regular sampling."],
      ["Madgwick filter", "Gyro + accelerometer fusion via gradient descent on an orientation quaternion, tuned by the β parameter."],
      ["World frame", "Acceleration is rotated into the Earth frame using the quaternion, then gravity is subtracted to keep only linear acceleration."],
      ["Stillness detection", "Over a sliding window: acceleration norm close to g and near-zero rotation → the sensor is considered stationary."],
      ["ZUPT correction", "At each stationary phase, velocity is forced to zero: accumulated error is cut off and position drift stays bounded."],
    ],
    code_lang: "C",
    code: `// Kalman update: virtual measurement "velocity = 0"
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
    a_world.z -= GRAVITY;                         // remove gravity

    // amag, gmag: norms of the acceleration and of the gyroscope
    // Stationary: acceleration ≈ g and almost no rotation, for ZUPT_WINDOW samples in a row
    if (fabsf(amag - GRAVITY) < ZUPT_ACCEL_TOL && gmag < ZUPT_GYRO_TOL)
        data->zupt_count++;
    else
        data->zupt_count = 0;
    data->zupt_active = (data->zupt_count >= ZUPT_WINDOW);

    // prediction: integrate the acceleration (same for y and z)
    axis_predict(&data->relative_pos.x, &data->velocity.x, &data->covariance[0], a_world.x, dt);

    // when stopped: Kalman correction (same for y and z)
    if (data->zupt_active)
        axis_zupt(&data->relative_pos.x, &data->velocity.x, &data->covariance[0]);
}`,
    learned: [
      "Developing with ESP-IDF and structuring a real-time application with FreeRTOS.",
      "Understanding sensor fusion and the physical limits of a low-cost IMU.",
      "Correcting drift with prior knowledge (here: stationary phases).",
    ],
  },
  eu: {
    title: "Dérisquage ESP32an",
    tagline: "Mugimenduaren estimazioa IMU bidez: Madgwick iragazkia + ZUPT zuzenketa, ESP32an.",
    domain: "Sistema txertatuak",
    tags: ["ESP32", "ESP-IDF", "FreeRTOS", "MPU6050", "I²C", "Sentsore-fusioa"],
    facts: [
      ["Txartela", "ESP32"],
      ["Lan-markoa", "ESP-IDF · FreeRTOS"],
      ["Sentsorea", "MPU6050 (azelerometroa + giroskopioa)"],
      ["Algoritmoak", "Madgwick · ZUPT"],
    ],
    context: `<p>MPU6050 batek 3 ardatzeko azelerazioak eta abiadura angeluarrak ematen ditu. Teorian, azelerazioa bi aldiz integratzea nahikoa da posizioa lortzeko. Praktikan, alborapenik txikiena ere lehertu egiten da: segundo gutxiren buruan posizioa hainbat metro desbideratzen da.</p>
<p>Proiektu honek bi teknika uztartzen ditu estimazioa erabilgarria izan dadin: <strong>Madgwick iragazkia</strong>, sentsorearen orientazioa ezagutzeko, eta <strong>ZUPT</strong> zuzenketa (Zero Velocity Update), sentsorea geldi dagoen bakoitzean abiadura zerora itzultzeko.</p>`,
    pipeline: [
      "MPU6050",
      "I²C irakurketa",
      "Alborapenen kalibrazioa",
      "Madgwick iragazkia",
      "Azel. munduko erreferentzian",
      "− grabitatea",
      "∫ abiadura",
      "Geldiune-detekzioa",
      "ZUPT: v = 0",
      "∫ posizioa",
    ],
    pipeline_caption: "ESP32an denbora errealean exekutatzen den prozesamendu-katea.",
    points: [
      ["I²C driverra", "MPU6050arekiko komunikazioa ESP-IDFren I²C APIaren bidez: tarteen konfigurazioa (±g, °/s) eta erregistroen irakurketa jarraitua."],
      ["FreeRTOS atazak", "Maiztasun finkoko eskuratze-ataza bat eta prozesamendu-ataza bat; ilara baten bidez trukatzen dituzte datuak, laginketa erregularra bermatzeko."],
      ["Madgwick iragazkia", "Giroskopioaren eta azelerometroaren fusioa, orientazio-kuaternioi baten gaineko gradiente-jaitsieraren bidez, β parametroaz doitua."],
      ["Munduko erreferentzia", "Azelerazioa Lurraren erreferentzia-sistemara biratzen da kuaternioiari esker, eta grabitatea kentzen zaio azelerazio lineala soilik gordetzeko."],
      ["Geldiune-detekzioa", "Leiho irristakor batean: azelerazioaren norma g-tik hurbil eta biraketa ia nulua → sentsorea geldi dagoela jotzen da."],
      ["ZUPT zuzenketa", "Geldiune bakoitzean abiadura zerora behartzen da: metatutako errorea mozten da eta posizioaren desbideratzea mugatuta geratzen da."],
    ],
    code_lang: "C",
    code: `// Kalman eguneraketa: "abiadura = 0" neurketa birtuala
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
    a_world.z -= GRAVITY;                         // grabitatea kendu

    // amag, gmag: azelerazioaren eta giroskopioaren moduluak
    // Geldirik: azelerazioa ≈ g eta ia biraketarik gabe, ZUPT_WINDOW lagin jarraian
    if (fabsf(amag - GRAVITY) < ZUPT_ACCEL_TOL && gmag < ZUPT_GYRO_TOL)
        data->zupt_count++;
    else
        data->zupt_count = 0;
    data->zupt_active = (data->zupt_count >= ZUPT_WINDOW);

    // aurreikuspena: azelerazioaren integrazioa (berdin y eta z-rentzat)
    axis_predict(&data->relative_pos.x, &data->velocity.x, &data->covariance[0], a_world.x, dt);

    // geldirik dagoenean: Kalman zuzenketa (berdin y eta z-rentzat)
    if (data->zupt_active)
        axis_zupt(&data->relative_pos.x, &data->velocity.x, &data->covariance[0]);
}`,
    learned: [
      "ESP-IDFrekin garatzea eta denbora errealeko aplikazio bat FreeRTOSekin egituratzea.",
      "Sentsore-fusioa eta kostu baxuko IMU baten muga fisikoak ulertzea.",
      "Desbideratze bat aurretiazko ezagutzaren bidez zuzentzea (hemen: geldiuneak).",
    ],
  },
};
