/* =============================================================================
 * الحاسبة الكهربائية — نسخة الويب (نسخة مطابقة لمحرك Python الأصلي)
 * Trilingual: العربية / Français / English
 * ========================================================================== */

const TRANSLATIONS = {
  // ---------- عام ----------
  app_title: { ar: "الحاسبة الكهربائية", fr: "Calculatrice Électrique", en: "Electrical Calculator" },
  help_btn: { ar: "مساعدة", fr: "Aide", en: "Help" },
  help_title: { ar: "شرح العملية الحسابية", fr: "Explication de la formule", en: "Calculation Explanation" },
  help_formula: { ar: "الصيغة الحسابية:", fr: "Formule de calcul :", en: "Formula:" },
  help_fields: { ar: "العناصر المراد إدخالها:", fr: "Champs à remplir :", en: "Input fields:" },
  close: { ar: "إغلاق", fr: "Fermer", en: "Close" },
  calc_btn: { ar: "احسب", fr: "Calculer", en: "Calculate" },

  // ---------- القائمة ----------
  mod_ohm: { ar: "1. قانون أوم", fr: "1. Loi d'Ohm", en: "1. Ohm's Law" },
  mod_vd: { ar: "2. هبوط الجهد", fr: "2. Chute de tension", en: "2. Voltage Drop" },
  mod_k2s2: { ar: "3. شرط ك²س²", fr: "3. Condition K²S²", en: "3. K²S² Condition" },
  mod_led: { ar: "4. مقاومة الـ LED", fr: "4. Résistance LED", en: "4. LED Resistor" },
  mod_volt: { ar: "5. حساب الجهد", fr: "5. Calcul de tension", en: "5. Voltage Calc" },
  mod_amp: { ar: "6. حساب التيار", fr: "6. Calcul de courant", en: "6. Current Calc" },
  mod_slip: { ar: "7. انزلاق المحرك", fr: "7. Glissement moteur", en: "7. Motor Slip" },
  mod_section: { ar: "8. مقطع الكابل", fr: "8. Section du câble", en: "8. Cable Section" },
  mod_res: { ar: "9. ألوان المقاومات", fr: "9. Code couleur", en: "9. Resistor Colors" },

  // ---------- عام للحقول ----------
  lbl_voltage: { ar: "الجهد (Volt):", fr: "Tension (V) :", en: "Voltage (V):" },
  lbl_current: { ar: "التيار (Ampere):", fr: "Courant (A) :", en: "Current (A):" },
  lbl_power: { ar: "القدرة (Watt):", fr: "Puissance (W) :", en: "Power (W):" },
  lbl_length: { ar: "الطول (متر):", fr: "Longueur (m) :", en: "Length (m):" },
  lbl_section: { ar: "المقطع (mm²):", fr: "Section (mm²) :", en: "Section (mm²):" },
  lbl_cosphi: { ar: "معامل القدرة Cos φ:", fr: "Facteur de puissance Cos φ :", en: "Power factor Cos φ:" },
  lbl_system: { ar: "النظام:", fr: "Système :", en: "System:" },
  lbl_material: { ar: "المادة:", fr: "Matériau :", en: "Material:" },
  lbl_resistance: { ar: "المقاومة (أوم):", fr: "Résistance (Ω) :", en: "Resistance (Ω):" },

  sys_single: { ar: "أحادي الطور", fr: "Monophasé", en: "Single-phase" },
  sys_three: { ar: "ثلاثي الطور", fr: "Triphasé", en: "Three-phase" },
  mat_cu: { ar: "نحاس (Cu)", fr: "Cuivre (Cu)", en: "Copper (Cu)" },
  mat_al: { ar: "ألمنيوم (Al)", fr: "Aluminium (Al)", en: "Aluminium (Al)" },

  // ---------- 1) أوم ----------
  ohm_title: { ar: "قانون أوم — حساب الجهد / التيار / المقاومة", fr: "Loi d'Ohm — tension / courant / résistance", en: "Ohm's Law — voltage / current / resistance" },
  ohm_hint: { ar: "أدخل أي قيمتين لحساب الباقي + القدرة", fr: "Entrez deux valeurs pour calculer le reste + puissance", en: "Enter any two values to compute the rest + power" },
  calculate: { ar: "حساب", fr: "Calculer", en: "Calculate" },

  // ---------- 2) هبوط الجهد ----------
  vd_title: { ar: "هبوط الجهد في الكابل", fr: "Chute de tension dans le câble", en: "Cable Voltage Drop" },
  vd_nominal_voltage: { ar: "الجهد الاسمي (Volt):", fr: "Tension nominale (V) :", en: "Nominal voltage (V):" },
  vd_nominal_current: { ar: "التيار (Ampere):", fr: "Courant (A) :", en: "Current (A):" },

  // ---------- 3) ك²س² ----------
  k2s2_title: { ar: "شرط ك²س² (السلامة الحرارية)", fr: "Condition K²S² (tenue thermique)", en: "K²S² Thermal Condition" },
  k2s2_k: { ar: "ثابت ك (K):", fr: "Constante k (K) :", en: "Constant k:" },
  k2s2_icc: { ar: "تيار القصر (A):", fr: "Courant de court-circuit (A) :", en: "Short-circuit current (A):" },
  k2s2_time: { ar: "زمن الفصل (ثانية):", fr: "Temps de coupure (s) :", en: "Clearing time (s):" },
  k2s2_result: { ar: "ك²×س² = {energy}\nإ²×ت = {demand}\n{status}", fr: "k²×s² = {energy}\nI²×t = {demand}\n{status}", en: "k²×s² = {energy}\nI²×t = {demand}\n{status}" },
  k2s2_ok: { ar: "✔ الشرط محقق — الموصل آمن", fr: "✔ Condition satisfaite — conducteur sûr", en: "✔ Condition met — conductor safe" },
  k2s2_bad: { ar: "✘ الشرط غير محقق — قلّص الزمن أو كبّر المقطع", fr: "✘ Condition non satisfaite — réduisez le temps ou augmentez la section", en: "✘ Condition not met — reduce time or increase section" },

  // ---------- 4) الليد ----------
  led_title: { ar: "حساب مقاومة الـ LED", fr: "Résistance de limitation LED", en: "LED Series Resistor" },
  led_source: { ar: "جهد المصدر (Volt):", fr: "Tension de source (V) :", en: "Source voltage (V):" },
  led_led: { ar: "جهد الـ LED (Volt):", fr: "Tension de la LED (V) :", en: "LED voltage (V):" },
  led_i: { ar: "تيار الـ LED (mA):", fr: "Courant LED (mA) :", en: "LED current (mA):" },

  // ---------- 5/6) الجهد والتيار ----------
  volt_title: { ar: "حساب الجهد من القدرة والتيار", fr: "Tension à partir de la puissance et du courant", en: "Voltage from power & current" },
  amp_title: { ar: "حساب التيار من القدرة والجهد", fr: "Courant à partir de la puissance et de la tension", en: "Current from power & voltage" },

  // ---------- 7) الانزلاق ----------
  slip_title: { ar: "انزلاق المحرك غير المتزامن", fr: "Glissement du moteur asynchrone", en: "Asynchronous Motor Slip" },
  slip_freq: { ar: "التردد (Hz):", fr: "Fréquence (Hz) :", en: "Frequency (Hz):" },
  slip_poles: { ar: "عدد الأقطاب:", fr: "Nombre de pôles :", en: "Number of poles:" },
  slip_rpm: { ar: "سرعة المحرك N (دورة/د):", fr: "Vitesse moteur N (tr/min) :", en: "Motor speed N (rpm):" },
  slip_pct: { ar: "الانزلاق g (٪):", fr: "Glissement g (%) :", en: "Slip g (%):" },
  slip_or: { ar: "— أدخل السرعة أو الانزلاق —", fr: "— entrez la vitesse OU le glissement —", en: "— enter speed OR slip —" },

  // ---------- 8) المقطع ----------
  sec_title: { ar: "حساب مقطع الكابل", fr: "Calcul de la section du câble", en: "Cable Cross-section" },
  sec_maxdrop: { ar: "هبوط الجهد الأقصى المسموح (٪):", fr: "Chute max admissible (%) :", en: "Max allowable drop (%):" },
  sec_none: { ar: "لا يوجد مقطع قياسي كافٍ ضمن القائمة.", fr: "Aucune section standard suffisante.", en: "No sufficient standard section." },

  // ---------- 9) ألوان المقاومات ----------
  res_title: { ar: "قراءة المقاومة من الألوان (IEC 60062)", fr: "Lecture résistance par code couleur (IEC 60062)", en: "Resistor Color Code (IEC 60062)" },
  res_bands_count: { ar: "عدد الحلقات:", fr: "Nombre d'anneaux :", en: "Number of bands:" },
  res_band: { ar: "الحلقة", fr: "Anneau", en: "Band" },
  res_digit: { ar: "رقم", fr: "Chiffre", en: "Digit" },
  res_mult: { ar: "المضاعف", fr: "Multiplicateur", en: "Multiplier" },
  res_tol: { ar: "التسامح", fr: "Tolérance", en: "Tolerance" },
  res_tcr: { ar: "معامل حراري TCR", fr: "Coeff. thermique TCR", en: "Temp. coeff. TCR" },
  res_blank: { ar: "-- فارغ --", fr: "-- vide --", en: "-- blank --" },
  res_calc: { ar: "حساب القيمة", fr: "Calculer la valeur", en: "Calculate value" },
  res_result: { ar: "القيمة: {val}\nالشكل المعياري: {norm}\nالتسامح: {tol}\nالمعامل الحراري: {tcr}", fr: "Valeur : {val}\nNormalisée : {norm}\nTolérance : {tol}\nCoefficient thermique : {tcr}", en: "Value: {val}\nNormalized: {norm}\nTolerance: {tol}\nTemp. coefficient: {tcr}" },

  // ---------- الألوان ----------
  color_black: { ar: "أسود", fr: "Noir", en: "Black" },
  color_brown: { ar: "بني", fr: "Brun", en: "Brown" },
  color_red: { ar: "أحمر", fr: "Rouge", en: "Red" },
  color_orange: { ar: "برتقالي", fr: "Orange", en: "Orange" },
  color_yellow: { ar: "أصفر", fr: "Jaune", en: "Yellow" },
  color_green: { ar: "أخضر", fr: "Vert", en: "Green" },
  color_blue: { ar: "أزرق", fr: "Bleu", en: "Blue" },
  color_violet: { ar: "بنفسجي", fr: "Violet", en: "Violet" },
  color_grey: { ar: "رمادي", fr: "Gris", en: "Grey" },
  color_white: { ar: "أبيض", fr: "Blanc", en: "White" },
  color_gold: { ar: "ذهبي", fr: "Or", en: "Gold" },
  color_silver: { ar: "فضي", fr: "Argent", en: "Silver" },

  // ---------- رسائل خطأ ----------
  err_two_values: { ar: "أدخل قيمتين على الأقل.", fr: "Entrez au moins deux valeurs.", en: "Enter at least two values." },
  err_positive: { ar: "يجب إدخال أرقام موجبة.", fr: "Entrez des nombres positifs.", en: "Enter positive numbers." },
  err_source_gt_led: { ar: "جهد المصدر يجب أن يكون أكبر من جهد الـ LED.", fr: "La tension source doit être supérieure à celle de la LED.", en: "Source voltage must exceed LED voltage." },
  err_freq_poles: { ar: "التردد وعدد الأقطاب كبيران من الصفر.", fr: "Fréquence et pôles doivent être > 0.", en: "Frequency and poles must be > 0." },
  err_rpm_negative: { ar: "السرعة لا يمكن أن تكون سالبة.", fr: "La vitesse ne peut pas être négative.", en: "Speed cannot be negative." },
  err_rpm_exceeds: { ar: "السرعة لا تتجاوز السرعة التزامنية.", fr: "La vitesse ne peut dépasser Ns.", en: "Speed cannot exceed Ns." },
  err_slip_range: { ar: "الانزلاق بين 0 و 100.", fr: "Glissement entre 0 et 100.", en: "Slip between 0 and 100." },
  err_rpm_or_slip: { ar: "أدخل السرعة أو الانزلاق.", fr: "Entrez la vitesse ou le glissement.", en: "Enter speed or slip." },
  err_res_first_black: { ar: "الحلقة الأولى لا يمكن أن تكون سوداء أو فارغة.", fr: "Le 1er anneau ne peut être noir ou vide.", en: "First band cannot be black or blank." },
  err_res_blank_last: { ar: "حلقة التسامح لا يمكن أن تكون فارغة.", fr: "L'anneau de tolérance ne peut être vide.", en: "Tolerance band cannot be blank." },

  // ---------- الصيغ (مساعدة) ----------
  help_ohm_formula: { ar: "U = R × I\nR = U / I\nI = U / R\nالقرية: P = U × I", fr: "U = R × I\nR = U / I\nI = U / R\nPuissance : P = U × I", en: "V = R × I\nR = V / I\nI = V / R\nPower: P = V × I" },
  help_ohm_fields: { ar: "- الجهد (Volt): فرق الجهد بين طرفي العنصر.\n- التيار (Ampere): شدة التيار المارّ.\n- المقاومة (أوم): مقاومة العنصر.\n\nأدخل أي قيمتين لحساب الثالث + القدرة.", fr: "- Tension (V) : différence de potentiel.\n- Courant (A) : intensité.\n- Résistance (Ω) : résistance.\n\nEntrez deux valeurs pour calculer la 3e + la puissance.", en: "- Voltage (V): potential difference.\n- Current (A): flowing intensity.\n- Resistance (Ω): component resistance.\n\nEnter two values to compute the 3rd + power." },
  help_vd_formula: { ar: "أحادي: ΔU = 2 × L × I × (ρ/S) × cosφ\nثلاثي: ΔU = √3 × L × I × (ρ/S) × cosφ\nغالبية التفاعل والنكد حسب NF C 15-100 / IEC 60364.", fr: "Monophasé : ΔU = 2 × L × I × (ρ/S) × cosφ\nTriphasé : ΔU = √3 × L × I × (ρ/S) × cosφ\nSelon NF C 15-100 / IEC 60364.", en: "Single: ΔV = 2 × L × I × (ρ/S) × cosφ\nThree: ΔV = √3 × L × I × (ρ/S) × cosφ\nPer NF C 15-100 / IEC 60364." },
  help_vd_fields: { ar: "- الجهد الاسمي: جهد الشبكة.\n- التيار: التيار المار بالكابل.\n- الطول: طول الكابل (م).\n- المقطع: مقطع الناقل (mm²).\n- Cos φ: معامل القدرة.\n- المادة: نحاس أو ألمنيوم.\n- النظام: أحادي أو ثلاثي الطور.", fr: "- Tension nominale : tension réseau.\n- Courant : courant dans le câble.\n- Longueur : longueur (m).\n- Section : section (mm²).\n- Cos φ : facteur de puissance.\n- Matériau : cuivre/aluminium.\n- Système : mono/triphasé.", en: "- Nominal voltage: network voltage.\n- Current: current in cable.\n- Length: cable length (m).\n- Section: conductor section (mm²).\n- Cos φ: power factor.\n- Material: copper/aluminium.\n- System: single/three phase." },
  help_k2s2_formula: { ar: "ك² × س² ≥ إ² × ت\nحيث ك=ثابت المادة، س=المقطع، إ=تيار القصر، ت=زمن القطع.", fr: "k² × s² ≥ I² × t\nk = constante, s = section, I = courant de court-circuit, t = temps.", en: "k² × s² ≥ I² × t\nk = constant, s = section, I = short-circuit current, t = time." },
  help_k2s2_fields: { ar: "- ثابت ك: ثابت المادة والعزل.\n- المقطع (mm²): مقطع موصل الحماية.\n- تيار القصر (A): تيار القصر المتوقع.\n- زمن الفصل (s): زمن قطع الحماية.", fr: "- Constante k : matériau/isolant.\n- Section (mm²) : conducteur PE.\n- Courant de court-circuit (A).\n- Temps de coupure (s).", en: "- Constant k: material/insulation.\n- Section (mm²): PE conductor.\n- Short-circuit current (A).\n- Clearing time (s)." },
  help_led_formula: { ar: "R = (U_src - U_led) / I_led\nالقدرة: P = (U_src - U_led)² / R", fr: "R = (U_src - U_led) / I_led\nPuissance : P = (U_src - U_led)² / R", en: "R = (V_src - V_led) / I_led\nPower: P = (V_src - V_led)² / R" },
  help_led_fields: { ar: "- جهد المصدر: جهد التغذية.\n- جهد الـ LED: هبوط الـ LED (غالباً 2-3.5V).\n- تيار الـ LED (mA): تيار التشغيل (غالباً 10-20mA).", fr: "- Tension source : alimentation.\n- Tension LED : chute (2-3,5V).\n- Courant LED (mA) : (10-20mA).", en: "- Source voltage: supply.\n- LED voltage: drop (2-3.5V).\n- LED current (mA): (10-20mA)." },
  help_volt_formula: { ar: "أحادي: U = P / (I × cosφ)\nثلاثي: U = P / (√3 × I × cosφ)", fr: "Monophasé : U = P / (I × cosφ)\nTriphasé : U = P / (√3 × I × cosφ)", en: "Single: V = P / (I × cosφ)\nThree: V = P / (√3 × I × cosφ)" },
  help_volt_fields: { ar: "- القدرة (W): القدرة الكهربائية.\n- التيار (A): شدة التيار.\n- Cos φ: معامل القدرة.\n- النظام: أحادي/ثلاثي الطور.", fr: "- Puissance (W).\n- Courant (A).\n- Cos φ : facteur de puissance.\n- Système : mono/triphasé.", en: "- Power (W).\n- Current (A).\n- Cos φ: power factor.\n- System: single/three." },
  help_amp_formula: { ar: "أحادي: I = P / (U × cosφ)\nثلاثي: I = P / (√3 × U × cosφ)", fr: "Monophasé : I = P / (U × cosφ)\nTriphasé : I = P / (√3 × U × cosφ)", en: "Single: I = P / (V × cosφ)\nThree: I = P / (√3 × V × cosφ)" },
  help_amp_fields: { ar: "- القدرة (W): القدرة الكهربائية.\n- الجهد (V): جهد الشبكة.\n- Cos φ: معامل القدرة.\n- النظام: أحادي/ثلاثي الطور.", fr: "- Puissance (W).\n- Tension (V).\n- Cos φ.\n- Système.", en: "- Power (W).\n- Voltage (V).\n- Cos φ.\n- System." },
  help_slip_formula: { ar: "Ns = (120 × f) / p\ng = ((Ns - N) / Ns) × 100\nfr = g × f", fr: "Ns = (120 × f) / p\ng = ((Ns - N) / Ns) × 100\nfr = g × f", en: "Ns = (120 × f) / p\ng = ((Ns - N) / Ns) × 100\nfr = g × f" },
  help_slip_fields: { ar: "- التردد (Hz): تردد الشبكة (50 أو 60).\n- عدد الأقطاب: 2، 4، 6...\n- أدخل السرعة N أو الانزلاق g٪.", fr: "- Fréquence (Hz) : 50 ou 60.\n- Nombre de pôles : 2, 4, 6...\n- Entrez N ou g%.", en: "- Frequency (Hz): 50 or 60.\n- Number of poles: 2, 4, 6...\n- Enter N or g%." },
  help_section_formula: { ar: "S = (b × ρ × L × I × cosφ × 100) / (ΔU٪ × U)\nb=2 أحادي، b=√3 ثلاثي.", fr: "S = (b × ρ × L × I × cosφ × 100) / (ΔU% × U)\nb=2 mono, b=√3 tri.", en: "S = (b × ρ × L × I × cosφ × 100) / (ΔU% × V)\nb=2 single, b=√3 three." },
  help_section_fields: { ar: "- الجهد الاسمي (V).\n- التيار (A).\n- الطول (m).\n- Cos φ.\n- الهبوط الأقصى (٪).\n- المادة: نحاس/ألمنيوم.\n- النظام.", fr: "- Tension nominale (V).\n- Courant (A).\n- Longueur (m).\n- Cos φ.\n- Chute max (%).\n- Matériau.\n- Système.", en: "- Nominal voltage (V).\n- Current (A).\n- Length (m).\n- Cos φ.\n- Max drop (%).\n- Material.\n- System." },
  help_res_formula: { ar: "4 حلقات: رقم، رقم، مضاعف، تسامح\n5 حلقات: رقم، رقم، رقم، مضاعف، تسامح\n6 حلقات: 3 أرقام + مضاعف + تسامح + TCR\n\nالقيمة = (الأرقام) × المضاعف", fr: "4 anneaux : chiffre, chiffre, mult., tol.\n5 anneaux : 3 chiffres + mult. + tol.\n6 anneaux : 3 chiffres + mult. + tol. + TCR\n\nValeur = (chiffres) × multiplicateur", en: "4 bands: digit, digit, mult, tol\n5 bands: 3 digits + mult + tol\n6 bands: 3 digits + mult + tol + TCR\n\nValue = (digits) × multiplier" },
  help_res_fields: { ar: "- عدد الحلقات: 4/5/6.\n- حلقة الرقم: لون يمثل رقماً (0-9).\n- المضاعف: ذهبي=÷10، أسود=×1، بني=×10...\n- التسامح: مجموعة (±1%, ±5%...).\n- TCR (6 حلقة): المعامل الحراري.", fr: "- Nombre d'anneaux : 4/5/6.\n- Chiffre : couleur = 0-9.\n- Multiplicateur : or=÷10, noir=×1...\n- Tolérance (±1%, ±5%...).\n- TCR (6 anneaux).", en: "- Number of bands: 4/5/6.\n- Digit: color = 0-9.\n- Multiplier: gold=÷10, black=×1...\n- Tolerance (±1%, ±5%...).\n- TCR (6 bands)." },
};

const LANG = { current: "ar" };

// قيم الألوان (مطابقة للمحرك الأصلي)
const COLOR_DIGIT = { black: 0, brown: 1, red: 2, orange: 3, yellow: 4, green: 5, blue: 6, violet: 7, grey: 8, white: 9 };
const COLOR_MULT = { black: 1, brown: 10, red: 100, orange: 1e3, yellow: 1e4, green: 1e5, blue: 1e6, violet: 1e7, grey: 1e8, white: 1e9, gold: 0.1, silver: 0.01 };
const COLOR_TOL = { brown: 1.0, red: 2.0, green: 0.5, blue: 0.25, violet: 0.1, grey: 0.05, gold: 5.0, silver: 10.0, none: 20.0 };
const COLOR_TCR = { brown: 100, red: 50, orange: 15, yellow: 25, blue: 10, violet: 5 };
const COLOR_HEX = { black: "#000000", brown: "#6b3a12", red: "#d32f2f", orange: "#ef6c00", yellow: "#fbc02d", green: "#388e3c", blue: "#1565c0", violet: "#6a1b9a", grey: "#757575", white: "#f5f5f5", gold: "#c9a227", silver: "#b0bec5" };
const COLOR_KEYS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white", "gold", "silver"];
const TOL_KEYS = ["brown", "red", "green", "blue", "violet", "grey", "gold", "silver", "none"];
const TCR_KEYS = ["brown", "red", "orange", "yellow", "blue", "violet"];

const MODULES = [
  { key: "ohm", title: "mod_ohm", render: renderOhm },
  { key: "vd", title: "mod_vd", render: renderVoltageDrop },
  { key: "k2s2", title: "mod_k2s2", render: renderK2S2 },
  { key: "led", title: "mod_led", render: renderLed },
  { key: "volt", title: "mod_volt", render: renderVolt },
  { key: "amp", title: "mod_amp", render: renderAmp },
  { key: "slip", title: "mod_slip", render: renderSlip },
  { key: "section", title: "mod_section", render: renderSection },
  { key: "res", title: "mod_res", render: renderResistor },
];

let state = {}; // يحوي قيم الحقول الحالية بين إعادة الرسم

// =============================================================================
// أدوات
// =============================================================================
function tr(key, kwargs) {
  const t = TRANSLATIONS[key] ? TRANSLATIONS[key][LANG.current] : key;
  if (kwargs) {
    return t.replace(/\{(\w+)\}/g, (m, k) => (kwargs[k] !== undefined ? kwargs[k] : m));
  }
  return t;
}

function $(sel, root) { return (root || document).querySelector(sel); }
function $$(sel, root) { return Array.from((root || document).querySelectorAll(sel)); }

function num(v) {
  if (typeof v === "number") return v;
  return parseFloat(String(v).replace(/,/g, "."));
}
function isPos(v) { return typeof v === "number" && isFinite(v) && v > 0; }
function isNonNeg(v) { return typeof v === "number" && isFinite(v) && v >= 0; }

function field(label, id, val, placeholder) {
  return `
    <div class="field">
      <label for="${id}">${label}</label>
      <input type="text" id="${id}" value="${val || ""}" placeholder="${placeholder || ""}" inputmode="decimal">
    </div>`;
}

function selectField(label, id, options, val) {
  let opts = options.map(o => `<option value="${o.value}" ${o.value === val ? "selected" : ""}>${o.label}</option>`).join("");
  return `
    <div class="field">
      <label for="${id}">${label}</label>
      <select id="${id}">${opts}</select>
    </div>`;
}

function radioField(label, id, options, val) {
  let opts = options.map(o =>
    `<label><input type="radio" name="${id}" value="${o.value}" ${o.value === val ? "checked" : ""}>${o.label}</label>`
  ).join("");
  return `<div class="field"><label>${label}</label><div class="radio-group">${opts}</div></div>`;
}

function resultBox(html, isError) {
  return `<div class="result ${isError ? "error" : ""}">${html}</div>`;
}

function showError(msg) {
  $("#page").insertAdjacentHTML("beforeend", resultBox(escapeHtml(msg), true));
}

function escapeHtml(s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function errBoxDiv() {
  // إزالة أي نتيجة سابقة في الصفحة
  $$("#page .result").forEach(e => e.remove());
}

function clearResults() { $$("#page .result").forEach(e => e.remove()); }

function helpBtn() {
  return `<button class="help-btn" onclick="openHelp('${state.module}')">❓ ${tr("help_btn")}</button>`;
}

// معالجة أخطاء input
function getPos(id, errMsg) {
  const v = num($("#" + id).value);
  if (!isPos(v)) throw new Error(errMsg);
  return v;
}
function getNonNeg(id, errMsg) {
  const v = num($("#" + id).value);
  if (typeof v !== "number" || !isFinite(v) || v < 0) throw new Error(errMsg);
  return v;
}

// معامل √3
const SQRT3 = Math.sqrt(3);

// =============================================================================
// محرك الحساب (مطابق للمحرك الأصلي في بايثون)
// =============================================================================
function engineOhm(kw) {
  const { v, i, r, p } = kw;
  if (v && i) return { R: v / i, P: v * i };
  if (p && v) return { I: p / v, R: (v * v) / p };
  if (p && i) return { V: p / i, R: p / (i * i) };
  if (r && i) return { V: r * i, P: r * (i * i) };
  throw new Error(tr("err_two_values"));
}

function engineVoltageDrop(opts) {
  const { is_three_phase, current, length, section, cos_phi, material, voltage } = opts;
  const rho = material === "Cu" ? 0.0225 : 0.036;
  const b = is_three_phase ? SQRT3 : 2.0;
  const cos = Math.min(Math.max(cos_phi, 0), 1);
  const sin = Math.sqrt(Math.max(1 - cos * cos, 0));
  const x = 0.08 / 1000;
  const r_res = rho * (length / section);
  const du = b * current * (r_res * cos + (x * length) * sin);
  const pct = (du / voltage) * 100;
  return { delta_u: round2(du), percentage: round2(pct), resistance: Math.round(r_res * 10000) / 10000 };
}

function engineK2S2(section, k) {
  return Math.pow(k * section, 2);
}

function engineVoltageFromPower(p, i, cos_phi, three) {
  const cos = Math.min(Math.max(cos_phi || 1.0, 0.01), 1.0);
  if (three) {
    const u = p / (SQRT3 * i * cos);
    return { U: round2(u), V_phase: round2(u / SQRT3) };
  }
  return { V: round2(p / (i * cos)), V_phase: null };
}

function engineCurrentFromPower(p, v, cos_phi, three) {
  const cos = Math.min(Math.max(cos_phi || 1.0, 0.01), 1.0);
  const i = three ? p / (SQRT3 * v * cos) : p / (v * cos);
  return { I: round2(i) };
}

function engineSlip(frequency, poles, rpm, slip_pct) {
  if (poles <= 0 || frequency <= 0) throw new Error(tr("err_freq_poles"));
  const ns = (120.0 * frequency) / poles;
  const res = { Ns: round1(ns) };
  let g_frac;
  if (rpm !== undefined && rpm !== null && String(rpm) !== "") {
    if (rpm < 0) throw new Error(tr("err_rpm_negative"));
    if (rpm > ns) throw new Error(tr("err_rpm_exceeds"));
    g_frac = (ns - rpm) / ns;
    res.N = round1(rpm);
  } else if (slip_pct !== undefined && slip_pct !== null && String(slip_pct) !== "") {
    if (slip_pct < 0 || slip_pct >= 100) throw new Error(tr("err_slip_range"));
    g_frac = slip_pct / 100.0;
    res.N = round1(ns * (1 - g_frac));
  } else {
    throw new Error(tr("err_rpm_or_slip"));
  }
  res.g = round2(g_frac * 100);
  res.f_rotor = round2(frequency * g_frac);
  return res;
}

function engineSection(is_three_phase, voltage, current, length, cos_phi, material, max_drop_pct) {
  const rho = material === "Cu" ? 0.0225 : 0.036;
  const b = is_three_phase ? SQRT3 : 2.0;
  const cos = Math.min(Math.max(cos_phi, 0), 1);
  const s_min = (b * current * length * rho * cos) / ((max_drop_pct / 100.0) * voltage);
  const STANDARD = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240, 300];
  const res = { s_min: round2(s_min), suggested: null };
  const start = STANDARD.findIndex(s => s >= s_min);
  if (start === -1) return res;
  for (let i = start; i < STANDARD.length; i++) {
    const s = STANDARD[i];
    const check = engineVoltageDrop({ is_three_phase, current, length, section: s, cos_phi: cos, material, voltage });
    if (check.percentage <= max_drop_pct + 1e-9) {
      res.suggested = s;
      res.actual_drop_pct = check.percentage;
      res.resistance = check.resistance;
      break;
    }
  }
  return res;
}

function engineResistor(bands) {
  const main = bands.filter(c => c !== "none" && c !== "");
  if (main.length < 3) throw new Error(tr("err_res_first_black"));
  if (main[0] === "black") throw new Error(tr("err_res_first_black"));
  if (bands.length === 4) {
    const [d1, d2, mult, tol] = bands;
    if (!(d1 in COLOR_DIGIT) || !(d2 in COLOR_DIGIT)) throw new Error(tr("err_res_first_black"));
    if (!(mult in COLOR_MULT)) throw new Error(tr("err_res_first_black"));
    const value = (COLOR_DIGIT[d1] * 10 + COLOR_DIGIT[d2]) * COLOR_MULT[mult];
    return { value, tolerance: COLOR_TOL[tol] !== undefined ? COLOR_TOL[tol] : 20.0, tcr: null };
  } else if (bands.length === 5) {
    const [d1, d2, d3, mult, tol] = bands;
    if (!(d1 in COLOR_DIGIT) || !(d2 in COLOR_DIGIT) || !(d3 in COLOR_DIGIT)) throw new Error(tr("err_res_first_black"));
    if (!(mult in COLOR_MULT)) throw new Error(tr("err_res_first_black"));
    const value = (COLOR_DIGIT[d1] * 100 + COLOR_DIGIT[d2] * 10 + COLOR_DIGIT[d3]) * COLOR_MULT[mult];
    return { value, tolerance: COLOR_TOL[tol] !== undefined ? COLOR_TOL[tol] : 20.0, tcr: null };
  } else if (bands.length === 6) {
    const [d1, d2, d3, mult, tol, tcr] = bands;
    if (!(d1 in COLOR_DIGIT) || !(d2 in COLOR_DIGIT) || !(d3 in COLOR_DIGIT)) throw new Error(tr("err_res_first_black"));
    if (!(mult in COLOR_MULT)) throw new Error(tr("err_res_first_black"));
    const value = (COLOR_DIGIT[d1] * 100 + COLOR_DIGIT[d2] * 10 + COLOR_DIGIT[d3]) * COLOR_MULT[mult];
    return { value, tolerance: COLOR_TOL[tol] !== undefined ? COLOR_TOL[tol] : 20.0, tcr: COLOR_TCR[tcr] !== undefined ? COLOR_TCR[tcr] : null };
  }
  throw new Error(tr("err_res_first_black"));
}

function normalizeResistance(ohms) {
  if (ohms >= 1e6) return round2(ohms / 1e6) + " MΩ";
  if (ohms >= 1e3) return round2(ohms / 1e3) + " kΩ";
  if (ohms >= 1) return round2(ohms) + " Ω";
  return round2(ohms * 1e3) + " mΩ";
}

function round2(v) { return Math.round(v * 100) / 100; }
function round1(v) { return Math.round(v * 10) / 10; }

// =============================================================================
// بناء الواجهات
// =============================================================================
function card(title) {
  return `<div class="card">
    <div class="page-title"><h2>${title}</h2>${helpBtn()}</div>`;
}

function renderOhm() {
  clearResultState();
  const s = state.ohm || {};
  $("#page").innerHTML = card(tr("ohm_title")) + `
    <p style="opacity:.8;margin-bottom:14px">${tr("ohm_hint")}</p>
    <div class="row2">
      ${field(tr("lbl_voltage"), "ohm_v", s.v, "230")}
      ${field(tr("lbl_current"), "ohm_i", s.i, "10")}
    </div>
    <div class="row2">
      ${field(tr("lbl_resistance"), "ohm_r", s.r, "23")}
      ${field(tr("lbl_power"), "ohm_p", s.p, "2300")}
    </div>
    <div class="btn-row"><button class="btn-main" onclick="calcOhm()">${tr("calculate")}</button></div>
  </div>`;
}

function calcOhm() {
  clearResults();
  try {
    const v = $("#ohm_v").value, i = $("#ohm_i").value, r = $("#ohm_r").value, p = $("#ohm_p").value;
    const kw = {};
    if (v !== "") kw.v = getPosN("ohm_v", "V");
    if (i !== "") kw.i = getPosN("ohm_i", "A");
    if (r !== "") kw.r = getPosN("ohm_r", "Ω");
    if (p !== "") kw.p = getPosN("ohm_p", "W");
    const res = engineOhm(kw);
    let lines = [];
    if (res.V !== undefined) lines.push("U = " + round2(res.V) + " V");
    if (res.V === undefined && res.U !== undefined) lines.push("U = " + round2(res.U) + " V");
    if (res.I !== undefined) lines.push("I = " + round2(res.I) + " A");
    if (res.R !== undefined) lines.push("R = " + round2(res.R) + " Ω");
    if (res.P !== undefined) lines.push("P = " + round2(res.P) + " W");
    saveState("ohm", { v, i, r, p });
    $("#page").insertAdjacentHTML("beforeend", resultBox(lines.join("<br>")));
  } catch (e) { showError(e.message); }
}

function getPosN(id, label) {
  const v = num($("#" + id).value);
  if (!isPos(v)) throw new Error(tr("err_positive"));
  return v;
}

function renderVoltageDrop() {
  clearResultState();
  const s = state.vd || {};
  $("#page").innerHTML = card(tr("vd_title")) + `
    <div class="row2">
      ${field(tr("vd_nominal_voltage"), "vd_v", s.v, "230")}
      ${field(tr("vd_nominal_current"), "vd_i", s.i, "10")}
    </div>
    <div class="row2">
      ${field(tr("lbl_length"), "vd_l", s.l, "50")}
      ${field(tr("lbl_section"), "vd_s", s.s, "2.5")}
    </div>
    <div class="row2">
      ${field(tr("lbl_cosphi"), "vd_cos", s.cos, "0.9")}
      ${selectField(tr("lbl_material"), "vd_mat", [
        { value: "Cu", label: tr("mat_cu") }, { value: "Al", label: tr("mat_al") }
      ], s.mat || "Cu")}
    </div>
    ${radioField(tr("lbl_system"), "vd_sys", [
      { value: "single", label: tr("sys_single") }, { value: "three", label: tr("sys_three") }
    ], s.sys || "single")}
    <div class="btn-row"><button class="btn-main" onclick="calcVoltageDrop()">${tr("calc_btn")}</button></div>
  </div>`;
}

function calcVoltageDrop() {
  clearResults();
  try {
    const v = getPosN("vd_v", "V"), i = getPosN("vd_i", "A");
    const l = getPosN("vd_l", "m"), s = getPosN("vd_s", "mm²");
    const cos = num($("#vd_cos").value);
    if (typeof cos !== "number" || !isFinite(cos) || cos < 0 || cos > 1) throw new Error(tr("err_positive"));
    const mat = $("#vd_mat").value;
    const three = $("input[name='vd_sys']:checked").value === "three";
    const res = engineVoltageDrop({ is_three_phase: three, current: i, length: l, section: s, cos_phi: cos, material: mat, voltage: v });
    saveState("vd", { v: $("#vd_v").value, i: $("#vd_i").value, l: $("#vd_l").value, s: $("#vd_s").value, cos: $("#vd_cos").value, mat, sys: three ? "three" : "single" });
    const result = `ΔU = ${res.delta_u} V<br>ΔU% = ${res.percentage} %<br>R = ${res.resistance} Ω`;
    $("#page").insertAdjacentHTML("beforeend", resultBox(result));
  } catch (e) { showError(e.message); }
}

function renderK2S2() {
  clearResultState();
  const s = state.k2s2 || {};
  $("#page").innerHTML = card(tr("k2s2_title")) + `
    <div class="row2">
      ${field(tr("lbl_section"), "k2s2_s", s.s, "2.5")}
      ${field(tr("k2s2_k"), "k2s2_k", s.k, "115")}
    </div>
    <div class="row2">
      ${field(tr("k2s2_icc"), "k2s2_i", s.i, "5000")}
      ${field(tr("k2s2_time"), "k2s2_t", s.t, "0.1")}
    </div>
    <div class="btn-row"><button class="btn-main" onclick="calcK2S2()">${tr("calc_btn")}</button></div>
  </div>`;
}

function calcK2S2() {
  clearResults();
  try {
    const s = getPosN("k2s2_s", "mm²"), k = getPosN("k2s2_k", "K");
    const i = getPosN("k2s2_i", "A"), t = getPosN("k2s2_t", "s");
    const energy = engineK2S2(s, k);
    const demand = i * i * t;
    const ok = energy >= demand;
    const status = ok
      ? `<span class="ok">${tr("k2s2_ok")}</span>`
      : `<span class="bad">${tr("k2s2_bad")}</span>`;
    saveState("k2s2", { s: $("#k2s2_s").value, k: $("#k2s2_k").value, i: $("#k2s2_i").value, t: $("#k2s2_t").value });
    $("#page").insertAdjacentHTML("beforeend", resultBox(tr("k2s2_result", { energy: round2(energy), demand: round2(demand), status })));
  } catch (e) { showError(e.message); }
}

function renderLed() {
  clearResultState();
  const s = state.led || {};
  $("#page").innerHTML = card(tr("led_title")) + `
    <div class="row3">
      ${field(tr("led_source"), "led_src", s.src, "12")}
      ${field(tr("led_led"), "led_led", s.led, "2.1")}
      ${field(tr("led_i"), "led_i", s.i, "20")}
    </div>
    <div class="btn-row"><button class="btn-main" onclick="calcLed()">${tr("calc_btn")}</button></div>
  </div>`;
}

function calcLed() {
  clearResults();
  try {
    const src = getPosN("led_src", "V"), led = getPosN("led_led", "V"), i = getPosN("led_i", "mA");
    if (src <= led) throw new Error(tr("err_source_gt_led"));
    const i_a = i / 1000.0;
    const r = (src - led) / i_a;
    const p = Math.pow(src - led, 2) / r;
    saveState("led", { src: $("#led_src").value, led: $("#led_led").value, i: $("#led_i").value });
    $("#page").insertAdjacentHTML("beforeend", resultBox(`R = ${round2(r)} Ω<br>P = ${round2(p)} W`));
  } catch (e) { showError(e.message); }
}

function renderVolt() {
  clearResultState();
  const s = state.volt || {};
  $("#page").innerHTML = card(tr("volt_title")) + `
    <div class="row2">
      ${field(tr("lbl_power"), "vt_p", s.p, "5000")}
      ${field(tr("lbl_current"), "vt_i", s.i, "25")}
    </div>
    <div class="row2">
      ${field(tr("lbl_cosphi"), "vt_cos", s.cos, "0.9")}
    </div>
    ${radioField(tr("lbl_system"), "vt_sys", [
      { value: "single", label: tr("sys_single") }, { value: "three", label: tr("sys_three") }
    ], s.sys || "single")}
    <div class="btn-row"><button class="btn-main" onclick="calcVolt()">${tr("calc_btn")}</button></div>
  </div>`;
}

function calcVolt() {
  clearResults();
  try {
    const p = getPosN("vt_p", "W"), i = getPosN("vt_i", "A");
    const cos = num($("#vt_cos").value);
    if (typeof cos !== "number" || !isFinite(cos) || cos < 0 || cos > 1) throw new Error(tr("err_positive"));
    const three = $("input[name='vt_sys']:checked").value === "three";
    const res = engineVoltageFromPower(p, i, cos, three);
    saveState("volt", { p: $("#vt_p").value, i: $("#vt_i").value, cos: $("#vt_cos").value, sys: three ? "three" : "single" });
    let html;
    if (three) html = `U = ${res.U} V<br>V_phase = ${res.V_phase} V`;
    else html = `U = ${res.V} V`;
    $("#page").insertAdjacentHTML("beforeend", resultBox(html));
  } catch (e) { showError(e.message); }
}

function renderAmp() {
  clearResultState();
  const s = state.amp || {};
  $("#page").innerHTML = card(tr("amp_title")) + `
    <div class="row2">
      ${field(tr("lbl_power"), "ap_p", s.p, "5000")}
      ${field(tr("lbl_voltage"), "ap_v", s.v, "230")}
    </div>
    <div class="row2">
      ${field(tr("lbl_cosphi"), "ap_cos", s.cos, "0.9")}
    </div>
    ${radioField(tr("lbl_system"), "ap_sys", [
      { value: "single", label: tr("sys_single") }, { value: "three", label: tr("sys_three") }
    ], s.sys || "single")}
    <div class="btn-row"><button class="btn-main" onclick="calcAmp()">${tr("calc_btn")}</button></div>
  </div>`;
}

function calcAmp() {
  clearResults();
  try {
    const p = getPosN("ap_p", "W"), v = getPosN("ap_v", "V");
    const cos = num($("#ap_cos").value);
    if (typeof cos !== "number" || !isFinite(cos) || cos < 0 || cos > 1) throw new Error(tr("err_positive"));
    const three = $("input[name='ap_sys']:checked").value === "three";
    const res = engineCurrentFromPower(p, v, cos, three);
    saveState("amp", { p: $("#ap_p").value, v: $("#ap_v").value, cos: $("#ap_cos").value, sys: three ? "three" : "single" });
    $("#page").insertAdjacentHTML("beforeend", resultBox(`I = ${res.I} A`));
  } catch (e) { showError(e.message); }
}

function renderSlip() {
  clearResultState();
  const s = state.slip || {};
  $("#page").innerHTML = card(tr("slip_title")) + `
    <div class="row2">
      ${field(tr("slip_freq"), "slp_f", s.f, "50")}
      ${field(tr("slip_poles"), "slp_p", s.p, "4")}
    </div>
    <div class="row2">
      ${field(tr("slip_rpm"), "slp_n", s.n, "")}
      ${field(tr("slip_pct"), "slp_g", s.g, "")}
    </div>
    <p style="opacity:.7;margin-bottom:14px">${tr("slip_or")}</p>
    <div class="btn-row"><button class="btn-main" onclick="calcSlip()">${tr("calc_btn")}</button></div>
  </div>`;
}

function calcSlip() {
  clearResults();
  try {
    const f = getPosN("slp_f", "Hz"), p = getPosN("slp_p", "pôles");
    const nv = $("#slp_n").value, gv = $("#slp_g").value;
    let rpm, slip;
    if (nv !== "") { rpm = num(nv); if (!isNonNeg(rpm)) throw new Error(tr("err_rpm_negative")); }
    if (gv !== "") { slip = num(gv); }
    const res = engineSlip(f, p, rpm, slip);
    saveState("slip", { f: $("#slp_f").value, p: $("#slp_p").value, n: nv, g: gv });
    let html = `Ns = ${res.Ns} tr/min<br>N = ${res.N} tr/min<br>g = ${res.g} %<br>fr = ${res.f_rotor} Hz`;
    $("#page").insertAdjacentHTML("beforeend", resultBox(html));
  } catch (e) { showError(e.message); }
}

function renderSection() {
  clearResultState();
  const s = state.section || {};
  $("#page").innerHTML = card(tr("sec_title")) + `
    <div class="row2">
      ${field(tr("vd_nominal_voltage"), "sc_v", s.v, "230")}
      ${field(tr("vd_nominal_current"), "sc_i", s.i, "25")}
    </div>
    <div class="row2">
      ${field(tr("lbl_length"), "sc_l", s.l, "50")}
      ${field(tr("sec_maxdrop"), "sc_d", s.d, "3")}
    </div>
    <div class="row2">
      ${field(tr("lbl_cosphi"), "sc_cos", s.cos, "0.9")}
      ${selectField(tr("lbl_material"), "sc_mat", [
        { value: "Cu", label: tr("mat_cu") }, { value: "Al", label: tr("mat_al") }
      ], s.mat || "Cu")}
    </div>
    ${radioField(tr("lbl_system"), "sc_sys", [
      { value: "single", label: tr("sys_single") }, { value: "three", label: tr("sys_three") }
    ], s.sys || "single")}
    <div class="btn-row"><button class="btn-main" onclick="calcSection()">${tr("calc_btn")}</button></div>
  </div>`;
}

function calcSection() {
  clearResults();
  try {
    const v = getPosN("sc_v", "V"), i = getPosN("sc_i", "A"), l = getPosN("sc_l", "m");
    const d = getPosN("sc_d", "%"), cos = num($("#sc_cos").value);
    if (typeof cos !== "number" || !isFinite(cos) || cos < 0 || cos > 1) throw new Error(tr("err_positive"));
    const mat = $("#sc_mat").value;
    const three = $("input[name='sc_sys']:checked").value === "three";
    const res = engineSection(three, v, i, l, cos, mat, d);
    saveState("section", { v: $("#sc_v").value, i: $("#sc_i").value, l: $("#sc_l").value, d: $("#sc_d").value, cos: $("#sc_cos").value, mat, sys: three ? "three" : "single" });
    let html = `S_min = ${res.s_min} mm²`;
    if (res.suggested) html += `<br>S_moyenne recommandée = ${res.suggested} mm²<br>ΔU réel = ${res.actual_drop_pct} %<br>R = ${res.resistance} Ω`;
    else html += `<br>${tr("sec_none") || "—"}`;
    $("#page").insertAdjacentHTML("beforeend", resultBox(html));
  } catch (e) { showError(e.message); }
}

let resState = { count: 4, values: {} };

function renderResistor() {
  clearResultState();
  const s = resState.count || 4;
  $("#page").innerHTML = card(tr("res_title")) + `
    <div class="field">
      <label>${tr("res_bands_count")}</label>
      <select id="res_count" onchange="resChangeBands(this.value)">
        ${[4, 5, 6].map(n => `<option value="${n}" ${n === s ? "selected" : ""}>${n}</option>`).join("")}
      </select>
    </div>
    <div class="color-band-preview" id="bandPreview"></div>
    <div id="bandsRow"></div>
    <div class="btn-row"><button class="btn-main" onclick="calcResistor()">${tr("res_calc")}</button></div>
  </div>`;
  resBuildBands(s);
}

function bandLabel(i, count) {
  // digit, digit, ..., multiplier, tolerance (التسامح), tcr (فقط 6)
  const digitCount = count === 4 ? 2 : 3;
  if (i === digitCount) return tr("res_mult");
  if (i < digitCount) return tr("res_digit") + " " + (i + 1);
  if (count === 6 && i === count - 1) return tr("res_tcr");
  return tr("res_tol");
}

function bandKeys(i, count) {
  const digitCount = count === 4 ? 2 : 3;
  if (i === digitCount) return COLOR_KEYS;
  if (i < digitCount) return COLOR_KEYS.filter(k => k !== "gold" && k !== "silver");
  if (count === 6 && i === count - 1) return TCR_KEYS;
  return TOL_KEYS;
}

function resChangeBands(n) {
  resState.count = parseInt(n, 10) || 4;
  resState.values = {};
  resBuildBands(resState.count);
}

function resBuildBands(count) {
  const rows = $("#bandsRow");
  if (!rows) return;
  let html = "";
  html += `<div class="row3">`;
  let j = 0;
  const digitCount = count === 4 ? 2 : 3;
  // أول مجموعة: الأرقام
  for (let i = 0; i < digitCount; i++) {
    html += bandSelect(i, bandLabel(i, count), bandKeys(i, count), j++);
  }
  html += `</div><div class="row3">`;
  // المضاعف
  html += bandSelect(digitCount, bandLabel(digitCount, count), bandKeys(digitCount, count), j++);
  // التسامح
  html += bandSelect(digitCount + 1, bandLabel(digitCount + 1, count), bandKeys(digitCount + 1, count), j++);
  // TCR (فقط 6)
  if (count === 6) html += bandSelect(5, tr("res_tcr"), bandKeys(5, count), j++);
  else html += `<div class="field"><label>&nbsp;</label><div></div></div>`;
  html += `</div>`;
  rows.innerHTML = html;
  $('#bandPreview').className = 'color-band-preview' + (count >= 5 ? ' dark' : '');
  updateBandPreview(count);
}

function bandSelect(idx, label, keys, pos) {
  const saved = resState.values[pos];
  const opts = keys.map(k => `<option value="${k}" style="background:#fff;color:#000">${k === "none" ? tr("res_blank") : tr("color_" + k)}</option>`).join("");
  return `
    <div class="field">
      <label>${label}</label>
      <select id="res_b${idx}" onchange="updateBandPreview(${resState.count})">
        ${opts}
      </select>
    </div>`;
}

function updateBandPreview(count) {
  const prev = $("#bandPreview");
  if (!prev) return;
  const digitCount = count === 4 ? 2 : 3;
  let html = "";
  for (let i = 0; i < count; i++) {
    const sel = $("#res_b" + i);
    const v = sel ? sel.value : "none";
    let color;
    if (v === "none" || v === "") color = "rgba(255,255,255,0.35)";
    else {
      const hex = COLOR_HEX[v] || "#cccccc";
      color = `${hex} 0 100%`;
    }
    html += `<div class="band-slot" style="background:${color}"></div>`;
  }
  prev.innerHTML = html;
}

function calcResistor() {
  clearResults();
  try {
    const count = resState.count;
    const bands = [];
    for (let i = 0; i < count; i++) {
      const sel = $("#res_b" + i);
      bands.push(sel ? sel.value : "none");
    }
    // التحقق: التسامح لا يمكن أن يكون فارغاً
    const main = bands.filter(c => c !== "none" && c !== "");
    if (main.length < count) throw new Error(tr("err_res_blank_last"));
    const res = engineResistor(bands);
    const tol = res.tolerance ? "±" + res.tolerance + "%" : "—";
    const tcr = res.tcr !== null && res.tcr !== undefined ? res.tcr + " ppm/°C" : "—";
    const val = round2(res.value) + " Ω";
    resState.values = {};
    $("#page").insertAdjacentHTML("beforeend", resultBox(tr("res_result", {
      val, norm: normalizeResistance(res.value), tol, tcr
    })));
  } catch (e) { showError(e.message); }
}

// حالة الحقول لكل وحدة
function clearResultState() {}

function saveState(module, values) {
  state[module] = values;
}

// =============================================================================
// المساعدة
// =============================================================================
function openHelp(module) {
  const f = tr("help_" + module + "_formula");
  const d = tr("help_" + module + "_fields");
  $("#helpModal").classList.add("open");
  $("#helpBox").innerHTML = `
    <h3>${tr("help_title")}</h3>
    <div class="help-sec">
      <h4>${tr("help_formula")}</h4>
      <pre>${escapeHtml(f)}</pre>
    </div>
    <div class="help-sec">
      <h4>${tr("help_fields")}</h4>
      <pre>${escapeHtml(d)}</pre>
    </div>
    <button id="helpClose" onclick="closeHelp()">${tr("close")}</button>`;
}

function closeHelp() {
  $("#helpModal").classList.remove("open");
}

// =============================================================================
// التنقل واللغة
// =============================================================================
function renderMenu(activeKey) {
  const menu = $("#menu");
  menu.innerHTML = MODULES.map(m =>
    `<button class="menu-item ${m.key === activeKey ? "active" : ""}" onclick="navigate('${m.key}')">${tr(m.title)}</button>`
  ).join("");
}

function navigate(key) {
  state.module = key;
  renderMenu(key);
  const mod = MODULES.find(m => m.key === key);
  $("#page").innerHTML = "";
  mod.render();
}

function applyLang(lang) {
  LANG.current = lang;
  document.documentElement.lang = lang;
  document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";
  $("#appTitle").textContent = tr("app_title");
  $$(".lang-btn").forEach(b => {
    b.classList.toggle("active", b.dataset.lang === lang);
  });
  renderMenu(state.module || MODULES[0].key);
  const mod = MODULES.find(m => m.key === state.module);
  if (mod) mod.render();
  // إعادة فتح المساعدة إن كانت مفتوحة
  if ($("#helpModal").classList.contains("open") && state.module) {
    openHelp(state.module);
  }
}

// =============================================================================
// الإقلاع
// =============================================================================
document.addEventListener("DOMContentLoaded", () => {
  // خلفية الحوار
  const modal = document.createElement("div");
  modal.id = "helpModal";
  modal.innerHTML = `<div id="helpBox"></div>`;
  document.body.appendChild(modal);
  modal.addEventListener("click", (e) => {
    if (e.target === modal) closeHelp();
  });

  $$(".lang-btn").forEach(b => b.addEventListener("click", () => applyLang(b.dataset.lang)));

  state.module = "ohm";
  navigate("ohm");
});