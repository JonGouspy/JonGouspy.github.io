// Project 03: Object Detection GPU.
// Text is written per language (fr, en, eu). See projects/_template.js for the fields.
export default {
  slug: "object-detection-gpu",
  num: "03",
  theme: "software",
  repo: "https://github.com/JonGouspy/gpgpu",
  fr: {
    title: "Object Detection GPU",
    tagline: "Détection d'objets en mouvement par soustraction de fond : un filtre GStreamer CUDA, 30 à 41× plus rapide que le CPU.",
    domain: "Vision · GPU",
    tags: ["CUDA", "C++20", "GStreamer", "Nsight", "CMake"],
    facts: [
      ["Langage", "C++ / CUDA"],
      ["Résultat", "×30 à ×41 vs CPU (1080p)"],
      ["Profilage", "Nsight Systems"],
      ["Type", "Projet de groupe (4)"],
    ],
    context: `<p>Projet GPGPU à l'EPITA, en groupe de quatre : écrire un filtre GStreamer CUDA qui sépare le fond des objets mobiles dans un flux vidéo, puis affiche les pixels en mouvement en rouge. C'est une étape préliminaire de nombreuses chaînes de traitement vidéo.</p>
<p>Nous avons d'abord écrit une version CPU de référence, puis un portage GPU naïf, que nous avons optimisé en huit étapes (v1.1.0 → v1.1.8). Chaque étape a été mesurée avec Nsight Systems avant d'en choisir la suivante.</p>`,
    pipeline: [
      "Frame vidéo",
      "Estimation du fond (réservoirs)",
      "Masque max(|I − B|)",
      "Ouverture (érosion + dilatation)",
      "Hystérésis",
      "Surbrillance rouge",
    ],
    pipeline_caption: "Pipeline du filtre, chaque étape étant un ou plusieurs kernels CUDA.",
    points: [
      ["Estimation du fond", "Chaque pixel garde k couleurs candidates pondérées (réservoir), mises à jour par tirage aléatoire cuRAND ; la couleur de plus fort poids est le fond."],
      ["Masque et hystérésis", "Écart maximal sur les canaux RGB, puis seuil bas / seuil haut : un pixel moyen n'est retenu que s'il est connecté à un pixel fort."],
      ["Hystérésis en mémoire partagée", "Propagation dans une tuile jusqu'à stabilité avec __syncthreads_or, puis saut des blocs inactifs : de 172 lancements par frame à environ 11, hystérésis de 12,7 à 0,55 ms."],
      ["Ouverture séparable", "Un min / max sur fenêtre carrée devient un passage horizontal puis vertical : 81 lectures par pixel ramenées à 18, puis fusionné en un kernel en mémoire partagée avec halo."],
      ["Données sur le GPU", "Frame et fond restent en mémoire GPU, buffers alloués une seule fois, masque en uint8_t au lieu de float, et réservoir en structure de tableaux pour des accès contigus."],
      ["Benchmark honnête", "Trois vidéos, mêmes paramètres, même machine. Au-delà de v1.1.3 le calcul ne pèse plus que ~2,4 ms sur 14,6 ms par frame : le décodage et les transferts dominent."],
    ],
    code_lang: "CUDA",
    code: `// Un thread par pixel : écart maximal sur les trois canaux entre l'image et le fond
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
}`,
    learned: [
      "Penser un algorithme en termes de parallélisme massif.",
      "Profiler avant d'optimiser : nous avions d'abord optimisé les copies (1,3 ms) alors que l'hystérésis en coûtait 12,7.",
      "Lire un résultat sans se mentir : une optimisation peut être neutre (v1.1.4) et rester utile pour la clarté du code.",
    ],
  },
  en: {
    title: "Object Detection GPU",
    tagline: "Moving-object detection through background subtraction: a CUDA GStreamer filter, 30 to 41× faster than the CPU.",
    domain: "Vision · GPU",
    tags: ["CUDA", "C++20", "GStreamer", "Nsight", "CMake"],
    facts: [
      ["Language", "C++ / CUDA"],
      ["Result", "×30 to ×41 vs CPU (1080p)"],
      ["Profiling", "Nsight Systems"],
      ["Type", "Group project (4)"],
    ],
    context: `<p>GPGPU project at EPITA, in a group of four: write a CUDA GStreamer filter that separates the background from moving objects in a video stream, then displays the moving pixels in red. It is a preliminary step in many video-processing chains.</p>
<p>We first wrote a reference CPU version, then a naive GPU port, which we optimized in eight steps (v1.1.0 → v1.1.8). Each step was measured with Nsight Systems before choosing the next one.</p>`,
    pipeline: [
      "Video frame",
      "Background estimation (reservoirs)",
      "Mask max(|I − B|)",
      "Opening (erosion + dilation)",
      "Hysteresis",
      "Red overlay",
    ],
    pipeline_caption: "Filter pipeline, each stage being one or more CUDA kernels.",
    points: [
      ["Background estimation", "Each pixel keeps k weighted candidate colors (a reservoir), updated by cuRAND random draws; the highest-weight color is the background."],
      ["Mask and hysteresis", "Maximum difference over the RGB channels, then low / high thresholds: a mid-level pixel is kept only if it is connected to a strong one."],
      ["Shared-memory hysteresis", "Propagation inside a tile until stable with __syncthreads_or, then skipping inactive blocks: from 172 launches per frame to about 11, hysteresis from 12.7 to 0.55 ms."],
      ["Separable opening", "A min / max over a square window becomes a horizontal then a vertical pass: 81 reads per pixel down to 18, then fused into a single shared-memory kernel with a halo."],
      ["Data stays on the GPU", "Frame and background stay in GPU memory, buffers are allocated once, the mask is uint8_t instead of float, and the reservoir is a structure of arrays for contiguous accesses."],
      ["Honest benchmark", "Three videos, same parameters, same machine. Past v1.1.3 the compute is only ~2.4 ms out of 14.6 ms per frame: decoding and transfers dominate."],
    ],
    code_lang: "CUDA",
    code: `// One thread per pixel: maximum difference over the three channels between frame and background
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
}`,
    learned: [
      "Thinking about an algorithm in terms of massive parallelism.",
      "Profile before optimizing: we first optimized copies (1.3 ms) while hysteresis cost 12.7.",
      "Reading a result honestly: an optimization can be neutral (v1.1.4) and still worth keeping for code clarity.",
    ],
  },
  eu: {
    title: "Object Detection GPU",
    tagline: "Mugitzen diren objektuen detekzioa hondoaren kenketaren bidez: CPUa baino 30-41 aldiz azkarragoa den CUDA GStreamer iragazkia.",
    domain: "Ikusmena · GPU",
    tags: ["CUDA", "C++20", "GStreamer", "Nsight", "CMake"],
    facts: [
      ["Lengoaia", "C++ / CUDA"],
      ["Emaitza", "×30-×41 CPUaren aldean (1080p)"],
      ["Profilatzea", "Nsight Systems"],
      ["Mota", "Talde-proiektua (4)"],
    ],
    context: `<p>GPGPU proiektua EPITAn, lau lagunen taldean: bideo-jario batean hondoa eta objektu mugikorrak bereizten dituen CUDA GStreamer iragazki bat idaztea, eta mugitzen diren pixelak gorriz erakustea. Bideo-prozesatze kate askoren aurreko urratsa da.</p>
<p>Lehenik CPU erreferentziazko bertsio bat idatzi genuen, gero GPU eramate sinple bat, eta zortzi urratsetan optimizatu (v1.1.0 → v1.1.8). Urrats bakoitza Nsight Systems-ekin neurtu zen hurrengoa aukeratu aurretik.</p>`,
    pipeline: [
      "Bideo-irudia",
      "Hondoaren estimazioa (erreserbak)",
      "Maskara max(|I − B|)",
      "Irekiera (higadura + dilatazioa)",
      "Histeresia",
      "Gain gorria",
    ],
    pipeline_caption: "Iragazkiaren katea; urrats bakoitza CUDA kernel bat edo gehiago da.",
    points: [
      ["Hondoaren estimazioa", "Pixel bakoitzak k kolore hautagai pisutu gordetzen ditu (erreserba), cuRAND zozketa aleatorioekin eguneratuak; pisu handieneko kolorea da hondoa."],
      ["Maskara eta histeresia", "RGB kanaletako alderik handiena, eta ondoren atalase baxua / altua: erdiko pixel bat atalase altuko pixel batekin konektatuta badago soilik mantentzen da."],
      ["Histeresia memoria partekatuan", "Lauza baten barruan hedapena egonkortu arte __syncthreads_or-ekin, gero bloke inaktiboak saltatuz: irudiko 172 abiarazletik 11ra inguru, histeresia 12,7 ms-tik 0,55 ms-ra."],
      ["Irekiera banagarria", "Leiho karratu baten min / max-a pasaldi horizontal eta bertikal bihurtzen da: pixeleko 81 irakurketa 18ra, eta gero memoria partekatuko kernel bakar batean batuta, ertzarekin."],
      ["Datuak GPUan geratzen dira", "Irudia eta hondoa GPUaren memorian daude, bufferrak behin esleituta, maskara float ordez uint8_t, eta erreserba array-egitura gisa sarbide jarraituetarako."],
      ["Benchmark zintzoa", "Hiru bideo, parametro berdinak, makina bera. v1.1.3-tik aurrera kalkulua irudiko 14,6 ms-tik ~2,4 ms baino ez da: deskodetzeak eta transferentziek menderatzen dute."],
    ],
    code_lang: "CUDA",
    code: `// Hari bat pixel bakoitzeko: irudiaren eta hondoaren arteko alderik handiena hiru kanaletan
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
}`,
    learned: [
      "Algoritmo bat paralelismo masiboaren ikuspegitik pentsatzea.",
      "Optimizatu aurretik profilatu: lehenik kopiak optimizatu genituen (1,3 ms) histeresiak 12,7 ms kostatzen zuenean.",
      "Emaitza bat zintzotasunez irakurtzea: optimizazio bat neutroa izan daiteke (v1.1.4) eta kodearen argitasunagatik mantentzea merezi du.",
    ],
  },
};
