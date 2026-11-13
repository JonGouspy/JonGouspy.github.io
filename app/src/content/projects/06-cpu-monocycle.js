// Project 06: CPU Monocycle.
// Text is written per language (fr, en, eu). See projects/_template.js for the fields.
export default {
  slug: "cpu-monocycle",
  num: "06",
  theme: "architecture",
  repo: "https://github.com/JonGouspy/cpu-monocycle",
  fr: {
    title: "CPU Monocycle",
    tagline: "Un processeur 32 bits monocycle de type ARM décrit en VHDL, validé en simulation et prévu pour une carte MAX 10.",
    domain: "Architecture · FPGA",
    tags: ["VHDL", "Architecture", "ModelSim", "Quartus", "FPGA"],
    facts: [
      ["Langage", "VHDL"],
      ["Jeu d'instructions", "Sous-ensemble ARM 32 bits"],
      ["Cible", "DE10-Lite (MAX 10)"],
      ["Vérification", "Un testbench par bloc"],
    ],
    context: `<p>Un processeur monocycle exécute chaque instruction — lecture, décodage, exécution, accès mémoire, écriture — en un seul cycle d'horloge. C'est l'architecture la plus simple à raisonner, et la base pour comprendre ensuite le pipeline.</p>
<p>Le projet, réalisé en deux étapes, décrit chaque bloc du chemin de données en VHDL avec ses tests unitaires, les assemble avec un décodeur d'instructions, puis exécute un vrai programme en assembleur. Le projet Quartus cible une carte DE10-Lite, avec le résultat affiché sur des afficheurs 7 segments.</p>`,
    pipeline: [
      "PC + mémoire d'instructions",
      "Décodeur",
      "Banc de registres",
      "Extension de signe",
      "ALU",
      "Mémoire de données",
      "Write-back",
    ],
    pipeline_caption: "Chemin de données du processeur monocycle.",
    points: [
      ["ALU", "Quatre opérations (A + B, A − B, A, B) et deux drapeaux, N (négatif) et Z (nul), stockés dans un registre d'état."],
      ["Banc de registres", "16 registres de 32 bits, deux ports de lecture asynchrones, un port d'écriture synchrone sur front d'horloge."],
      ["Décodeur", "Reconnaît MOV, ADD (registre ou immédiat), CMP, LDR, STR, B et BLT à partir de la condition, du type et de l'opcode ARM, et génère neuf signaux de commande."],
      ["Mémoires séparées", "64 mots pour les instructions, 64 mots pour les données (Harvard). Le programme de test somme un tableau en mémoire avec une boucle LDR / ADD / CMP / BLT."],
      ["Gestion du PC", "PC + 1 ou branchement relatif à partir d'un déplacement de 24 bits étendu en signe ; BLT ne branche que si le drapeau N est levé."],
      ["Vérification", "Testbench et script ModelSim pour chaque bloc (ALU, mux, extension, registres, mémoire, décodeur, gestion du PC), puis pour le processeur complet."],
    ],
    code_lang: "VHDL",
    code: `entity DECODER is
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
end case;`,
    learned: [
      "Penser en matériel : concurrence, signaux, timing, plutôt qu'en séquence d'instructions.",
      "Comprendre concrètement comment un mot de 32 bits devient des signaux de commande.",
      "Valider chaque bloc seul, puis en intégration, avant d'assembler le tout.",
    ],
  },
  en: {
    title: "Single-Cycle CPU",
    tagline: "A 32-bit ARM-style single-cycle processor described in VHDL, validated in simulation and targeted at a MAX 10 board.",
    domain: "Architecture · FPGA",
    tags: ["VHDL", "Architecture", "ModelSim", "Quartus", "FPGA"],
    facts: [
      ["Language", "VHDL"],
      ["Instruction set", "32-bit ARM subset"],
      ["Target", "DE10-Lite (MAX 10)"],
      ["Verification", "One testbench per block"],
    ],
    context: `<p>A single-cycle processor executes each instruction — fetch, decode, execute, memory access, write-back — in one clock cycle. It's the simplest architecture to reason about, and the foundation for understanding pipelining later on.</p>
<p>The project, done in two steps, describes each datapath block in VHDL with its unit tests, wires them together with an instruction decoder, then runs a real assembly program. The Quartus project targets a DE10-Lite board, with the result shown on its 7-segment displays.</p>`,
    pipeline: [
      "PC + instruction memory",
      "Decoder",
      "Register file",
      "Sign extension",
      "ALU",
      "Data memory",
      "Write-back",
    ],
    pipeline_caption: "Datapath of the single-cycle processor.",
    points: [
      ["ALU", "Four operations (A + B, A − B, A, B) and two flags, N (negative) and Z (zero), stored in a status register."],
      ["Register file", "16 registers of 32 bits, two asynchronous read ports, one write port synchronous on the clock edge."],
      ["Decoder", "Recognizes MOV, ADD (register or immediate), CMP, LDR, STR, B and BLT from the ARM condition, type and opcode fields, and drives nine control signals."],
      ["Separate memories", "64 words for instructions, 64 words for data (Harvard). The test program sums an array in memory with an LDR / ADD / CMP / BLT loop."],
      ["PC logic", "PC + 1 or a relative branch from a sign-extended 24-bit offset; BLT only branches when the N flag is set."],
      ["Verification", "A testbench and ModelSim script for each block (ALU, mux, extender, registers, memory, decoder, PC unit), then for the whole processor."],
    ],
    code_lang: "VHDL",
    code: `entity DECODER is
    port(
      Instruction : in std_logic_vector(31 downto 0);
      RegPSR      : in std_logic_vector(3 downto 0);
      nPCSel, RegWr, ALUSrc, PSREn, MemWr, WrSrc, RegSel, RegAff : out std_logic;
      ALUCtr      : out std_logic_vector(1 downto 0)
    );
end entity;

-- Control signals of each instruction
case current_instr is
  when MOV  => RegWr <= '1'; ALUSrc <= '1'; ALUCtr <= "01";
  when ADDi => RegWr <= '1'; ALUSrc <= '1';
  when ADDr => RegWr <= '1';
  when CMP  => ALUSrc <= '1'; ALUCtr <= "10"; PSREn <= '1';
  when LDR  => RegWr <= '1'; ALUSrc <= '1'; WrSrc <= '1';
  when STR  => ALUSrc <= '1'; MemWr <= '1'; RegSel <= '1'; RegAff <= '1';
  when BAL  => nPCSel <= '1';
  when BLT  => nPCSel <= RegPSR(3);  -- branch if N = 1
  when others => null;
end case;`,
    learned: [
      "Thinking in hardware: concurrency, signals, timing, rather than a sequence of instructions.",
      "Understanding concretely how a 32-bit word becomes control signals.",
      "Validating each block alone, then in integration, before assembling everything.",
    ],
  },
  eu: {
    title: "Ziklo bakarreko CPUa",
    tagline: "VHDLz deskribatutako ARM motako 32 biteko ziklo bakarreko prozesadorea, simulazioan balioztatua eta MAX 10 txartel baterako pentsatua.",
    domain: "Arkitektura · FPGA",
    tags: ["VHDL", "Arkitektura", "ModelSim", "Quartus", "FPGA"],
    facts: [
      ["Lengoaia", "VHDL"],
      ["Agindu-multzoa", "ARM 32 biteko azpimultzoa"],
      ["Helburua", "DE10-Lite (MAX 10)"],
      ["Egiaztapena", "Testbench bat bloke bakoitzeko"],
    ],
    context: `<p>Ziklo bakarreko prozesadore batek agindu bakoitza — bilaketa, deskodetzea, exekuzioa, memoria-sarbidea, idazketa — erloju-ziklo bakar batean exekutatzen du. Arrazoitzeko arkitekturarik sinpleena da, eta ondoren pipeline-a ulertzeko oinarria.</p>
<p>Bi urratsetan egindako proiektuak datu-bideko bloke bakoitza VHDLz deskribatzen du bere proba unitarioekin, agindu-deskodetzaile batekin elkartzen ditu, eta gero benetako programa bat exekutatzen du mihiztadura-lengoaian. Quartus proiektuak DE10-Lite txartel bat du helburu, emaitza 7 segmentuko pantailetan erakutsiz.</p>`,
    pipeline: [
      "PC + agindu-memoria",
      "Deskodetzailea",
      "Erregistro-bankua",
      "Zeinu-hedapena",
      "ALU",
      "Datu-memoria",
      "Idazketa (write-back)",
    ],
    pipeline_caption: "Ziklo bakarreko prozesadorearen datu-bidea.",
    points: [
      ["ALU", "Lau eragiketa (A + B, A − B, A, B) eta bi adierazle, N (negatiboa) eta Z (nulua), egoera-erregistro batean gordeak."],
      ["Erregistro-bankua", "32 biteko 16 erregistro, bi irakurketa-ataka asinkrono eta idazketa-ataka bat, erloju-ertzean sinkronoa."],
      ["Deskodetzailea", "MOV, ADD (erregistroa edo berehalakoa), CMP, LDR, STR, B eta BLT ezagutzen ditu ARM baldintza, mota eta opcode eremuetatik, eta bederatzi kontrol-seinale sortzen ditu."],
      ["Memoria bereiziak", "64 hitz aginduentzat, 64 hitz datuentzat (Harvard). Proba-programak memoriako array bat batzen du LDR / ADD / CMP / BLT begizta batekin."],
      ["PCaren kudeaketa", "PC + 1 edo zeinuz hedatutako 24 biteko desplazamendu batetik jauzi erlatiboa; BLT-k N adierazlea altxatuta dagoenean soilik egiten du jauzi."],
      ["Egiaztapena", "Testbench eta ModelSim script bat bloke bakoitzeko (ALU, mux, hedatzailea, erregistroak, memoria, deskodetzailea, PC unitatea), eta gero prozesadore osoarentzat."],
    ],
    code_lang: "VHDL",
    code: `entity DECODER is
    port(
      Instruction : in std_logic_vector(31 downto 0);
      RegPSR      : in std_logic_vector(3 downto 0);
      nPCSel, RegWr, ALUSrc, PSREn, MemWr, WrSrc, RegSel, RegAff : out std_logic;
      ALUCtr      : out std_logic_vector(1 downto 0)
    );
end entity;

-- Aginduen kontrol-seinaleak
case current_instr is
  when MOV  => RegWr <= '1'; ALUSrc <= '1'; ALUCtr <= "01";
  when ADDi => RegWr <= '1'; ALUSrc <= '1';
  when ADDr => RegWr <= '1';
  when CMP  => ALUSrc <= '1'; ALUCtr <= "10"; PSREn <= '1';
  when LDR  => RegWr <= '1'; ALUSrc <= '1'; WrSrc <= '1';
  when STR  => ALUSrc <= '1'; MemWr <= '1'; RegSel <= '1'; RegAff <= '1';
  when BAL  => nPCSel <= '1';
  when BLT  => nPCSel <= RegPSR(3);  -- jauzi egin N = 1 bada
  when others => null;
end case;`,
    learned: [
      "Hardwarean pentsatzea: konkurrentzia, seinaleak, denbora, agindu-sekuentzia baten ordez.",
      "32 biteko hitz bat kontrol-seinale bihurtzen den modua zehazki ulertzea.",
      "Bloke bakoitza bakarka eta gero integrazioan balioztatzea, dena elkartu aurretik.",
    ],
  },
};
