import sys
import math
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QStackedWidget, QListWidget,
    QMessageBox, QComboBox, QRadioButton, QButtonGroup, QGroupBox, QScrollArea,
    QDialog
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

# ==============================================================================
# 0.1 الثيم البصري (Theme): ألوان جذابة ومتناسقة + تكبير الخطوط
# ==============================================================================
# لوحة ألوان متدرجة (نيلي/بنفسجي داكن)
COLORS = {
    "bg": "#f5f3ff",          # خلفية النافذة الرئيسية (بنفسجي فاتح جداً)
    "sidebar": "#29234d",     # خلفية القائمة الجانبية (نيلة داكنة)
    "sidebar_item": "#3d3470",# عناصر القائمة
    "sidebar_selected": "#7c4dff",  # العنصر المحدد (بنفسجي نابض)
    "sidebar_hover": "#453a80",
    "accent": "#6a3de8",      # اللون الأساسي (بنفسجي)
    "accent_dark": "#4b2a9e",
    "card": "#ffffff",        # بطاقات / حقول
    "text": "#1f1b36",        # نص داكن
    "text_light": "#eae6ff",  # نص فاتح على الداكن
    "field_border": "#c9c2f2",
    "warn": "#ff8a3d",
}

APP_FONT = "Segoe UI"

ICON_SHORTCUTS = "⚡🔌🧲💡🔋⚡🌀📏🎨⚠"

APP_STYLESHEET = f"""
* {{ font-family: '{APP_FONT}'; }}
QMainWindow, QWidget#MainArea {{ background-color: {COLORS['bg']}; }}
QWidget#PageCard {{ background-color: {COLORS['card']}; border-radius: 18px; border: 1px solid {COLORS['field_border']}; }}

QLabel#PageTitle {{ font-size: 22px; font-weight: 700; color: {COLORS['accent_dark']}; }}
QLabel#FieldLabel {{ font-size: 15px; color: {COLORS['text']}; font-weight: 600; }}
QLabel#ResultLabel {{ font-size: 16px; font-weight: 700; padding: 12px; border-radius: 12px; background-color: #ede9ff; }}
QLabel#HelpBody {{
    font-size: 15px; color: {COLORS['text']}; padding: 12px; border-radius: 10px;
    background-color: #f3f0ff; border: 1px solid {COLORS['field_border']}; line-height: 1.4;
}}
QPushButton#HelpButton {{
    background-color: {COLORS['sidebar_selected']}; color: #ffffff; font-size: 14px; font-weight: 700;
    padding: 8px 14px; border: none; border-radius: 10px;
}}
QPushButton#HelpButton:hover {{ background-color: {COLORS['accent_dark']}; }}

QGroupBox {{
    font-size: 15px; font-weight: 700; color: {COLORS['accent_dark']};
    border: 2px solid {COLORS['field_border']}; border-radius: 14px; margin-top: 14px; padding: 14px;
    background-color: #fbfaff;
}}
QGroupBox::title {{ subcontrol-origin: margin; subcontrol-position: top center; padding: 0 10px; }}

QLineEdit {{
    font-size: 16px; padding: 10px 12px; border-radius: 10px;
    border: 2px solid {COLORS['field_border']}; background-color: #ffffff; color: {COLORS['text']};
}}
QLineEdit:focus {{ border-color: {COLORS['accent']}; background-color: #fbfaff; }}

QComboBox {{
    font-size: 15px; padding: 8px 12px; border-radius: 10px;
    border: 2px solid {COLORS['field_border']}; background-color: #ffffff; color: {COLORS['text']};
}}

QPushButton {{
    font-size: 17px; font-weight: 700; padding: 12px 20px; border-radius: 12px;
    background-color: {COLORS['accent']}; color: #ffffff; border: none;
}}
QPushButton:hover {{ background-color: #7c53ef; }}
QPushButton:pressed {{ background-color: {COLORS['accent_dark']}; }}

QRadioButton {{ font-size: 15px; color: {COLORS['text']}; font-weight: 600; }}
QRadioButton::indicator {{ width: 18px; height: 18px; }}

QListWidget#Sidebar {{
    background-color: {COLORS['sidebar']}; border: none; outline: 0;
    padding: 10px; font-size: 16px; color: {COLORS['text_light']};
}}
QListWidget#Sidebar::item {{
    padding: 14px 12px; margin: 4px 0; border-radius: 12px; background-color: {COLORS['sidebar_item']};
}}
QListWidget#Sidebar::item:selected {{
    background-color: {COLORS['sidebar_selected']}; color: #ffffff; font-weight: 700;
}}
QListWidget#Sidebar::item:hover {{ background-color: {COLORS['sidebar_hover']}; }}

QLabel#LangLabel {{ font-size: 15px; font-weight: 700; color: {COLORS['text_light']}; }}
QComboBox#LangCombo {{
    background-color: #ffffff; color: #000000; border: 2px solid #c9c2f2; font-size: 15px;
    padding: 6px 10px; border-radius: 8px;
}}
QComboBox#LangCombo::drop-down {{ border: none; width: 26px; }}
QComboBox#LangCombo::down-arrow {{ image: none; border-left: 5px solid transparent; border-right: 5px solid transparent; border-top: 6px solid #4b2a9e; margin-right: 6px; }}
QComboBox#LangCombo QAbstractItemView {{
    background-color: #ffffff; color: #000000; border: 2px solid #c9c2f2;
    selection-background-color: #6a3de8; selection-color: #ffffff; font-size: 15px;
    outline: 0;
}}

QWidget#HeaderCont {{ background-color: {COLORS['sidebar']}; border-radius: 16px; }}
QLabel#HeaderTitle {{ font-size: 20px; font-weight: 800; color: {COLORS['text_light']}; }}
"""


def base_font() -> QFont:
    return QFont(APP_FONT, 10)

# ==============================================================================
# 0. نظام اللغات والترجمة (Internationalization: AR / FR / EN)
# ==============================================================================
LANG = {"current": "ar"}

TRANSLATIONS = {
    # ---------- عام ----------
    "app_title": {
        "ar": "تطبيق الحسابات الكهربائية الشامل",
        "fr": "Calculatrice Électrique Universelle",
        "en": "Universal Electrical Calculator"
    },
    "lang_label": {"ar": "اللغة:", "fr": "Langue :", "en": "Language:"},
    "btn_calculate": {"ar": "حساب", "fr": "Calculer", "en": "Calculate"},
    "result_default": {"ar": "النتيجة: --", "fr": "Résultat : --", "en": "Result: --"},
    "err_title_data": {"ar": "خطأ في البيانات", "fr": "Erreur de données", "en": "Data Error"},
    "err_title_calc": {"ar": "خطأ في الحساب", "fr": "Erreur de calcul", "en": "Calculation Error"},
    "err_title_input": {"ar": "خطأ إدخال", "fr": "Erreur d'entrée", "en": "Input Error"},

    # ---------- عناوين الوحدات (القائمة الجانبية) ----------
    "mod_ohm": {
        "ar": "1. قانون أوم والقدرة",
        "fr": "1. Loi d'Ohm et Puissance",
        "en": "1. Ohm's Law & Power"
    },
    "mod_vdrop": {
        "ar": "2. هبوط الجهد (ΔV)",
        "fr": "2. Chute de tension (ΔV)",
        "en": "2. Voltage Drop (ΔV)"
    },
    "mod_k2s2": {
        "ar": "3. الطاقة الحرارية للكابل (K²S²)",
        "fr": "3. Énergie thermique K²S²",
        "en": "3. Cable Thermal Stress (K²S²)"
    },
    "mod_led": {
        "ar": "4. مقاومة الـ LED",
        "fr": "4. Résistance pour LED",
        "en": "4. LED Resistor"
    },
    "mod_volt": {
        "ar": "5. حساب الفولت",
        "fr": "5. Calcul de la tension",
        "en": "5. Voltage Calculation"
    },
    "mod_amp": {
        "ar": "6. حساب الأمبير",
        "fr": "6. Calcul du courant",
        "en": "6. Current Calculation"
    },
    "mod_slip": {
        "ar": "7. انزلاق المحرك (Glissement)",
        "fr": "7. Glissement du moteur",
        "en": "7. Motor Slip"
    },
    "mod_colors": {
        "ar": "9. ألوان المقاومات (Code couleur)",
        "fr": "9. Code couleur des résistances",
        "en": "9. Resistor Color Codes"
    },
    "mod_shortcircuit_soon": {
        "ar": "10. تيار القصر (قريباً)",
        "fr": "10. Court-circuit (Bientôt)",
        "en": "10. Short-Circuit (Soon)"
    },

    # ---------- شاشة ألوان المقاومات (IEC 60062) ----------
    "res_title": {
        "ar": "حساب المقاومة حسب ألوان الحلقات (IEC 60062)",
        "fr": "Calcul de la résistance par code de couleur (IEC 60062)",
        "en": "Resistor Value by Color Bands (IEC 60062)"
    },
    "res_help": {
        "ar": "اضبط ألوان الحلقات من القوائم ثم احسب القيمة والتسامح.",
        "fr": "Réglez les couleurs des anneaux puis calculez la valeur et la tolérance.",
        "en": "Set the band colors from the menus, then calculate value and tolerance."
    },
    "res_max_bands": {
        "ar": "الحد الأقصى: 6 حلقات. عدّل عدد الحلقات:",
        "fr": "Maximum : 6 anneaux. Réglez le nombre d'anneaux :",
        "en": "Maximum: 6 bands. Set number of bands:"
    },
    "res_bands": {"ar": "الحلقات:", "fr": "Anneaux :", "en": "Bands:"},
    "res_btn": {"ar": "حساب المقاومة", "fr": "Calculer la résistance", "en": "Calculate value"},
    "res_btn_normalize": {"ar": "عرض الشكل المعياري (كيلو-أومأوم وما بعدها)", "fr": "Afficher forme normalisée (kΩ, MΩ…)", "en": "Show normalized value (kΩ, MΩ…)"},
    "res_blank": {"ar": "-- (فارغ)", "fr": "-- (vide)", "en": "-- (blank)"},
    "res_result": {
        "ar": "القيمة: {val} | شكل معياري: {norm} | التسامح: {tol} | المعامل الحراري: {tcr}",
        "fr": "Valeur : {val} | Forme normalisée : {norm} | Tolérance : {tol} | Coefficient thermique : {tcr}",
        "en": "Value: {val} | Normalized: {norm} | Tolerance: {tol} | Temp. coefficient: {tcr}"
    },
    "res_no_value": {
        "ar": "الرقم الأول لا يمكن أن يكون أسود أو فارغاً.",
        "fr": "Le premier chiffre ne peut pas être noir ou vide.",
        "en": "The first digit cannot be black or blank."
    },
    "res_none_band": {
        "ar": "حلقة التسامح (الأخيرة) لا يمكن أن تكون فارغة إلا إذا أزلت الحلقة.",
        "fr": "L'anneau de tolérance (dernier) ne peut pas être vide sauf si vous le retirez.",
        "en": "The tolerance band (last) cannot be blank unless removed."
    },
    "res_x": {"ar": "×", "fr": "×", "en": "×"},
    "res_ohms": {"ar": "أوم", "fr": "Ω", "en": "Ω"},
    "res_normalized_btn2": {
        "ar": "عرض القيمة فقط",
        "fr": "Afficher uniquement la valeur",
        "en": "Show value only"
    },
    # تسميات الحلقات
    "res_digit": {"ar": "رقم", "fr": "Chiffre", "en": "Digit"},
    "res_mult": {"ar": "المضاعف", "fr": "Multiplicateur", "en": "Multiplier"},
    "res_tol": {"ar": "التسامح", "fr": "Tolérance", "en": "Tolerance"},
    "res_tcr": {"ar": "المعامل الحراري TCR", "fr": "Coefficient thermique TCR", "en": "Temp. coefficient TCR"},
    # أسماء الألوان
    "color_black": {"ar": "أسود", "fr": "Noir", "en": "Black"},
    "color_brown": {"ar": "بني", "fr": "Brun", "en": "Brown"},
    "color_red": {"ar": "أحمر", "fr": "Rouge", "en": "Red"},
    "color_orange": {"ar": "برتقالي", "fr": "Orange", "en": "Orange"},
    "color_yellow": {"ar": "أصفر", "fr": "Jaune", "en": "Yellow"},
    "color_green": {"ar": "أخضر", "fr": "Vert", "en": "Green"},
    "color_blue": {"ar": "أزرق", "fr": "Bleu", "en": "Blue"},
    "color_violet": {"ar": "بنفسجي", "fr": "Violet", "en": "Violet"},
    "color_grey": {"ar": "رمادي", "fr": "Gris", "en": "Grey"},
    "color_white": {"ar": "أبيض", "fr": "Blanc", "en": "White"},
    "color_gold": {"ar": "ذهبي", "fr": "Or", "en": "Gold"},
    "color_silver": {"ar": "فضي", "fr": "Argent", "en": "Silver"},

    # ---------- زر المساعدة ----------
    "help_btn": {"ar": "مساعدة", "fr": "Aide", "en": "Help"},
    "btn_close": {"ar": "إغلاق", "fr": "Fermer", "en": "Close"},
    "help_title": {"ar": "شرح العملية الحسابية", "fr": "Explication de la formule", "en": "Calculation Explanation"},

    # النصوص التمهيدية لشاشة المساعدة
    "help_formula": {"ar": "الصيغة الحسابية:", "fr": "Formule de calcul :", "en": "Formula:"},
    "help_fields": {"ar": "العناصر المراد إدخالها:", "fr": "Champs à remplir :", "en": "Input fields:"},

    # 1) قانون أوم
    "help_ohm_formula": {
        "ar": "U = R × I    (الجهد = المقاومة × التيار)\n\nاشتقاقات:\nR = U / I\nI = U / R",
        "fr": "U = R × I    (tension = résistance × courant)\n\nDérivations :\nR = U / I\nI = U / R",
        "en": "U = R × I    (voltage = resistance × current)\n\nDerivations:\nR = U / I\nI = U / R"
    },
    "help_ohm_fields": {
        "ar": "- الجهد (Volt): فرق الجهد بين طرفي العنصر.\n- التيار (Ampere): شدة التيار المار.\n- المقاومة (أوم): مقاومة العنصر.\n\nأدخل أي قيمتين واترك القيمة المطلوبة فارغة، أو طبّق نوع العملية المختار.",
        "fr": "- Tension (Volt) : différence de potentiel.\n- Courant (Ampère) : intensité traversante.\n- Résistance (Ohm) : résistance de l'élément.\n\nRenseignez deux valeurs et laissez vide la valeur cherchée.",
        "en": "- Voltage (V): potential difference.\n- Current (A): flowing intensity.\n- Resistance (Ω): component resistance.\n\nEnter any two values and leave the target blank."
    },

    # 2) هبوط الجهد
    "help_vd_formula": {
        "ar": "هبوط الجهد في كابل:\n\nأحادب الطور (مونوفاز):\nΔU = 2 × L × I × (ρ/S) × cosφ\n\nثلاثي الطور:\nΔU = √3 × L × I × (ρ/S) × cosφ\n\nحيث ρ هي مقاومية الناقل.",
        "fr": "Chute de tension dans un câble :\n\nMonophasé :\nΔU = 2 × L × I × (ρ/S) × cosφ\n\nTriphasé :\nΔU = √3 × L × I × (ρ/S) × cosφ",
        "en": "Voltage drop in a cable:\n\nSingle-phase:\nΔU = 2 × L × I × (ρ/S) × cosφ\n\nThree-phase:\nΔU = √3 × L × I × (ρ/S) × cosφ"
    },
    "help_vd_fields": {
        "ar": "- الجهد الاسمي (Volt): جهد الشبكة.\n- التيار (Ampere): التيار المار في الكابل.\n- الطول (متر): طول الكابل.\n- المقطع (mm²): مقطع النحاس/الألمنيوم.\n- Cos φ: معامل القدرة.\n- النظام: أحادي أو ثلاثي الطور.",
        "fr": "- Tension nominale (V) : tension du réseau.\n- Courant (A) : courant dans le câble.\n- Longueur (m) : longueur du câble.\n- Section (mm²) : section du conducteur.\n- Cos φ : facteur de puissance.\n- Système : monophasé ou triphasé.",
        "en": "- Nominal voltage (V): network voltage.\n- Current (A): current in the cable.\n- Length (m): cable length.\n- Section (mm²): conductor cross-section.\n- Cos φ: power factor.\n- System: single or three phase."
    },

    # 3) ك²س² (K2S2)
    "help_k2s2_formula": {
        "ar": "شرط السلامة الحرارية لموصل الحماية (PE):\n\nك² × س² ≥ I² × t\n\nحيث:\nك = ثابت يعتمد على مادة الموصل وعزله.\nس = مقطع الموصل (mm²).\nI = تيار القصر المتوقع (A).\nt = زمن الفصل (ثانية).",
        "fr": "Condition de sécurité thermique du conducteur de protection (PE) :\n\nk² × s² ≥ I² × t\n\nk = constante matériau/isolant, s = section (mm²), I = courant de court-circuit (A), t = temps de coupure (s).",
        "en": "Thermal protection condition for the PE conductor:\n\nk² × s² ≥ I² × t\n\nk = material/insulation constant, s = section (mm²), I = short-circuit current (A), t = clearing time (s)."
    },
    "help_k2s2_fields": {
        "ar": "- ثابت ك (K): قيمة تعتمد على المادة والعزل.\n- المقطع (mm²): مقطع موصل الحماية.\n- تيار القصر (A): تيار القصر المتوقع.\n- الزمن (ثانية): زمن قطع الجهاز الواقي.",
        "fr": "- Constante k (K) : dépend du matériau et de l'isolant.\n- Section (mm²) : section du conducteur PE.\n- Courant de court-circuit (A).\n- Temps (s) : temps de coupure du dispositif.",
        "en": "- Constant k: depends on material and insulation.\n- Section (mm²): PE conductor section.\n- Short-circuit current (A).\n- Time (s): protective device clearing time."
    },

    # 4) مقاومة الـ LED
    "help_led_formula": {
        "ar": "حساب مقاومة التخفيض للـ LED:\n\nR = (U_source - U_led) / I_led\n\nالقدرة المبددة:\nP = (U_source - U_led)² / R",
        "fr": "Calcul de la résistance de limitation pour LED :\n\nR = (U_source - U_led) / I_led\n\nPuissance dissipée :\nP = (U_source - U_led)² / R",
        "en": "LED series resistor calculation:\n\nR = (V_source - V_led) / I_led\n\nDissipated power:\nP = (V_source - V_led)² / R"
    },
    "help_led_fields": {
        "ar": "- جهد المصدر (Volt): جهد التغذية.\n- جهد الـ LED (Volt): الهبوط عادة 2-3.5V حسب اللون.\n- تيار الـ LED (mA): عادة 10-20mA.",
        "fr": "- Tension de source (V) : alimentation.\n- Tension de la LED (V) : chute typique 2-3,5V.\n- Courant LED (mA) : typiquement 10-20mA.",
        "en": "- Source voltage (V): supply voltage.\n- LED voltage (V): typical 2-3.5V drop.\n- LED current (mA): typically 10-20mA."
    },

    # 5) حساب الجهد
    "help_volt_formula": {
        "ar": "حساب الجهد من القدرة والتيار:\n\nأحادي الطور:\nU = P / I\n\nثلاثي الطور:\nU = P / (√3 × I × cosφ)\n\n(قدرة ≥ 1 تقسيم → أحادي الطور)",
        "fr": "Calcul de la tension à partir de la puissance et du courant :\n\nMonophasé :\nU = P / I\n\nTriphasé :\nU = P / (√3 × I × cosφ)",
        "en": "Voltage from power and current:\n\nSingle-phase:\nU = P / I\n\nThree-phase:\nU = P / (√3 × I × cosφ)"
    },
    "help_volt_fields": {
        "ar": "- القدرة (Watt): القدرة الكهربائية.\n- التيار (Ampere): شدة التيار.\n- Cos φ: معامل القدرة.\n- النظام: أحادي أو ثلاثي الطور.",
        "fr": "- Puissance (W) : puissance électrique.\n- Courant (A) : intensité.\n- Cos φ : facteur de puissance.\n- Système : monophasé ou triphasé.",
        "en": "- Power (W): electrical power.\n- Current (A): intensity.\n- Cos φ: power factor.\n- System: single or three phase."
    },

    # 6) حساب التيار
    "help_amp_formula": {
        "ar": "حساب التيار من القدرة والجهد:\n\nأحادي الطور:\nI = P / U\n\nثلاثي الطور:\nI = P / (√3 × U × cosφ)",
        "fr": "Calcul du courant à partir de la puissance et de la tension :\n\nMonophasé :\nI = P / U\n\nTriphasé :\nI = P / (√3 × U × cosφ)",
        "en": "Current from power and voltage:\n\nSingle-phase:\nI = P / U\n\nThree-phase:\nI = P / (√3 × U × cosφ)"
    },
    "help_amp_fields": {
        "ar": "- القدرة (Watt): القدرة الكهربائية.\n- الجهد (Volt): جهد الشبكة.\n- Cos φ: معامل القدرة.\n- النظام: أحادي أو ثلاثي الطور.",
        "fr": "- Puissance (W) : puissance électrique.\n- Tension (V) : tension du réseau.\n- Cos φ : facteur de puissance.\n- Système : monophasé ou triphasé.",
        "en": "- Power (W): electrical power.\n- Voltage (V): network voltage.\n- Cos φ: power factor.\n- System: single or three phase."
    },

    # 7) انزلاق المحرك
    "help_slip_formula": {
        "ar": "انزلاق المحرك غير المتزامن:\n\ng = (n_synchrone - n_rotor) / n_synchrone × 100\n\nالسرعة المتزامنة:\nn_sync = (120 × f) / p\n\nحيث f التردد (هرتز) وp عدد الأقطاب.",
        "fr": "Glissement du moteur asynchrone :\n\ng = (n_synchrone - n_rotor) / n_synchrone × 100\n\nVitesse synchrone :\nn_sync = (120 × f) / p",
        "en": "Asynchronous motor slip:\n\ng = (n_synchronous - n_rotor) / n_synchronous × 100\n\nSynchronous speed:\nn_sync = (120 × f) / p"
    },
    "help_slip_fields": {
        "ar": "- التردد (Hz): تردد الشبكة (عادة 50 أو 60).\n- عدد الأقطاب: أقطاب المحرك (2، 4، 6...).\n- السرعة (rpm): سرعة المحرك الفعلية.\n- (اختياري) التردد الدوار: تردد التيار في العضو الدوار.",
        "fr": "- Fréquence (Hz) : fréquence réseau (50 ou 60).\n- Nombre de pôles : pôles du moteur (2, 4, 6...).\n- Vitesse (tr/min) : vitesse réelle du moteur.\n- (Optionnel) fréquence rotorique.",
        "en": "- Frequency (Hz): network frequency (50 or 60).\n- Number of poles: motor poles (2, 4, 6...).\n- Speed (rpm): actual motor speed.\n- (Optional) rotor frequency."
    },

    # 8) مقطع الكابل
    "help_section_formula": {
        "ar": "حساب مقطع الكابل حسب هبوط الجهد المسموح:\n\nأحادي الطور:\nS = (2 × L × I × ρ × cosφ) / ΔU_max\n\nثلاثي الطور:\nS = (√3 × L × I × ρ × cosφ) / ΔU_max",
        "fr": "Calcul de la section du câble selon la chute de tension admissible :\n\nMonophasé :\nS = (2 × L × I × ρ × cosφ) / ΔU_max\n\nTriphasé :\nS = (√3 × L × I × ρ × cosφ) / ΔU_max",
        "en": "Cable cross-section from allowable voltage drop:\n\nSingle-phase:\nS = (2 × L × I × ρ × cosφ) / ΔU_max\n\nThree-phase:\nS = (√3 × L × I × ρ × cosφ) / ΔU_max"
    },
    "help_section_fields": {
        "ar": "- الجهد الاسمي (Volt): جهد الشبكة.\n- التيار (Ampere): تيار الحمل.\n- الطول (متر): طول الكابل.\n- Cos φ: معامل القدرة.\n- هبوط الجهد الأقصى المسموح (٪): الحد المسموح.\n- المادة: نحاس أو ألمنيوم (تؤثر على ρ).\n- النظام: أحادي أو ثلاثي الطور.",
        "fr": "- Tension nominale (V) : tension du réseau.\n- Courant (A) : courant de charge.\n- Longueur (m) : longueur du câble.\n- Cos φ : facteur de puissance.\n- Chute max admissible (%).\n- Matériau : cuivre ou aluminium (ρ).\n- Système : monophasé ou triphasé.",
        "en": "- Nominal voltage (V): network voltage.\n- Current (A): load current.\n- Length (m): cable length.\n- Cos φ: power factor.\n- Max allowable drop (%).\n- Material: copper or aluminium (ρ).\n- System: single or three phase."
    },

    # 9) ألوان المقاومات
    "help_res_formula": {
        "ar": "قراءة قيمة المقاومة من الألوان (IEC 60062):\n\n4 حلقات: رقم، رقم، مضاعف، تسامح\n5 حلقات: رقم، رقم، رقم، مضاعف، تسامح\n6 حلقات: 3 أرقام + مضاعف + تسامح + معامل حراري\n\nالقيمة = (أرقام) × المضاعف\nالألوان مرتبطة بالأرقام: أسود=0، بني=1، أحمر=2 ...",
        "fr": "Lecture de la résistance par code couleur (IEC 60062) :\n\n4 anneaux : chiffre, chiffre, multiplicateur, tolérance\n5 anneaux : 3 chiffres + multiplicateur + tolérance\n6 anneaux : 3 chiffres + multiplicateur + tolérance + TCR\n\nValeur = (chiffres) × multiplicateur",
        "en": "Resistor color code reading (IEC 60062):\n\n4 bands: digit, digit, multiplier, tolerance\n5 bands: 3 digits + multiplier + tolerance\n6 bands: 3 digits + multiplier + tolerance + TCR\n\nValue = (digits) × multiplier"
    },
    "help_res_fields": {
        "ar": "- عدد الحلقات: 4 أو 5 أو 6.\n- حلقة الرقم: لون يمثل رقماً (0-9).\n- حلقة المضاعف: لون يضرب القيمة (ذهبي=÷10، أسود=×1...).\n- حلقة التسامح: تحدد النسبة (±1%، ±5%...).\n- حلقة TCR (فقط 6 حلقات): المعامل الحراري.",
        "fr": "- Nombre d'anneaux : 4, 5 ou 6.\n- Anneau chiffre : couleur = chiffre (0-9).\n- Anneau multiplicateur : facteur (or=÷10, noir=×1...).\n- Anneau tolérance : pourcentage (±1%, ±5%...).\n- Anneau TCR (6 anneaux) : coefficient thermique.",
        "en": "- Number of bands: 4, 5 or 6.\n- Digit band: color = digit (0-9).\n- Multiplier band: factor (gold=÷10, black=×1...).\n- Tolerance band: percentage (±1%, ±5%...).\n- TCR band (6 bands): temperature coefficient."
    },



    # ---------- حقول مشتركة ----------
    "lbl_voltage": {"ar": "الجهد (Volt):", "fr": "Tension (Volt) :", "en": "Voltage (V):"},
    "lbl_current": {"ar": "التيار (Ampere):", "fr": "Courant (Ampère) :", "en": "Current (A):"},
    "lbl_power": {"ar": "القدرة (Watt):", "fr": "Puissance (Watt) :", "en": "Power (W):"},
    "lbl_resistance": {"ar": "المقاومة (R - Ohm):", "fr": "Résistance (R - Ohm) :", "en": "Resistance (R - Ω):"},
    "lbl_cosphi": {"ar": "معامل القدرة (Cos φ):", "fr": "Facteur de puissance (Cos φ) :", "en": "Power factor (Cos φ):"},
    "phase_3p": {"ar": "ثلاثي الأوجه", "fr": "Triphasé", "en": "Three-Phase"},
    "phase_1p": {"ar": "أحادي الوجه", "fr": "Monophasé", "en": "Single-Phase"},
    "method1_pi": {
        "ar": "الطريقة 1: من القدرة والتيار (P & I)",
        "fr": "Méthode 1 : à partir de P & I",
        "en": "Method 1: From Power & Current (P & I)"
    },
    "method2_ohm": {
        "ar": "الطريقة 2: قانون أوم (أدخل قيمتين على الأقل)",
        "fr": "Méthode 2 : loi d'Ohm (au moins deux valeurs)",
        "en": "Method 2: Ohm's Law (at least two values)"
    },

    # ---------- شاشة قانون أوم ----------
    "ohm_title": {
        "ar": "حسابات قانون أوم والقدرة الأحادي",
        "fr": "Loi d'Ohm et puissance monophasée",
        "en": "Ohm's Law & Single-Phase Power"
    },
    "ohm_group": {"ar": "أدخل أي قيمتين للحساب:", "fr": "Entrez deux valeurs au choix :", "en": "Enter any two values:"},
    "ph_voltage": {"ar": "مثال: 230", "fr": "Ex : 230", "en": "e.g., 230"},
    "ph_current": {"ar": "مثال: 10", "fr": "Ex : 10", "en": "e.g., 10"},
    "ph_power": {"ar": "مثال: 2300", "fr": "Ex : 2300", "en": "e.g., 2300"},
    "ohm_results": {"ar": "النتائج المتبقية: ", "fr": "Résultats restants : ", "en": "Remaining results: "},

    # ---------- شاشة هبوط الجهد ----------
    "vd_title": {
        "ar": "حساب هبوط الجهد (ΔV)",
        "fr": "Calcul de la chute de tension (ΔV)",
        "en": "Voltage Drop Calculation (ΔV)"
    },
    "vd_nominal_voltage": {"ar": "الجهد الإسمي (V):", "fr": "Tension nominale (V) :", "en": "Nominal voltage (V):"},
    "vd_nominal_current": {"ar": "التيار الإسمي (I - Ampere):", "fr": "Courant nominal (I - A) :", "en": "Rated current (I - A):"},
    "vd_length": {"ar": "طول الكابل (L - Meters):", "fr": "Longueur du câble (L - m) :", "en": "Cable length (L - m):"},
    "vd_section": {"ar": "مقطع الموصل (S - mm²):", "fr": "Section du conducteur (S - mm²) :", "en": "Conductor cross-section (S - mm²):"},
    "vd_material": {"ar": "مادة الموصل:", "fr": "Matériau du conducteur :", "en": "Conductor material:"},
    "mat_cu": {"ar": "Cu (نحاس)", "fr": "Cu (Cuivre)", "en": "Cu (Copper)"},
    "mat_al": {"ar": "Al (ألومنيوم)", "fr": "Al (Aluminium)", "en": "Al (Aluminum)"},
    "vd_btn": {"ar": "حساب هبوط الجهد", "fr": "Calculer la chute de tension", "en": "Calculate voltage drop"},
    "ph_vd_current": {"ar": "مثال: 50", "fr": "Ex : 50", "en": "e.g., 50"},
    "ph_vd_length": {"ar": "مثال: 120", "fr": "Ex : 120", "en": "e.g., 120"},
    "ph_vd_section": {"ar": "مثال: 16", "fr": "Ex : 16", "en": "e.g., 16"},
    "vd_result_fmt": {
        "ar": "هبوط الجهد (ΔU): {du} Volt | النسبة: {pct}% | مقاومة السلك: {r} Ω",
        "fr": "Chute de tension (ΔU) : {du} V | Taux : {pct} % | Résistance du câble : {r} Ω",
        "en": "Voltage drop (ΔU): {du} V | Percentage: {pct}% | Cable resistance: {r} Ω"
    },

    # ---------- شاشة K²S² ----------
    "k2s2_title": {
        "ar": "الطاقة الحرارية القصوى المسموح بها للكابل (K²S²)",
        "fr": "Énergie thermique maximale admise du câble (K²S²)",
        "en": "Maximum Permissible Cable Thermal Energy (K²S²)"
    },
    "k2s2_lbl_section": {"ar": "مقطع الموصل (S - mm²):", "fr": "Section (S - mm²) :", "en": "Cross-section (S - mm²):"},
    "k2s2_lbl_k": {"ar": "المعامل القياسي (K):", "fr": "Coefficient normalisé (K) :", "en": "Standard coefficient (K):"},
    "k2s2_ph_section": {"ar": "مقطع الموصل mm²", "fr": "Section en mm²", "en": "Cross-section in mm²"},
    "k2s2_ph_k": {
        "ar": "معامل الموصل K (مثلاً 115 للنحاس PVC)",
        "fr": "Coefficient K (ex : 115 pour cuivre PVC)",
        "en": "Conductor coefficient K (e.g., 115 for PVC copper)"
    },
    "k2s2_btn": {"ar": "حساب K²S²", "fr": "Calculer K²S²", "en": "Calculate K²S²"},
    "k2s2_result_fmt": {
        "ar": "الطاقة الحرارية المسموح بها (K²S²): {val:,.2f} A²s",
        "fr": "Énergie thermique admise (K²S²) : {val:,.2f} A²s",
        "en": "Permissible thermal energy (K²S²): {val:,.2f} A²s"
    },

    # ---------- شاشة LED ----------
    "led_title": {
        "ar": "حساب مقاومة الحماية للـ LED",
        "fr": "Calcul de la résistance pour LED",
        "en": "LED Protection Resistor Calculation"
    },
    "led_lbl_vs": {"ar": "جهد المصدر (Vs - Volt):", "fr": "Tension source (Vs - V) :", "en": "Source voltage (Vs - V):"},
    "led_lbl_vled": {"ar": "جهد الـ LED (Vled - Volt):", "fr": "Tension LED (Vled - V) :", "en": "LED voltage (Vled - V):"},
    "led_lbl_iled": {"ar": "تيار الـ LED (Iled - mA):", "fr": "Courant LED (Iled - mA) :", "en": "LED current (Iled - mA):"},
    "led_btn": {"ar": "حساب المقاومة", "fr": "Calculer la résistance", "en": "Calculate resistor"},
    "led_result_fmt": {
        "ar": "المقاومة المطلوبة: {r} Ω | استهلاك القدرة للمقاومة: {p} Watt",
        "fr": "Résistance requise : {r} Ω | Puissance dissipée : {p} W",
        "en": "Required resistance: {r} Ω | Power dissipated: {p} W"
    },

    # ---------- شاشة حساب الفولت ----------
    "volt_title": {"ar": "حساب الفولت / الجهد", "fr": "Calcul de la tension", "en": "Voltage Calculation"},
    "volt_btn": {"ar": "حساب الفولت", "fr": "Calculer la tension", "en": "Calculate voltage"},
    "volt_result_3p": {
        "ar": "الجهد بين الأطوار (U): {u} Volt | بين الطور والحيادي: {v} Volt",
        "fr": "Tension entre phases (U) : {u} V | Phase-neutre : {v} V",
        "en": "Line-to-line voltage (U): {u} V | Line-to-neutral: {v} V"
    },
    "volt_result_1p": {"ar": "الجهد (V): {v} Volt", "fr": "Tension (V) : {v} V", "en": "Voltage (V): {v} V"},
    "volt_result_ri": {"ar": "الجهد (V = R×I): {v} Volt", "fr": "Tension (V = R×I) : {v} V", "en": "Voltage (V = R×I): {v} V"},
    "volt_result_pr": {"ar": "الجهد (V = √(P×R)): {v} Volt", "fr": "Tension (V = √(P×R)) : {v} V", "en": "Voltage (V = √(P×R)): {v} V"},

    # ---------- شاشة حساب الأمبير ----------
    "amp_title": {"ar": "حساب الأمبير / التيار", "fr": "Calcul du courant", "en": "Current Calculation"},
    "amp_method1_pv": {
        "ar": "الطريقة 1: من القدرة والجهد (P & V)",
        "fr": "Méthode 1 : à partir de P & V",
        "en": "Method 1: From Power & Voltage (P & V)"
    },
    "amp_btn": {"ar": "حساب الأمبير", "fr": "Calculer le courant", "en": "Calculate current"},
    "amp_formula_3p": {"ar": "(I = P/(√3·U·cosφ))", "fr": "(I = P/(√3·U·cosφ))", "en": "(I = P/(√3·U·cosφ))"},
    "amp_formula_1p": {"ar": "(I = P/(V·cosφ))", "fr": "(I = P/(V·cosφ))", "en": "(I = P/(V·cosφ))"},
    "amp_result_fmt": {"ar": "التيار {formula}: {i} Ampere", "fr": "Courant {formula} : {i} A", "en": "Current {formula}: {i} A"},
    "amp_result_vr": {"ar": "التيار (I = V/R): {i} Ampere", "fr": "Courant (I = V/R) : {i} A", "en": "Current (I = V/R): {i} A"},
    "amp_result_pr": {"ar": "التيار (I = √(P/R)): {i} Ampere", "fr": "Courant (I = √(P/R)) : {i} A", "en": "Current (I = √(P/R)): {i} A"},

    # ---------- شاشة انزلاق المحرك ----------
    "gl_title": {
        "ar": "حساب انزلاق المحرك اللامتزامن (Glissement)",
        "fr": "Glissement du moteur asynchrone",
        "en": "Induction Motor Slip Calculation"
    },
    "gl_group_net": {"ar": "بيانات الشبكة والمحرك:", "fr": "Données réseau et moteur :", "en": "Network & motor data:"},
    "gl_freq": {"ar": "التردد (f - Hz):", "fr": "Fréquence (f - Hz) :", "en": "Frequency (f - Hz):"},
    "gl_poles": {"ar": "عدد الأقطاب (p):", "fr": "Nombre de pôles (p) :", "en": "Number of poles (p):"},
    "gl_poles_ph": {
        "ar": "مثال: 4 (محرك 4 أقطاب عند 50Hz → Ns=1500 tr/min)",
        "fr": "Ex : 4 (moteur 4 pôles à 50 Hz → Ns = 1500 tr/min)",
        "en": "E.g.: 4 (4-pole motor at 50Hz → Ns=1500 rpm)"
    },
    "gl_method1": {
        "ar": "الطريقة 1: من السرعة المقاسة (tr/min)",
        "fr": "Méthode 1 : à partir de la vitesse mesurée (tr/min)",
        "en": "Method 1: From measured speed (rpm)"
    },
    "gl_lbl_rpm": {"ar": "سرعة الدوران المقاسة (N - tr/min):", "fr": "Vitesse mesurée (N - tr/min) :", "en": "Measured speed (N - rpm):"},
    "gl_rpm_ph": {"ar": "مثال: 1440", "fr": "Ex : 1440", "en": "e.g., 1440"},
    "gl_method2": {"ar": "الطريقة 2: من نسبة الانزلاق (%)", "fr": "Méthode 2 : à partir du glissement (%)", "en": "Method 2: From slip percentage (%)"},
    "gl_lbl_slip": {"ar": "نسبة الانزلاق (g %):", "fr": "Glissement (g %) :", "en": "Slip percentage (g %):"},
    "gl_slip_ph": {"ar": "مثال: 4", "fr": "Ex : 4", "en": "e.g., 4"},
    "gl_btn": {"ar": "حساب الانزلاق", "fr": "Calculer le glissement", "en": "Calculate slip"},
    "gl_result_fmt": {
        "ar": "Ns: {ns} tr/min | N: {n} tr/min | g: {g}% | fr: {fr} Hz",
        "fr": "Ns : {ns} tr/min | N : {n} tr/min | g : {g} % | fr : {fr} Hz",
        "en": "Ns: {ns} rpm | N: {n} rpm | Slip: {g}% | Rotor freq.: {fr} Hz"
    },

    # ---------- شاشة مقطع الكابل ----------
    "mod_section": {
        "ar": "8. مقطع الكابل (Section du câble)",
        "fr": "8. Section du câble",
        "en": "8. Cable Cross-Section"
    },
    "sec_title": {
        "ar": "حساب مقطع الكابل حسب هبوط الجهد",
        "fr": "Calcul de la section du câble par chute de tension",
        "en": "Cable Cross-Section by Voltage Drop"
    },
    "sec_max_drop": {"ar": "أقصى هبوط جهد مسموح (ΔU%):", "fr": "Chute de tension admissible (ΔU %) :", "en": "Max permissible voltage drop (ΔU%):"},
    "ph_drop_pct": {"ar": "مثال: 3 للإنارة، 5 لأخرى", "fr": "Ex : 3 éclairage, 5 autre", "en": "e.g., 3 lighting, 5 other"},
    "sec_btn": {"ar": "حساب المقطع", "fr": "Calculer la section", "en": "Calculate cross-section"},
    "sec_result_fmt": {
        "ar": "المقطع الأدنى المحسوب: {smin} mm² | المقطع القياسي المقترح: {s} mm² | هبوط الجهد الفعلي به: {du}% | مقاومة السلك: {r} Ω",
        "fr": "Section minimale calculée : {smin} mm² | Section normalisée suggérée : {s} mm² | Chute réelle : {du} % | Résistance : {r} Ω",
        "en": "Minimum calculated section: {smin} mm² | Suggested standard section: {s} mm² | Actual drop with it: {du}% | Resistance: {r} Ω"
    },
    "err_section_too_large": {
        "ar": "الحمل كبير جداً على مقطع قياسي واحد (أقصى 300 mm²) - يلزم موصلات متوازية.",
        "fr": "Charge trop élevée pour une section normalisée unique (max 300 mm²) - conducteurs en parallèle nécessaires.",
        "en": "Load too high for a single standard section (max 300 mm²) - parallel conductors required."
    },

    # ---------- رسائل الأخطاء (التحقق والمحرك) ----------
    "err_positive_required": {
        "ar": "قيم الحقل '{field}' يجب أن تكون أكبر من الصفر.",
        "fr": "La valeur de '{field}' doit être supérieure à zéro.",
        "en": "The value of '{field}' must be greater than zero."
    },
    "err_number_positive": {
        "ar": "يرجى إدخال رقم صحيح وموجب في حقل '{field}'.",
        "fr": "Veuillez entrer un nombre positif valide dans '{field}'.",
        "en": "Please enter a valid positive number in '{field}'."
    },
    "err_negative_not_allowed": {
        "ar": "قيم الحقل '{field}' لا يمكن أن تكون سالبة.",
        "fr": "La valeur de '{field}' ne peut pas être négative.",
        "en": "The value of '{field}' cannot be negative."
    },
    "err_number_valid": {
        "ar": "يرجى إدخال رقم صحيح في حقل '{field}'.",
        "fr": "Veuillez entrer un nombre valide dans '{field}'.",
        "en": "Please enter a valid number in '{field}'."
    },
    "err_two_values": {
        "ar": "يرجى إدخال قيمتين على الأقل لإتمام الحساب.",
        "fr": "Veuillez saisir au moins deux valeurs pour le calcul.",
        "en": "Please enter at least two values to calculate."
    },
    "err_enter_any_method": {
        "ar": "أدخل القيم المطلوبة لإحدى الطريقتين على الأقل.",
        "fr": "Entrez les valeurs d'au moins une des deux méthodes.",
        "en": "Enter the values for at least one of the two methods."
    },
    "err_source_gt_led": {
        "ar": "جهد المصدر يجب أن يكون أكبر من جهد الـ LED.",
        "fr": "La tension source doit être supérieure à la tension de la LED.",
        "en": "Source voltage must be greater than the LED voltage."
    },
    "err_freq_poles_positive": {
        "ar": "التردد وعدد الأقطاب يجب أن يكونا أكبر من الصفر.",
        "fr": "La fréquence et le nombre de pôles doivent être supérieurs à zéro.",
        "en": "Frequency and number of poles must be greater than zero."
    },
    "err_rpm_negative": {
        "ar": "سرعة الدوران لا يمكن أن تكون سالبة.",
        "fr": "La vitesse ne peut pas être négative.",
        "en": "Speed cannot be negative."
    },
    "err_rpm_exceeds_ns": {
        "ar": "سرعة المحرك لا يمكن أن تتجاوز السرعة التزامنية (Ns).",
        "fr": "La vitesse du moteur ne peut pas dépasser la vitesse synchrone (Ns).",
        "en": "Motor speed cannot exceed synchronous speed (Ns)."
    },
    "err_slip_range": {
        "ar": "نسبة الانزلاق يجب أن تكون بين 0% و 100%.",
        "fr": "Le glissement doit être compris entre 0 % et 100 %.",
        "en": "Slip must be between 0% and 100%."
    },
    "err_rpm_or_slip": {
        "ar": "أدخل سرعة المحرك (N) أو نسبة الانزلاق (g%).",
        "fr": "Entrez la vitesse (N) ou le glissement (g %).",
        "en": "Enter motor speed (N) or slip percentage (g%)."
    },

    # ---------- صفحات مؤقتة ----------
    "ph_mod_shortcircuit": {"ar": "حسابات تيار القصر Icc", "fr": "Courant de court-circuit Icc", "en": "Short-circuit current Icc"},
    "placeholder_body": {
        "ar": "وحدة: {title}\n\nهذه الشاشة معدة كقالب لتزويدها بالقوانين التكميلية بسهولة.",
        "fr": "Module : {title}\n\nCet écran est un modèle prêt pour ajouter facilement les formules complémentaires.",
        "en": "Module: {title}\n\nThis screen is a template ready for adding complementary formulas."
    }
}

LANG_CODES = ["ar", "fr", "en"]
LANG_NAMES = {"ar": "العربية", "fr": "Français", "en": "English"}


def tr(key: str, **kwargs) -> str:
    """ترجمة نص حسب اللغة الحالية مع دعم التنسيق"""
    text = TRANSLATIONS[key][LANG["current"]]
    return text.format(**kwargs) if kwargs else text


# ==============================================================================
# 1. أدوات الأمان والتحقق من البيانات (Input Validation & Safety)
# ==============================================================================
class InputValidator:
    """طبقة الحماية لمنع استثناءات الإدخال والتأكد من صحة القيم المدخلة"""

    @staticmethod
    def validate_positive_float(value: str, field_name: str) -> float:
        """التحقق من أن الرقم موجب وأكبر من الصفر"""
        try:
            val = float(value.replace(',', '.'))
        except ValueError:
            raise ValueError(tr("err_number_positive", field=field_name))
        if val <= 0:
            raise ValueError(tr("err_positive_required", field=field_name))
        return val

    @staticmethod
    def validate_non_negative_float(value: str, field_name: str) -> float:
        """التحقق من أن الرقم غير سالب (يسمح بالصفر)"""
        try:
            val = float(value.replace(',', '.'))
        except ValueError:
            raise ValueError(tr("err_number_valid", field=field_name))
        if val < 0:
            raise ValueError(tr("err_negative_not_allowed", field=field_name))
        return val


# ==============================================================================
# 2. المحرك الحسابي القائم على المعايير الدولية (IEC 60364 & NF C 15-100)
# ==============================================================================
class ElectricalEngine:
    # المقاومة النوعية للأسلاك Ω·mm²/m عند درجات حرارة العمل (IEC 60364-5-52)
    RHO_COPPER = 0.0225   # النحاس (Cu)
    RHO_ALU = 0.036       # الألومنيوم (Al)

    # المقاطع القياسية الموحدة (mm²) حسب IEC 60228
    STANDARD_SECTIONS = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240, 300]

    @staticmethod
    def calculate_cable_section(is_three_phase: bool, voltage: float, current: float,
                                length: float, cos_phi: float, material: str,
                                max_drop_pct: float) -> dict:
        """حساب الحد الأدنى لمقطع الكابل لضمان هبوط جهد ضمن الحد المسموح
        من ΔU% = 100·b·ρ·L·I·cosφ / (S·U) نستخرج: S = b·ρ·L·I·cosφ·100 / (ΔU%·U)
        ثم يُختار المقطع القياسي ويُتحقق منه فعلياً (مع مفاعلة X) حتى الالتزام بالحد.
        """
        rho = ElectricalEngine.RHO_COPPER if material == "Cu" else ElectricalEngine.RHO_ALU
        b = math.sqrt(3) if is_three_phase else 2.0
        cos_phi = min(max(cos_phi, 0.0), 1.0)

        s_min = b * current * length * rho * cos_phi / ((max_drop_pct / 100.0) * voltage)

        result = {"s_min": round(s_min, 2), "suggested": None}

        start_idx = next((i for i, s in enumerate(ElectricalEngine.STANDARD_SECTIONS) if s >= s_min), None)
        if start_idx is None:
            return result

        for s in ElectricalEngine.STANDARD_SECTIONS[start_idx:]:
            check = ElectricalEngine.calculate_voltage_drop(
                is_three_phase=is_three_phase, current=current, length=length,
                section=s, cos_phi=cos_phi, material=material, voltage=voltage
            )
            if check["percentage"] <= max_drop_pct + 1e-9:
                result["suggested"] = s
                result["actual_drop_pct"] = check["percentage"]
                result["resistance"] = check["resistance"]
                break

        return result

    @staticmethod
    def calculate_ohms_law(v=None, i=None, r=None, p=None):
        """حسابات قانون أوم والقدرة الأحادية"""
        if v and i:
            return {"R": v / i, "P": v * i}
        elif p and v:
            return {"I": p / v, "R": (v ** 2) / p}
        elif p and i:
            return {"V": p / i, "R": p / (i ** 2)}
        elif r and i:
            return {"V": r * i, "P": r * (i ** 2)}
        else:
            raise ValueError(tr("err_two_values"))

    @staticmethod
    def calculate_voltage_drop(is_three_phase: bool, current: float, length: float,
                               section: float, cos_phi: float, material: str, voltage: float) -> dict:
        """حساب هبوط الجهد بناءً على معايير NF C 15-100 / IEC 60364"""
        rho = ElectricalEngine.RHO_COPPER if material == "Cu" else ElectricalEngine.RHO_ALU
        # معامل النظام: √3 للثلاثي (بين الأطوار)، 2 للأحادي (الذهاب والعودة)
        b = math.sqrt(3) if is_three_phase else 2.0

        cos_phi = min(max(cos_phi, 0.0), 1.0)
        sin_phi = math.sqrt(max(1 - cos_phi**2, 0))

        x_reactance = 0.08 / 1000
        r_resistance = rho * (length / section)

        delta_u = b * current * (r_resistance * cos_phi + (x_reactance * length) * sin_phi)
        percentage_drop = (delta_u / voltage) * 100

        return {
            "delta_u": round(delta_u, 2),
            "percentage": round(percentage_drop, 2),
            "resistance": round(r_resistance, 4)
        }

    @staticmethod
    def calculate_thermal_stress(section: float, k_constant: float) -> float:
        """حساب الطاقة الحرارية القصوى المسموح بها للكابل (K²S²)"""
        return (k_constant * section) ** 2

    @staticmethod
    def calc_voltage_from_power(p: float, i: float, cos_phi: float = 1.0, is_three_phase: bool = False) -> dict:
        """حساب الجهد من القدرة والتيار (أحادي: V=P/(I·cosφ) | ثلاثي: U=P/(√3·I·cosφ))"""
        cos_phi = min(max(cos_phi, 0.01), 1.0)
        if is_three_phase:
            u = p / (math.sqrt(3) * i * cos_phi)
            return {"U": round(u, 2), "V_phase": round(u / math.sqrt(3), 2)}
        return {"V": round(p / (i * cos_phi), 2), "V_phase": None}

    @staticmethod
    def calc_current_from_power(p: float, v: float, cos_phi: float = 1.0, is_three_phase: bool = False) -> dict:
        """حساب التيار من القدرة والجهد (أحادي: I=P/(V·cosφ) | ثلاثي: I=P/(√3·U·cosφ))"""
        cos_phi = min(max(cos_phi, 0.01), 1.0)
        if is_three_phase:
            i = p / (math.sqrt(3) * v * cos_phi)
        else:
            i = p / (v * cos_phi)
        return {"I": round(i, 2)}

    @staticmethod
    def calculate_motor_slip(frequency: float, poles: float, rpm: float = None, slip_pct: float = None) -> dict:
        """حساب انزلاق المحرك اللامتزامن (Glissement)
        السرعة التزامنية: Ns = 120·f/p | الانزلاق: g = (Ns-N)/Ns | تردد الدوار: fr = g·f
        """
        if poles <= 0 or frequency <= 0:
            raise ValueError(tr("err_freq_poles_positive"))

        ns = (120.0 * frequency) / poles
        result = {"Ns": round(ns, 1)}

        if rpm is not None:
            if rpm < 0:
                raise ValueError(tr("err_rpm_negative"))
            if rpm > ns:
                raise ValueError(tr("err_rpm_exceeds_ns"))
            g_frac = (ns - rpm) / ns
            result["N"] = round(rpm, 1)
        elif slip_pct is not None:
            if slip_pct < 0 or slip_pct >= 100:
                raise ValueError(tr("err_slip_range"))
            g_frac = slip_pct / 100.0
            result["N"] = round(ns * (1 - g_frac), 1)
        else:
            raise ValueError(tr("err_rpm_or_slip"))

        result["g"] = round(g_frac * 100, 2)
        result["f_rotor"] = round(frequency * g_frac, 2)
        return result

    # جداول ألوان المقاومات حسب المعيار الدولي IEC 60062
    COLOR_DIGIT = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    COLOR_MULT = {
        "black": 1, "brown": 10, "red": 100, "orange": 1e3, "yellow": 1e4,
        "green": 1e5, "blue": 1e6, "violet": 1e7, "grey": 1e8, "white": 1e9,
        "gold": 0.1, "silver": 0.01
    }
    COLOR_TOL = {
        "brown": 1.0, "red": 2.0, "green": 0.5, "blue": 0.25,
        "violet": 0.1, "grey": 0.05, "gold": 5.0, "silver": 10.0, "none": 20.0
    }
    COLOR_TCR = {"brown": 100, "red": 50, "orange": 15, "yellow": 25, "blue": 10, "violet": 5}

    @staticmethod
    def normalize_resistance(ohms: float) -> str:
        """تحويل القيمة الأومية إلى شكل معياري (أوم، كيلوأوم، ميغاأوم...)"""
        if ohms >= 1e6:
            return f"{ohms / 1e6:.2f} MΩ"
        if ohms >= 1e3:
            return f"{ohms / 1e3:.2f} kΩ"
        if ohms >= 1:
            return f"{ohms:.2f} Ω"
        return f"{ohms * 1e3:.2f} mΩ"

    @staticmethod
    def calculate_resistor_color(bands: list):
        """حساب قيمة المقاومة وسماحيتها من قائمة ألوان الحلقات (IEC 60062)
        bands: قائمة ألوان من الأيسر إلى الأيمن، مثال ['brown','black','red','gold']
        يدعم 4، 5، و6 حلقات.
        """
        # التحقق الأساسي
        if not bands:
            raise ValueError(tr("err_two_values"))

        digit_colors = [c for c in bands if c not in ("gold", "silver", "none", "")]
        main_bands = [c for c in bands if c not in ("none", "")]

        if len(main_bands) < 3:
            raise ValueError(tr("res_no_value"))

        # أول رقم لا يمكن أن يكون أسود
        if main_bands[0] == "black":
            raise ValueError(tr("res_no_value"))

        tol_pct = None
        tcr_val = None

        if len(bands) == 4:
            # 4 حلقات: رقم، رقم، مضاعف، تسامح
            d1, d2, mult, tol = bands
            if d1 not in ElectricalEngine.COLOR_DIGIT or d2 not in ElectricalEngine.COLOR_DIGIT:
                raise ValueError(tr("res_no_value"))
            if mult not in ElectricalEngine.COLOR_MULT:
                raise ValueError(tr("res_no_value"))
            value = (ElectricalEngine.COLOR_DIGIT[d1] * 10 + ElectricalEngine.COLOR_DIGIT[d2]) * ElectricalEngine.COLOR_MULT[mult]
            tol_pct = ElectricalEngine.COLOR_TOL.get(tol, 20.0)

        elif len(bands) == 5:
            # 5 حلقات: رقم، رقم، رقم، مضاعف، تسامح
            d1, d2, d3, mult, tol = bands
            for d in (d1, d2, d3):
                if d not in ElectricalEngine.COLOR_DIGIT:
                    raise ValueError(tr("res_no_value"))
            if mult not in ElectricalEngine.COLOR_MULT:
                raise ValueError(tr("res_no_value"))
            value = (ElectricalEngine.COLOR_DIGIT[d1] * 100 + ElectricalEngine.COLOR_DIGIT[d2] * 10 + ElectricalEngine.COLOR_DIGIT[d3]) * ElectricalEngine.COLOR_MULT[mult]
            tol_pct = ElectricalEngine.COLOR_TOL.get(tol, 20.0)

        elif len(bands) == 6:
            # 6 حلقات: 4 أرقام أو 3 أرقام+مضاعف... المعيار: رقم*3، مضاعف، تسامح، TCr
            # نعالج كـ 5 حلقات + TCr كنمط إرشادي
            d1, d2, d3, mult, tol, tcr = bands
            for d in (d1, d2, d3):
                if d not in ElectricalEngine.COLOR_DIGIT:
                    raise ValueError(tr("res_no_value"))
            if mult not in ElectricalEngine.COLOR_MULT:
                raise ValueError(tr("res_no_value"))
            value = (ElectricalEngine.COLOR_DIGIT[d1] * 100 + ElectricalEngine.COLOR_DIGIT[d2] * 10 + ElectricalEngine.COLOR_DIGIT[d3]) * ElectricalEngine.COLOR_MULT[mult]
            tol_pct = ElectricalEngine.COLOR_TOL.get(tol, 20.0)
            tcr_val = ElectricalEngine.COLOR_TCR.get(tcr)
        else:
            raise ValueError(tr("res_bands"))

        base = tr("res_ohms")
        return {
            "value": value,
            "normalized": ElectricalEngine.normalize_resistance(value),
            "tolerance": tol_pct,
            "tcr": tcr_val,
            "bands_count": len(bands)
        }

    @staticmethod
    def calculate_led_resistor(v_source: float, v_led: float, i_led_ma: float) -> dict:
        """حساب مقاومة تخفيض الجهد للـ LED"""
        if v_source <= v_led:
            raise ValueError(tr("err_source_gt_led"))

        i_led_a = i_led_ma / 1000.0
        r_resistor = (v_source - v_led) / i_led_a
        p_resistor = ((v_source - v_led) ** 2) / r_resistor

        return {
            "R": round(r_resistor, 2),
            "P": round(p_resistor, 2)
        }


# ==============================================================================
# 3. الواجهة البرمجية الموحدة وتطبيق سطح المكتب (PyQt6 UI)
# ==============================================================================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(tr("app_title"))
        self.resize(1300, 800)
        self.setMinimumSize(1000, 650)
        self.setStyleSheet(APP_STYLESHEET)
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        root_layout = QVBoxLayout(main_widget)
        root_layout.setContentsMargins(14, 8, 14, 14)
        root_layout.setSpacing(10)

        # ==================== الشريط العلوي (Header) ====================
        header = QWidget()
        header.setObjectName("HeaderCont")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(16, 8, 16, 8)
        header_layout.setSpacing(12)

        header_title = QLabel("⚡ " + tr("app_title"))
        header_title.setObjectName("HeaderTitle")
        header_title.setWordWrap(False)
        header_layout.addWidget(header_title)
        header_layout.addStretch()

        # اختيار اللغة في الزاوية المقابلة للشريط الجانبي (بعيدة عنه)
        lang_label = QLabel(tr("lang_label"))
        lang_label.setObjectName("LangLabel")
        header_layout.addWidget(lang_label)
        self.lang_combo = QComboBox()
        self.lang_combo.setObjectName("LangCombo")
        for code in LANG_CODES:
            self.lang_combo.addItem(LANG_NAMES[code], code)
        self.lang_combo.setCurrentIndex(LANG_CODES.index(LANG["current"]))
        self.lang_combo.currentIndexChanged.connect(self.change_language)
        header_layout.addWidget(self.lang_combo)

        root_layout.addWidget(header)

        # ==================== محتوى التطبيق (الشريط الجانبي + العرض) ====================
        content = QWidget()
        main_layout = QHBoxLayout(content)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(14)

        # ---------- العمود الجانبي: القائمة ----------
        sidebar_container = QWidget()
        sidebar_container.setObjectName("SidebarWrap")
        sidebar_layout = QVBoxLayout(sidebar_container)
        sidebar_layout.setContentsMargins(6, 6, 6, 6)
        sidebar_layout.setSpacing(10)

        self.sidebar = QListWidget()
        self.sidebar.setObjectName("Sidebar")
        self.sidebar.setFixedWidth(330)
        self.sidebar.setFont(QFont(APP_FONT, 10))

        self.modules_keys = [
            "mod_ohm", "mod_vdrop", "mod_k2s2", "mod_led",
            "mod_volt", "mod_amp", "mod_slip", "mod_section",
            "mod_colors", "mod_shortcircuit_soon"
        ]
        for k in self.modules_keys:
            self.sidebar.addItem(tr(k))
        self.sidebar.currentRowChanged.connect(self.display_page)
        sidebar_layout.addWidget(self.sidebar)

        # ---------- منطقة العرض المتغيرة (Stacked Widget) داخل بطاقة قابلة للتمرير ----------
        self.pages_container = QStackedWidget()
        self.pages_container.setObjectName("PageCard")

        self.pages = QStackedWidget()
        self.pages.addWidget(self.create_ohm_page())
        self.pages.addWidget(self.create_voltage_drop_page())
        self.pages.addWidget(self.create_k2s2_page())
        self.pages.addWidget(self.create_led_page())
        self.pages.addWidget(self.create_voltage_calc_page())
        self.pages.addWidget(self.create_current_calc_page())
        self.pages.addWidget(self.create_glissement_page())
        self.pages.addWidget(self.create_section_page())
        self.pages.addWidget(self.create_resistor_color_page())
        self.pages.addWidget(self.create_placeholder_page("ph_mod_shortcircuit"))

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.Shape.NoFrame)
        scroll.setWidget(self.pages)
        inner = scroll.viewport()
        if inner is not None:
            inner.setAutoFillBackground(False)
        self.pages_container.addWidget(scroll)

        main_layout.addWidget(sidebar_container, 0)
        main_layout.addWidget(self.pages_container, 1)
        root_layout.addWidget(content, 1)
        self.sidebar.setCurrentRow(0)

    def change_language(self):
        """تغيير لغة الواجهة وإعادة بناء كل العناصر مع حفظ الشاشة الحالية"""
        lang = self.lang_combo.currentData()
        if lang is None or lang == LANG["current"]:
            return

        row = max(self.sidebar.currentRow(), 0) if hasattr(self, "sidebar") else 0
        LANG["current"] = lang

        app = QApplication.instance()
        app.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft if lang == "ar" else Qt.LayoutDirection.LeftToRight
        )

        self.setWindowTitle(tr("app_title"))

        old = self.takeCentralWidget()
        old.deleteLater()
        self.init_ui()

        self.sidebar.blockSignals(True)
        self.sidebar.setCurrentRow(row)
        self.sidebar.blockSignals(False)
        self.pages.setCurrentIndex(row)

    # --------------------------------------------------------------------------
    # أدوات مساعدة لبناء صفحات موحّدة (بطاقة + عنوان كبير + حقول كبيرة)
    # --------------------------------------------------------------------------
    def _make_title(self, widget, text: str, help_key: str = None) -> QVBoxLayout:
        """إضافة عنوان كبير متناسق أعلى الصفحة، مع زر مساعدة اختياري"""
        layout = widget.layout()
        outer = QHBoxLayout()
        title = QLabel(text)
        title.setObjectName("PageTitle")
        title.setWordWrap(True)
        outer.addWidget(title, 1)
        if help_key:
            btn = QPushButton("❓ " + tr("help_btn"))
            btn.setObjectName("HelpButton")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda _, k=help_key: self._show_help(k))
            outer.addWidget(btn, 0, Qt.AlignmentFlag.AlignTop)
        layout.addLayout(outer)
        layout.addSpacing(6)
        return layout

    def _show_help(self, help_key: str):
        """فتح نافذة حوار تشرح الصيغة الحسابية والعناصر المراد إدخالها"""
        dlg = QDialog(self)
        dlg.setWindowTitle(tr("help_title"))
        dlg.setMinimumWidth(620)
        lay = QVBoxLayout(dlg)
        lay.setSpacing(12)

        formula = tr(f"help_{help_key}_formula")
        fields = tr(f"help_{help_key}_fields")

        f_label = QLabel(tr("help_formula"))
        f_label.setObjectName("FieldLabel")
        lay.addWidget(f_label)
        f_box = QLabel(formula)
        f_box.setObjectName("HelpBody")
        f_box.setWordWrap(True)
        f_box.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        lay.addWidget(f_box)

        d_label = QLabel(tr("help_fields"))
        d_label.setObjectName("FieldLabel")
        lay.addWidget(d_label)
        d_box = QLabel(fields)
        d_box.setObjectName("HelpBody")
        d_box.setWordWrap(True)
        d_box.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        lay.addWidget(d_box)

        close_btn = QPushButton(tr("btn_close"))
        close_btn.clicked.connect(dlg.accept)
        lay.addWidget(close_btn)
        dlg.exec()

    def _field(self, placeholder: str = "", default: str = "") -> QLineEdit:
        fld = QLineEdit()
        fld.setFont(QFont(APP_FONT, 15))
        if default != "":
            fld.setText(default)
        elif placeholder:
            fld.setPlaceholderText(placeholder)
        return fld

    def _field_row(self, layout, label_text: str, field: QLineEdit):
        lab = QLabel(label_text)
        lab.setObjectName("FieldLabel")
        layout.addWidget(lab)
        layout.addWidget(field)

    def _result_label(self) -> QLabel:
        lab = QLabel(tr("result_default"))
        lab.setObjectName("ResultLabel")
        lab.setWordWrap(True)
        return lab

    # --------------------------------------------------------------------------
    # الشاشة 1: قانون أوم
    # --------------------------------------------------------------------------
    def create_ohm_page(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)
        self._make_title(widget, tr("ohm_title"), "ohm")

        group = QGroupBox(tr("ohm_group"))
        group_layout = QVBoxLayout(group)
        group_layout.setSpacing(8)

        self.ohm_v = self._field(tr("ph_voltage"))
        self.ohm_i = self._field(tr("ph_current"))
        self.ohm_p = self._field(tr("ph_power"))

        self._field_row(group_layout, tr("lbl_voltage"), self.ohm_v)
        self._field_row(group_layout, tr("lbl_current"), self.ohm_i)
        self._field_row(group_layout, tr("lbl_power"), self.ohm_p)

        layout.addWidget(group)

        btn = QPushButton(tr("btn_calculate"))
        btn.clicked.connect(self.run_ohm_calc)
        layout.addWidget(btn)

        self.ohm_result = self._result_label()
        layout.addWidget(self.ohm_result)

        layout.addStretch()
        return widget

    def run_ohm_calc(self):
        try:
            v = float(self.ohm_v.text()) if self.ohm_v.text() else None
            i = float(self.ohm_i.text()) if self.ohm_i.text() else None
            p = float(self.ohm_p.text()) if self.ohm_p.text() else None

            res = ElectricalEngine.calculate_ohms_law(v=v, i=i, p=p)
            text = tr("ohm_results") + " | ".join([f"{k} = {val:.2f}" for k, val in res.items()])
            self.ohm_result.setText(text)
        except Exception as e:
            QMessageBox.critical(self, tr("err_title_calc"), str(e))

    # --------------------------------------------------------------------------
    # الشاشة 2: هبوط الجهد
    # --------------------------------------------------------------------------
    def create_voltage_drop_page(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)
        self._make_title(widget, tr("vd_title"), "vd")

        self.vd_phase_3 = QRadioButton(tr("phase_3p") + " (400V)")
        self.vd_phase_1 = QRadioButton(tr("phase_1p") + " (230V)")
        self.vd_phase_3.setChecked(True)

        phase_box = QHBoxLayout()
        phase_box.addWidget(self.vd_phase_3)
        phase_box.addWidget(self.vd_phase_1)
        layout.addLayout(phase_box)

        group = QGroupBox(tr("vd_title"))
        gl = QVBoxLayout(group)
        gl.setSpacing(8)

        self.vd_current = self._field(tr("ph_vd_current"))
        self.vd_length = self._field(tr("ph_vd_length"))
        self.vd_section = self._field(tr("ph_vd_section"))
        self.vd_cosphi = self._field("", "0.8")
        self.vd_voltage = self._field("", "400")

        self.vd_material = QComboBox()
        self.vd_material.addItem(tr("mat_cu"), "Cu")
        self.vd_material.addItem(tr("mat_al"), "Al")

        self._field_row(gl, tr("vd_nominal_voltage"), self.vd_voltage)
        self._field_row(gl, tr("vd_nominal_current"), self.vd_current)
        self._field_row(gl, tr("vd_length"), self.vd_length)
        self._field_row(gl, tr("vd_section"), self.vd_section)
        lab = QLabel(tr("lbl_cosphi")); lab.setObjectName("FieldLabel")
        gl.addWidget(lab); gl.addWidget(self.vd_cosphi)
        lab2 = QLabel(tr("vd_material")); lab2.setObjectName("FieldLabel")
        gl.addWidget(lab2); gl.addWidget(self.vd_material)
        layout.addWidget(group)

        btn = QPushButton(tr("vd_btn"))
        btn.clicked.connect(self.run_vd_calc)
        layout.addWidget(btn)

        self.vd_result = self._result_label()
        layout.addWidget(self.vd_result)

        layout.addStretch()
        return widget

    def run_vd_calc(self):
        try:
            v_nom = InputValidator.validate_positive_float(self.vd_voltage.text(), tr("vd_nominal_voltage"))
            i = InputValidator.validate_positive_float(self.vd_current.text(), tr("vd_nominal_current"))
            l = InputValidator.validate_positive_float(self.vd_length.text(), tr("vd_length"))
            s = InputValidator.validate_positive_float(self.vd_section.text(), tr("vd_section"))
            cos_phi = InputValidator.validate_non_negative_float(self.vd_cosphi.text(), "Cos φ")

            mat = self.vd_material.currentData()
            is_3p = self.vd_phase_3.isChecked()

            res = ElectricalEngine.calculate_voltage_drop(
                is_three_phase=is_3p, current=i, length=l, section=s,
                cos_phi=cos_phi, material=mat, voltage=v_nom
            )

            self.vd_result.setText(tr("vd_result_fmt", du=res['delta_u'], pct=res['percentage'], r=res['resistance']))
        except Exception as e:
            QMessageBox.warning(self, tr("err_title_data"), str(e))

    # --------------------------------------------------------------------------
    # الشاشة 3: الطاقة الحرارية K²S²
    # --------------------------------------------------------------------------
    def create_k2s2_page(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)
        self._make_title(widget, tr("k2s2_title"), "k2s2")

        group = QGroupBox(tr("k2s2_title"))
        gl = QVBoxLayout(group)
        gl.setSpacing(8)
        self.k2s2_section = self._field(tr("k2s2_ph_section"))
        self.k2s2_k = self._field(tr("k2s2_ph_k"), "115")
        self._field_row(gl, tr("k2s2_lbl_section"), self.k2s2_section)
        self._field_row(gl, tr("k2s2_lbl_k"), self.k2s2_k)
        layout.addWidget(group)

        btn = QPushButton(tr("k2s2_btn"))
        btn.clicked.connect(self.run_k2s2_calc)
        layout.addWidget(btn)

        self.k2s2_result = self._result_label()
        layout.addWidget(self.k2s2_result)

        layout.addStretch()
        return widget

    def run_k2s2_calc(self):
        try:
            s = InputValidator.validate_positive_float(self.k2s2_section.text(), tr("k2s2_lbl_section"))
            k = InputValidator.validate_positive_float(self.k2s2_k.text(), tr("k2s2_lbl_k"))

            val = ElectricalEngine.calculate_thermal_stress(s, k)
            self.k2s2_result.setText(tr("k2s2_result_fmt", val=val))
        except Exception as e:
            QMessageBox.warning(self, tr("err_title_input"), str(e))

    # --------------------------------------------------------------------------
    # الشاشة 4: مقاومة الـ LED
    # --------------------------------------------------------------------------
    def create_led_page(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)
        self._make_title(widget, tr("led_title"), "led")

        group = QGroupBox(tr("led_title"))
        gl = QVBoxLayout(group)
        gl.setSpacing(8)
        self.led_vs = self._field(tr("ph_voltage"))
        self.led_vled = self._field("", "2.1")
        self.led_iled = self._field("", "20")

        self._field_row(gl, tr("led_lbl_vs"), self.led_vs)
        self._field_row(gl, tr("led_lbl_vled"), self.led_vled)
        self._field_row(gl, tr("led_lbl_iled"), self.led_iled)
        layout.addWidget(group)

        btn = QPushButton(tr("led_btn"))
        btn.clicked.connect(self.run_led_calc)
        layout.addWidget(btn)

        self.led_result = self._result_label()
        layout.addWidget(self.led_result)

        layout.addStretch()
        return widget

    def run_led_calc(self):
        try:
            vs = InputValidator.validate_positive_float(self.led_vs.text(), tr("led_lbl_vs"))
            vled = InputValidator.validate_positive_float(self.led_vled.text(), tr("led_lbl_vled"))
            iled = InputValidator.validate_positive_float(self.led_iled.text(), tr("led_lbl_iled"))

            res = ElectricalEngine.calculate_led_resistor(vs, vled, iled)
            self.led_result.setText(tr("led_result_fmt", r=res['R'], p=res['P']))
        except Exception as e:
            QMessageBox.warning(self, tr("err_title_input"), str(e))

    # --------------------------------------------------------------------------
    # الشاشة 5: حساب الفولت (الجهد)
    # --------------------------------------------------------------------------
    def create_voltage_calc_page(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)
        self._make_title(widget, tr("volt_title"), "volt")

        self.volt_phase_3 = QRadioButton(tr("phase_3p"))
        self.volt_phase_1 = QRadioButton(tr("phase_1p"))
        self.volt_phase_1.setChecked(True)

        phase_box = QHBoxLayout()
        phase_box.addWidget(self.volt_phase_1)
        phase_box.addWidget(self.volt_phase_3)
        layout.addLayout(phase_box)

        group_power = QGroupBox(tr("method1_pi"))
        gp_layout = QVBoxLayout(group_power)
        gp_layout.setSpacing(8)
        self.volt_p = self._field(tr("ph_power"))
        self.volt_i = self._field(tr("ph_current"))
        self.volt_cosphi = self._field("", "1")

        self._field_row(gp_layout, tr("lbl_power"), self.volt_p)
        self._field_row(gp_layout, tr("lbl_current"), self.volt_i)
        self._field_row(gp_layout, tr("lbl_cosphi"), self.volt_cosphi)
        layout.addWidget(group_power)

        group_ohm = QGroupBox(tr("method2_ohm"))
        go_layout = QVBoxLayout(group_ohm)
        go_layout.setSpacing(8)
        self.volt_r = self._field("23")
        self._field_row(go_layout, tr("lbl_resistance"), self.volt_r)
        layout.addWidget(group_ohm)

        btn = QPushButton(tr("volt_btn"))
        btn.clicked.connect(self.run_voltage_calc)
        layout.addWidget(btn)

        self.volt_result = self._result_label()
        layout.addWidget(self.volt_result)

        layout.addStretch()
        return widget

    def run_voltage_calc(self):
        try:
            is_3p = self.volt_phase_3.isChecked()
            has_pi = self.volt_p.text() and self.volt_i.text()
            has_ri = self.volt_r.text() and self.volt_i.text()
            has_pr = self.volt_p.text() and self.volt_r.text()

            if has_pi:
                p = InputValidator.validate_positive_float(self.volt_p.text(), tr("lbl_power"))
                i = InputValidator.validate_positive_float(self.volt_i.text(), tr("lbl_current"))
                cos_phi = InputValidator.validate_non_negative_float(self.volt_cosphi.text(), "Cos φ")

                res = ElectricalEngine.calc_voltage_from_power(p, i, cos_phi, is_3p)
                if is_3p:
                    text = tr("volt_result_3p", u=res['U'], v=res['V_phase'])
                else:
                    text = tr("volt_result_1p", v=res['V'])
            elif has_ri:
                r = InputValidator.validate_positive_float(self.volt_r.text(), tr("lbl_resistance"))
                i = InputValidator.validate_positive_float(self.volt_i.text(), tr("lbl_current"))
                text = tr("volt_result_ri", v=round(r * i, 2))
            elif has_pr:
                p = InputValidator.validate_positive_float(self.volt_p.text(), tr("lbl_power"))
                r = InputValidator.validate_positive_float(self.volt_r.text(), tr("lbl_resistance"))
                text = tr("volt_result_pr", v=round(math.sqrt(p * r), 2))
            else:
                raise ValueError(tr("err_enter_any_method"))

            self.volt_result.setText(text)
        except Exception as e:
            QMessageBox.warning(self, tr("err_title_data"), str(e))

    # --------------------------------------------------------------------------
    # الشاشة 6: حساب الأمبير (التيار)
    # --------------------------------------------------------------------------
    def create_current_calc_page(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)
        self._make_title(widget, tr("amp_title"), "amp")

        self.amp_phase_3 = QRadioButton(tr("phase_3p"))
        self.amp_phase_1 = QRadioButton(tr("phase_1p"))
        self.amp_phase_1.setChecked(True)

        phase_box = QHBoxLayout()
        phase_box.addWidget(self.amp_phase_1)
        phase_box.addWidget(self.amp_phase_3)
        layout.addLayout(phase_box)

        group_power = QGroupBox(tr("amp_method1_pv"))
        gp_layout = QVBoxLayout(group_power)
        gp_layout.setSpacing(8)
        self.amp_p = self._field(tr("ph_power"))
        self.amp_v = self._field(tr("ph_voltage"))
        self.amp_cosphi = self._field("", "1")

        self._field_row(gp_layout, tr("lbl_power"), self.amp_p)
        self._field_row(gp_layout, tr("lbl_voltage"), self.amp_v)
        self._field_row(gp_layout, tr("lbl_cosphi"), self.amp_cosphi)
        layout.addWidget(group_power)

        group_ohm = QGroupBox(tr("method2_ohm"))
        go_layout = QVBoxLayout(group_ohm)
        go_layout.setSpacing(8)
        self.amp_r = self._field("23")
        self._field_row(go_layout, tr("lbl_resistance"), self.amp_r)
        layout.addWidget(group_ohm)

        btn = QPushButton(tr("amp_btn"))
        btn.clicked.connect(self.run_current_calc)
        layout.addWidget(btn)

        self.amp_result = self._result_label()
        layout.addWidget(self.amp_result)

        layout.addStretch()
        return widget

    def run_current_calc(self):
        try:
            is_3p = self.amp_phase_3.isChecked()
            has_pv = self.amp_p.text() and self.amp_v.text()
            has_vr = self.amp_v.text() and self.amp_r.text()
            has_pr = self.amp_p.text() and self.amp_r.text()

            if has_pv:
                p = InputValidator.validate_positive_float(self.amp_p.text(), tr("lbl_power"))
                v = InputValidator.validate_positive_float(self.amp_v.text(), tr("lbl_voltage"))
                cos_phi = InputValidator.validate_non_negative_float(self.amp_cosphi.text(), "Cos φ")

                res = ElectricalEngine.calc_current_from_power(p, v, cos_phi, is_3p)
                formula = tr("amp_formula_3p") if is_3p else tr("amp_formula_1p")
                text = tr("amp_result_fmt", formula=formula, i=res['I'])
            elif has_vr:
                v = InputValidator.validate_positive_float(self.amp_v.text(), tr("lbl_voltage"))
                r = InputValidator.validate_positive_float(self.amp_r.text(), tr("lbl_resistance"))
                text = tr("amp_result_vr", i=round(v / r, 2))
            elif has_pr:
                p = InputValidator.validate_positive_float(self.amp_p.text(), tr("lbl_power"))
                r = InputValidator.validate_positive_float(self.amp_r.text(), tr("lbl_resistance"))
                text = tr("amp_result_pr", i=round(math.sqrt(p / r), 2))
            else:
                raise ValueError(tr("err_enter_any_method"))

            self.amp_result.setText(text)
        except Exception as e:
            QMessageBox.warning(self, tr("err_title_data"), str(e))

    # --------------------------------------------------------------------------
    # الشاشة 7: انزلاق المحرك (Glissement)
    # --------------------------------------------------------------------------
    def create_glissement_page(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)
        self._make_title(widget, tr("gl_title"), "slip")

        group_net = QGroupBox(tr("gl_group_net"))
        gn_layout = QVBoxLayout(group_net)
        gn_layout.setSpacing(8)
        self.gl_freq = self._field("", "50")
        self.gl_poles = self._field(tr("gl_poles_ph"))

        self._field_row(gn_layout, tr("gl_freq"), self.gl_freq)
        self._field_row(gn_layout, tr("gl_poles"), self.gl_poles)
        layout.addWidget(group_net)

        group_speed = QGroupBox(tr("gl_method1"))
        gs_layout = QVBoxLayout(group_speed)
        gs_layout.setSpacing(8)
        self.gl_rpm = self._field(tr("gl_rpm_ph"))
        self._field_row(gs_layout, tr("gl_lbl_rpm"), self.gl_rpm)
        layout.addWidget(group_speed)

        group_slip = QGroupBox(tr("gl_method2"))
        gsl_layout = QVBoxLayout(group_slip)
        gsl_layout.setSpacing(8)
        self.gl_slip = self._field(tr("gl_slip_ph"))
        self._field_row(gsl_layout, tr("gl_lbl_slip"), self.gl_slip)
        layout.addWidget(group_slip)

        btn = QPushButton(tr("gl_btn"))
        btn.clicked.connect(self.run_glissement_calc)
        layout.addWidget(btn)

        self.gl_result = self._result_label()
        layout.addWidget(self.gl_result)

        layout.addStretch()
        return widget

    def run_glissement_calc(self):
        try:
            f = InputValidator.validate_positive_float(self.gl_freq.text(), tr("gl_freq"))
            p = InputValidator.validate_positive_float(self.gl_poles.text(), tr("gl_poles"))

            rpm = None
            slip = None
            if self.gl_rpm.text():
                rpm = InputValidator.validate_non_negative_float(self.gl_rpm.text(), tr("gl_lbl_rpm"))
            elif self.gl_slip.text():
                slip = InputValidator.validate_non_negative_float(self.gl_slip.text(), tr("gl_lbl_slip"))

            res = ElectricalEngine.calculate_motor_slip(f, p, rpm=rpm, slip_pct=slip)

            self.gl_result.setText(tr("gl_result_fmt", ns=res['Ns'], n=res['N'], g=res['g'], fr=res['f_rotor']))
        except Exception as e:
            QMessageBox.warning(self, tr("err_title_data"), str(e))

    # --------------------------------------------------------------------------
    # الشاشة 8: حساب مقطع الكابل (Section du câble)
    # --------------------------------------------------------------------------
    def create_section_page(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)
        self._make_title(widget, tr("sec_title"), "section")

        self.sec_phase_3 = QRadioButton(tr("phase_3p"))
        self.sec_phase_1 = QRadioButton(tr("phase_1p"))
        self.sec_phase_3.setChecked(True)

        phase_box = QHBoxLayout()
        phase_box.addWidget(self.sec_phase_3)
        phase_box.addWidget(self.sec_phase_1)
        layout.addLayout(phase_box)

        group = QGroupBox(tr("sec_title"))
        gl = QVBoxLayout(group)
        gl.setSpacing(8)

        self.sec_voltage = self._field("", "400")
        self.sec_current = self._field(tr("ph_vd_current"))
        self.sec_length = self._field(tr("ph_vd_length"))
        self.sec_cosphi = self._field("", "0.8")
        self.sec_maxdrop = self._field(tr("ph_drop_pct"), "3")

        self.sec_material = QComboBox()
        self.sec_material.addItem(tr("mat_cu"), "Cu")
        self.sec_material.addItem(tr("mat_al"), "Al")

        self._field_row(gl, tr("vd_nominal_voltage"), self.sec_voltage)
        self._field_row(gl, tr("vd_nominal_current"), self.sec_current)
        self._field_row(gl, tr("vd_length"), self.sec_length)
        self._field_row(gl, tr("lbl_cosphi"), self.sec_cosphi)
        self._field_row(gl, tr("sec_max_drop"), self.sec_maxdrop)
        labm = QLabel(tr("vd_material")); labm.setObjectName("FieldLabel")
        gl.addWidget(labm); gl.addWidget(self.sec_material)
        layout.addWidget(group)

        btn = QPushButton(tr("sec_btn"))
        btn.clicked.connect(self.run_section_calc)
        layout.addWidget(btn)

        self.sec_result = self._result_label()
        layout.addWidget(self.sec_result)

        layout.addStretch()
        return widget

    def run_section_calc(self):
        try:
            v = InputValidator.validate_positive_float(self.sec_voltage.text(), tr("vd_nominal_voltage"))
            i = InputValidator.validate_positive_float(self.sec_current.text(), tr("vd_nominal_current"))
            l = InputValidator.validate_positive_float(self.sec_length.text(), tr("vd_length"))
            cos_phi = InputValidator.validate_non_negative_float(self.sec_cosphi.text(), "Cos φ")
            max_drop = InputValidator.validate_positive_float(self.sec_maxdrop.text(), tr("sec_max_drop"))

            mat = self.sec_material.currentData()
            is_3p = self.sec_phase_3.isChecked()

            res = ElectricalEngine.calculate_cable_section(
                is_three_phase=is_3p, voltage=v, current=i, length=l,
                cos_phi=cos_phi, material=mat, max_drop_pct=max_drop
            )

            if res["suggested"] is None:
                raise ValueError(tr("err_section_too_large"))

            self.sec_result.setText(tr(
                "sec_result_fmt",
                smin=res["s_min"], s=res["suggested"],
                du=res["actual_drop_pct"], r=res["resistance"]
            ))
        except Exception as e:
            QMessageBox.warning(self, tr("err_title_data"), str(e))

    # --------------------------------------------------------------------------
    # الشاشة 9: حساب المقاومة حسب الألوان (IEC 60062)
    # --------------------------------------------------------------------------
    RES_COLOR_PALETTE = [
        ("black", "#000000"), ("brown", "#6b3a12"), ("red", "#d32f2f"),
        ("orange", "#ef6c00"), ("yellow", "#fbc02d"), ("green", "#388e3c"),
        ("blue", "#1565c0"), ("violet", "#6a1b9a"), ("grey", "#757575"),
        ("white", "#f5f5f5"), ("gold", "#c9a227"), ("silver", "#b0bec5")
    ]
    RES_TOLERANCE_NAMES = {
        "brown": "±1%", "red": "±2%", "green": "±0.5%", "blue": "±0.25%",
        "violet": "±0.1%", "grey": "±0.05%", "gold": "±5%", "silver": "±10%"
    }
    RES_TCR_NAMES = {
        "brown": "100 ppm/°C", "red": "50 ppm/°C", "orange": "15 ppm/°C",
        "yellow": "25 ppm/°C", "blue": "10 ppm/°C", "violet": "5 ppm/°C"
    }

    def create_resistor_color_page(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)
        self._make_title(widget, tr("res_title"), "res")

        help_lbl = QLabel(tr("res_help"))
        help_lbl.setObjectName("FieldLabel")
        help_lbl.setWordWrap(True)
        layout.addWidget(help_lbl)

        # عدد الحلقات (4، 5، 6)
        band_row = QHBoxLayout()
        band_row.addWidget(QLabel(tr("res_max_bands")))
        band_row.addStretch()
        self.res_band_count = QComboBox()
        for n in (4, 5, 6):
            self.res_band_count.addItem(f"{n}", n)
        self.res_band_count.setCurrentIndex(0)
        self.res_band_count.currentIndexChanged.connect(self.res_rebuild_bands)
        band_row.addWidget(self.res_band_count)
        layout.addLayout(band_row)

        # حاويات الحلقات
        self.res_containers = []
        self.res_group = QGroupBox(tr("res_bands"))
        self.res_group_layout = QVBoxLayout(self.res_group)
        self.res_group_layout.setSpacing(8)
        layout.addWidget(self.res_group)

        self.res_rebuild_bands()

        btn = QPushButton(tr("res_btn"))
        btn.clicked.connect(self.run_resistor_color_calc)
        layout.addWidget(btn)

        self.res_result = self._result_label()
        layout.addWidget(self.res_result)

        layout.addStretch()
        return widget

    def _new_color_combo(self, allow_blank=True, role="digit") -> QComboBox:
        """إنشاء قائمة ألوان مع خيار فارغ (فقط مكان حلقات التسامح)"""
        cb = QComboBox()
        if allow_blank:
            cb.addItem(tr("res_blank"), None)
        for key, hexcolor in self.RES_COLOR_PALETTE:
            cb.addItem(tr(f"color_{key}"), key)
        return cb

    def res_rebuild_bands(self):
        """إعادة بناء قوائم الألوان حسب عدد الحلقات المختار"""
        count = self.res_band_count.currentData() or 4
        self.res_combos = []

        # تفريغ الحاويات القديمة
        while self.res_group_layout.count():
            item = self.res_group_layout.takeAt(0)
            w = item.widget()
            if w is not None:
                w.deleteLater()

        # هيكل الحلقات حسب العدد (IEC 60062)
        # 4:  [رقم، رقم، مضاعف، تسامح]
        # 5:  [رقم، رقم، رقم، مضاعف، تسامح]
        # 6:  [رقم، رقم، رقم، مضاعف، تسامح، TCR]
        digit_count = 2 if count == 4 else 3

        # أسماء التسميات
        digit_labels = [f"1", f"2", f"3", f"4", f"5", f"6"]

        for i in range(count):
            row_widget = QWidget()
            row_layout = QHBoxLayout(row_widget)
            row_layout.setContentsMargins(0, 0, 0, 0)

            if i == digit_count:
                # حلقة المضاعف
                row_layout.addWidget(QLabel(tr("res_x") + " " + tr("res_mult")))
                cb = self._new_color_combo(allow_blank=False)
                cb.setCurrentIndex(1)
            elif i < digit_count:
                # حلقة رقم
                row_layout.addWidget(QLabel(tr("res_x") + " " + tr("res_digit") + " " + digit_labels[i]))
                cb = self._new_color_combo(allow_blank=False)
                cb.setCurrentIndex(1)
            elif i == digit_count + 1 and count >= 5:
                # حلقة التسامح (semi-last)
                row_layout.addWidget(QLabel(tr("res_x") + " " + tr("res_tol")))
                cb = self._new_color_combo(allow_blank=True)
                cb.setCurrentIndex(0)
            else:
                # آخر حلقة: تسامح (4/5 حلقات) أو TCR (6 حلقات)
                if count == 6:
                    row_layout.addWidget(QLabel(tr("res_x") + " " + tr("res_tcr")))
                    cb = self._new_color_combo(allow_blank=True)
                    cb.setCurrentIndex(0)
                else:
                    row_layout.addWidget(QLabel(tr("res_x") + " " + tr("res_tol")))
                    cb = self._new_color_combo(allow_blank=True)
                    cb.setCurrentIndex(0)

            row_layout.addWidget(cb, 1)
            self.res_combos.append(cb)
            self.res_group_layout.addWidget(row_widget)

    def run_resistor_color_calc(self):
        try:
            bands = []
            for cb in self.res_combos:
                bands.append(cb.currentData())

            res = ElectricalEngine.calculate_resistor_color(bands)

            val_txt = f"{res['value']:.5g} Ω"
            norm_txt = res["normalized"]
            tol_txt = f"±{res['tolerance']}%"
            tcr_txt = "—" if res["tcr"] is None else self.RES_TCR_NAMES.get(
                bands[-1] if bands else "", "")
            if res["tcr"] is not None:
                tcr_txt = f"{res['tcr']} ppm/°C"

            self.res_result.setText(tr(
                "res_result",
                val=val_txt, norm=norm_txt, tol=tol_txt, tcr=tcr_txt
            ))
        except Exception as e:
            QMessageBox.warning(self, tr("err_title_data"), str(e))

    # --------------------------------------------------------------------------
    # شاشة عامة للحسابات المستقبيلية (Placeholder)
    # --------------------------------------------------------------------------
    def create_placeholder_page(self, title_key: str) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(18, 18, 18, 18)
        self._make_title(widget, tr(title_key))
        layout.addStretch()

        lbl = QLabel(tr("placeholder_body", title=tr(title_key)))
        lbl.setFont(QFont(APP_FONT, 14))
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl.setWordWrap(True)
        lbl.setStyleSheet("color: " + COLORS["text"])
        layout.addWidget(lbl)
        layout.addStretch()
        return widget

    def display_page(self, index: int):
        self.pages.setCurrentIndex(index)


# ==============================================================================
# 4. تشغيل التطبيق (Application Entry Point)
# ==============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyle('Fusion')
    app.setLayoutDirection(
        Qt.LayoutDirection.RightToLeft if LANG["current"] == "ar" else Qt.LayoutDirection.LeftToRight
    )

    window = MainWindow()
    # توسيط النافذة على الشاشة
    screen = app.primaryScreen().availableGeometry()
    x = (screen.width() - window.width()) // 2
    y = (screen.height() - window.height()) // 2
    window.move(x, y)
    window.show()
    sys.exit(app.exec())
