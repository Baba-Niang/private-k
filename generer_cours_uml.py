from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# --- Configuration du style ---
BLEU_FONCE = RGBColor(20, 60, 120)
BLEU_CLAIR = RGBColor(220, 235, 255)
ORANGE = RGBColor(255, 165, 0)
NOIR = RGBColor(0, 0, 0)
BLANC = RGBColor(255, 255, 255)
GRIS = RGBColor(220, 220, 220)

def ajouter_titre(prs, texte, sous_titre=""):
    slide_layout = prs.slide_layouts[1] # Titre + Contenu
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = texte
    slide.shapes.title.text_frame.paragraphs[0].font.size = Pt(36)
    slide.shapes.title.text_frame.paragraphs[0].font.bold = True
    slide.shapes.title.text_frame.paragraphs[0].font.color.rgb = BLEU_FONCE
    if sous_titre:
        slide.placeholders[1].text = sous_titre
    return slide

def ajouter_contenu(prs, titre, contenu_liste):
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = titre
    slide.shapes.title.text_frame.paragraphs[0].font.size = Pt(30)
    slide.shapes.title.text_frame.paragraphs[0].font.bold = True
    slide.shapes.title.text_frame.paragraphs[0].font.color.rgb = BLEU_FONCE
    body = slide.placeholders[1]
    tf = body.text_frame
    tf.clear()
    for i, texte in enumerate(contenu_liste):
        p = tf.add_paragraph()
        p.text = texte
        p.font.size = Pt(18)
        p.font.color.rgb = NOIR
        if i == 0:
            p.font.bold = True

# --- Création du PPTX ---
prs = Presentation()

# Page 1 : Couverture
slide_layout = prs.slide_layouts[6] # Slide vide
slide = prs.slides.add_slide(slide_layout)
# Ajouter le titre principal
left = Inches(1); top = Inches(2); width = Inches(8); height = Inches(2)
txBox = slide.shapes.add_textbox(left, top, width, height)
tf = txBox.text_frame
tf.text = "COURS COMPLET"
p = tf.add_paragraph()
p.text = "UML"
p.font.size = Pt(60)
p.font.bold = True
p.font.color.rgb = BLEU_FONCE
p = tf.add_paragraph()
p.text = "Unified Modeling Language"
p.font.size = Pt(24)
p.font.color.rgb = ORANGE

# Page 2 : Sommaire
ajouter_contenu(prs, "Sommaire", [
    "01. Introduction à UML",
    "   - Définitions, origines, objectifs",
    "02. Diagrammes structurels",
    "   - Classes, objets, composants, déploiement, paquetages",
    "03. Diagrammes comportementaux",
    "   - Cas d'utilisation, séquence, communication, états, activités",
    "04. Méthodologie",
    "   - Démarche de modélisation, bonnes pratiques"
])

# Page 3 : Qu'est-ce qu'UML ?
ajouter_contenu(prs, "Qu'est-ce qu'UML ?", [
    "Un langage graphique de modélisation",
    "• Standardisé par l'OMG (Object Management Group)",
    "• Né en 1997 (fusion Booch, Rumbaugh, Jacobson)",
    "• Indépendant de toute méthode ou langage de programmation",
    "",
    "⚠️ Ce n'est PAS un langage de programmation !"
])

# Page 4 : Pourquoi UML ?
ajouter_contenu(prs, "Pourquoi utiliser UML ?", [
    "1. Communiquer : vocabulaire visuel commun",
    "2. Visualiser : représenter avant de coder",
    "3. Documenter : garder une trace des choix",
    "4. Anticiper : détecter les erreurs en amont"
])

# Page 5 : Diagramme de classes (Exemple)
slide = prs.slides.add_slide(prs.slide_layouts[6])
left = Inches(2); top = Inches(1); width = Inches(6); height = Inches(4)
shape = slide.shapes.add_shape(1, left, top, width, height) # 1 = Rectangle
shape.fill.solid()
shape.fill.fore_color.rgb = BLEU_CLAIR
shape.line.color.rgb = BLEU_FONCE
tf = shape.text_frame
tf.text = "Compte"
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.size = Pt(24)
tf.paragraphs[0].alignment = PP_ALIGN.CENTER
p = tf.add_paragraph(); p.text = "- solde : double"
p = tf.add_paragraph(); p.text = "- titulaire : string"
p = tf.add_paragraph(); p.text = "# dateOuverture : Date"
p = tf.add_paragraph()
p = tf.add_paragraph(); p.text = "+ deposer(montant : double)"
p = tf.add_paragraph(); p.text = "+ retirer(montant : double) : bool"
p = tf.add_paragraph(); p.text = "+ consulterSolde() : double"

# Pages suivantes (simplifiées ici pour la démo) ...
ajouter_contenu(prs, "Les 4 relations entre classes", [
    "Association (———) : Lien simple",
    "Agrégation (◇———) : Contient (faible)",
    "Composition (◆———) : Possède (fort)",
    "Héritage (▷———) : Est un"
])

ajouter_contenu(prs, "Diagramme de cas d'utilisation", [
    "Acteur : Personne ou système externe",
    "Cas d'utilisation : Fonctionnalité (ellipse)",
    "Frontière : Rectangle englobant",
    "Association : Trait relatif"
])

ajouter_contenu(prs, "La démarche de modélisation", [
    "Étape 1 : Recueillir les besoins",
    "Étape 2 : Identifier les acteurs (Cas d'utilisation)",
    "Étape 3 : Modéliser la structure (Classes)",
    "Étape 4 : Modéliser le comportement (Séquence, États)",
    "Étape 5 : Concevoir l'architecture (Composants)"
])

ajouter_contenu(prs, "MERCI", [
    "UML : un langage, quatorze diagrammes, une seule ambition.",
    "Mieux penser avant de construire."
])

prs.save("Cours_UML_Ameliore.pptx")
print("✅ PowerPoint généré : Cours_UML_Ameliore.pptx")